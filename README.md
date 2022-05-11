# pspy
Photoshop scripting with python has a small community on discord https://discord.gg/VXFFy8FWVA


## Photoshop Action descriptors in python

Action descriptors logic is pretty much hidden from us and because we won't necesseraly be able to structure descriptor code by intuition alone, a converter is essential to make sense of action descriptor structures. The log file 'ScriptingListenerJS.log' contains Javascript log entries of Photoshop's actions and events that were executed while we interacted with it. By converting these entries into python functions you could further inspect, adjust and execute customized solutions.

Some entries are useless to us and some include actions usually not accessible through regular actions in Photoshop, thus giving us access to hidden functionality we can edit and customize. 

lg_scriptlistener_pyconverter will do this for you.


## Excluded entries in the 'ScriptingListenerJS.log' file

Below an ignor-list of entries not relevant to us. Photoshop updates may introduce new editions from time to time which means that the ignore-list would need to be extended with these added id strings:

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
 
