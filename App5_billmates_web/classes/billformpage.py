from flask.templating import render_template
from flask.views import MethodView

class BillFormPage(MethodView):
    def get(self):
        return 'bill page'