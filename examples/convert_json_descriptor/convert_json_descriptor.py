"""
# convert_json_descriptor.py

author: LG
tested: Adobe Photoshop Version: 23.3.1
os: win

Convert ps data as json encoded data. 
Saves it as a json file using the key as the file name or prints results to the console
- saves json_descriptor(key:str, save_file:bool=None)
- current keys that work: application, document, layer
"""
import json
from pprint import pprint
from win32com.client import Dispatch


def s(name=None):
    '''convert string name into type id'''
    app = Dispatch("Photoshop.Application")
    return app.StringIDToTypeID(f"{name}")


def json_descriptor(key:str =None, save_file: bool=None):
    '''Extracts ps data as json encoded data'''

    app = Dispatch("Photoshop.Application")
    d01 = Dispatch("Photoshop.ActionDescriptor")
    r01 = Dispatch("Photoshop.ActionReference")
    r01.PutEnumerated(s(key), s('ordinal'), s('targetEnum'))
    d01 = app.ExecuteActionGet(r01)
    result_d01 = Dispatch("Photoshop.ActionDescriptor")
    result_d01.PutObject(s('object'), s('object'), d01)
    json_d01 = app.ExecuteAction(s('convertJSONdescriptor'), result_d01, 3)
    json_result = json_d01.GetString(s('json'))
    file = f'convert_json_descriptor_{key}.json'
    if save_file:
        with open(file, 'w', encoding='utf-8') as f:
            data = json.loads(json_result.encode("utf-8"))
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f'+ {file} saved')
    else:
        print(f'\n+ {key} data:')
        pprint(json.loads(json_result.encode("utf-8")))


def main():
    json_descriptor('application', save_file=True)
    # requires a document to be selected
    json_descriptor('document', save_file=True)
    # requires a layer to be selected
    json_descriptor('layer', save_file=True)


    # json_descriptor('application')
    # requires a document to be selected
    # json_descriptor('document')
    # requires a layer to be selected
    json_descriptor('layer')

if __name__ == '__main__':
    main()            