from flask import Flask, render_template, redirect, url_for, request
from models import db, Pesquisa
from forms import PesquisaForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/seu_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/pesquisa', methods=['GET', 'POST'])
def listar_pesquisas():
    pesquisas = Pesquisa.query.all()
    return render_template('pesquisa.html', pesquisas=pesquisas)

@app.route('/pesquisa/novo', methods=['GET', 'POST'])
def nova_pesquisa():
    form = PesquisaForm()
    if form.validate_on_submit():
        nova_pesquisa = Pesquisa(
            pesquisa_nome=form.pesquisa_nome.data,
            data_inicio=form.data_inicio.data,
            data_fim=form.data_fim.data
        )
        db.session.add(nova_pesquisa)
        db.session.commit()
        return redirect(url_for('listar_pesquisas'))
    return render_template('pesquisa_form.html', form=form)

@app.route('/pesquisa/<int:id>/editar', methods=['GET', 'POST'])
def editar_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    form = PesquisaForm(obj=pesquisa)
    if form.validate_on_submit():
        pesquisa.pesquisa_nome = form.pesquisa_nome.data
        pesquisa.data_inicio = form.data_inicio.data
        pesquisa.data_fim = form.data_fim.data
        db.session.commit()
        return redirect(url_for('listar_pesquisas'))
    return render_template('pesquisa_form.html', form=form, pesquisa=pesquisa)

@app.route('/pesquisa/<int:id>/deletar', methods=['POST'])
def deletar_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    db.session.delete(pesquisa)
    db.session.commit()
    return redirect(url_for('listar_pesquisas'))

if __name__ == '__main__':
    app.run(debug=True)
