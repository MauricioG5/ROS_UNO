# ROS_UNO

## DESCRIPTION


This package contains ROS nodes from A to H wich post and subscribe different type of variables including Bool, Int16, FLoat32, Char and String.
Finally, there is a Node with a serial comunication between ROS and Arduno for real world implementation.

(H -> ARDUINO, ARDUINO -> A), these ROS nodes are intended to use a Fuzzy logic controller to consider 3 signals and make a decision for a final actuator.

- A Node: Subscribes to a String topic from Arduino and substract from it the value of each sensor. It publishes each value on a differen topic: Bool, Int16 and Float32  
- B Node: It subscribes to a a Bool topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- C Node: It subscribes to an Int topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- D Node: It subscribes to a Float topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- E Node: It subscribes to a String topic from Node B, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- F Node: It subscribes to a String topic from Node C, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- G Node: It subscribes to a String topic from Node D, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- H Node: It subscribes to a char topic from Nodes B,C and D, wich are converted to a 0 - 100% value wich is published on a String topic.
- Arduino Node: It subscribes to a String topic from Node H, it uses te value to set a motor Speed, it also takes the value from 3 sensors and publishes a String with the sensors value. 



