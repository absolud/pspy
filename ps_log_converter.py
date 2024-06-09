# native libs
import re
import json
import argparse
from typing import Union, Dict, List, Generator, Any
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# third-party libs
from win32com.client import Dispatch


###########################################################
# PS LOG CONVERTER
###########################################################
''' 
This script processes Photoshop's ScriptListener log files and converts PS events into human readable Python functions. 
This is a renewed version compared to "photoshop_scriptlistener2python.py" script.

Improvements include:
    added typing and docstring to the functions
    better handling of xmpmeta entries
    excluded events are now stored in a JSON file and loaded independently "excluded_events.json"
    better handling of file paths
    better handling of terminal arguments
    new name for the script "ps_log_converter.py"
    log files are sanitzed and saved in the "__temp" folder than removed after processing
    python scripts are now stored in a separate folder "__temp"

ATTENTION:
    excluded_events.json has to be present for the script to run
    There is always a chance if the script stops working that a new event has been introduced in Photoshop. In this case, whatever this event name is, it should be added to the ignore list.

Example
01 single entry:
python ps_log_converter.py JS.log

Example
02 browse entry: If the file path doesn't exist or mistyped you will be asked to browse to a valid log file for processing. The browsing mode only allows for single file conversion.

Example
03 multiple entries: Only terminal command line arguments will support batch conversions (multiple log files).
python ps_log_converter.py JS01.log JS02.log JS03.log
'''
###########################################################



VARS = {}

def _browse() -> str:
    """
    Open a file dialog to select a file.

    Returns:
        str: The path to the selected file.
    """
    allowed_file = "JS.log"
    Tk().withdraw()
    path = askopenfilename()
    if path:
        return path
    else:
        print('No file picked')
        return ''

def load_excluded_events_gen(file_path: Union[str, Path]) -> Generator[Dict[str, Any], None, None]:
    """
    Generator function that loads the contents of a JSON file containing excluded events.

    Args:
        file_path (Union[str, Path]): The path to the JSON file.

    Yields:
        dict: A dictionary containing the data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        ValueError: If the file content cannot be decoded as JSON.
    """
    path = Path(file_path)
    try:
        with path.open("r") as file:
            data = json.load(file)
            yield data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {file_path} not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON in file {file_path}.") from e

def get_excluded_events_gen(data_gen: Generator[Dict[str, List[str]], None, None]) -> Generator[str, None, None]:
    """
    Generator function that extracts excluded events from the provided data generator.

    Args:
        data_gen (Generator[Dict[str, List[str]], None, None]): Generator yielding a dictionary of data.

    Yields:
        str: An individual excluded event from the data.
    """
    data = next(data_gen)
    for event in data["excluded_events"]:
        yield event

def fix_and_flatten_xmpmeta_log_entry(log_entry: str) -> str:
    """
    Replace triple-quoted strings in a log entry with single-quoted strings and remove line breaks.

    Args:
        log_entry (str): A log entry containing triple-quoted strings.

    Returns:
        str: The corrected log entry with multiline triple-quoted strings replaced by single-quoted strings and no line breaks.
    """
    def replacement(match):
        content = match.group(1).replace('\n', '').replace('\r', '')
        corrected_content = content.replace('"', "'")
        return f'"""{corrected_content}"""'

    return re.sub(r'"""\s*(.*?)\s*"""', replacement, log_entry, flags=re.DOTALL)

def coroutine(func):
    """
    Decorator to initialize a coroutine function.

    Args:
        func (Callable): A coroutine function to be wrapped.

    Returns:
        Callable: The wrapped coroutine function with initial execution started.
    """
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def should_exclude_gen(exclusions: Generator[str, None, None], out):
    """
    Coroutine that filters out entries based on a generator of excluded events.

    Args:
        exclusions (Generator[str, None, None]): Generator yielding excluded events.
        out (Generator): The next coroutine to which filtered entries are sent.
    """
    exclusions_list = list(exclusions)
    while True:
        entry = (yield)
        entry = fix_and_flatten_xmpmeta_log_entry(entry)  # Sanitize the entry
        if not any(event in entry for event in exclusions_list):
            out.send(entry)

@coroutine
def save_entries(output_dir: Path, original_name: str):
    """
    Coroutine that saves filtered log entries to a new log file.

    Args:
        output_dir (Path): Directory where the filtered log files will be stored.
        original_name (str): Original name of the log file.

    Prints:
        The path where the log files have been saved.

    Yields:
        None: Continuously accepts log entries to be written to the filtered log file.
    """
    temp_name = f"{original_name.stem}__temp{original_name.suffix}"
    filtered_file_path = output_dir / temp_name
    with filtered_file_path.open("w") as filtered_file:
        while True:
            entry = (yield)
            filtered_file.write(f"// =======================================================\n{entry}\n\n")

def process_logs(log_files: List[str]) -> List[Path]:
    """
    Process and filter multiple log files based on exclusions specified in a JSON file.

    Args:
        log_files (List[str]): List of paths to log files to be processed.

    Returns:
        List[Path]: List of paths to the converted log files.

    Raises:
        FileNotFoundError: If the file with excluded events is not found.
    """
    excluded_events_path = 'excluded_events.json'
    converted_files = []

    for log_file_path in log_files:
        log_path = Path(log_file_path)
        output_dir = log_path.parent / "__temp"
        output_dir.mkdir(exist_ok=True)

        filtered_name = f"{log_path.stem}__temp{log_path.suffix}"
        filtered_file_path = output_dir / filtered_name
        converted_files.append(filtered_file_path)

        entries_saver = save_entries(output_dir, log_path)
        excluded_checker = should_exclude_gen(
            get_excluded_events_gen(load_excluded_events_gen(excluded_events_path)),
            entries_saver
        )

        with log_path.open("r") as log:
            content = log.read()

        entries = (
            entry.strip()
            for entry in content.split("// =======================================================")
            if entry.strip()
        )

        for entry in entries:
            excluded_checker.send(entry)

        excluded_checker.close()
        entries_saver.close()

    return converted_files

class Indenter:
    """Context manager to indent code and text."""

    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def style(self, text: str) -> str:
        """Returns a string indented based on the level."""
        return '    ' * self.level + text

def _regex_patterns_dict(ids: str) -> str:
    """
    Returns a regular expression pattern specific to parsing Photoshop's ScriptingListenerJS.log file.

    Args:
        ids (str): Identifier for the regular expression pattern.

    Returns:
        str: The regular expression pattern.
    """
    return {
        "var_id_name": r"^var\s(id\w+)",
        "var_id": r"\s*var\s(\w+)\W+(\w+)\(\s?(.+)\s\)",
        "descriptor": r"\s*var\s(\w+)\W+new\s(\w+)\(\);",
        "datatype": r"\s*(\w+)\.(\w+)\(\s?(.+?)\s\);",
        "exec": r"(\w+)\(\s?(.+)\s\)",
        "new_file": r"new\sFile\(\s(\W.*\")\s\W*",
        "start": r"^var\s",
        "end": r"^executeAction\("
    }.get(ids, '')

def _setup_regex_compiles(ids: str) -> re.Pattern:
    """
    Sets up and returns the regex compiler based on the provided identifier.

    Args:
        ids (str): Identifier for the regular expression pattern.

    Returns:
        re.Pattern: The compiled regular expression pattern.
    """
    regex = _regex_patterns_dict(ids)
    compiled = re.compile(regex, re.DOTALL)
    return compiled

def _descriptor_getter(variable: str, descriptor: str) -> str:
    """
    Returns a valid line of main Photoshop Dispatcher python code.

    Args:
        variable (str): Variable name.
        descriptor (str): Descriptor type.

    Returns:
        str: A line of Photoshop Dispatcher python code.
    """
    return {
        "ActionDescriptor": f'{variable} = Dispatch("Photoshop.ActionDescriptor")',
        "ActionReference": f'{variable} = Dispatch("Photoshop.ActionReference")',
        "ActionList": f'{variable} = Dispatch("Photoshop.ActionList")',
    }.get(descriptor, '')

def _convert_datatype(line: str) -> str:
    """
    Converts an incoming line into datatype parts and concatenates them into a valid line of python.

    Args:
        line (str): The line to be converted.

    Returns:
        str: The converted line.
    """
    pattern_datatype = _setup_regex_compiles("datatype")
    pattern_new_file = _setup_regex_compiles("new_file")
    match_datatype = pattern_datatype.match(line)
    if match_datatype:
        descriptor = match_datatype.group(1)
        datatype = match_datatype.group(2)
        values = match_datatype.group(3)
        first_letter_upper = datatype[0].upper()
        datatype_converted = first_letter_upper + datatype[1:]
        values = values.split(",")

        for idx, prop in enumerate(values):
            prop = prop.strip()
            if "new File(" in prop:
                match_new_file = pattern_new_file.match(prop)
                if match_new_file:
                    link = match_new_file.group(1)
                    values[idx] = link
            if prop in VARS:
                if prop == "idnull":
                    VARS[prop] = 's("target")'
                values[idx] = VARS[prop]

        value_prop2string = ", ".join(values)
        if "false" in value_prop2string:
            value_prop2string = value_prop2string.replace("false", "False")
        elif "true" in value_prop2string:
            value_prop2string = value_prop2string.replace("true", "True")

        return f"{descriptor}.{datatype_converted}({value_prop2string})"
    return ''

def _convert_exec(line: str, value: str) -> str:
    """
    Converts an incoming line into exec parts and concatenates them into a valid line of python.

    Args:
        line (str): The line to be converted.
        value (str): The value to be used in the conversion.

    Returns:
        str: The converted line.
    """
    pattern_exec = _setup_regex_compiles("exec")
    match_exec = pattern_exec.match(line)
    if match_exec:
        exec_func = match_exec.group(1)
        values = match_exec.group(2)
        first_letter = exec_func[0].upper()
        exec_func_converted = first_letter + exec_func[1:]
        values = values.split(",")

        for idx, prop in enumerate(values):
            prop = prop.strip()
            if prop in VARS:
                values[idx] = VARS[prop]
        value_prop2string = ",".join(values)
        return f"app.{exec_func_converted}({value_prop2string})"
    return ''

def _convert_descriptor(line: str) -> str:
    """
    Converts an incoming line into descriptor parts and concatenates them into a valid line of python.

    Args:
        line (str): The line to be converted.

    Returns:
        str: The converted line.
    """
    pattern_descriptor = _setup_regex_compiles("descriptor")
    match_descriptor = pattern_descriptor.match(line)
    if match_descriptor:
        var_name = match_descriptor.group(1)
        descriptor = match_descriptor.group(2)
        result = _descriptor_getter(var_name, descriptor)
        return result
    return ''

def _convert_var_id(line: str, group_count: int = None, position: int = None) -> Dict[str, str]:
    """
    Converts variable ID lines into valid python.

    Args:
        line (str): The line to be converted.
        group_count (int, optional): The group count for the conversion. Defaults to None.
        position (int, optional): The position of the line. Defaults to None.

    Returns:
        Dict[str, str]: A dictionary with function name, function call, and variable value.
    """
    pattern_var_id = _setup_regex_compiles("var_id")
    match_var_id = pattern_var_id.match(line)

    if match_var_id:
        var_name = match_var_id.group(1)
        func = match_var_id.group(2)
        id_string = match_var_id.group(3)
        id_string = id_string.replace('"', "")
        convert_func = 's'

        if func.startswith("charID"):
            id_value = cs(id_string)
            if id_value == '':
                convert_func = 'c'
                id_value = id_string
        elif func.startswith("stringID"):
            id_value = id_string

        VARS[var_name] = f'{convert_func}("{id_value}")'

        if position == 0:
            _name = f"{id_value}_{group_count}"
            return {
                "func_name": f"def {_name}():",
                "func": f"{_name}()\n\n",
                "var_value": VARS[var_name]
            }
    return {}

def _convert_lines(lines: Generator[str, None, None], event_id: int) -> Generator[str, None, None]:
    """
    Distributes incoming lines into first, middle, and last parts and converts these into valid python.

    Args:
        lines (Generator[str, None, None]): The lines to be converted.
        event_id (int): The event ID for the conversion.

    Yields:
        str: The converted lines.
    """
    lines_local = list(lines)
    first_line, *body, last_line = lines_local
    first_line = _convert_var_id(first_line, group_count=event_id, position=0)

    with Indenter() as indent:
        yield Indenter().style(first_line['func_name'])

        if len(body) > 0:
            for line in body:
                if "charID" in line or "stringID" in line:
                    _convert_var_id(line)
                elif any(item in line for item in ["ActionDescriptor", "ActionReference", "ActionList"]):
                    line = _convert_descriptor(line)
                    yield indent.style(line)
                elif ".put" in line:
                    line = _convert_datatype(line)
                    yield indent.style(line)

        last_line = _convert_exec(last_line, first_line["var_value"])
        if "DialogModes" in last_line:
            last_line = last_line.replace("DialogModes.NO", "dialog()")
        if "undefined" in last_line:
            last_line = last_line.replace("undefined", "None")

        yield indent.style(last_line)
        yield Indenter().style('')
        yield Indenter().style(first_line['func'])
        VARS.clear()

def generate_boilerplate() -> Generator[str, None, None]:
    """
    Generates the boilerplate code required for the script.

    Yields:
        str: The lines of boilerplate code.
    """
    yield Indenter().style("###########################################################")
    yield Indenter().style("# Required boilerplate code")
    yield Indenter().style("###########################################################")
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style("from win32com.client import Dispatch")
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style('app = Dispatch("Photoshop.Application")')
    yield Indenter().style("")

    yield Indenter().style("def s(name):")
    with Indenter() as indenter:
        yield indenter.style('"""convert string name into type id"""')
        yield indenter.style('return app.StringIDToTypeID(f"{name}")')
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style("def c(name):")
    with Indenter() as indenter:
        yield indenter.style('"""convert char name into type id"""')
        yield indenter.style('return app.CharIDToTypeID(f"{name}")')
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style("def _ps_display_dialogs():")
    with Indenter() as indenter:
        yield indenter.style('"""Dictionary with dialog constants"""')
        yield indenter.style('return {"all": 1, "error": 2, "no": 3}')
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style('def dialog(dialog_type="no"):')
    with Indenter() as indenter:
        yield indenter.style('"""Photoshop dialog windows settings using "all": 1, "error": 2, "no": 3"""')
        yield indenter.style('dialogs = _ps_display_dialogs()')
        yield indenter.style('return dialogs.get(dialog_type, lambda: None)')
    yield Indenter().style("")
    yield Indenter().style("")

    yield Indenter().style("###########################################################")
    yield Indenter().style("# Generated JS to Python Action manager code")
    yield Indenter().style("###########################################################")
    yield Indenter().style("")
    yield Indenter().style("")

def convert_events(log_file: str, events: List[str]):
    """
    Converts JS events to Python functions and writes them to an output file.

    Args:
        log_file (str): The log file containing JS events.
        events (List[str]): The list of JS events.
    """
    log_path = Path(log_file)
    output_file = log_path.with_suffix('.py')

    with output_file.open('w') as f:
        for x in generate_boilerplate():
            f.write(x + '\n')

        for idx, event in enumerate(events):
            lines = (x for x in event.splitlines())
            for x in _convert_lines(lines, event_id=idx):
                f.write(x + '\n')

def get_js_events(log_file: str) -> Generator[str, None, None]:
    """
    Extracts allowed Photoshop events for conversion from the log file.

    Args:
        log_file (str): The log file containing JS events.

    Returns:
        Generator[str, None, None]: The extracted JS events.
    """
    with open(log_file, "rt") as f:
        data = f.read().split("// =======================================================")
        return (event.strip() for idx, event in enumerate(data) if idx != 0)

def process_logs_gen(log_files: List[str]) -> Generator[Path, None, None]:
    """
    Process and filter multiple log files based on exclusions specified in a JSON file, yielding the paths of converted log files.

    Args:
        log_files (List[str]): List of paths to log files to be processed.

    Yields:
        Path: Path to each converted log file.
    """
    for log_file in log_files:
        converted_files = process_logs([log_file])
        for file_path in converted_files:
            yield file_path

        Path(file_path).unlink(missing_ok=True)

###########################################################
# Required boilerplate code
###########################################################

app = Dispatch("Photoshop.Application")

def s(name):
    """convert string name into type id"""
    return app.StringIDToTypeID(f"{name}")


def c(name):
    """convert char name into type id"""
    return app.CharIDToTypeID(f"{name}")


def cs(name):
    """convert char name into type id"""
    return app.TypeIDToStringID(app.CharIDToTypeID(name))


def _ps_display_dialogs():
    """Dictionary with dialog constants"""
    return {"all": 1, "error": 2, "no": 3}


def dialog(dialog_type="no"):
    """Photoshop dialog windows settings using 'all': 1, 'error': 2, 'no': 3"""
    dialogs = _ps_display_dialogs()
    return dialogs.get(dialog_type, lambda: None)

def main():
    """
    Main function to process log files and convert JS events to Python.
    """
    parser = argparse.ArgumentParser(description="Process log files.")
    parser.add_argument('paths', metavar='P', type=str, nargs='+', help='Paths to log files')
    args = parser.parse_args()

    log_files = []
    for path_str in args.paths:
        path = Path(path_str)
        if path.exists():
            log_files.append(path_str)
        else:
            print(f"Path '{path_str}' does not exist. Using _browse() function.")
            log_files.append(_browse())

    try:
        for path in process_logs_gen(log_files):
            print(path)
            events = get_js_events(log_file=path)
            convert_events(path, events)
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
