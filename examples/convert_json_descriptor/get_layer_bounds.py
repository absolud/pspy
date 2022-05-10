'''get_layer_bounds.py

tested: Adobe Photoshop Version: 23.3.1
os: windows
'''
from win32com.client import Dispatch

ps = Dispatch("Photoshop.Application")

doc = ps.ActiveDocument
doc_active_layer = doc.ActiveLayer

layer_bounds = doc_active_layer.Bounds
width = layer_bounds[2] - layer_bounds[0]
height = layer_bounds[3] - layer_bounds[1]

print(f'bounds: {layer_bounds}')
print(f'width: {width}, height: {height}')