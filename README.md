# PascalVOC2YOLO

## This is the simplest method of converting Pascal VOC annotation file into YOLO annotation file
### Pascal VOC formate
Pascal VOC stores annotation in XML file. Below is an example of Pascal VOC annotation file for object detection.

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
    
    
YOLO: In YOLO labeling format, a .txt file with the same name is created for each image file in the same directory. Each .txt file contains the annotations for the corresponding image file, that is object class, object center coordinates, height and width.
<object-class> <bb center x> <bb center y> <bb width> <bb height>
For each object, a new line is created.
Below is an example of annotation in YOLO format where the image contains two different objects.
