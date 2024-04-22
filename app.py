from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    @app.route("/about/")
    def about():
        return render_template("about.html")

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
