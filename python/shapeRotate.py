import pya
import shapeMisc 

class ShapeRotate(object):
    def __init__(self, layoutView):
        super(ShapeRotate, self).__init__() 
        self.layoutView  = layoutView
        self.unit        = layoutView.active_cellview().layout().dbu
        
    def selectedShapes(self):
        return shapeMisc.selectedShapes(self.layoutView)
          
    def rotateAbout(self, r, rotate = 0, rx = 0, ry = 0, flipH = False, flipV = False):
        item      = (r.inst() if r.is_cell_inst() else r.shape)
        d         = r.trans().to_itrans(self.unit).disp
        cx, cy    = item.dbbox().center().x, item.dbbox().center().y
        mirror    = False
        mirror    = not(mirror)  if flipV else mirror
        mirror    = not(mirror)  if flipH else mirror
        rotate    = rotate + 180 if flipH else rotate
        
        item.transform(pya.DTrans(  d.x - rx,  d.y - ry))
        item.transform(pya.DCplxTrans(1, rotate, mirror, 0, 0))
        item.transform(pya.DTrans( -d.x + rx, -d.y + ry))
        
    def rotateFlipShape(self, rotate = 0, flipH = False, flipV = False, applyEach = False):
        self.layoutView.transaction("Rotation %.2f %s%s" % (rotate, ("H" if flipH else ""), ("V" if flipH else "")))
        try:
            groupBox = pya.DBox()  
            for r in self.selectedShapes():
                item      = (r.inst() if r.is_cell_inst() else r.shape)
                d         = r.trans().to_itrans(self.unit).disp
                cx, cy    = item.dbbox().center().x, item.dbbox().center().y
                if applyEach:
                    self.rotateAbout(r, rotate, (cx + d.x), (cy + d.y), flipH, flipV)
                else:
                    groupBox += item.dbbox().transformed(pya.DTrans(d.x, d.y))
                    
            if not(applyEach):
                groupCenter = groupBox.center()
                for r in self.selectedShapes():
                    self.rotateAbout(r, rotate, groupCenter.x, groupCenter.y, flipH, flipV)
        finally:
            self.layoutView.commit()
            
if __name__ == "__main__": 
    mainWindow = pya.Application.instance().main_window()    
    sr = ShapeRotate(mainWindow.current_view())
    sr.rotateFlipShape(90, False, False, False)