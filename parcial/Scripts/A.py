#!/usr/bin/env python3
import rospy						#Importar librerías de Python hacia ROS
from std_msgs.msg import String				#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Bool				#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Int16				#Importar tipo de dato String de la librería std_msgs
from std_msgs.msg import Float32			#Importar tipo de dato String de la librería std_msgs

"""Importante: 
El nombre del archivo no puede ser el mismo que el de la librería que se quiere importar, esto ocasiona un 'llamado circular' """
import random						#Importar librería "random" para generar números pseudo-aleatorios

recibido="Bool=0/Int=0/Float=0.00"			#Se definee la variable global "recibido" iniciándola con cualquier String
def callback(data):					#Declaración de función callback que hace de Handler para los datos entrantes
	global recibido					#Especificar que dentro de la función se use la variable global "recibido"
							#Guardar en "recibido" el dato entrante a través del Topic al que suscrito
	recibido = data.data;						
	rospy.loginfo(recibido)			#Mostrar en el terminal los datos leidos de los topics



def rand():	#Definir función rand
#Establecer nombre de los topics, tipo de dato y tamaño del buffer a utilizar en cada uno
	rospy.Subscriber('String_Ard', String, callback)		#Se suscribe al Topic "String_B" de tipo String por la función callback
	pub_bool = rospy.Publisher('Booleano', Bool, queue_size=10)	
	pub_int = rospy.Publisher('Entero', Int16, queue_size=10)
	pub_float = rospy.Publisher('Flotante', Float32, queue_size=10)
	rospy.init_node('Nodo_A', anonymous=False);			""" Inicializa el nodo asignándole su nombre 
									(anonimo opcional para topics del mismo nombre) """	
									
										
	rate = rospy.Rate(10) 						#Asigna la velocidad de envío de datos a 10 hz
	while not rospy.is_shutdown():					#Ciclo que dura mientrasrospy esté activo
				
		r_bool  = bool(int(recibido[5]))						#Capturar numéricamente el porcentaje de "Bool"
		r_int   = int(recibido[recibido.find("Int")+4:recibido.find("Float")-1])#Capturar numéricamente el porcentaje de "Int"
		r_float = float(recibido[recibido.find("Float")+6:len(recibido)])	#Capturar numéricamente el porcentaje de "Float"	
		#rospy.loginfo(r_float)
		
		
		'''							#Generar valores aleatorios	
		r_bool = random.randrange(2)				#Genera dato binario
		#rospy.loginfo(type(r_bool))				#Testigo del tipo de dato que se envía
		r_int = random.randint(0,255)				#Genera dato entero
		r_float = random.uniform(0,5)				#Genera dato flotante
#		Hi = "Saludo"						#Valor de prueba dato que se va a enviar
		#rospy.loginfo(r_int);					""" Mostrar por el terminal alguno de los mensajes a enviar con fines 	
									depuración	"""
		'''							
									
		pub_bool.publish(r_bool);				#Publicar dato Booleano
		pub_int.publish(r_int)					#Publicar dato Entero
		pub_float.publish(r_float)				#Publicar dato Flotante
		rate.sleep();						""" Esperar el tiempo necesario para mantener constante la frecuencia de 									envío de datos"""
		
		
if __name__ == '__main__':						#Entrar al main de la función
	try:
		rand()							#Llamar a la función rand definida prevamente
	except rospy.ROSInterruptException:				#Excepción para evitar que se bloquee el programa
		pass

