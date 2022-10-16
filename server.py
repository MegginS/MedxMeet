from flask import (Flask, render_template, request, flash, session, redirect, make_response)

import model
import newsfeed

app = Flask(__name__)

app.secret_key = "dev"

@app.route('/news')
def news():
    """View links to news articles."""

    all_articles = newsfeed.news_results()

    return all_articles

if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)