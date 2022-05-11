# PSPY Photoshop scripting with Python

'lg_scriptlistener_2_Python.py' transpiles Photoshop Javascript action records into Python functions including human-readable stringIDs. 

## Photoshop action descriptors in Python

Action descriptor logic is pretty much hidden from us and because we won't necesseraly be able to structure descriptor code by intuition alone, a converter is essential to make sense of the action descriptor formatting and charID names. The 'ScriptingListenerJS.log' file we usually use as a reference contains Javascript log entries of Photoshop's actions and events that has executed while we've been interacting with the application. By filtering out the useful parts and converting these entries into Python functions you could further inspect, adjust and execute customized solutions in Photoshop.

## Usage

Assuming the 'ScriptingListenerJS.log' file is on the Desktop, run the lg_scriptlistener_2_Python script.

A 'ScriptingListenerJS_Js2Py.py' file will be created on the Desktop

## Example conversion

Log entry
```log
// =======================================================
var idsetd = charIDToTypeID( "setd" );
    var desc422 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref15 = new ActionReference();
        var idAdjL = charIDToTypeID( "AdjL" );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref15.putEnumerated( idAdjL, idOrdn, idTrgt );
    desc422.putReference( idnull, ref15 );
    var idT = charIDToTypeID( "T   " );
        var desc423 = new ActionDescriptor();
        var idpresetKind = stringIDToTypeID( "presetKind" );
        var idpresetKindType = stringIDToTypeID( "presetKindType" );
        var idpresetKindCustom = stringIDToTypeID( "presetKindCustom" );
        desc423.putEnumerated( idpresetKind, idpresetKindType, idpresetKindCustom );
        var idAdjs = charIDToTypeID( "Adjs" );
            var list12 = new ActionList();
                var desc424 = new ActionDescriptor();
                var idLclR = charIDToTypeID( "LclR" );
                desc424.putInteger( idLclR, 1 );
                var idBgnR = charIDToTypeID( "BgnR" );
                desc424.putInteger( idBgnR, 315 );
                var idBgnS = charIDToTypeID( "BgnS" );
                desc424.putInteger( idBgnS, 345 );
                var idEndS = charIDToTypeID( "EndS" );
                desc424.putInteger( idEndS, 15 );
                var idEndR = charIDToTypeID( "EndR" );
                desc424.putInteger( idEndR, 45 );
                var idH = charIDToTypeID( "H   " );
                desc424.putInteger( idH, 0 );
                var idStrt = charIDToTypeID( "Strt" );
                desc424.putInteger( idStrt, -7 );
                var idLght = charIDToTypeID( "Lght" );
                desc424.putInteger( idLght, 0 );
            var idHsttwo = charIDToTypeID( "Hst2" );
            list12.putObject( idHsttwo, desc424 );
        desc423.putList( idAdjs, list12 );
    var idHStr = charIDToTypeID( "HStr" );
    desc422.putObject( idT, idHStr, desc423 );
executeAction( idsetd, desc422, DialogModes.NO );

```

Transpiled
```py
"""
LG Photoshop ScriptListenerJS to Python
"""


from win32com.client import Dispatch


def s(name):
    '''convert string name into type id'''
    app = Dispatch("Photoshop.Application")
    return app.StringIDToTypeID(f"{name}")

def set_1():
    app = Dispatch("Photoshop.Application")
    desc422 = Dispatch("Photoshop.ActionDescriptor")
    ref15 = Dispatch("Photoshop.ActionReference")
    desc423 = Dispatch("Photoshop.ActionDescriptor")
    list12 = Dispatch("Photoshop.ActionList")
    desc424 = Dispatch("Photoshop.ActionDescriptor")
    ref15.PutEnumerated(s("adjustmentLayer"), s("ordinal"), s("targetEnum"))
    desc422.PutReference(s("target"),  ref15)
    desc423.PutEnumerated(s("presetKind"), s("presetKindType"), s("presetKindCustom"))
    desc424.PutInteger(s("localRange"),  1)
    desc424.PutInteger(s("beginRamp"),  315)
    desc424.PutInteger(s("beginSustain"),  345)
    desc424.PutInteger(s("endSustain"),  15)
    desc424.PutInteger(s("endRamp"),  45)
    desc424.PutInteger(s("hue"),  0)
    desc424.PutInteger(s("saturation"),  -7)
    desc424.PutInteger(s("lightness"),  0)
    list12.PutObject(s("hueSatAdjustmentV2"),  desc424)
    desc423.PutList(s("adjustment"),  list12)
    desc422.PutObject(s("to"), s("hueSaturation"),  desc423)
    app.ExecuteAction(s("set"), desc422, 3)


set_1()
```

## Excluded entries in the 'ScriptingListenerJS.log' file

Some entries are useless to us and some include actions usually not accessible through regular actions in Photoshop, thus giving us access to hidden functionality we can edit and customize. 

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
 
Photoshop updates may introduce new entries from time to time which means that the ignore-list would need to be extended with these new actions or events deemed irrelevant. If for some reason you want to include one of these excluded actions back into the search, just comment it out in the script. A small few may trigger convertion errors if included.

## Collaboration 

Yes, please! Photoshop scripting with Python has a small community on Discord https://discord.gg/VXFFy8FWVA

