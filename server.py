from flask import (Flask, render_template, request, flash, session, redirect, make_response)

import model
import newsfeed
import bcrypt

app = Flask(__name__)

app.secret_key = "dev"


@app.route('/')
def home():
    """Homepage"""

# to be designed on front end

    return "Welcome"


@app.route('/api/news')
def news():
    """View news articles related to the specific disease."""

    all_articles = newsfeed.news_results()

    return all_articles


@app.route('/api/create_account')
def create_account():
    """Create an account"""

    # return "MS working"
    # get from frontend: email, password, first name, last name
    email = "placeholder@okay.com"
    password = "placeholder may need to encode"
    category = "placeholder"
    default_disease = "placeholder"
    disease = "placeholder"


    user = model.User.query.filter(model.User.email == email).first()
    # this row checks if there is a user with that email already
    if user:
        return ("An account is already associated with this email")
    else:
        hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")
        model.User.create_user(email = email,
                        password = hashed,
                        category= category,
                        default_disease= default_disease,
                        disease = disease,
                        posts = [],
                        comments = [])
        return "Successfully created"


@app.route('/api/login')
def login():
    """Login Page"""

# to be built (backend needs to return json to front)

    return "Placeholder for login"


@app.route('/api/logout')
def logout():
    """Logout page"""

 # to be built (backend needs to return json to front)

    return "Placeholder for logout"


@app.route('/api/clinical_trials')
def clinical_trials():
    """View clinical trials related to the specific disease."""

 # to be built (backend needs to return json to front)

    return "Placeholder for clinical trials"



@app.route('/api/posts_by_disease')
def posts_by_disease_id():
    """Returns posts by disease id."""

 # to be built (backend needs to return json to front)

    return "Placeholder for posts_by_disease_id"


@app.route('/api/posts_by_user')
def posts_by_user_id():
    """Returns posts by user id."""

#  to be built (backend needs to return json to front)

    return "Placeholder for posts_by_user_id"

@app.route('/api/comments_by_post')
def comments_by_post_id():
    """Returns comments by post id."""

 # to be built (backend needs to return json to front)

    return "Placeholder for comments_by_post_id"


@app.route('/api/comments_by_user')
def comments_by_user_id():
    """Returns comments by user id."""

 # to be built (backend needs to return json to front)

    return "Placeholder for posts_by_user_id"


@app.route('/api/add_post')
def add_post():
    """Add's a post."""

#   "frontend needs to send json to backend"

    return "Placeholder for adds posts"


@app.route('/api/edit_post')
def edit_post():
    """Edits a post."""

 #   "frontend needs to send json to backend"

    return "Placeholder for edits posts"


@app.route('/api/delete_post')
def delete_post():
    """deletes a post."""

 # to be built (backend needs to return json to front)

    return "Placeholder for deletes posts"


@app.route('/api/add_comment')
def add_comment():
    """Add's a comment."""

 #   "frontend needs to send json to backend"

    return "Placeholder for adds comments"


@app.route('/api/edit_comment')
def edit_comment():
    """Edits a comment."""

 #   "frontend needs to send json to backend"

    return "Placeholder for edits comments"


@app.route('/api/delete_comment')
def delete_comment():
    """deletes a comment."""

 # to be built (backend needs to return json to front)

    return "Placeholder for deletes comments"


if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(host="0.0.0.0", port=8000, debug=True)