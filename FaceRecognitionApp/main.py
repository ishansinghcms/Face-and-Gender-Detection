from logging import debug
from flask import Flask
import views

app= Flask(__name__)


app.add_url_rule('/', 'base', views.base)
app.add_url_rule('/faceapp', 'faceapp', views.faceapp)
app.add_url_rule('/faceapp/gender', 'gender', views.gender, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)