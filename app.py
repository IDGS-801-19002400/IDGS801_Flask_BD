from flask import Flask, redirect, request,url_for,render_template
import forms

from flask import jsonify
from config import DevelopmetConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask("__name__")
app.config.from_object(DevelopmetConfig)
csrf = CSRFProtect()

@app.route('/', methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       email = create_form.email.data)
        db.session.add(alum)
        db.session.commit()

    return render_template('index.html', form = create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000)




