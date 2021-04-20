#!/usr/bin/env python3
import rospy							#Importar librerías de Python hacia ROS
from std_msgs.msg import String					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Bool					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Int8					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Float32				#Importar tipo de dato String de la librería std_msgs"""


recibido = 1								#Se definee la variable global "recibido" iniciándola en cualquier valor
def callback(data):							#Declaración de función callback que hace de Handler para los datos entrantes
	global recibido							#Especificar que dentro de la función se use la variable global "recibido"
	recibido = data.data;						""" Guardar en "recibido" el dato entrante a través del Topic al que esté 										suscrito """
	rospy.loginfo(recibido)					#Mostrar en el terminal los datos leidos de los topics

""" Definir función Bool_ (No puede tener el nombre 
de un tipo de dato, podría generar problemas) """
def Nodo_B():
	rospy.init_node('Nodo_B', anonymous=False)			#Inicializar el nodo con su nombre asignado
	rospy.Subscriber('Booleano', Bool, callback);			"""Declarar el Topic al que está suscrito, el tipo de dato que se va a 										recibir y el nombre de la función "Handler" """
	pub_bool = rospy.Publisher('String_B', String, queue_size=10);	""" Declara qué Topic va a publicar, el tipo de dato a publicar y el tamaño 										del Buffer """
	rate = rospy.Rate(1)						#Declarar a qué frecuencia se publican los Topics
		
	while not rospy.is_shutdown():					#Ciclo que dura mientras ROS esté activo
										
		if recibido == True:					#Asigna 100% al Alto y 0% a los demás si llega un "1"
			Str = "Alto=100%/Medio=0%/Bajo=0%"		#String estandarizado para responder al dato Booleano
		else: 							#Asigna 100% al Bajo y 0% a los demás si llega un "0"
			Str = "Alto=0%/Medio=0%/Bajo=100%"		#String estandarizado para responder al dato Booleano
		pub_bool.publish(Str);					#Publicar dato r_bool por el Topic "String_B"
		rate.sleep()						#Esperar para mantener frecuencia de transmisión
		
if __name__ == '__main__':						#Entrar al main de la función
	try:
		Nodo_B()						#Llamar a la función "Nodo_B"
	except rospy.ROSInterruptException:				#Excepción para evitar que se blquee el programa
		pass

