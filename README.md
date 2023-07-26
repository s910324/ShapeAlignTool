# ShapeAlignTool

![image](https://github.com/s910324/ShapeAlignTool/assets/1561043/3999d5e2-0425-4037-8a52-2f59dbbfdd6a)

Klayout shape alignment plugin, can be installed from app Package manager

[Menu] --> [Tool] --> [Align Tool]

can be set bind with hot key "A" from setting menu

<b>shape alignment</b>
* align shape to top, mid, bottom, left center and right
* align shape to four corners
* align shape to four border center.
* align shape to ruler/annotation<b><sup>1<sup></b> (https://github.com/KLayout/klayout/issues/1375)

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
