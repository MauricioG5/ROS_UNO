#!/usr/bin/env python3
import rospy							#Importar librerías de Python hacia ROS
from std_msgs.msg import String					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Bool					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Int16					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Float32				#Importar tipo de dato String de la librería std_msgs"""


X = 1								#Se definee la variable global "X" iniciándola con cualquier valor entero

def callback(data):						#Declaración de función callback que hace de Handler para los datos entrantes

	global X						#Especificar que dentro de la función se use la variable global "X"
	X = data.data;						""" Guardar en "X" el dato entrante a través del Topic al que esté 									suscrito """
	#rospy.loginfo(X)					#Mostrar en el terminal los datos leidos de los topics

def Nodo_C():	#Definir función random

	rospy.init_node('Nodo_C', anonymous=False)				#Inicializar el nodo con su nombre asignado
	rospy.Subscriber('Entero', Int16 , callback);				"""Declarar el Topic al que está suscrito, el tipo de dato que se va a 										recibir y el nombre de la función "Handler" """
	pub_int = rospy.Publisher('String_C', String, queue_size=10);		""" Declara qué Topic va a publicar, el tipo de dato a publicar y el tamaño 											del Buffer """
	rate = rospy.Rate(1)							#Declarar a qué frecuencia se publican los Topics
		
	while not rospy.is_shutdown():							#Ciclo que dura mientras rospy esté activo
		#pub_bool.publish(X);
		if X<100: Bajo=100-X							#Ecuación de la recta para variable Bajo
		else: Bajo=0								#Se mantiene en 0 en las X que no correspondan a su recta
		
		if X<80 or X>168: Medio =0						#Se mantiene en 0 en las X que no correspondan a su recta
		elif X>=80 and X<=122: Medio = (50/11)*(X-80) 				#Ecuación de la recta para variable Medio
		elif X>122 and X<=168: Medio = (-50/11)*(X-122) +100			#Ecuación de la recta para variable Medio
		
		if X<=144: Alto = 0							#Se mantiene en 0 en las X que no correspondan a su recta
		else: Alto = (100/111)*(X-144)						#Ecuación de la recta para variable ALto
		Str= "Alto="+str(Alto)+"%/Medio="+str(Medio)+"%/Bajo="+str(Bajo)+"%"	#Concatena los datos de porcentajes en un String
		pub_int.publish(Str)								#Publica el string que se acaba de crear
		rospy.loginfo(Str)							#Muestra el String generado
		
		rate.sleep()
		
if __name__ == '__main__':	
	try:
		Nodo_C()				#Llamar a la función "Bool"
	except rospy.ROSInterruptException:		#Excepción para evitar que se blquee el programa
		pass

