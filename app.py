from flask import Flask, render_template

app = Flask (__name__)


@app.route('/')

def index ():
    
    return render_template("index.html")

@app.route('/about')
def about () :
    return render_template("about.html")

@app.route('/Sarmale')
def sarmale () :
    return render_template("Sarmale.html")

@app.route('/mici')
def mici () :
    return render_template("mici.html")

@app.route('/ciorbaBurta')
def ciorbaBurta () :
    return render_template("ciorbaBurta.html")








