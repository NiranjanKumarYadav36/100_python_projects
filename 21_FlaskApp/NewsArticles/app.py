from flask import Flask, render_template
import requests

# api_key = ""
# url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&q=business"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/business')
def business_news():
    response = requests.get(url)
    data = response.json()
    return render_template('business.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)



















