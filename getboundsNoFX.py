import photoshop.api as ps
app = ps.Application

def layer_bounds_no_effects(layer):
    """
    Returns the bounds of a given layer without its effects applied.
    @param layer: A layer object
    @return list: Pixel location top left, top right, bottom left, bottom right.
    """
    current = app.activeDocument.activeLayer
    app.activeDocument.activeLayer = layer
    bounds = app.eval_javascript(
        "app.activeDocument.activeLayer.boundsNoEffects"
    )
    app.activeDocument.activeLayer = current
    return [int(num) for num in bounds.replace(" px", "").split(",")]

# Test it out
layer = app.activeDocument.getByName("My Layer")
print(layer_bounds_no_effects(layer))