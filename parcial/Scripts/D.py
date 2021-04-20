#!/usr/bin/env python3
import rospy							#Importar librerías de Python hacia ROS
from std_msgs.msg import String					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Bool					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Int16					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Float32				#Importar tipo de dato String de la librería std_msgs"""


X = 0.0								#Se definee la variable global "X" iniciándola en cualquier valor flotante
def callback(data):						#Declaración de función callback que hace de Handler para los datos entrantes

	global X						#Especificar que dentro de la función se use la variable global "X"
	X = data.data;						""" Guardar en "X" el dato entrante a través del Topic al que esté 									suscrito """
	#rospy.loginfo(X)					#Mostrar en el terminal los datos leidos de los topics
	
def Nodo_D():							#Definir función "NOdo_D"

	rospy.init_node('Nodo_D', anonymous=False)		#Inicializar el nodo con su nombre asignado
	
	rospy.Subscriber('Flotante', Float32 , callback);			"""Declarar el Topic al que está suscrito, el tipo de dato que se va a 										recibir y el nombre de la función "Handler" """
	pub_int = rospy.Publisher('String_D', String, queue_size=10);		""" Declara qué Topic va a publicar, el tipo de dato a publicar y el tamaño 										del Buffer """
	rate = rospy.Rate(1)							#Declarar a qué frecuencia se publican los Topics
	
	while not rospy.is_shutdown():					#Ciclo que dura mientras rospy esté activo
		#pub_bool.publish(X);	#Ecuación de la recta para variable Bajo
		if X<2: Bajo=100-50*X					#B1
		else: Bajo=0						#B2
		
		if X<=1 or X>=4: Medio =0				#M1 and M4
		elif X>1 and X<=2.5: Medio = (100/1.5)*(X-1) 	#M2
		elif X>2.5 and X<4: Medio = (-100/1.5)*(X-2.5) +100	#M3
		
		if X<=3: Alto = 0
		else: Alto = (50)*(X-3)
		Str= "Alto="+str(Alto)+"%/Medio="+str(Medio)+"%/Bajo="+str(Bajo)+"%"
		pub_int.publish(Str)
		rospy.loginfo(Str)
		
		rate.sleep()
		
if __name__ == '__main__':	
	try:
		Nodo_D()				#Llamar a la función "Bool"
	except rospy.ROSInterruptException:		#Excepción para evitar que se blquee el programa
		pass

