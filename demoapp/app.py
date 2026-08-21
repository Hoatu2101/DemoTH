from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key="dsddsdf"

db = SQLAlchemy(app)

login_manager = LoginManager(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

def add_sample_user():
    sample_user = User(username="1", password="1", is_active=True)
    db.session.add(sample_user)
    db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/login", methods=["GET", "POST"])
def login_view():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter(User.username == username).first()
        if user and user.password == password:
            login_user(user)
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_sample_user()
    app.run(debug=True)