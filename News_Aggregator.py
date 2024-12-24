from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_KEY = "aa0c059409da443f84b40738b41aa73d"

url = "https://newsapi.org/v2/everything"

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get("query", '')
    language = request.form.get("language", "en")
    category = request.form.get("category", "bbc-news, cnn, reuters, al-jazeera-english, associated-press, fox-news")
    sortBy = request.form.get("sortBy", "relevancy")
    if query:
        params = {
            'q': query,
            'language': language,
            'sources': category,
            'sortBy': sortBy, 
            'apiKey': API_KEY,
            'pageSize': 50
        }

        # Make the API request
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])
            
    else:
        articles = []
        
    return render_template("index.html", articles=articles, json=json)

if __name__ == "__main__":
    app.run(debug=True)