import pya 
import math


def selectedShapes(view):
    return sorted([o for o in view.each_object_selected()], key=lambda s: s.seq)
    
def selectedAnnotationBox(view):
    box = pya.DBox()
    for a in view.each_annotation_selected():
        box += a.box()
    return box
    
def globalTrans(o, x, y):
    transPath(o)
    trans  = o.dtrans()
    inv    = trans.inverted()
    trans2 = pya.DTrans(float(x), float(y))

    if o.is_cell_inst():
        o.inst().transform(inv * trans2 * trans)
    else:
        o.shape.transform(inv * trans2 * trans)
        
def visibleLayers(view):
    return [ layerProp.layer_index() for layerProp in view.each_layer() if layerProp.visible]
    
def shapeShadow(view, o, boxOnly = False, useVisibleLayers = False): 
    box  = None
    poly = None
    if not(o.is_cell_inst()):
        if o.shape.dpolygon:
            poly = o.shape.dpolygon.transformed(o.dtrans())      
            box  = poly.bbox()
    else:
        if useVisibleLayers:
            box = DBox()
            for layer_index in visibleLayers(view):
                box += o.inst().dbbox(layer_index)
            poly = pya.DPolygon(box)  
        else: 
            poly = pya.DPolygon(o.inst().dbbox())
            box  = o.inst().dbbox()
        trans = o.dtrans()
        box   = box.transformed(trans)
        poly  = poly.transformed(trans)
        
    return box if boxOnly else poly
    
def visibleBBox(view, o, useVisibleLayers = False):
    return shapeShadow(view, o, boxOnly = True, useVisibleLayers = useVisibleLayers) 
