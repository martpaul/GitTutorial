from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          					#This is the main URL
def index():
    return render_template("home.html")	#The argument should be in templates folder

@app.route('/home')   
def home():
    return render_template("home.html")

@app.route('/about')   
def about():
    return render_template("about.html")

@app.route('/contact')  
def contact():
    return render_template("contact.html")

@app.route('/process')  
def process():
    return render_template("process.html")

@app.route('/work')
def work():
	return render_template("work.html")

if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
