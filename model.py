"""Models for Med x Meet app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import datetime


db = SQLAlchemy()


class Disease(db.Model):
    """A rare disease."""

    __tablename__ = "diseases"

    disease_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    disease_name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    posts = db.relationship("Post", back_populates="disease")
    comments = db.relationship("Comment", back_populates="disease")
    users = db.relationship("User", back_populates="disease")

    def __repr__(self):
        return f"<Disease disease_id={self.disease_id} disease_name={self.disease_name} description={self.description}>"

    @classmethod
    def create_disease(cls, disease_name, description, posts=[], comments=[]):
        """Create and return a new user."""

        disease = cls(disease_name=disease_name,
                    description=description,
                    posts=posts,
                    comments=comments)

        # db.session.add(disease)
        # db.session.commit()

        return disease

    # @classmethod
    # def get_disease_by_keyword(cls, query):
    #     """Return a disease by query."""

    #     pass
    #     # split query by word
    #     # search within disease_name and description


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    default_disease = db.Column(db.Integer, db.ForeignKey("diseases.disease_id"), nullable=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)


    disease = db.relationship("Disease", back_populates="users")
    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username} category={self.category}>"

    @classmethod
    def create_user(cls, username, email, password, category, default_disease, disease=disease, posts=[], comments=[]):
        """Create and return a new user."""

        user = cls(username = username,
                email=email,
                password=password,
                category=category,
                default_disease=default_disease,
                disease=disease,
                posts=posts,
                comments=comments)

        return user

    @classmethod
    def get_user_by_email(cls, email):
        """Return a user by email."""

        return db.session.query(cls).filter(cls.email == email).first()


    @classmethod
    def get_posts_by_user_id(cls, user_id):
        """Return all posts by user_id."""

        pass

    @classmethod
    def get_comments_by_user_id(cls, user_id):
        """Return all comments by user_id."""

        pass


class Post(db.Model):
    """A post."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    disease_id = db.Column(db.Integer, db.ForeignKey("diseases.disease_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    subject = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    edit = db.Column(db.Boolean, default=False, nullable=False)
    date_edited = db.Column(db.DateTime, default=None, nullable=True)

    disease = db.relationship("Disease", back_populates="posts")
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")
    
    def __repr__(self):
        return f"<Post post_id={self.post_id} body={self.body}>"


    def to_dict(self):
        
        return {
            "post_id": self.post_id,
            "disease_id": self.disease_id,
            "user_id": self.user_id,
            "subject": self.subject,
            "body": self.body,
            "date_created": self.date_created,
            "edit": self.edit,
            "date_edited": self.date_edited,
            "comments": self.comments
        }


    @classmethod
    def create_post(cls, disease_id, user_id, subject, body, date_created, edit, date_edited, comments=[]):
        """Create and return a new comment."""

        post = cls(
            disease_id=disease_id,
            user_id=user_id,
            subject=subject,
            body=body,
            date_created=date_created,
            edit=edit,
            date_edited=date_edited,
            comments=comments
        )

        return post


    @classmethod
    def get_posts_by_disease_id(cls, disease_id):
        """Return posts by disease_id."""

        pass


class Comment(db.Model):
    """Comment on a post."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    disease_id = db.Column(db.Integer, db.ForeignKey("diseases.disease_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    edit = db.Column(db.Boolean, default=False, nullable=False)
    date_edited = db.Column(db.DateTime, default=None, nullable=True)

    disease = db.relationship("Disease", back_populates="comments")
    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment comment_id={self.comment_id} body={self.body}>"

    @classmethod
    def create_comment(cls, post_id, disease_id, user_id, body, date_created, edit, date_edited, disease, user, post):
        """Create and return a new comment."""

        comment = cls(post_id=post_id,
                      disease_id=disease_id,
                      user_id=user_id,
                      body=body,
                      date_created=date_created,
                      edit=edit,
                      date_edited=date_edited,
                      disease=disease,
                      user=user,
                      post=post)

        return comment

    @classmethod
    def get_comment_by_user_id(cls, user_id):
        """Return all comments by user_id."""

        return (db.session.query(cls)
                          .filter_by(user_id=user_id)
                          .order_by(cls.date_created.desc())
                          .all())


def connect_to_db(flask_app, db_uri="postgresql:///medxmeet", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


# def example_data():
#     """Create example data for the test database."""
    
#     test_disease = Disease(
#         disease_name="Ocular Pharengyl Muscular Dystrophy",
#         description="Oculopharyngeal muscular dystrophy (OPMD) is a genetic disorder characterized by slowly progressing muscle disease (myopathy) affecting the muscles of the upper eyelids and the throat. Symptoms may include: eyelid drooping (ptosis), arm and leg weakness, and difficulty swallowing (dysphagia). There are two types of OPMD, distinguished by their patterns of inheritance. They are known as the autosomal dominant and autosomal recessive types.",
#         posts=[],
#         comments=[]
#     )
#     test_user = User(username="test",
#         email="test@test.com",
#         password="test",
#         category="Patient",
#         default_disease="default_disease",
#         posts=[],
#         comments=[]
#     )
#     test_post = Post()
#     test_comment = Comment()
    
#     db.session.add_all([test_disease, test_user, test_post, test_comment])
#     db.session.commit()


if __name__ == "__main__":

    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
