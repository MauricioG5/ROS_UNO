# ROS_UNO

## DESCRIPTION


This package contains ROS nodes from A to H wich post and subscribe different type of variables including Bool, Int16, FLoat32, Char and String.
Finally, there is a Node with a serial comunication between ROS and Arduno for real world implementation.

(H -> ARDUINO, ARDUINO -> A), these ROS nodes are intended to use a Fuzzy logic controller to consider 3 signals and make a decision for a final actuator.

## NODES

- A Node: Subscribes to a String topic from Arduino and substract from it the value of each sensor. It publishes each value on a differen topic: Bool, Int16 and Float32  
- B Node: It subscribes to a a Bool topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- C Node: It subscribes to an Int topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- D Node: It subscribes to a Float topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- E Node: It subscribes to a String topic from Node B, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- F Node: It subscribes to a String topic from Node C, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- G Node: It subscribes to a String topic from Node D, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- H Node: It subscribes to a char topic from Nodes B,C and D, wich are converted to a 0 - 100% value wich is published on a String topic.
- Arduino Node: It subscribes to a String topic from Node H, it uses te value to set a motor Speed, it also takes the value from 3 sensors and publishes a String with the sensors value. 

## EXECUTION

**To execute the program, it may be done on this way:**

1. Execute roscore:
> roscore

2. Execute the following command from a different terminal:
> rosrun <folder_name> <scrypt_name>.py

3. To visualize the correct linking between nodes, this command can be used:
> rqt_graph

## ARDUINO NODE EXECUTION

- In order tu execute Arduino node, the first thing must be done is to give permisions to the serial port, it can be done this way:
> sudo chmod 777 /dev/ttyACM0
o
> sudo chmod 777 /dev/ttyUSB0

- Load the code on the Arduino board and execute the following commands:
> roscore
> rosrun rosserial_python serial_node.py /dev/ttyACM0 


# AUTHORS

- Mauricio Gómez Menjura
- Eymer S. Tapias
- Nikcolas Rojas
