'''generate_ps_script_support.py

author: LG, Ludwig Geerman 2022 NL
tested: Adobe Photoshop Version: 23.3.1
os: win
takes the ScriptSupport.8li library and converts it into a python file
- used as reference
'''
import sys
from win32com.client import makepy

sys.argv = ["makepy", r"C:\Program Files\Adobe\Adobe Photoshop 2022\Required\Plug-ins\Extensions\ScriptingSupport.8li"]
makepy.main ()
print("done!")
# result saved in a windows temp folder location: C:\Users\{username}\AppData\Local\Temp