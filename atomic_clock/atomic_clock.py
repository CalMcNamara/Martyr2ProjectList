import requests
from flask import Flask, render_template

# calling the api 
req_get = requests.get("http://worldclockapi.com/api/json/est/now")
response = req_get.json()
print(response['currentDateTime'])

current_date = response['currentDateTime'][:10]
print(current_date)

current_time = response['currentDateTime'][11:]
print(current_time)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', current_date = current_date, current_time = current_time)

if __name__ == '__main__':
    app.run()