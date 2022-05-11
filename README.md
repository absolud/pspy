# pspy
Photoshop scripting with python has a small community on discord https://discord.gg/VXFFy8FWVA

By combining Python 3 and Photoshop we can interact with documents, layers, footage, images and text but we can also tap into hidden functionalities using action descriptors.
Most of us have struggles with this topic. 'LG Photoshop ScriptListenerJS to Pyhton' converts Javascript action records into python functions. 

## Photoshop action descriptors in python

Action descriptors logic is pretty much hidden from us and because we won't necesseraly be able to structure descriptor code by intuition alone, a converter is essential to make sense of action descriptor structures. The log file 'ScriptingListenerJS.log' contains Javascript log entries of Photoshop's actions and events that has executed while we've been interacting with the application. By converting these entries into python functions you could further inspect, adjust and execute customized solutions.

## Excluded entries in the 'ScriptingListenerJS.log' file

Some entries are useless to us and some include actions usually not accessible through regular actions in Photoshop, thus giving us access to hidden functionality we can edit and customize. 

lg_scriptlistener_pyconverter will do this for you.

Below an ignor-list of entries not relevant to us.

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
 
Photoshop updates may introduce new editions from time to time which means that the ignore-list would need to be extended with these new actions or events deemed irrelevant: