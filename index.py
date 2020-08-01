from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about') 
def about():
    return render_template('about.html')   
    
@app.route('/one')    
def one():
    return render_template('one.html')

@app.route('/two')    
def two():
    return render_template('two.html')

@app.route('/three')
def tree():
    return render_template('three.html')      

if __name__ == '__main__':
    app.run(debug=True)