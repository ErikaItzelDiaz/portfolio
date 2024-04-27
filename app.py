from flask import Flask, render_template, request, abort
from dotenv import load_dotenv

load_dotenv()

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/tracker.png",
        "hero": "img/tracker.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://www.tracker.erikadiaz.dev/",
        "git": "https://github.com/ErikaItzelDiaz/habitTracker",
    },
    {
        "name": "MicroBlog app with Python and MongoDB",
        "thumb": "img/blog.png",
        "hero": "img/blog.png",
        "categories": ["python", "web"],
        "slug": "micro-blog",
        "prod": "https://www.blog.erikadiaz.dev/",
        "git": "https://github.com/ErikaItzelDiaz/microBlog",
    },
    {
        "name": "Password Generator app with Python",
        "thumb": "img/generator.png",
        "hero": "img/generator.png",
        "categories": ["python", "web"],
        "slug": "password-generator",
        "prod": "https://www.generator.erikadiaz.dev/",
        "git": "https://github.com/ErikaItzelDiaz/passwordGenerator",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html",title="Erika Diaz | Portfolio", projects=projects)

    @app.route("/about/")
    def about():
        return render_template("about.html",title="About")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug], title=slug_to_project[slug]["name"])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("base.html", title="Not found"), 404

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
