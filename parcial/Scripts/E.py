#!/usr/bin/env python3

import rospy							#Importar librerías de Python hacia ROS			
from std_msgs.msg import String					#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Char					#Importar tipo de dato Char de la librería std_msgs

recibido="Alto=0%/Medio=0%/Bajo=100%"		#Se definee la variable global "recibido" iniciándola con cualquier String 
def callback(data):							#Declaración de función callback que hace de Handler para los datos entrantes
	global recibido#Especificar que dentro de la función se use la variable global "recibido"
#Guardar en "recibido" el dato entrante a través del Topic al que suscrito
	recibido = data.data;""" Guardar en "recibido" el dato entrante a través del Topic al que esté 										suscrito """					
	#rospy.loginfo(recibido)	#Mostrar en el terminal los datos leidos de los topics

def Nodo_E():								#Declarar función "Nodo_E"
	rospy.init_node('Nodo_E', anonymous=False)			#Inicializar el nodo con su nombre asignado
	rospy.Subscriber('String_B', String, callback)			#Se suscribe al Topic "String_B" de tipo String por la función callback
	pub_bool = rospy.Publisher('Char_E', Char, queue_size=10);""" Declara qué Topic va a publicar, el tipo de dato a publicar y el tamaño 										del Buffer """
	rate = rospy.Rate(0.5)#Declarar a qué frecuencia se publican los Topics
	#rospy.spin()							#Mantiene el script ejecutándose sin hacer nada a la espera del siguiente dato
	while not rospy.is_shutdown():					#Ciclo que dura mientras ROS esté activo
		#rospy.loginfo(recibido)
		vect=[None,None,None]
		vect[0] = int(recibido[5:recibido.find("Medio")-2])				#Capturar numéricamente el porcentaje de "Alto"
		vect[1] = int(recibido[recibido.find("Medio")+6:recibido.find("Bajo")-2])	#Capturar numéricamente el porcentaje de "Medio"
		vect[2] = int(recibido[recibido.find("Bajo")+5:len(recibido)-1])		#Capturar numéricamente el porcentaje de "Bajo"
		mayor=None
		i_max=None
		i=0
		for n in vect:
			if mayor==None:
				mayor = n 
				i_max = i
			elif n>=mayor:
				mayor=n
				i_max=i
			i=i+1
		enviar=""
		if i_max ==0: enviar="A"; ASCII=65
		elif i_max==1: enviar="M"; ASCII=77
		elif i_max==2: enviar="B"; ASCII=66
		
		
		pub_bool.publish(ASCII)	
		rospy.loginfo(enviar)
		rate.sleep()
		

if __name__ == '__main__':						#Entrar al main de la función
	try:
		Nodo_E()						#Llamar a la función "recibir"
	except rospy.ROSInterruptException:				#Excepción para evitar que se blquee el programa
		pass
