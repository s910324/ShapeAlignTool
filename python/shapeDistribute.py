import pya
import shapeMisc

class ShapeDistribute(object):
    def __init__(self, layoutView):
        super(ShapeDistribute, self).__init__() 
        self.layoutView  = layoutView
        self.unit        = layoutView.active_cellview().layout().dbu
        
    def selectedShapes(self):
        return shapeMisc.selectedShapes(self.layoutView)
        
    def visibleLayers(self):
        return shapeMisc.visibleLayers(self.layoutView)
        
    def visibleBBox(self, o, useVisibleLayers = False):
        return shapeMisc.visibleBBox(self.layoutView, o, useVisibleLayers = False)

                        
    def distrubute(self, distributeH = False, distributeV = False, centerPitch = True, useVisibleLayers = False):
        sortedShapesH = sorted(self.selectedShapes(), key = lambda o : self.visibleBBox(o, useVisibleLayers).center().x)
        sortedShapesV = sorted(self.selectedShapes(), key = lambda o : self.visibleBBox(o, useVisibleLayers).center().y)
        
        oFirstH       = sortedShapesH[ 0]
        oLastH        = sortedShapesH[-1]
        oFirstV       = sortedShapesV[ 0]
        oLastV        = sortedShapesV[-1]       
        oFirstBoxH    = self.visibleBBox(oFirstH, useVisibleLayers)
        oLastBoxH     = self.visibleBBox(oLastH,  useVisibleLayers)
        oFirstBoxV    = self.visibleBBox(oFirstV, useVisibleLayers)
        oLastBoxV     = self.visibleBBox(oLastV,  useVisibleLayers)
        oFirstCX      = oFirstBoxH.center().x
        oLastCX       = oLastBoxH.center().x
        oFirstCY      = oFirstBoxV.center().y
        oLastCY       = oLastBoxV.center().y
        objCount      = len(sortedShapesH)
        sepprationH   = int((oLastCX - oFirstCX)/(objCount-1))
        sepprationV   = int((oLastCY - oFirstCY)/(objCount-1))
        

        self.layoutView.transaction("ditribute %s%s" % (("H" if distributeH else ""), ("V" if distributeV else "")))
        try:
            if distributeH:
                for index, o in enumerate(sortedShapesH):
                    box    = self.visibleBBox(o,   useVisibleLayers)
                    shiftH = oFirstCX + (index * sepprationH) - box.center().x
                    shapeMisc.globalTrans(o, shiftH, 0)
                    
            if distributeV:
                for index, r in enumerate(sortedShapesV):
                    item   = (r.inst() if r.is_cell_inst() else r.shape)
                    box    = self.visibleBBox(r,   useVisibleLayers)
                    shiftV = oFirstCY + (index * sepprationV) - box.center().y
                    shapeMisc.globalTrans(o, 0, shiftV)
                
        finally:
            self.layoutView.commit()

                
    def distrubuteH(self, centerPitch = True, useVisibleLayers = False):
        self.distrubute(distributeH = True, distributeV = False, centerPitch = centerPitch, useVisibleLayers = useVisibleLayers)

    def distrubuteV(self, centerPitch = True, useVisibleLayers = False):           
        self.distrubute(distributeH = False, distributeV = True, centerPitch = centerPitch, useVisibleLayers = useVisibleLayers)

if __name__ == "__main__":    
    mainWindow = pya.Application.instance().main_window()    
    sd = ShapeDistribute(mainWindow.current_view())
    sd.distrubuteH()
    sd.distrubuteV()