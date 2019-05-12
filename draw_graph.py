import pygal

#tvorba noveho grafu
def new_graph():
	weather = pygal.Line(range=(20,30),secondary_range=(30,60))
	return weather

#nacteni hodnot do grafu
def add(log_file, name, is_secondary, weather):
	temp = []
	file = open(log_file,"r")

	for line in file.read().splitlines():
		if line:
			temp.append(float(line))
	file.close()

	weather.add(name, temp, secondary = is_secondary)

#vykresleni grafu
def draw(weather):
	weather.x_labels = range(1,25)
	weather.title = "Weather"
	weather.render_to_file("graph.svg")
