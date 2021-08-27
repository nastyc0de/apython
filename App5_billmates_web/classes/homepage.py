from flask.views import MethodView
from flask import render_template

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')