# Photoshop scriptlistener to python 
tested: Adobe Photoshop Version: 23.3.2
os: Windows

Converts Photoshop 'ScriptingListenerJS.log' file into Python single-shot functions you could further explore as reference, edit and customize.
Most keys have been converted from charIDs into the more human-readable stringIDs making it more obvious what the action descriptor is doing.
The generated python file is not made to be run. It may run in some cases but these converted functions are meant to be integrated in your own code.

## Usage

Assuming the 'ScriptingListenerJS.log' file is on the Desktop, run the photoshop_scriptlistener2python.py script. 
Generates 'ScriptingListenerJS_Js2Py.py' on your Desktop

```shell
python photoshop_scriptlistener2python.py
```

## Example conversion

source: ScriptingListenerJS.log
```log
// =======================================================
var idpluginRun = stringIDToTypeID( "pluginRun" );
    var desc268 = new ActionDescriptor();
    var idNm = charIDToTypeID( "Nm  " );
    desc268.putString( idNm, """ScriptingSupport.8li""" );
    var idisFirstParty = stringIDToTypeID( "isFirstParty" );
    desc268.putBoolean( idisFirstParty, true );
    var idIjsx = charIDToTypeID( "Ijsx" );
    desc268.putBoolean( idIjsx, false );
executeAction( idpluginRun, desc268, DialogModes.NO );

// =======================================================
var idAdobeScriptAutomationScripts = stringIDToTypeID( "AdobeScriptAutomation Scripts" );
    var desc269 = new ActionDescriptor();
    var idjsNm = charIDToTypeID( "jsNm" );
    desc269.putString( idjsNm, """ScriptListenerOn""" );
    var idjsMs = charIDToTypeID( "jsMs" );
    desc269.putString( idjsMs, """[ActionDescriptor]""" );
executeAction( idAdobeScriptAutomationScripts, desc269, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc270 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc270.putInteger( idcommandID, 10 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc270.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc270, DialogModes.NO );

// =======================================================
var idnewDocument = stringIDToTypeID( "newDocument" );
    var desc271 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc271.putInteger( idDocI, 513 );
executeAction( idnewDocument, desc271, DialogModes.NO );

// =======================================================
var idhistoryStateChanged = stringIDToTypeID( "historyStateChanged" );
    var desc272 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc272.putInteger( idDocI, 513 );
    var idIdnt = charIDToTypeID( "Idnt" );
    desc272.putInteger( idIdnt, 514 );
    var idNm = charIDToTypeID( "Nm  " );
    desc272.putString( idNm, """New""" );
    var idhasEnglish = stringIDToTypeID( "hasEnglish" );
    desc272.putBoolean( idhasEnglish, true );
    var idItmI = charIDToTypeID( "ItmI" );
    desc272.putInteger( idItmI, 1 );
executeAction( idhistoryStateChanged, desc272, DialogModes.NO );

// =======================================================
var idMk = charIDToTypeID( "Mk  " );
    var desc273 = new ActionDescriptor();
    var idNw = charIDToTypeID( "Nw  " );
        var desc274 = new ActionDescriptor();
        var idartboard = stringIDToTypeID( "artboard" );
        desc274.putBoolean( idartboard, false );
        var idautoPromoteBackgroundLayer = stringIDToTypeID( "autoPromoteBackgroundLayer" );
        desc274.putBoolean( idautoPromoteBackgroundLayer, false );
        var idMd = charIDToTypeID( "Md  " );
        var idRGBM = charIDToTypeID( "RGBM" );
        desc274.putClass( idMd, idRGBM );
        var idWdth = charIDToTypeID( "Wdth" );
        var idRlt = charIDToTypeID( "#Rlt" );
        desc274.putUnitDouble( idWdth, idRlt, 491.520000 );
        var idHght = charIDToTypeID( "Hght" );
        var idRlt = charIDToTypeID( "#Rlt" );
        desc274.putUnitDouble( idHght, idRlt, 491.520000 );
        var idRslt = charIDToTypeID( "Rslt" );
        var idRsl = charIDToTypeID( "#Rsl" );
        desc274.putUnitDouble( idRslt, idRsl, 300.000000 );
        var idpixelScaleFactor = stringIDToTypeID( "pixelScaleFactor" );
        desc274.putDouble( idpixelScaleFactor, 1.000000 );
        var idFl = charIDToTypeID( "Fl  " );
        var idFl = charIDToTypeID( "Fl  " );
        var idClr = charIDToTypeID( "Clr " );
        desc274.putEnumerated( idFl, idFl, idClr );
        var idFlCl = charIDToTypeID( "FlCl" );
            var desc275 = new ActionDescriptor();
            var idH = charIDToTypeID( "H   " );
            var idAng = charIDToTypeID( "#Ang" );
            desc275.putUnitDouble( idH, idAng, 0.000000 );
            var idStrt = charIDToTypeID( "Strt" );
            desc275.putDouble( idStrt, 0.000000 );
            var idBrgh = charIDToTypeID( "Brgh" );
            desc275.putDouble( idBrgh, 50.196078 );
        var idHSBC = charIDToTypeID( "HSBC" );
        desc274.putObject( idFlCl, idHSBC, desc275 );
        var idDpth = charIDToTypeID( "Dpth" );
        desc274.putInteger( idDpth, 16 );
        var idprofile = stringIDToTypeID( "profile" );
        desc274.putString( idprofile, """sRGB IEC61966-2.1""" );
        var idGdes = charIDToTypeID( "Gdes" );
            var list8 = new ActionList();
        desc274.putList( idGdes, list8 );
    var idDcmn = charIDToTypeID( "Dcmn" );
    desc273.putObject( idNw, idDcmn, desc274 );
    var idDocI = charIDToTypeID( "DocI" );
    desc273.putInteger( idDocI, 513 );
executeAction( idMk, desc273, DialogModes.NO );

// =======================================================
var idlayersFiltered = stringIDToTypeID( "layersFiltered" );
executeAction( idlayersFiltered, undefined, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc276 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc276.putInteger( idcommandID, -704 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc276.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc276, DialogModes.NO );

```

Result: Filtered and Transpiled
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


# I've commented below out cause this part doesn't seem to run
# def newDocument_0():
#     desc271 = Dispatch("Photoshop.ActionDescriptor")
#     desc271.PutInteger(s("documentID"),  513)
#     app.ExecuteAction(s("newDocument"), desc271, dialog())
# newDocument_0()

def make_1():
    desc273 = Dispatch("Photoshop.ActionDescriptor")
    desc274 = Dispatch("Photoshop.ActionDescriptor")
    desc275 = Dispatch("Photoshop.ActionDescriptor")
    list8 = Dispatch("Photoshop.ActionList")
    desc274.PutBoolean(s("artboard"), False)
    desc274.PutBoolean(s("autoPromoteBackgroundLayer"), False)
    desc274.PutClass(s("mode"), s("RGBColorMode"))
    desc274.PutUnitDouble(s("width"), s("distanceUnit"),  491.520000)
    desc274.PutUnitDouble(s("height"), s("distanceUnit"),  491.520000)
    desc274.PutUnitDouble(s("resolution"), s("densityUnit"),  300.000000)
    desc274.PutDouble(s("pixelScaleFactor"),  1.000000)
    desc274.PutEnumerated(s("fill"), s("fill"), s("color"))
    desc275.PutUnitDouble(s("hue"), s("angleUnit"),  0.000000)
    desc275.PutDouble(s("saturation"),  0.000000)
    desc275.PutDouble(s("brightness"),  50.196078)
    desc274.PutObject(s("fillColor"), s("HSBColorClass"),  desc275)
    desc274.PutInteger(s("depth"),  16)
    desc274.PutString(s("profile"),  """sRGB IEC61966-2.1""")
    desc274.PutList(s("guides"),  list8)
    desc273.PutObject(s("new"), s("document"),  desc274)
    desc273.PutInteger(s("documentID"),  513)
    app.ExecuteAction(s("make"), desc273, dialog())

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

