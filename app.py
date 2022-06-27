from flask import Flask, render_template, request
#Initializing Flask
app = Flask(__name__)

#Route Webpage
@app.route('/')
def visitors():
	#Load Current Count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	#Increment The Count
	visitors_count = visitors_count + 1

	#Overwrite The Count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	#Render HTML
	return render_template("index.html", count = visitors_count)

#Route Webpage
@app.route('/', methods = ['POST'])
def covid_stats():
	# Load Current Count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	text = request.form['text']

	corona_data = "https://covid-api-262.herokuapp.com/?country=" + text
	print(corona_data)

	return render_template("index.html", image = corona_data, count = visitors_count)
#Code for executing flask
if __name__ == '__main__':
	app.run()