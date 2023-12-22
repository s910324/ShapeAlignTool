import pya
import shapeMisc
import shapeShadow

class ShapeTransRuler(object):
    def __init__(self, layoutView):
        super(ShapeTransRuler, self).__init__() 
        self.layoutView  = layoutView
        self.unit        = layoutView.active_cellview().layout().dbu
        self.shadowHdl   = shapeShadow.ShapeShadow(layoutView)
        self.grabRuler   = None
        
    def selectedShapes(self):
        return shapeMisc.selectedShapes(self.layoutView)
        
    def attemptGrabRuler(self):
        if self.grabRuler: 
            self.releaseTransRuler()
            self.releaseGrabShadows()
            
        else : 
            self.grabTransRuler()
            ruler  = self.grabRuler
            if ruler:
                vector = (ruler.p2-ruler.p1)
                self.shadowHdl.grabSelectedShadow(vector.x, vector.y)
            
    def grabTransRuler(self):
        annotationList = list(self.layoutView.each_annotation_selected())
        if len(annotationList) == 1:
            ruler = annotationList[0]
            valid = [
                len(ruler.points) == 2,
                ruler.segments()  == 1,
                ruler.outline not in [
                    pya.Annotation.OutlineRadius, 
                    pya.Annotation.OutlineEllipse, 
                    pya.Annotation.OutlineAngle
                ],
            ]

            if all(valid):
                self.grabRuler     = ruler
                self.grabTheme     = {
                    "fmt"     : ruler.fmt, 
                    "outline" : ruler.outline, 
                    "style"   : ruler.style
                }
                
                ruler.fmt     = "Move by ruler\ndx $X um\ndy $Y um"
                ruler.outline = pya.Annotation.OutlineDiag
                ruler.style   = pya.Annotation.StyleArrowEnd
    
    def releaseTransRuler(self):
        if self.grabRuler: 
            self.grabRuler.fmt     = self.grabTheme["fmt"]
            self.grabRuler.outline = self.grabTheme["outline"]
            self.grabRuler.style   = self.grabTheme["style"]
            self.grabTheme         = {}
        self.grabRuler = None
        self.shadowHdl.releaseGrabShadows()
        
    def transByRuler(self):        

        if self.grabRuler and self.selectedShapes():
            ruler  = self.grabRuler
            vector = (ruler.p2-ruler.p1)
            self.layoutView.transaction("move by ruler")
            try:
                for o in self.selectedShapes(): 
                    shapeMisc.globalTrans(o, vector.x, vector.y)

            finally:
                self.layoutView.commit()
        else: 
            pya.QToolTip().showText(
                pya.QCursor().pos,
                "Select one linear Ruler for shape translation\n"+ \
                "Select atleast one object for shape translation."
            ) 
            
            
if __name__ == "__main__": 
    mainWindow = pya.Application.instance().main_window()    
    stbr = ShapeTransRuler(mainWindow.current_view())
    stbr.attemptGrabRuler()
    stbr.transByRuler()
    stbr.releaseTransRuler()