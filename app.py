from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/samsara')
def samsara():
    return render_template('samsara.html')

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == ('__main__'):
    app.run(debug=True)
