'''convert_ps_api.py

tested: Adobe Photoshop Version: 23.3.1
os: windows
takes the ScriptSupport.8li library and converts it into a python file
- used as reference
'''
import sys
from win32com.client import makepy

sys.argv = ["makepy", r"C:\Program Files\Adobe\Adobe Photoshop 2022\Required\Plug-ins\Extensions\ScriptingSupport.8li"]
makepy.main ()
print("done!")
# result saved in a windows temp folder location: C:\Users\{username}\AppData\Local\Temp