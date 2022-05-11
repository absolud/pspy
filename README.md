# photoshop scriptlistener to python

'photoshop_scriptlistener2python.py' converts Photoshop Javascript action records into Python functions including human-readable stringIDs. 

## Usage

Assuming the 'ScriptingListenerJS.log' file is on the Desktop, run the photoshop_scriptlistener2python.py script. A 'ScriptingListenerJS_Js2Py.py' file will be created on the Desktop

## Example conversion

Log entry
```log
// =======================================================
var idnewDocument = stringIDToTypeID( "newDocument" );
    var desc8 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc8.putInteger( idDocI, 489 );
executeAction( idnewDocument, desc8, DialogModes.NO );

// =======================================================
var idMk = charIDToTypeID( "Mk  " );
    var desc11 = new ActionDescriptor();
    var idNw = charIDToTypeID( "Nw  " );
        var desc12 = new ActionDescriptor();
        var idNm = charIDToTypeID( "Nm  " );
        desc12.putString( idNm, """DEMO-2K""" );
        var idartboard = stringIDToTypeID( "artboard" );
        desc12.putBoolean( idartboard, false );
        var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
        desc12.putBoolean( idautoPromoteBackgroundLayer, false );
        var idMd = charIDToTypeID( "Md  " );
        var idRGBM = charIDToTypeID( "RGBM" );
        desc12.putClass( idMd, idRGBM );
        var idWdth = charIDToTypeID( "Wdth" );
        var idRlt = charIDToTypeID( "#Rlt" );
        desc12.putUnitDouble( idWdth, idRlt, 491.520000 );
        var idHght = charIDToTypeID( "Hght" );
        var idRlt = charIDToTypeID( "#Rlt" );
        desc12.putUnitDouble( idHght, idRlt, 491.520000 );
        var idRslt = charIDToTypeID( "Rslt" );
        var idRsl = charIDToTypeID( "#Rsl" );
        desc12.putUnitDouble( idRslt, idRsl, 300.000000 );
        var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
        desc12.putDouble( idpixelScaleFactor, 1.000000 );
        var idFl = charIDToTypeID( "Fl  " );
        var idFl = charIDToTypeID( "Fl  " );
        var idClr = charIDToTypeID( "Clr " );
        desc12.putEnumerated( idFl, idFl, idClr );
        var idFlCl = charIDToTypeID( "FlCl" );
            var desc13 = new ActionDescriptor();
            var idH = charIDToTypeID( "H   " );
            var idAng = charIDToTypeID( "#Ang" );
            desc13.putUnitDouble( idH, idAng, 0.000000 );
            var idStrt = charIDToTypeID( "Strt" );
            desc13.putDouble( idStrt, 0.000000 );
            var idBrgh = charIDToTypeID( "Brgh" );
            desc13.putDouble( idBrgh, 50.196078 );
        var idHSBC = charIDToTypeID( "HSBC" );
        desc12.putObject( idFlCl, idHSBC, desc13 );
        var idDpth = charIDToTypeID( "Dpth" );
        desc12.putInteger( idDpth, 16 );
        var idprofile = stringIDToTypeID( "profile" );
        desc12.putString( idprofile, """sRGB IEC61966-2.1""" );
        var idGdes = charIDToTypeID( "Gdes" );
            var list1 = new ActionList();
        desc12.putList( idGdes, list1 );
    var idDcmn = charIDToTypeID( "Dcmn" );
    desc11.putObject( idNw, idDcmn, desc12 );
    var idDocI = charIDToTypeID( "DocI" );
    desc11.putInteger( idDocI, 489 );
executeAction( idMk, desc11, DialogModes.NO );


```

Transpiled
```py
"""
Photoshop ScriptListenerJS to Pyhton
"""
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

def newDocument_0():
    desc8 = Dispatch("Photoshop.ActionDescriptor")
    desc8.PutInteger(s("documentID"),  489)
    app.ExecuteAction(s("newDocument"), desc8, dialog())

newDocument_0()

def make_1():
    desc11 = Dispatch("Photoshop.ActionDescriptor")
    desc12 = Dispatch("Photoshop.ActionDescriptor")
    desc13 = Dispatch("Photoshop.ActionDescriptor")
    list1 = Dispatch("Photoshop.ActionList")
    desc12.PutString(s("name"),  """DEMO-2K""")
    desc12.PutBoolean(s("artboard"), False)
    desc12.PutBoolean(s("autoPromoteBackgroundLayer"), False)
    desc12.PutClass(s("mode"), s("RGBColorMode"))
    desc12.PutUnitDouble(s("width"), s("distanceUnit"),  491.520000)
    desc12.PutUnitDouble(s("height"), s("distanceUnit"),  491.520000)
    desc12.PutUnitDouble(s("resolution"), s("densityUnit"),  300.000000)
    desc12.PutDouble(s("pixelScaleFactor"),  1.000000)
    desc12.PutEnumerated(s("fill"), s("fill"), s("color"))
    desc13.PutUnitDouble(s("hue"), s("angleUnit"),  0.000000)
    desc13.PutDouble(s("saturation"),  0.000000)
    desc13.PutDouble(s("brightness"),  50.196078)
    desc12.PutObject(s("fillColor"), s("HSBColorClass"),  desc13)
    desc12.PutInteger(s("depth"),  16)
    desc12.PutString(s("profile"),  """sRGB IEC61966-2.1""")
    desc12.PutList(s("guides"),  list1)
    desc11.PutObject(s("new"), s("document"),  desc12)
    desc11.PutInteger(s("documentID"),  489)
    app.ExecuteAction(s("make"), desc11, dialog())

make_1()

```

## Excluded entries in the 'ScriptingListenerJS.log' file

Below the ignore-list of entries not relevant to us.

- "idhistoryStateChanged"
- "idExternalHistoryStateChanged"
- "idmodalStateChanged"
- "idinvokeCommand"
- "idhomeScreenVisibilityChanged"
- "idMRUFileListChanged"
- "idtoolModalStateChanged"
- "invokeCommand"
- "iduiInfo"
- "idfeatureInfo"
- "idowlAction"
- "idlayersFiltered"
- "idLoadedPluginsNames"
- "identerModalWorkspace"
- "idneuralGalleryFilters"
- "idhostFocusChanged"
- "idAdobeScriptAutomationScripts"
- "idnglProfileChanged"
- "idpluginRun"
 

## Collaboration 

Yes, please! Photoshop scripting with Python has a small community on Discord https://discord.gg/VXFFy8FWVA

