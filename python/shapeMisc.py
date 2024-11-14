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
    otrans  = o.dtrans()
    xytrans = pya.DTrans(float(x), float(y))

    if o.is_cell_inst():
        itrans = o.inst().dtrans      
        gtrans = (otrans * itrans)
        inv    = (gtrans.inverted())
        o.inst().transform(inv * xytrans * gtrans)
        
    else:
        o.shape.transform(xytrans)


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
        inst = o.inst()

        if not(boxOnly):
            box = pya.DBox()
            for layer_index in visibleLayers(view):
                box += inst.dbbox(layer_index)
            poly = pya.DPolygon(box)  
        else: 
            box  = inst.dbbox()
            poly = pya.DPolygon(box)
            
        trans = o.source_dtrans()
        box   = box.transformed(trans)
        poly  = poly.transformed(trans)
        
    return box if boxOnly else poly
    
def visibleBBox(view, o, useVisibleLayers = False):
    return shapeShadow(view, o, boxOnly = True, useVisibleLayers = useVisibleLayers) 
    
    
if __name__ == "__main__": 
    mw = pya.Application.instance().main_window() 
    vw = mw.current_view() 
    
    def draw_test():
        for o in selectedShapes(vw):
            print(shapeShadow(vw, o))
            
    def move_test():
        for o in selectedShapes(vw):
            globalTrans(o, -20, 30)
            
    def select_test():
        print(len(selectedShapes(vw)))
        for o in selectedShapes(vw):
            print(o)
    
    #select_test()
            