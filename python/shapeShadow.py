import pya
import shapeMisc

class ShapeShadow(object):
    def __init__(self, layoutView):
        super(ShapeShadow, self).__init__() 
        self.grabShadows = []
        self.layoutView  = layoutView
        self.unit        = layoutView.active_cellview().layout().dbu

    def selectedShapes(self):
        return shapeMisc.selectedShapes(self.layoutView)

    def drawShadow(self, polygon):
        shadow = pya.Annotation()
        if polygon:
            polygon        = pya.DPolygon(polygon) if isinstance(polygon, pya.DBox) else polygon
            points         = [ p for p in polygon.each_point_hull()]
            shadow.outline = pya.Annotation.OutlineDiag
            shadow.style   = pya.Annotation.StyleLine
            shadow.fmt     = ""
            shadow.points  = points + [points[0]]
        return shadow
    
    
    def grabSelectedShadow(self, offset_x=0, offset_y=0, boxOnly = False): 
        shapeArray       = self.selectedShapes()
        self.grabShadows = []
        useVisibleLayers = False
        
        if shapeArray:
            for o in shapeArray:
                shadowShape = shapeMisc.shapeShadow(self.layoutView, o, boxOnly, useVisibleLayers)
                shadow      = self.drawShadow(shadowShape).transformed(pya.DTrans(float(offset_x), float(offset_y)))
                
                #shadow      = self.globalShadowTrans( o, shadow, offset_x, offset_y)
                self.grabShadows.append(shadow)
                self.layoutView.insert_annotation(shadow)
                
    def globalShadowTrans(self, o, shadow, x, y):
        trans  = o.dtrans()
        inv    = trans.inverted()
        v      = pya.DVector(float(x), float(y)) * inv.mag
        rad    = inv.rot() * 0.0174533 
        trans2 = pya.DTrans(float(x), float(y))#pya.DTrans(v.x * math.cos(rad) - v.y * math.sin(rad), v.x * math.sin(rad) + v.y * math.cos(rad))
        return shadow.transformed(trans2)
                
    def releaseGrabShadows(self):
        for shadow in self.grabShadows:
            self.layoutView.erase_annotation(shadow.id())
            shadow.detach()
            shadow.delete()
        self.grabShadows = []



                
if __name__ == "__main__":    
    mainWindow = pya.Application.instance().main_window()    
    ss = ShapeShadow(mainWindow.current_view())
    ss.grabSelectedShadow(10, 0)