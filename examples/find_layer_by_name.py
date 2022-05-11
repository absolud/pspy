'''find_layer_by_name.py

author: LG, Ludwig Geerman 2022 NL
tested: Adobe Photoshop Version: 23.3.1
os: win

Example finding first occurance of a layer name
'''
from win32com.client import Dispatch


def find_layer_by_name(search: str, layers=None):
    for layer in layers:
        if search==layer.name:
            print(f'first match found: {layer.name}')
            break
        if layer.LayerType == 2:
            sub_layers = layer.Layers
            find_layer_by_name(search, sub_layers)


ps = Dispatch("Photoshop.Application")
doc = ps.ActiveDocument
target_layer_name = "item_06"
layers = doc.Layers
find_layer_by_name(target_layer_name, layers)

