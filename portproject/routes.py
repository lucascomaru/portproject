from flask import render_template, url_for
from portproject import app


@app.route('/')
def home ():
    foto_perfil = url_for('static', filename='images/fotolucas.jpg')
    github = url_for('static', filename='images/github2.png')
    contato = url_for('static', filename='images/contato.png')
    cursos = url_for('static', filename='images/cursos.png')
    projetos = url_for('static', filename='images/projetos.png')
    linkedin = url_for('static', filename='images/linkedin.png')
    return render_template('homepage.html', foto_perfil=foto_perfil, github=github, contato=contato
                           ,cursos=cursos, projetos=projetos, linkedin=linkedin)