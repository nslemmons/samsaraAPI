from flask import Flask, redirect, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/samsara', methods=['POST', 'GET'])
def samsara():
    if request.method == 'POST':
        apiKey = request.form['apiKey']
        return redirect(url_for('authenticated',apiKey = apiKey))
    else:
        return render_template('samsara.html')

@app.route('/authenticated/<apiKey>')
def auth(apiKey):
    return 'API key authenticated: %s' %apiKey

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == ('__main__'):
    app.run(debug=True)
