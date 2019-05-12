#urceno pro Python 3.5
from sense_hat import SenseHat
from time import sleep
import draw_graph
import mail_sender
import os

sense = SenseHat()
one_hour = 1

while True:
	#otevreni souboru se zaznamy a odstraneni predchozich zaznamu
	file_temp = open("temp_log.txt","a")
	file_temp.truncate(0)

	file_hum = open("hum_log.txt","a")
	file_hum.truncate(0)

	#zmereni 24 hodnot v intervalech one_hour
	for i in range(0,24):
		file_temp.write(str(sense.get_temperature()) + "\n")
		file_hum.write(str(sense.get_humidity()) + "\n")
		sleep(one_hour)

	file_temp.close()
	file_hum.close()

	#tvorba noveho grafu
	graph = draw_graph.new_graph()
	draw_graph.add("temp_log.txt", "Temperature",False, graph)
	draw_graph.add("hum_log.txt", "Humidity",True, graph)

	#volani funkci na vykresleni a odeslani grafu
	draw_graph.draw(graph)
	mail_sender.email()
	os.remove("graph.svg")
