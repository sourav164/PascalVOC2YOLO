# PascalVOC2YOLO

## This is the simplest method of converting Pascal VOC annotation file into Darknet YOLO annotation file
To convert the annotation file


Requirements:
- Python 3.X
- argparse

To install argparse 
- pip install argparse

### Pascal VOC formate
Pascal VOC stores annotation in XML file. Below is an example of Pascal VOC annotation file for object detection.
#### Pascal VOC Example
    <annotation> 
      <folder>Train</folder> 
      <filename>01.png</filename>      
      <path>/path/Train/01.png</path> 
      <source>  
        <database>Unknown</database> 
      </source>
      <size>  
        <width>224</width>  
        <height>224</height>  
        <depth>3</depth>   
      </size> 
      <segmented>0</segmented> 
      <object>  
        <name>36</name>  
        <pose>Frontal</pose>  
        <truncated>0</truncated>  
        <difficult>0</difficult>  
        <occluded>0</occluded>  
        <bndbox>   
          <xmin>90</xmin>   
          <xmax>190</xmax>   
          <ymin>54</ymin>   
          <ymax>70</ymax>  
        </bndbox> 
      </object>
    </annotation>
    
    
### YOLO Darknet: 
The label file specifications are:

One row per object
Each row is 

    class x_center y_center width height format.
Box coordinates must be in normalized xywh format (from 0 - 1). 
Class numbers are zero-indexed (start from 0).

#### YOLO Darknet Example
    0 0.409 0.225 0.134 0.113
    0 0.406 0.266 0.068 0.135
    0 0.406 0.256 0.068 0.156
    1 0.437 0.279 0.023 0.119
    1 0.47 0.279 0.089 0.119
