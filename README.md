# ShapeAlignTool


<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/96bc0e27-58b0-45ce-80a1-892e9b9ade8e" alt="Screen shot" width="800"/>
</p>

# Installation and setup

<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/57713186-b32b-415e-92dc-d503c79b2d80" alt="installation" width="800"/>
</p>

<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/17f70bd7-0aa4-423a-a2cf-de9c2e94b1cd" alt="setup" width="800"/>
</p>

This app can be installed through KLayout package manager

After installation the app can be accessed through [Menu] --> [Tool] --> [Align Tool]

The app can be bined to hot key through setup dialog
# Functions
* Shape alignment
* Shape snap
* Shape rotate
* Shape distribution
* Translate shape by ruler
* Utilities - Shape shadow


### Shape alignment
<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/7be9a4dc-1795-4510-bbd3-72e695400705" alt="alignment" width="800"/>
</p>

* align shape to top, mid, bottom, left center and right
* align shape to four corners
* align shape to four border center.
* align shape to ruler/annotation<b><sup>1<sup></b> (https://github.com/KLayout/klayout/issues/1375)
* translate shape by ruler
<b><sup>1<sup></b> if allow align to Ruler is enabled, selected ruler object(s) will be dim as major shape, which overrides the piority of selection order.
this is due to the klayout currently does not provide selection seq order attribute to rulers.
a feature resuest function: https://github.com/KLayout/klayout/issues/1375

### Shape snap
<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/fc704534-38c4-43a2-877c-20a604826529" alt="snap" width="800"/>
</p>

* snap to shape four corners
* snap to shape four sides

### Shape rotate
<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/39971689-b78d-4711-97e2-8e300a8b976e" alt="rotate" width="800"/>
</p>

* rotate CW, CCW, Moirror by X and Y axis
* rotate by selection center
* rotate by each shape center

### Shape distribution
* distribute shapes horizontally and vertically by center pitch

### Translate shape by ruler
<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/ab60eb85-8a63-4f9f-969f-66153c63c9df" alt="tran by ruler" width="800"/>
</p>

- **(a)** Prepare shape
- **(b)** Apply two point ruler from target shape to destination, translation direction will be the same as the ruler.
- **(c)** Select target shape(s) and ruler for translation, selection order will not affect results.
- **(d)** If a valid ruler is selected, the ruler will turn into a direction arrow while cursor hovers over the **translate shape by ruler** buttom
- **(e)** Click the **translate shape by ruler** button to perform the alignment.
Arc, ellipse or cross type rulers are not supported.

### Utilities
<p align="center">
<img align="middle" src="https://github.com/s910324/ShapeAlignTool/assets/1561043/b2ea5a4c-88f8-4c4e-a14d-b7cb30792560" alt="shadow" width="800"/>
</p>
* Shadow, trace the border of selected objects using annotation, shadow can be cleared by clear ruler function.



