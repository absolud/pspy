'''
Copyright (c) 2022, Ludwig Geerman
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

# photoshop_scriptlistener2python.py

tested: Adobe Photoshop Version: 23.3.2
os: win
description: converts Photoshop's ScriptingListenerJS.log into human-readable python code. The ScriptingListenerJS.log file is usually saved to your desktop 
The ScriptingListenerJSJs2Py.py file will also be saved to the same location as the log file
'''
import sys
import re
from functools import wraps
from pprint import pprint
from pathlib import Path, PurePath
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from win32com.client import Dispatch


DEV = True
USE_XMP = False


def msg(txt, prettify=None):
    '''When dev is false nothing prints'''
    dev = DEV
    if dev:
        if prettify:
            pprint(txt)
        else:
            print(txt)


# VALUE
class BaseValueError(ValueError): pass


class ActionNameNotSetError(BaseValueError):pass


class DescriptorNameNotValidError(BaseValueError):pass


class ConvertIdConversionTypeError(BaseValueError):pass

# ATTRIBUTE
class BaseAttributeError(AttributeError): pass


class ContentNotLoadedError(ValueError): pass    


class Indenter(object):
    '''Context manager to indent code and text'''
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def style(self, text):
        '''Returns a string 
        
        Indented text based on the level
        '''
        return ('    ' * self.level + text + '\n')


class ScriptLogLoader(object):

    def __init__(self, filepath):
        self._filepath = filepath
        self._excludelist = self._ignore_list()
        self._found_file = False

    def _ignore_list(self):
        return [
        "idhistoryStateChanged",
        "idExternalHistoryStateChanged",
        "idmodalStateChanged",
        "idinvokeCommand",
        "idhomeScreenVisibilityChanged",
        "idpifInvalidatedAttributes",
        "idMRUFileListChanged",
        "idtoolModalStateChanged",
        "iduiInfo",
        "idfeatureInfo",
        "idowlAction",
        "idlayersFiltered",
        "idLoadedPluginsNames",
        "identerModalWorkspace",
        "idneuralGalleryFilters",
        "idhostFocusChanged",
        "idAdobeScriptAutomationScripts",
        "idnglProfileChanged",
        "idpluginRun",
        "idnewDocument",
        "idtoggleBrushesFlyout",
        "idbackgroundSaveCompleted"]

    def _browse(self):
        allowed_file = "JS.log"
        Tk().withdraw()
        path = askopenfilename()
        if path:
            return path
        else:
            msg('No file picked')

    def _filter_by_ignore_list(self, lines):
        '''returns a dictionary with allowed actions'''
        hold = False
        group = []
        groups = {}
        group_count = 0
        is_first_line = False
        regex_variable_name = r'(?<=var\s)(id\w+)'
        pattern_variable_name = re.compile(regex_variable_name)
        current_group_name = ""
        exclude_list = self._excludelist
        for idx, line in enumerate(lines):
            if line.startswith('// ==') and not hold:
                is_first_line = True
                hold = True
            elif is_first_line:
                match = pattern_variable_name.search(line)
                variable_name = match.group(1)
                if variable_name not in exclude_list:
                    group.append(line)
                    current_group_name = variable_name
                else:
                    hold = False
                is_first_line = False
            elif not is_first_line and hold and len(line) > 2:
                group.append(line)
            else:
                if hold:
                    hold = False
                    group_count += 1
                    group_name = f'{current_group_name}_{group_count}'
                    groups[group_name] = [x for x in group]
                    group.clear()

        return groups

    def _extract_xmp_sequence(self, sequence):
        duplicates = {i: sequence.count(i)for i in sequence if sequence.count(i) == 2}
        index_start_group = {key: sequence.index(key)+1 for key in duplicates}
        allowed_keys = [x for x in index_start_group]
        allowed_keys.sort()
        ranges = {}
        sequences = {}
        splices = {}

        for idx, grpnum in enumerate(allowed_keys):
            next_group = allowed_keys[idx + 1] if (idx + 1) < len(allowed_keys) else None
            
            if next_group:        
                ranges[grpnum] = sequence[index_start_group[grpnum]
                    :index_start_group[next_group]-1]

                splices[grpnum] = {
                    'start': index_start_group[grpnum]-1,
                    'end': index_start_group[next_group]-1
                }

            else:
                ranges[grpnum] = sequence[index_start_group[grpnum]:len(sequence)]
                splices[grpnum] = {
                    'start': index_start_group[grpnum],
                    'end': len(sequence)
                }

        sequences['count'] = len(sequence)
        sequences['splices'] = splices
        sequences['parts'] = ranges
        return sequences

    def _correct_xmp(self, action_set):
        collected_id = []
        locked = False
        count = 0

        for idx, line in enumerate(action_set):
            # lookup strings for xmp
            start_pattern = '"""<'
            start_pattern_corrected = "r'<"
            end_pattern = '""" );'
            end_pattern_corrected = "' );"
 
            if start_pattern in line:
                corrected_start = line.replace(start_pattern, start_pattern_corrected)
                collected_id.append(idx)
                action_set[idx] = corrected_start
                locked = True
            # making sure the first recorded idx is not captured twice
            if locked and not line.startswith(end_pattern):
                collected_id.append(idx)
            elif line.startswith(end_pattern):
                corrected_end = line.replace(end_pattern, end_pattern_corrected)
                collected_id.append(idx)
                action_set[idx] = corrected_end
                locked = False
            count = idx

        seq = self._extract_xmp_sequence(collected_id)
        text = ''
        removable_slots = []

        reg_datatype = r"(?s),\s(\s?(?:[\w|\W].*?)(?:.))\s\);"
        subst = ", \"\"\"xmp\"\"\" );"
        seq_keys = seq["parts"].keys()

        for key in seq_keys:
            xmp_code_seq = seq["parts"][key]
            start = seq["splices"][key]['start']
            end = seq["splices"][key]['end']
            for l in xmp_code_seq:
                text += action_set[l]
            matched = re.sub(reg_datatype, subst, text, 0, re.MULTILINE)

            use_xmp = USE_XMP

            if use_xmp:
                action_set[key] = text
            else:
                action_set[key] = matched

            for remove_id in seq["parts"][key][1:]:
                removable_slots.append(remove_id)

            text = ''
        '''
        Filter only the result without the appended lines
        '''
        result = [x for idx, x in enumerate(
            action_set) if action_set.index(x) not in removable_slots]
        '''
        Overide actionset with new corrected data
        '''
        action_set = result
        return action_set

    def _filter_xmp(self, actions):
        allowed_keys = [x for x in actions]
        action_sets = actions
        corrected_action_set = []

        for key in allowed_keys:
            corrected_action_set.append(self._correct_xmp(action_sets[key]))

        return corrected_action_set

    def _load_content(self):
        data = None
        file_path = self._file_info['path']
        with open(file_path, 'r', newline='') as f:
            msg('+ Loading lines ...')
            data_raw = (x for x in f.readlines())
            data_raw = self._filter_by_ignore_list(data_raw)
            data = self._filter_xmp(data_raw)
            if data:
                msg('+ Success! data loaded \n')
                self._found_file = True
    
        return data

    def _load_file(self):
        file_path = self._filepath
        if file_path and Path(file_path).exists():
            msg(f"+ Custom file detected: loading {file_path} ...")
        else:
            file_path = self._browse()
            msg(f'+ File detected: loading {file_path} ...')

        path = Path(file_path)
        file_info = {
             'folder': path.parent,
             'name': path.stem,
             'path': path,
         }
        # self._loaded_content = self._load_content(self._file_info['path'])
        self._file_info = file_info
        msg(f'+ {file_info}')

    def remove_from_ignore_list(self, *args):
        '''The args should be in the ignorelist
        
        otherwise nothing happens'''
        ignore_list = self._ignore_list()
        adjusted_ignore_list = (x for x in ignore_list 
                                if x not in args)
        self._excludelist = list(adjusted_ignore_list)
        # msg(self._excludelist, 1)
    
    def add_to_ignore_list(self, *args):
        '''Pass var names which starts with id so these can be ignored onwards'''
        excludelist = self._excludelist
        adjusted_excludelist = [x for x in args 
                                if x.startswith('id') and
                                x not in excludelist]
        self._excludelist = [y for x in [excludelist, adjusted_excludelist] 
                             for y in x]
        # msg(self._excludelist, 1)

    def load(self):
        self._load_file()

    def content(self):
        return self._load_content()

    def folder(self):
        return self._file_info['folder']

    def file_name(self):
        return self._file_info['name']


class ScriptLogParser(object):
    _regex = {
        'var_id': r'\s*var\s(\w+)\W+(\w+)\(\s?(.+)\s\)',
        'descriptor': r'\s*var\s(\w+)\W+new\s(\w+)\(\);',
        'datatype': r'\s*(\w+)\.(\w+)\(\s?(.+)\s\);',
        'exec': r'(\w+)\(\s?(.+)\s\)',
        'new_file': r'new\sFile\(\s(\W.*\")\s\W*',
        'start': r'^var\s',
        'end': r'^executeAction\('
    }

    def __init__(self):
        self._name = ''
        self._vars = {}
        self._setup_regex_compiles()
    
    def _compile(self, pattern):
        return re.compile(pattern)

    def _setup_regex_compiles(self):
        compile_ = self._compile
        regex = self._regex
        self.pattern_var_id = compile_(regex['var_id'])
        self.pattern_descriptor = compile_(regex['descriptor'])
        self.pattern_datatype = compile_(regex['datatype'])
        self.pattern_exec = compile_(regex['exec'])
        self.pattern_new_file = compile_(regex['new_file'])

    def _convert_exec(self, line):
        match_exec = self.pattern_exec.match(line)
        if match_exec:
            exec_func = match_exec.group(1)
            values = match_exec.group(2)
            first_letter = exec_func[0].upper()
            exec_func_converted = first_letter + exec_func[1:]
            values = values.split(",")
            vars_ = self._vars

            for idx, prop in enumerate(values):
                prop = prop.strip()
                if prop in vars_:
                    values[idx] = vars_[prop]
            value_prop2string = ",".join(values)
            return f"app.{exec_func_converted}({value_prop2string})"

    def _convert_datatype(self, line):
        match_datatype = self.pattern_datatype.match(line)
        if match_datatype:
            descriptor = match_datatype.group(1)
            datatype = match_datatype.group(2)
            values = match_datatype.group(3)
            first_letter_upper = datatype[0].upper()
            datatype_converted = first_letter_upper + datatype[1:]
            values = values.split(",")

            for idx, prop in enumerate(values):
                prop = prop.strip()
                # looks for new File( "link" ) and replaces it
                if "new File(" in prop:
                    match_new_file = self.pattern_new_file.match(prop)
                    if match_new_file:
                        link = match_new_file.group(1)
                        values[idx] = link
                if prop in self._vars:
                    if prop == "idnull":
                        self._vars[prop] = 's("target")'
                    values[idx] = self._vars[prop]
            value_prop2string = ", ".join(values)
            return f"{descriptor}.{datatype_converted}({value_prop2string})"

    def _descriptor_getter(self, variable, descriptor):
        return {
            "ActionDescriptor": f'{variable} = Dispatch("Photoshop.ActionDescriptor")',
            "ActionReference": f'{variable} = Dispatch("Photoshop.ActionReference")',
            "ActionList": f'{variable} = Dispatch("Photoshop.ActionList")',
        }.get(descriptor, None)

    def _convert_descriptor(self, line):
        match_descriptor = self.pattern_descriptor.match(line)
        if match_descriptor:
            var_name = match_descriptor.group(1)
            descriptor = match_descriptor.group(2)
            result = self._descriptor_getter(var_name, descriptor)
            return result

    def _conversion_types(self):
        return ("s2t", "s2c", "c2t", "c2s", "t2s", "t2c")

    def _ps_convertion_funcs(self, idx):
        app = Dispatch("Photoshop.Application")
        return {
            "c2t": lambda: app.CharIDToTypeID(idx),
            "s2t": lambda: app.StringIDToTypeID(idx),
            "t2s": lambda: app.TypeIDToStringID(idx),
            "t2c": lambda: app.TypeIDToCharID(idx),
            "c2s": lambda: app.TypeIDToStringID(app.CharIDToTypeID(idx)),
            "s2c": lambda: app.TypeIDToCharID(app.StringIDToTypeID(idx)),
        }

    def _convert_id(self, idx, conversion_type="s2t"):
        app = Dispatch("Photoshop.Application")
        conversion_types = self._conversion_types
        ps_conversion_funcs = self._ps_convertion_funcs
        if conversion_type in conversion_types():
            id_convertion_dict = ps_conversion_funcs(idx)
            return id_convertion_dict.get(conversion_type, lambda: None)()
        else:
            print(
                f'Attention! The conversion type "{conversion_type}" is not a valid choice. '
                f"Please choose from one of the following: {self._conversion_types()}"
            )
            raise ConvertIdConversionTypeError(conversion_type)

    def _c2s(self, idchar):
        '''Takes a char id and converts it to a string id'''
        convert_id = self._convert_id
        return convert_id(idchar, "c2s")

    def _convert_var_id(self, line, group_count=None, position=None):
        match_var_id = self.pattern_var_id.match(line)
        id_value = ""
        var_id = {}

        if match_var_id:
            var_name = match_var_id.group(1)
            func = match_var_id.group(2)
            id_string = match_var_id.group(3)
            id_string = id_string.replace('"', "")
            convert_func = 's'

            if func.startswith("charID"):
                id_value = self._c2s(id_string)
                if id_value == '':
                    convert_func = 'c'
                    id_value = id_string
            elif func.startswith("stringID"):
                id_value = id_string

            var_id["var"] = var_name
            var_id["value"] = f'{convert_func}("{id_value}")'
            self._vars[var_name] = f'{convert_func}("{id_value}")'
            if position == 0:
                self._name = f"{id_value}_{group_count}"

    def _convert(self, line, position, group_count=None):
        _line = line
        convert_var_id = self._convert_var_id
  
        if position == 0:
            convert_var_id(_line, group_count, position)
        elif position == -1:
            _line = self._convert_exec(_line)
        else:
            if "charID" in _line or "stringID" in _line:
                convert_var_id(_line)
            elif any(item in _line for item in ["ActionDescriptor", "ActionReference", "ActionList"]):
                _line = self._convert_descriptor(_line)

            elif ".put" in _line:
                _line = self._convert_datatype(_line)
        return _line

    def _get_actions(self, groupnum):
        '''AI is creating summary for _get_actions

        Args:
            groupnum (int): current number id

        Yields:
            dict:   "id", "name", "descriptors", "datatypes", "execute"
        '''
        regex = self._regex
        compile_ = self._compile
        pattern_start = compile_(regex['start'])
        pattern_end = compile_(regex['end'])
        # count serves as start and end of am action group
        count = 0
        allow_in_group = False
        group_count = groupnum
        action_group = {}
        lines = self._lines
        for idx, line in enumerate(lines):
            if pattern_start.match(line):
                allow_in_group = True
                self._vars["false"] = "False"
                self._vars["true"] = "True"
                self._vars["DialogModes.NO"] = " dialog()"
                self._vars["undefined"] = "None"
                collected_descriptors = []
                collected_datatypes = []
                exec_line = ""

            if pattern_end.match(line):
                allow_in_group = False
                # Returns -1 to denote end of a group
                count = count - (count + 1)
                converted_line = self._convert(line, count)
                if "app." in converted_line:
                    exec_line = converted_line
                # clear out all stored vars
                self._vars.clear()
                yield {
                    "id": group_count,
                    "name": self._name,
                    "descriptors": collected_descriptors,
                    "datatypes": collected_datatypes,
                    "execute": exec_line,
                }
                collected_descriptors.clear()
                collected_datatypes.clear()
                exec_line = ""
                count = 0
                group_count += 1

            if allow_in_group:
                converted_line = self._convert(line, count, group_count)
                # print(converted_line + "\n")
                if ".Put" in converted_line:
                    collected_datatypes.append(converted_line)

                if "Dispatch(" in converted_line:
                    collected_descriptors.append(converted_line)
                count += 1

    def boilerplate_code(self, names=None, file=None):
        '''Generates upper part of the boilerplate code
        
        Constructs code including indentation
        Args:
            names (list, optional): list of function names. Defaults to None.
            file (io, optional): file o write to. Defaults to None.
        '''
        export_file = msg
        if file:
            export_file = file.write
        # start py doc boilerplate code and indenting
        export_file(Indenter().style(f'"""'))
        export_file(Indenter().style("Photoshop ScriptListenerJS to Python"))
        # list function names if true
        if names:
            export_file(Indenter().style("- Overview functions"))
            export_file(Indenter().style(f"- {names}"))
        export_file(Indenter().style('"""'))
        # imports
        export_file(Indenter().style("from win32com.client import Dispatch"))
        export_file(Indenter().style(""))
        export_file(Indenter().style(""))
        # global app reference
        export_file(Indenter().style('app = Dispatch("Photoshop.Application")'))
        export_file(Indenter().style(""))
        # required string to type id converter function
        export_file(Indenter().style("def s(name):"))
        with Indenter() as indent:
            export_file(indent.style("'''convert string name into type id'''"))    
            export_file(indent.style('return app.StringIDToTypeID(f"{name}")'))  
        export_file(Indenter().style(""))
        # required charid to type id converter function
        export_file(Indenter().style("def c(name):"))
        with Indenter() as indent:
            export_file(indent.style("'''convert char name into type id'''"))        
            export_file(indent.style('return app.CharIDToTypeID(f"{name}")'))
        export_file(Indenter().style(""))
        # required dialog constants
        export_file(Indenter().style('def ps_display_dialogs():'))
        with Indenter() as indent:
            export_file(indent.style("'''Dictionary with dialog constants'''"))    
            export_file(indent.style('return {"all": 1, "error": 2, "no": 3}'))    
        export_file(Indenter().style(""))
        # required dialog function
        export_file(Indenter().style('def dialog(dialog_type="no"):'))
        with Indenter() as indent:
            export_file(indent.style("'''Photoshop dialog windows settings using \"all\": 1, \"error\": 2, \"no\": 3'''"))    
            export_file(indent.style('dialogs = ps_display_dialogs()'))    
            export_file(indent.style('return dialogs.get(dialog_type, lambda: None)'))
        export_file(Indenter().style(""))

    def add_new_lines(self, lines):
        '''temporarely stores a collection of lines globally

        Args:
            lines (list): [code lines]
        '''
        self._lines = lines
    
    def get_actions(self, idx):
        '''returns a usable action fromt the filtered log'''
        return self._get_actions(idx)

    def generate_code(self, action, file=None):
        '''Generates the action descriptor functions

        Args:
            action (dict): [keys - descriptors, datatypes, execute, name]
            file (io, optional): file to write to. Defaults to None.
        '''
        export_file = msg
        if file:
            export_file = file.write
        code = action
        export_file(Indenter().style(""))
        export_file(Indenter().style(f'def {code["name"]}():'))
        with Indenter() as indent:
            for desc in code["descriptors"]:
                export_file(indent.style(desc))
            for action in code["datatypes"]:
                export_file(indent.style(action))
            export_file(indent.style(code["execute"]))
        export_file(Indenter().style(""))
        export_file(Indenter().style(f'{code["name"]}()'))


def main(log_file_path=None):
    # loads essential entries only
    log = ScriptLogLoader(log_file_path)
    log.load()
    log_file_folder = log.folder()
    log_file_name = log.file_name()
    new_file_name = f'{log_file_name}_Js2Py.py'
    new_file_path = log_file_folder.joinpath(new_file_name)
    content = log.content()
  
    # transpile to python
    with open(new_file_path, 'w') as f:
        parser = ScriptLogParser()
        parser.boilerplate_code(file=f) # file=f
        for idx, action in enumerate(content):
            parser.add_new_lines(action)
            actions_transpiled = parser.get_actions(idx)
            for ac in actions_transpiled:
                parser.generate_code(ac, file=f) #file=f
    

if (__name__) == "__main__":
 
    user = Path.home().stem
    log_file_path = f'C:\\Users\\{user}\\Desktop\\ScriptingListenerJS.log'
    main(log_file_path=log_file_path)
