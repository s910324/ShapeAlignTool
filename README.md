# ShapeAlignTool

![image](https://github.com/s910324/ShapeAlignTool/assets/1561043/38759453-72ed-40c7-80b7-283d5524d2ee)

----
Klayout shape alignment plugin, can be installed from app Package manager

[Menu] --> [Tool] --> [Align Tool]

can be set bind with hot key "A" from setting menu

<b>shape alignment</b>
* align shape to top, mid, bottom, left center and right
* align shape to four corners
* align shape to four border center.
* align shape to ruler/annotation<b><sup>1<sup></b> (https://github.com/KLayout/klayout/issues/1375)
* translate shape by ruler

<b>shape snap</b>
* snap to shape four corners
* snap to shape four sides

<b>shape rotate</b>
* rotate CW, CCW, Moirror by X and Y axis
* rotate by selection center
* rotate by each shape center

<b>shape distribution</b>
* distribute shapes horizontally and vertically by center pitch

<b><sup>1<sup></b> if allow align to Ruler is enabled, selected ruler object(s) will be dim as major shape, which overrides the piority of selection order.
this is due to the klayout currently does not provide selection seq order attribute to rulers.
a feature resuest function: https://github.com/KLayout/klayout/issues/1375


----
<b> Translate shape by ruler</b>
![image](https://github.com/s910324/ShapeAlignTool/assets/1561043/ab60eb85-8a63-4f9f-969f-66153c63c9df)


- **(a)** Prepare shape
- **(b)** Apply two point ruler from target shape to destination, translation direction will be the same as the ruler.
- **(c)** Select target shape(s) and ruler for translation, selection order will not affect results.
- **(d)** If a valid ruler is selected, the ruler will turn into a direction arrow while cursor hovers over the **translate shape by ruler** buttom
- **(e)** Click the **translate shape by ruler** button to perform the alignment.
Arc, ellipse or cross type rulers are not supported.
