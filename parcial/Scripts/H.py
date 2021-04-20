#!/usr/bin/env python3


import rospy								#Importar librerías de Python hacia ROS
from std_msgs.msg import String			#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Char			#Importar tipo de dato Char de la librería std_msgs
from std_msgs.msg import Int16					#Importar tipo de dato String de la librería std_msgs

#Declarar variables globales para recibir cada dato
Vel1=0
Vel2=0
Vel3=0


#Declarar Handlers para cada Topic recibido
def callback(data):
    global Vel1
    if data.data == 65: Vel1=33
    elif data.data == 77: Vel1=22
    elif data.data == 66: Vel1=11
    #rospy.loginfo(Vel1)#Mostrar en el terminal los datos leidos de los topics
    
def callback1(data):
    global Vel2
    if data.data == 65: Vel2=33
    elif data.data == 77: Vel2=22
    elif data.data == 66: Vel2=11
    #rospy.loginfo(Vel2)#Mostrar en el terminal los datos leidos de los topics
    
def callback2(data):
    global Vel3
    if data.data == 65: Vel3=33
    elif data.data == 77: Vel3=22
    elif data.data == 66: Vel3=11
    #rospy.loginfo(Vel3)#Mostrar en el terminal los datos leidos de los topics

def Nodo_H():
	rospy.init_node('Nodo_H', anonymous=False)
	#Inicializar los nodos con sus nombres respectivos
	rospy.Subscriber('Char_E', Char, callback)
	rospy.Subscriber('Char_F', Char, callback1)
	rospy.Subscriber('Char_G', Char, callback2)
	pub = rospy.Publisher('Int_H', Int16, queue_size=10)
	rate = rospy.Rate(0.2)#Declarar a qué frecuencia se publican los Topics
	
	while not rospy.is_shutdown():	#Ciclo que dura mientras ROS esté activo
		Vel=Vel1+Vel2+Vel3
		pub.publish(Vel)
		rospy.loginfo(Vel)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		Nodo_H()			#Llamar a la función "Bool"
	except rospy.ROSInterruptException:		#Excepción para evitar que se blquee el programa
		pass
