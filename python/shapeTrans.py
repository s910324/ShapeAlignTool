import pya
import shapeMisc

class ShapeTrans(object):
    def __init__(self, layoutView):
        super(ShapeTrans, self).__init__() 
        self.layoutView  = layoutView
        self.unit        = layoutView.active_cellview().layout().dbu

    def selectedShapes(self):
        return shapeMisc.selectedShapes(self.layoutView)
        
    def selectedAnnotationBox(self):
        return shapeMisc.selectedAnnotationBox(self.layoutView)
        
    def visibleLayers(self):
        return shapeMisc.visibleLayers(self.layoutView)
        
    def visibleBBox(self, r, useVisibleLayers = False):
        return shapeMisc.visibleBBox(self.layoutView, r, useVisibleLayers = False)

    def alignSnap(self, vOpts, hOpts, useVisibleLayers = False, alignAnnotation = True):
        firstBox   = pya.DBox() if not(alignAnnotation) else self.selectedAnnotationBox()
        transTextV = ["", "alignTop",  "alignMiddle", "alignBottom", "snapTop",  "snapBottom"][vOpts]
        transTextH = ["", "alignLeft", "alignCenter", "alignright",  "snapLeft", "snapRight"][hOpts]

        self.layoutView.transaction(f"{transTextV}{transTextH}")
        try:

            for o in self.selectedShapes(): 
                vbox = self.visibleBBox(o, useVisibleLayers)

                if firstBox.empty():
                    firstBox    = vbox
                    
                else:
                    secondBox   = vbox
                    alignLeft   = firstBox.left       - secondBox.left       
                    alignCenter = firstBox.center().x - secondBox.center().x
                    alignright  = firstBox.right      - secondBox.right      
                    alignTop    = firstBox.top        - secondBox.top        
                    alignMiddle = firstBox.center().y - secondBox.center().y 
                    alignBottom = firstBox.bottom     - secondBox.bottom   
                    snapLeft    = firstBox.left       - secondBox.right      
                    snapRight   = firstBox.right      - secondBox.left       
                    snapTop     = firstBox.top        - secondBox.bottom     
                    snapBottom  = firstBox.bottom     - secondBox.top 
                    vTrans      = [0.0, alignTop,  alignMiddle, alignBottom, snapTop,  snapBottom][vOpts]
                    hTrans      = [0.0, alignLeft, alignCenter, alignright,  snapLeft, snapRight][hOpts]
                    shapeMisc.globalTrans(o, hTrans, vTrans)
        finally:
            self.layoutView.commit()
            
if __name__ == "__main__":    
    mainWindow = pya.Application.instance().main_window()    
    st = ShapeTrans(mainWindow.current_view())
    st.alignSnap(1, 1)