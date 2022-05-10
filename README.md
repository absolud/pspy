# pspy
lg photoshop python

## Dealing with action descriptors in Photoshop
My take on how to use action descriptors in python is to have a system in place that converts the log file 'ScriptingListenerJS.log' into python functions you could further inspect, adjust and execute.

Action descriptors have logic that is pretty much hidden from us and because you won't necesseraly be able to structure code by intuition alone, a converter system concept I mentioned above is essential.

The log file includes an array of actions and events Photoshop executed while we interacted with it. Some of these logs are useless to us and some include actiondescriptor structures of certain actions usually not accessible through regular actions in Photoshop, thus giving us new access to hidden functionality.


## Examining the 'ScriptingListenerJS.log' file
So first we need a converter that takes the log entries, filters out usable js code and transpile them to human-readable python functions.
Excluding unusable entries. This is a list of things you would want to exlude:

- "idhistoryStateChanged"
- "idmodalStateChanged"
- "idinvokeCommand"
- "idhomeScreenVisibilityChanged"
- "idMRUFileListChanged"
- "idAdobeScriptAutomation Scripts"
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
 