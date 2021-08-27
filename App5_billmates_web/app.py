from logging import debug
from flask import Flask
from classes.homepage import HomePage
from classes.billformpage import BillFormPage

app = Flask(__name__)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)