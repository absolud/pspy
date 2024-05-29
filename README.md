# PS LOG CONVERTER
tested: Adobe Photoshop Version: 25.9.0
os: Windows

## CURRENT VERSION
This script processes Photoshop's ScriptListener log files and converts PS events into human readable Python functions. This is a renewed version compared to "photoshop_scriptlistener2python.py" script.

### Improvements include:
- added typing and docstring to the functions
- better handling of xmpmeta entries
- excluded events are now stored in a JSON file and loaded independently "excluded_events.json"
- better handling of file paths
- handles really large log files easily
- better handling of commandline arguments
- handle multiple log files if needed (commandline)
- processing based on generators and coroutines
- new name for the script "ps_log_converter.py"
- log files are sanitzed and saved in the "__temp" folder than removed after processing
- converted python scripts are now stored in a separate folder "__temp"


### ATTENTION:
- excluded_events.json has to be present for the script to run
- There is always a chance if the script stops working that a new event has been introduced in Photoshop. In this case, whatever this event name is, it should be added to the ignore list.

### Example
01 single entry:
```shell
python ps_log_converter.py JS.log
```

### Example
02 browse entry:
If the file path doesn't exist or mistyped you will be asked to browse to a valid log file for processing. 
The browsing mode only allows for single file conversion.

### Example
03 multiple entries:
Only terminal command line arguments will support batch conversions (multiple log files).
```shell
python ps_log_converter.py JS01.log JS02.log JS03.log
```

### Example
original ScriptingListenerJS.log file
```log
// =======================================================
var idLoadedPluginsNames = stringIDToTypeID( "LoadedPluginsNames" );
    var desc235 = new ActionDescriptor();
    var idPlgn = charIDToTypeID( "Plgn" );
        var list3 = new ActionList();
        list3.putString( """Adaptive Wide Angle...""" );
        list3.putString( """Average""" );
        list3.putString( """Camera Raw""" );
        list3.putString( """Camera Raw Filter""" );
        list3.putString( """Picture Package Filter...""" );
        list3.putString( """Matlab Operation""" );
        list3.putString( """Cineon""" );
        list3.putString( """Clouds""" );
        list3.putString( """Difference Clouds""" );
        list3.putString( """Crop and Straighten Photos""" );
        list3.putString( """Dicom""" );
        list3.putString( """Export Color Lookup Tables""" );
        list3.putString( """Render Color Lookup Grid""" );
        list3.putString( """FastCore Routines""" );
        list3.putString( """Filter Gallery...""" );
        list3.putString( """Colored Pencil...""" );
        list3.putString( """Cutout...""" );
        list3.putString( """Dry Brush...""" );
        list3.putString( """Film Grain...""" );
        list3.putString( """Fresco...""" );
        list3.putString( """Neon Glow...""" );
        list3.putString( """Paint Daubs...""" );
        list3.putString( """Palette Knife...""" );
        list3.putString( """Plastic Wrap...""" );
        list3.putString( """Poster Edges...""" );
        list3.putString( """Rough Pastels...""" );
        list3.putString( """Smudge Stick...""" );
        list3.putString( """Sponge...""" );
        list3.putString( """Underpainting...""" );
        list3.putString( """Watercolor...""" );
        list3.putString( """Accented Edges...""" );
        list3.putString( """Angled Strokes...""" );
        list3.putString( """Crosshatch...""" );
        list3.putString( """Dark Strokes...""" );
        list3.putString( """Ink Outlines...""" );
        list3.putString( """Spatter...""" );
        list3.putString( """Sprayed Strokes...""" );
        list3.putString( """Sumi-e...""" );
        list3.putString( """Diffuse Glow...""" );
        list3.putString( """Glass...""" );
        list3.putString( """Ocean Ripple...""" );
        list3.putString( """Bas Relief...""" );
        list3.putString( """Chalk && Charcoal...""" );
        list3.putString( """Charcoal...""" );
        list3.putString( """Chrome...""" );
        list3.putString( """Cont� Crayon...""" );
        list3.putString( """Graphic Pen...""" );
        list3.putString( """Halftone Pattern...""" );
        list3.putString( """Note Paper...""" );
        list3.putString( """Photocopy...""" );
        list3.putString( """Plaster...""" );
        list3.putString( """Reticulation...""" );
        list3.putString( """Stamp...""" );
        list3.putString( """Torn Edges...""" );
        list3.putString( """Water Paper...""" );
        list3.putString( """Glowing Edges...""" );
        list3.putString( """Craquelure...""" );
        list3.putString( """Grain...""" );
        list3.putString( """Mosaic Tiles...""" );
        list3.putString( """Patchwork...""" );
        list3.putString( """Stained Glass...""" );
        list3.putString( """Texturizer...""" );
        list3.putString( """ApplyImageDataFilter""" );
        list3.putString( """Topaz Gigapixel AI...""" );
        list3.putString( """GatherImageDataFilter""" );
        list3.putString( """GoZPlugIn...""" );
        list3.putString( """Halide Bottlenecks""" );
        list3.putString( """HDRMergeUI""" );
        list3.putString( """JPEG 2000""" );
        list3.putString( """Lens Blur...""" );
        list3.putString( """Lens Correction...""" );
        list3.putString( """Liquify...""" );
        list3.putString( """Parametric Filter""" );
        list3.putString( """SP Substance Suite""" );
        list3.putString( """Measurement Core""" );
        list3.putString( """MMXCore Routines""" );
        list3.putString( """Multiprocessor Support""" );
        list3.putString( """NTSC Colors""" );
        list3.putString( """Portable Bit Map""" );
        list3.putString( """PCX""" );
        list3.putString( """Pixar""" );
        list3.putString( """Radiance""" );
        list3.putString( """Save for Web...""" );
        list3.putString( """ScriptingSupport""" );
        list3.putString( """ScriptListener...""" );
        list3.putString( """Solarize""" );
        list3.putString( """Crystallize...""" );
        list3.putString( """Pointillize...""" );
        list3.putString( """Pinch...""" );
        list3.putString( """Extrude...""" );
        list3.putString( """Fibers...""" );
        list3.putString( """Lens Flare...""" );
        list3.putString( """Ripple...""" );
        list3.putString( """Shear...""" );
        list3.putString( """Twirl...""" );
        list3.putString( """Polar Coordinates...""" );
        list3.putString( """Smart Blur...""" );
        list3.putString( """Spherize...""" );
        list3.putString( """Wind...""" );
        list3.putString( """ZigZag...""" );
        list3.putString( """Mezzotint...""" );
        list3.putString( """Radial Blur...""" );
        list3.putString( """Wave...""" );
        list3.putString( """Crop and Straighten Photos Filter""" );
        list3.putString( """De-Interlace...""" );
        list3.putString( """Displace...""" );
        list3.putString( """Tiles...""" );
        list3.putString( """BMP""" );
        list3.putString( """Targa""" );
        list3.putString( """IFF Format""" );
        list3.putString( """HSB/HSL""" );
        list3.putString( """Paths to Illustrator...""" );
        list3.putString( """OpenEXR""" );
        list3.putString( """Color Halftone...""" );
        list3.putString( """Mean""" );
        list3.putString( """Summation""" );
        list3.putString( """Minimum""" );
        list3.putString( """Maximum""" );
        list3.putString( """Median""" );
        list3.putString( """Variance""" );
        list3.putString( """Standard Deviation""" );
        list3.putString( """Skewness""" );
        list3.putString( """Kurtosis""" );
        list3.putString( """Range""" );
        list3.putString( """Entropy""" );
        list3.putString( """Topaz Photo AI...""" );
        list3.putString( """TPAIApplyImageDataFilter""" );
        list3.putString( """Topaz Photo AI...""" );
        list3.putString( """TPAIGatherImageDataFilter""" );
        list3.putString( """Vanishing Point...""" );
        list3.putString( """Wireless Bitmap""" );
        list3.putString( """WIA Support...""" );
    desc235.putList( idPlgn, list3 );
executeAction( idLoadedPluginsNames, desc235, DialogModes.NO );

// =======================================================
var idnewDocument = stringIDToTypeID( "newDocument" );
    var desc236 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc236.putInteger( idDocI, 59 );
executeAction( idnewDocument, desc236, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc237 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc237.putInteger( idLvl, 1 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var identer = stringIDToTypeID( "enter" );
    desc237.putEnumerated( idStte, idStte, identer );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc237.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc237.putString( idTtl, """Missing Profile""" );
executeAction( idmodalStateChanged, desc237, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc238 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc238.putInteger( idLvl, 0 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var idexit = stringIDToTypeID( "exit" );
    desc238.putEnumerated( idStte, idStte, idexit );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc238.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc238.putString( idTtl, """Missing Profile""" );
executeAction( idmodalStateChanged, desc238, DialogModes.NO );

// =======================================================
var idhistoryStateChanged = stringIDToTypeID( "historyStateChanged" );
    var desc239 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc239.putInteger( idDocI, 59 );
    var idIdnt = charIDToTypeID( "Idnt" );
    desc239.putInteger( idIdnt, 61 );
    var idNm = charIDToTypeID( "Nm  " );
    desc239.putString( idNm, """Open""" );
    var idhasEnglish = stringIDToTypeID( "hasEnglish" );
    desc239.putBoolean( idhasEnglish, true );
    var idItmI = charIDToTypeID( "ItmI" );
    desc239.putInteger( idItmI, 1 );
    var idcommandID = stringIDToTypeID( "commandID" );
    desc239.putInteger( idcommandID, 0 );
executeAction( idhistoryStateChanged, desc239, DialogModes.NO );

// =======================================================
var idhomeScreenVisibilityChanged = stringIDToTypeID( "homeScreenVisibilityChanged" );
    var desc240 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc240.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc240.putBoolean( idforceNotify, true );
    var idVsbl = charIDToTypeID( "Vsbl" );
    desc240.putBoolean( idVsbl, false );
executeAction( idhomeScreenVisibilityChanged, desc240, DialogModes.NO );

// =======================================================
var idMRUFileListChanged = stringIDToTypeID( "MRUFileListChanged" );
    var desc241 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc241.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc241.putBoolean( idforceNotify, true );
executeAction( idMRUFileListChanged, desc241, DialogModes.NO );

// =======================================================
var idOpn = charIDToTypeID( "Opn " );
    var desc242 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc242.putBoolean( iddontRecord, false );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc242.putBoolean( idforceNotify, true );
    var idnull = charIDToTypeID( "null" );
    desc242.putPath( idnull, new File( "J:\\appdata\\download\\textures_source\\banana_1_ambientocclusion.png" ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc242.putInteger( idDocI, 59 );
    var idtemplate = stringIDToTypeID( "template" );
    desc242.putBoolean( idtemplate, false );
executeAction( idOpn, desc242, DialogModes.NO );

// =======================================================
var idlayersFiltered = stringIDToTypeID( "layersFiltered" );
executeAction( idlayersFiltered, undefined, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc243 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc243.putInteger( idcommandID, 1161 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc243.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc243, DialogModes.NO );

// =======================================================
var idhistoryStateChanged = stringIDToTypeID( "historyStateChanged" );
    var desc244 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc244.putInteger( idDocI, 59 );
    var idIdnt = charIDToTypeID( "Idnt" );
    desc244.putInteger( idIdnt, 64 );
    var idNm = charIDToTypeID( "Nm  " );
    desc244.putString( idNm, """8 Bits/Channel""" );
    var idhasEnglish = stringIDToTypeID( "hasEnglish" );
    desc244.putBoolean( idhasEnglish, true );
    var idItmI = charIDToTypeID( "ItmI" );
    desc244.putInteger( idItmI, 2 );
    var idcommandID = stringIDToTypeID( "commandID" );
    desc244.putInteger( idcommandID, 5024 );
executeAction( idhistoryStateChanged, desc244, DialogModes.NO );

// =======================================================
var idCnvM = charIDToTypeID( "CnvM" );
    var desc245 = new ActionDescriptor();
    var idDpth = charIDToTypeID( "Dpth" );
    desc245.putInteger( idDpth, 8 );
    var idMrge = charIDToTypeID( "Mrge" );
    desc245.putBoolean( idMrge, false );
executeAction( idCnvM, desc245, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc246 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc246.putInteger( idcommandID, 32 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc246.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc246, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc247 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc247.putInteger( idLvl, 1 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var identer = stringIDToTypeID( "enter" );
    desc247.putEnumerated( idStte, idStte, identer );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc247.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc247.putString( idTtl, """Save As""" );
executeAction( idmodalStateChanged, desc247, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc248 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc248.putInteger( idLvl, 0 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var idexit = stringIDToTypeID( "exit" );
    desc248.putEnumerated( idStte, idStte, idexit );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc248.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc248.putString( idTtl, """Save As""" );
executeAction( idmodalStateChanged, desc248, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc249 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc249.putInteger( idLvl, 1 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var identer = stringIDToTypeID( "enter" );
    desc249.putEnumerated( idStte, idStte, identer );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc249.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc249.putString( idTtl, """PNG Format Options""" );
executeAction( idmodalStateChanged, desc249, DialogModes.NO );

// =======================================================
var idmodalStateChanged = stringIDToTypeID( "modalStateChanged" );
    var desc250 = new ActionDescriptor();
    var idLvl = charIDToTypeID( "Lvl " );
    desc250.putInteger( idLvl, 0 );
    var idStte = charIDToTypeID( "Stte" );
    var idStte = charIDToTypeID( "Stte" );
    var idexit = stringIDToTypeID( "exit" );
    desc250.putEnumerated( idStte, idStte, idexit );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc250.putBoolean( idkcanDispatchWhileModal, true );
    var idTtl = charIDToTypeID( "Ttl " );
    desc250.putString( idTtl, """PNG Format Options""" );
executeAction( idmodalStateChanged, desc250, DialogModes.NO );

// =======================================================
var idsave = charIDToTypeID( "save" );
    var desc251 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc252 = new ActionDescriptor();
        var idMthd = charIDToTypeID( "Mthd" );
        var idPNGMethod = stringIDToTypeID( "PNGMethod" );
        var idquick = stringIDToTypeID( "quick" );
        desc252.putEnumerated( idMthd, idPNGMethod, idquick );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIN = charIDToTypeID( "PGIN" );
        desc252.putEnumerated( idPGIT, idPGIT, idPGIN );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPGAd = charIDToTypeID( "PGAd" );
        desc252.putEnumerated( idPNGf, idPNGf, idPGAd );
        var idCmpr = charIDToTypeID( "Cmpr" );
        desc252.putInteger( idCmpr, 6 );
        var idembedIccProfileLastState = stringIDToTypeID( "embedIccProfileLastState" );
        var idembedOff = stringIDToTypeID( "embedOff" );
        var idembedOn = stringIDToTypeID( "embedOn" );
        desc252.putEnumerated( idembedIccProfileLastState, idembedOff, idembedOn );
    var idPNGF = charIDToTypeID( "PNGF" );
    desc251.putObject( idAs, idPNGF, desc252 );
    var idIn = charIDToTypeID( "In  " );
    desc251.putPath( idIn, new File( "E:\\caches\\desktop\\banana_1_ambientocclusion.png" ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc251.putInteger( idDocI, 59 );
    var idLwCs = charIDToTypeID( "LwCs" );
    desc251.putBoolean( idLwCs, true );
    var idEmbP = charIDToTypeID( "EmbP" );
    desc251.putBoolean( idEmbP, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveBegin = stringIDToTypeID( "saveBegin" );
    desc251.putEnumerated( idsaveStage, idsaveStageType, idsaveBegin );
executeAction( idsave, desc251, DialogModes.NO );

// =======================================================
var idsave = charIDToTypeID( "save" );
    var desc253 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc254 = new ActionDescriptor();
        var idMthd = charIDToTypeID( "Mthd" );
        var idPNGMethod = stringIDToTypeID( "PNGMethod" );
        var idquick = stringIDToTypeID( "quick" );
        desc254.putEnumerated( idMthd, idPNGMethod, idquick );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIN = charIDToTypeID( "PGIN" );
        desc254.putEnumerated( idPGIT, idPGIT, idPGIN );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPGAd = charIDToTypeID( "PGAd" );
        desc254.putEnumerated( idPNGf, idPNGf, idPGAd );
        var idCmpr = charIDToTypeID( "Cmpr" );
        desc254.putInteger( idCmpr, 6 );
        var idembedIccProfileLastState = stringIDToTypeID( "embedIccProfileLastState" );
        var idembedOff = stringIDToTypeID( "embedOff" );
        var idembedOn = stringIDToTypeID( "embedOn" );
        desc254.putEnumerated( idembedIccProfileLastState, idembedOff, idembedOn );
    var idPNGF = charIDToTypeID( "PNGF" );
    desc253.putObject( idAs, idPNGF, desc254 );
    var idIn = charIDToTypeID( "In  " );
    desc253.putPath( idIn, new File( "E:\\caches\\desktop\\banana_1_ambientocclusion.png" ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc253.putInteger( idDocI, 59 );
    var idLwCs = charIDToTypeID( "LwCs" );
    desc253.putBoolean( idLwCs, true );
    var idEmbP = charIDToTypeID( "EmbP" );
    desc253.putBoolean( idEmbP, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveSucceeded = stringIDToTypeID( "saveSucceeded" );
    desc253.putEnumerated( idsaveStage, idsaveStageType, idsaveSucceeded );
executeAction( idsave, desc253, DialogModes.NO );

// =======================================================
var idMRUFileListChanged = stringIDToTypeID( "MRUFileListChanged" );
    var desc255 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc255.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc255.putBoolean( idforceNotify, true );
executeAction( idMRUFileListChanged, desc255, DialogModes.NO );

// =======================================================
var idbackgroundSaveCompleted = stringIDToTypeID( "backgroundSaveCompleted" );
    var desc256 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc256.putInteger( idDocI, 59 );
    var idsaveScheduleMode = stringIDToTypeID( "saveScheduleMode" );
    desc256.putString( idsaveScheduleMode, """auto""" );
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc256.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc256.putBoolean( idforceNotify, true );
executeAction( idbackgroundSaveCompleted, desc256, DialogModes.NO );

// =======================================================
var idCls = charIDToTypeID( "Cls " );
    var desc257 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc257.putInteger( idDocI, 59 );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc257.putBoolean( idforceNotify, true );
executeAction( idCls, desc257, DialogModes.NO );

// =======================================================
var idhomeScreenVisibilityChanged = stringIDToTypeID( "homeScreenVisibilityChanged" );
    var desc258 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc258.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc258.putBoolean( idforceNotify, true );
    var idVsbl = charIDToTypeID( "Vsbl" );
    desc258.putBoolean( idVsbl, true );
executeAction( idhomeScreenVisibilityChanged, desc258, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc259 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc259.putInteger( idcommandID, -687 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc259.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc259, DialogModes.NO );



````

The converter extracts only the useful parts and ignores events found in our excluded_events.json

```py
###########################################################
# Required boilerplate code
###########################################################


from win32com.client import Dispatch


app = Dispatch("Photoshop.Application")

def s(name):
    """convert string name into type id"""
    return app.StringIDToTypeID(f"{name}")


def c(name):
    """convert char name into type id"""
    return app.CharIDToTypeID(f"{name}")


def _ps_display_dialogs():
    """Dictionary with dialog constants"""
    return {"all": 1, "error": 2, "no": 3}


def dialog(dialog_type="no"):
    """Photoshop dialog windows settings using "all": 1, "error": 2, "no": 3"""
    dialogs = _ps_display_dialogs()
    return dialogs.get(dialog_type, lambda: None)


###########################################################
# Generated JS to Python Action manager code
###########################################################


def open_0():
    desc242 = Dispatch("Photoshop.ActionDescriptor")
    desc242.PutBoolean(s("dontRecord"),  False)
    desc242.PutBoolean(s("forceNotify"),  True)
    desc242.PutPath(s("target"), "J:\\appdata\\download\\textures_source\\banana_1_ambientocclusion.png")
    desc242.PutInteger(s("documentID"),  59)
    desc242.PutBoolean(s("template"),  False)
    app.ExecuteAction(s("open"), desc242, dialog())

open_0()


def convertMode_1():
    desc245 = Dispatch("Photoshop.ActionDescriptor")
    desc245.PutInteger(s("depth"),  8)
    desc245.PutBoolean(s("merge"),  False)
    app.ExecuteAction(s("convertMode"), desc245, dialog())

convertMode_1()


def save_2():
    desc251 = Dispatch("Photoshop.ActionDescriptor")
    desc252 = Dispatch("Photoshop.ActionDescriptor")
    desc252.PutEnumerated(s("method"), s("PNGMethod"), s("quick"))
    desc252.PutEnumerated(s("PNGInterlaceType"), s("PNGInterlaceType"), s("PNGInterlaceNone"))
    desc252.PutEnumerated(s("PNGFilter"), s("PNGFilter"), s("PNGFilterAdaptive"))
    desc252.PutInteger(s("compression"),  6)
    desc252.PutEnumerated(s("embedIccProfileLastState"), s("embedOff"), s("embedOn"))
    desc251.PutObject(s("as"), s("PNGFormat"),  desc252)
    desc251.PutPath(s("in"), "E:\\caches\\desktop\\banana_1_ambientocclusion.png")
    desc251.PutInteger(s("documentID"),  59)
    desc251.PutBoolean(s("lowerCase"),  True)
    desc251.PutBoolean(s("embedProfiles"),  True)
    desc251.PutEnumerated(s("saveStage"), s("saveStageType"), s("saveBegin"))
    app.ExecuteAction(s("save"), desc251, dialog())

save_2()


def save_3():
    desc253 = Dispatch("Photoshop.ActionDescriptor")
    desc254 = Dispatch("Photoshop.ActionDescriptor")
    desc254.PutEnumerated(s("method"), s("PNGMethod"), s("quick"))
    desc254.PutEnumerated(s("PNGInterlaceType"), s("PNGInterlaceType"), s("PNGInterlaceNone"))
    desc254.PutEnumerated(s("PNGFilter"), s("PNGFilter"), s("PNGFilterAdaptive"))
    desc254.PutInteger(s("compression"),  6)
    desc254.PutEnumerated(s("embedIccProfileLastState"), s("embedOff"), s("embedOn"))
    desc253.PutObject(s("as"), s("PNGFormat"),  desc254)
    desc253.PutPath(s("in"), "E:\\caches\\desktop\\banana_1_ambientocclusion.png")
    desc253.PutInteger(s("documentID"),  59)
    desc253.PutBoolean(s("lowerCase"),  True)
    desc253.PutBoolean(s("embedProfiles"),  True)
    desc253.PutEnumerated(s("saveStage"), s("saveStageType"), s("saveSucceeded"))
    app.ExecuteAction(s("save"), desc253, dialog())

save_3()


def close_4():
    desc257 = Dispatch("Photoshop.ActionDescriptor")
    desc257.PutInteger(s("documentID"),  59)
    desc257.PutBoolean(s("forceNotify"),  True)
    app.ExecuteAction(s("close"), desc257, dialog())

close_4()

```


# PREVIOUS VERSION Photoshop script listener to python 
You can find this file in the 'old' folder.
Converts Photoshop 'ScriptingListenerJS.log' file into Python functions you could further explore as reference, edit and customize.
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

result: Filtered and Transpiled
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
        "idbackgroundSaveCompleted"
 

## Collaboration 

Yes, please! Photoshop scripting with Python has a small community on Discord https://discord.gg/VXFFy8FWVA

