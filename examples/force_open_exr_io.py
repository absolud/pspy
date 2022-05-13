# force_open_exr_io.py
"""
Simple customized script example of the generated file below. For demonstration purpose only. 
Shows how to force open exr file with 3DIO in Photoshop and convert to 16b

command-line example:
python force_open_exr_io.py "K:\\houdini projects\\lg_laboratory\\lg_laboratory_experiments\\render\\sphere_uv\\baseColor.0059.exr"

###########################################################
###########################################################

ORIGINAL GENERATED OUTPUT WITH 'photoshop_scriptlistener2python.py':

from win32com.client import Dispatch


app = Dispatch("Photoshop.Application")

def s(name):
    '''convert string name into type id'''
    return app.StringIDToTypeID(f"{name}")

def c(name):
    '''convert char name into type id'''
    return app.CharIDToTypeID(f"{name}")

def ps_display_dialogs():
    '''Dictionary with dialog constants'''
    return {"all": 1, "error": 2, "no": 3}

def dialog(dialog_type="no"):
    '''Photoshop dialog windows settings using "all": 1, "error": 2, "no": 3'''
    dialogs = ps_display_dialogs()
    return dialogs.get(dialog_type, lambda: None)

def open_1():
    desc8 = Dispatch("Photoshop.ActionDescriptor")
    desc9 = Dispatch("Photoshop.ActionDescriptor")
    desc8.PutBoolean(s("dontRecord"), False)
    desc8.PutBoolean(s("forceNotify"), True)
    desc8.PutPath(s("target"), "K:\\houdini projects\\lg_laboratory\\lg_laboratory_experiments\\render\\sphere_uv\\baseColor.0059.exr")
    desc9.PutBoolean(c("ioty"), False)
    desc9.PutBoolean(c("iosa"), False)
    desc9.PutBoolean(c("ioac"), False)
    desc9.PutBoolean(c("ioal"), False)
    desc9.PutBoolean(c("iocm"), False)
    desc9.PutBoolean(c("ioca"), False)
    desc9.PutBoolean(c("iocd"), False)
    desc9.PutBoolean(c("ioll"), False)
    desc9.PutBoolean(c("ioci"), False)
    desc9.PutBoolean(c("iodw"), False)
    desc9.PutBoolean(c("iocg"), False)
    desc9.PutBoolean(c("iosr"), True)
    desc9.PutBoolean(c("ioso"), True)
    desc9.PutBoolean(c("iosh"), True)
    desc9.PutInteger(c("iocw"),  1000)
    desc8.PutObject(s("as"), s("3d-io Exr-IO"),  desc9)
    desc8.PutInteger(s("documentID"),  489)
    app.ExecuteAction(s("open"), desc8, dialog())

open_1()

def convertMode_2():
    desc16 = Dispatch("Photoshop.ActionDescriptor")
    desc16.PutInteger(s("depth"),  16)
    desc16.PutBoolean(s("merge"), False)
    app.ExecuteAction(s("convertMode"), desc16, dialog())

convertMode_2()

"""
###########################################################
# CUSTOMIZED force_open_exr_io.py
###########################################################
import os
import sys
from random import randrange
from pathlib import Path, PurePath

###########################################################
# Required boilerplate code
###########################################################
from win32com.client import Dispatch


app = Dispatch("Photoshop.Application")

def s(name):
    '''convert string name into type id'''
    return app.StringIDToTypeID(f"{name}")

def c(name):
    '''convert char name into type id'''
    return app.CharIDToTypeID(f"{name}")

def ps_display_dialogs():
    '''Dictionary with dialog constants'''
    return {"all": 1, "error": 2, "no": 3}

def dialog(dialog_type="no"):
    '''Photoshop dialog windows settings using "all": 1, "error": 2, "no": 3'''
    dialogs = ps_display_dialogs()
    return dialogs.get(dialog_type, lambda: None)

###########################################################
# customized action descriptors
###########################################################

def force_open_exr_3dio(file:str):
    '''Force-open exr file, requires 3DIO to be installed.

    Args:
        file (str): target exr file path to open

    Returns:
        dict: doc_id, name, folder
    '''
    random_id = randrange(222, 999, 3)
    desc8 = Dispatch("Photoshop.ActionDescriptor")
    desc9 = Dispatch("Photoshop.ActionDescriptor")
    desc8.PutBoolean(s("dontRecord"), False)
    desc8.PutBoolean(s("forceNotify"), True)
    desc8.PutPath(s("target"), file)
    desc9.PutBoolean(c("ioty"), False)
    desc9.PutBoolean(c("iosa"), False)
    desc9.PutBoolean(c("ioac"), False)
    desc9.PutBoolean(c("ioal"), False)
    desc9.PutBoolean(c("iocm"), False)
    desc9.PutBoolean(c("ioca"), False)
    desc9.PutBoolean(c("iocd"), False)
    desc9.PutBoolean(c("ioll"), False)
    desc9.PutBoolean(c("ioci"), False)
    desc9.PutBoolean(c("iodw"), False)
    desc9.PutBoolean(c("iocg"), False)
    desc9.PutBoolean(c("iosr"), True)
    desc9.PutBoolean(c("ioso"), True)
    desc9.PutBoolean(c("iosh"), True)
    desc9.PutInteger(c("iocw"),  1000)
    desc8.PutObject(s("as"), s("3d-io Exr-IO"),  desc9)
    desc8.PutInteger(s("documentID"),  random_id)
    app.ExecuteAction(s("open"), desc8, dialog())
    # extended functionality
    file_name = file.stem
    folder = file.parent
    # dictionary with file info
    return {"doc_id": random_id, 'name': file_name, 'folder': folder}

def convert_bitdepth(bit_depth:int):
    '''Convert bitdepth'''
    desc16 = Dispatch("Photoshop.ActionDescriptor")
    desc16.PutInteger(s("depth"),  bit_depth)
    desc16.PutBoolean(s("merge"), False)
    app.ExecuteAction(s("convertMode"), desc16, dialog())


if __name__ == "__main__":

    # Command line argument check
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the path to be listed')
        sys.exit()

    exr_file = Path(sys.argv[1])

    if not exr_file.is_file():
        print('The exr path specified does not exist')
        sys.exit()

    # force open and convert to 16b
    exr_doc = force_open_exr_3dio(file=exr_file)
    convert_bitdepth(bit_depth=16)

    # test returned exr_doc dict
    print(f"Opened a new exr doc with doc id: {exr_doc['doc_id']}, name: {exr_doc['name']}")
    print(f"Parent folder of the exr: {exr_doc['folder']}")

