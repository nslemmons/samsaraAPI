from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/samsara, methods=[POST]')
def samsara():

    var = request.form['POST']

    url = "https://api.samsara.com/fleet/drivers"

    headers = {"Accept": "application/json","Authorization": ""}

    headers.update(Authorization="Bearer "+var)

    params = {'driverActivationStatus':'active'}

    response = requests.request("GET", url, headers=headers, params=params).json()
    
    return render_template('samsara.html', response)
    

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == ('__main__'):
    app.run(host='0.0.0.0',debug=True)
