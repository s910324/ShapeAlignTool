import os
import pya

import shapeDistribute
import shapeMisc
import shapeRotate
import shapeShadow
import shapeTrans
import shapeTransRuler


iconPath = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "icon")) 

class AlignWidget(pya.QWidget):
    def __init__(self, alignUI = True, snapUI = True, rotateUI = True, booleanUI = False, distributeUI = True, utilUI = True, parent = None):
        super(AlignWidget, self).__init__(parent)  
        bgColor            = pya.QWidget().palette.color(pya.QWidget().backgroundRole)
        colorWt            = sum([bgColor.red, bgColor.green, bgColor.blue])
        iconPathStr        = iconPath + "/" + ("dark" if  colorWt < 256 else "light") + "/%s.png" #path from alignShapeFactory
        self.firstObj      = None
    
        self.layoutView    = pya.Application.instance().main_window().current_view()  
        self.alignSnapHdl  = shapeTrans.ShapeTrans(self.layoutView)
        self.transRulerHdl = shapeTransRuler.ShapeTransRuler(self.layoutView)
        self.distributeHdl = shapeDistribute.ShapeDistribute(self.layoutView)
        self.rotateHdl     = shapeRotate.ShapeRotate(self.layoutView)
        self.shadowHdl     = shapeShadow.ShapeShadow(self.layoutView)
        
        self.initUI(iconPathStr, alignUI, snapUI, rotateUI, booleanUI, distributeUI, utilUI)

    def initUI(self, iconPathStr, alignUI, snapUI, rotateUI, booleanUI, distributeUI, utilUI):
        columnSpacing            = 20
        rowSpacing               = 20
        categorySpacing          = 20
        self.grabRuler           = None
        self.grabShadows         = []
        self.grabTheme           = {}
        self.alignmentLB         = TitleLB("Alignment")
        self.snapLB              = TitleLB("Snap")
        self.rotationLB          = TitleLB("Rotate")
        self.booleanLB           = TitleLB("Boolean")
        self.distributeLB        = TitleLB("Distribute")
        self.utilLB              = TitleLB("Utilities")
        self.configLB            = TitleLB("Configuration")
        
        self.alignLeftPB         = SquarePB(iconPathStr % "alignLeft",         lambda : self.alignSnapHdl.alignSnap(0, 1, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignCenterPB       = SquarePB(iconPathStr % "alignCenter",       lambda : self.alignSnapHdl.alignSnap(0, 2, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignRightPB        = SquarePB(iconPathStr % "alignRight",        lambda : self.alignSnapHdl.alignSnap(0, 3, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.alignTopPB          = SquarePB(iconPathStr % "alignTop",          lambda : self.alignSnapHdl.alignSnap(1, 0, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignMiddlePB       = SquarePB(iconPathStr % "alignMiddle",       lambda : self.alignSnapHdl.alignSnap(2, 0, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignBottomPB       = SquarePB(iconPathStr % "alignBottom",       lambda : self.alignSnapHdl.alignSnap(3, 0, self.useVisibleLayers(), self.allowAnnoAlign()))

        self.alignTopLeftPB      = SquarePB(iconPathStr % "alignTopLeft",      lambda : self.alignSnapHdl.alignSnap(1, 1, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignTopCenterPB    = SquarePB(iconPathStr % "alignTopCenter",    lambda : self.alignSnapHdl.alignSnap(1, 2, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignTopRightPB     = SquarePB(iconPathStr % "alignTopRight",     lambda : self.alignSnapHdl.alignSnap(1, 3, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.alignMiddleLeftPB   = SquarePB(iconPathStr % "alignMiddleLeft",   lambda : self.alignSnapHdl.alignSnap(2, 1, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignMiddleCenterPB = SquarePB(iconPathStr % "alignMiddleCenter", lambda : self.alignSnapHdl.alignSnap(2, 2, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignMiddleRightPB  = SquarePB(iconPathStr % "alignMiddleRight",  lambda : self.alignSnapHdl.alignSnap(2, 3, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.alignBottomLeftPB   = SquarePB(iconPathStr % "alignBottomLeft",   lambda : self.alignSnapHdl.alignSnap(3, 1, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignBottomCenterPB = SquarePB(iconPathStr % "alignBottomCenter", lambda : self.alignSnapHdl.alignSnap(3, 2, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.alignBottomRightPB  = SquarePB(iconPathStr % "alignBottomRight",  lambda : self.alignSnapHdl.alignSnap(3, 3, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.transByRulerPB      = SquarePB(iconPathStr % "transByRuler",      lambda : self.transRulerHdl.transByRuler(), hoverFunction = lambda : self.transRulerHdl.attemptGrabRuler())
         
        self.snapLeftPB          = SquarePB(iconPathStr % "snapLeft",          lambda : self.alignSnapHdl.alignSnap(0, 4, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.snapRightPB         = SquarePB(iconPathStr % "snapRight",         lambda : self.alignSnapHdl.alignSnap(0, 5, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.snapTopPB           = SquarePB(iconPathStr % "snapTop",           lambda : self.alignSnapHdl.alignSnap(4, 0, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.snapBottomPB        = SquarePB(iconPathStr % "snapBottom",        lambda : self.alignSnapHdl.alignSnap(5, 0, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.snapDummyPB         = SquarePB(iconPathStr % "snapDummy",         lambda : self.dummy())
        
        self.snapTopLeftPB       = SquarePB(iconPathStr % "snapTopLeft",       lambda : self.alignSnapHdl.alignSnap(4, 4, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.snapTopRightPB      = SquarePB(iconPathStr % "snapTopRight",      lambda : self.alignSnapHdl.alignSnap(4, 5, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.snapBottomLeftPB    = SquarePB(iconPathStr % "snapBottomLeft",    lambda : self.alignSnapHdl.alignSnap(5, 4, self.useVisibleLayers(), self.allowAnnoAlign()))
        self.snapBottomRightPB   = SquarePB(iconPathStr % "snapBottomRight",   lambda : self.alignSnapHdl.alignSnap(5, 5, self.useVisibleLayers(), self.allowAnnoAlign()))
        
        self.distributeHPB       = SquarePB(iconPathStr % "distributeH",       lambda : self.distributeHdl.distrubuteH(True, self.useVisibleLayers()))
        self.distributeVPB       = SquarePB(iconPathStr % "distributeV",       lambda : self.distributeHdl.distrubuteV(True, self.useVisibleLayers()))
        
        self.booleanMergePB      = SquarePB(iconPathStr % "booleanMerge")
        self.booleanIntersectPB  = SquarePB(iconPathStr % "booleanIntersect")
        self.booleanSubstractPB  = SquarePB(iconPathStr % "booleanSubstract")
        self.booleanSeperatePB   = SquarePB(iconPathStr % "booleanSeperate")
        
        self.rotateCCW90PB       = SquarePB(iconPathStr % "rotateCCW90",       lambda : self.rotateHdl.rotateFlipShape( 90, False, False, self.rotateByEachCenter()))
        self.rotateCW90PB        = SquarePB(iconPathStr % "rotateCW90",        lambda : self.rotateHdl.rotateFlipShape(-90, False, False, self.rotateByEachCenter()))
        self.flipHorizontalPB    = SquarePB(iconPathStr % "flipHorizontal",    lambda : self.rotateHdl.rotateFlipShape(  0,  True, False, self.rotateByEachCenter()))
        self.flipVerticalPB      = SquarePB(iconPathStr % "flipVertical",      lambda : self.rotateHdl.rotateFlipShape(  0, False,  True, self.rotateByEachCenter()))

        self.drawShadowPB        = SquarePB(iconPathStr % "drawShadow",        lambda : self.shadowHdl.grabSelectedShadow())
        
        self.configUseVisCB      = pya.QCheckBox ("Use visible only for align/snap")
        self.configUseAnnoCB     = pya.QCheckBox ("Allow Align to Ruler")
        self.configRotEachCB     = pya.QCheckBox ("Rotate each shape center")

        self.donePB              = pya.QPushButton("Done")

        self.alignGrid           = pya.QGridLayout()
        self.snapGrid            = pya.QGridLayout()
        self.rotateGrid          = pya.QGridLayout()
        self.boolGrid            = pya.QGridLayout()
        self.distGrid            = pya.QGridLayout()
        self.configGrid          = pya.QGridLayout()
        self.utilGrid            = pya.QGridLayout()
        self.bottomBarGrid       = pya.QGridLayout()
        self.grid                = pya.QGridLayout()

        
        
        self.donePB.clicked(lambda : self.close())

        self.alignGrid.addWidget(self.alignmentLB,         0, 0, 1, 5)
        self.alignGrid.addWidget(self.alignTopLeftPB,      1, 2, 1, 1)
        self.alignGrid.addWidget(self.alignTopCenterPB,    1, 3, 1, 1)
        self.alignGrid.addWidget(self.alignTopRightPB,     1, 4, 1, 1)
        self.alignGrid.addWidget(self.alignTopPB,          1, 0, 1, 1)
             
        self.alignGrid.addWidget(self.alignMiddleLeftPB,   2, 2, 1, 1)
        self.alignGrid.addWidget(self.alignMiddleCenterPB, 2, 3, 1, 1)
        self.alignGrid.addWidget(self.alignMiddleRightPB,  2, 4, 1, 1)
        self.alignGrid.addWidget(self.alignMiddlePB,       2, 0, 1, 1)
             
        self.alignGrid.addWidget(self.alignBottomLeftPB,   3, 2, 1, 1)
        self.alignGrid.addWidget(self.alignBottomCenterPB, 3, 3, 1, 1)
        self.alignGrid.addWidget(self.alignBottomRightPB,  3, 4, 1, 1)
        self.alignGrid.addWidget(self.alignBottomPB,       3, 0, 1, 1)
             
        self.alignGrid.addWidget(self.alignLeftPB,         5, 2, 1, 1)
        self.alignGrid.addWidget(self.alignCenterPB,       5, 3, 1, 1)
        self.alignGrid.addWidget(self.alignRightPB,        5, 4, 1, 1)
        self.alignGrid.addWidget(self.transByRulerPB,      5, 0, 1, 1)
        
        
        self.alignGrid.setColumnMinimumWidth(1, columnSpacing)
        self.alignGrid.setRowMinimumHeight(4, rowSpacing)        
        self.alignGrid.setRowStretch(6, 1)

        
        self.snapGrid.addWidget(self.snapLB,               0, 0, 1, 3)                
        self.snapGrid.addWidget(self.snapTopLeftPB,        1, 0, 1, 1)
        self.snapGrid.addWidget(self.snapTopPB,            1, 1, 1, 1)
        self.snapGrid.addWidget(self.snapTopRightPB,       1, 2, 1, 1)

        self.snapGrid.addWidget(self.snapLeftPB,           2, 0, 1, 1)
        self.snapGrid.addWidget(self.snapDummyPB,          2, 1, 1, 1)
        self.snapGrid.addWidget(self.snapRightPB,          2, 2, 1, 1)
        
        self.snapGrid.addWidget(self.snapBottomLeftPB,     3, 0, 1, 1)
        self.snapGrid.addWidget(self.snapBottomPB,         3, 1, 1, 1)
        self.snapGrid.addWidget(self.snapBottomRightPB,    3, 2, 1, 1)
        self.snapGrid.setRowStretch(4, 1)


        self.rotateGrid.addWidget(self.rotationLB,         0, 0, 1, 1)  
        self.rotateGrid.addWidget(self.rotateCCW90PB,      1, 0, 1, 1)
        self.rotateGrid.addWidget(self.rotateCW90PB,       2, 0, 1, 1)
        self.rotateGrid.addWidget(self.flipHorizontalPB,   3, 0, 1, 1)     
        self.rotateGrid.addWidget(self.flipVerticalPB,     4, 0, 1, 1)
        self.rotateGrid.setRowStretch(5, 1)
    
     
        self.boolGrid.addWidget(self.booleanLB,            0, 0, 1, 1)     
        self.boolGrid.addWidget(self.booleanMergePB,       1, 0, 1, 1)
        self.boolGrid.addWidget(self.booleanIntersectPB,   2, 0, 1, 1)
        self.boolGrid.addWidget(self.booleanSubstractPB,   3, 0, 1, 1)     
        self.boolGrid.addWidget(self.booleanSeperatePB,    4, 0, 1, 1)
        self.boolGrid.setRowStretch(5, 1)        


        self.distGrid.addWidget(self.distributeLB,         0, 0, 1, 1)
        self.distGrid.addWidget(self.distributeHPB,        1, 0, 1, 1)
        self.distGrid.addWidget(self.distributeVPB,        2, 0, 1, 1)
        self.distGrid.setRowStretch(3, 1) 

        self.utilGrid.addWidget(self.utilLB,               0, 0, 1, 1)
        self.utilGrid.addWidget(self.drawShadowPB,         1, 0, 1, 1)
        self.utilGrid.setRowStretch(2, 1)         
                
        self.configGrid.addWidget(self.configLB,           0, 0, 1, 8)
        self.configGrid.addWidget(self.configUseVisCB,     1, 0, 1, 4)
        self.configGrid.addWidget(self.configUseAnnoCB,    2, 0, 1, 4)
        self.configGrid.addWidget(self.configRotEachCB,    1, 3, 1, 4)
        self.configGrid.addWidget(self.donePB,             2, 7, 1, 1)
        
        uiDict = {
            self.alignGrid  : alignUI,
            self.snapGrid   : snapUI, 
            self.rotateGrid : rotateUI, 
            self.boolGrid   : booleanUI, 
            self.distGrid   : distributeUI,
            self.utilGrid   : utilUI
        }
        
        uiCount = 0
        for ui in uiDict:
            if uiDict[ui]:
                self.grid.addLayout(ui, 0, uiCount * 2, 1, 1)
                self.grid.setColumnMinimumWidth((uiCount * 2) + 1 , categorySpacing)
                uiCount += 1
                 
        self.grid.addLayout(self.configGrid,1, 0, 1, (uiCount * 2))        
                   
        self.grid.setHorizontalSpacing(2)
        self.grid.setVerticalSpacing(2)
        self.setLayout(self.grid)
        self.setWindowFlags(pya.Qt.WindowStaysOnTopHint)
        self.setWindowTitle ("Align Tool")
        
    def allowAnnoAlign(self):
        return self.configUseAnnoCB.isChecked()
        
    def useVisibleLayers(self):
        return self.configUseVisCB.isChecked()
        
    def rotateByEachCenter(self):
        return self.configRotEachCB.isChecked()
        
    def keyPressEvent(self, event):
        if event.type() == pya.QEvent.KeyPress:
            if event.key() in (pya.Qt.Key_Return, pya.Qt.Key_Escape, pya.Qt.Key_Enter):
                self.close()
                
class TitleLB(pya.QLabel):
    def __init__(self, title):
        super(TitleLB, self).__init__()    
        self.setText(title)
        self.setAlignment(pya.Qt.AlignCenter)
        self.setFixedHeight(20)
        self.setStyleSheet(
        """
            QLabel{
                background-color : rgba(180, 180, 180, 30);
            }
        """
        )
class SquarePB(pya.QPushButton):
    def __init__(self, icon = None, bindFunction = None, hoverFunction = None, parent = None):
        super(SquarePB, self).__init__()    
        self.setFixedSize(50, 50)    
        self.setStyleSheet(
        """
            QPushButton {
                background: rgba(239, 239, 239, 10);
                border: 1px solid transparent;
                border-radius: 2px;
            }
            
            QPushButton::hover {
                border: 1px solid #33ccaa;
            }
            
            QPushButton::pressed {
                border: 1px solid #009966;
            }
        """
        )

        if icon:
            self.setIcon(pya.QIcon(icon))
            self.setIconSize(pya.QSize(40, 40))
            
        if bindFunction:
            self.clicked(bindFunction)
        self.hoverFunction = hoverFunction

    def enterEvent(self, event):
        if not(self.hoverFunction) == None : self.hoverFunction()
        
    def leaveEvent(self, event):
        if not(self.hoverFunction) == None : self.hoverFunction()
                
if __name__ == "__main__":    
    mainWindow = pya.Application.instance().main_window()    
    aw = AlignWidget()
    aw.show()