from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import PesquisaForm
from models import db, Pesquisa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/seu_banco_de_dados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta'

db.init_app(app)

@app.route('/')
def index():
    pesquisas = Pesquisa.query.all()
    return render_template('index.html', pesquisas=pesquisas)

@app.route('/pesquisa/new', methods=['GET', 'POST'])
def create_pesquisa():
    form = PesquisaForm()
    if form.validate_on_submit():
        nova_pesquisa = Pesquisa(
            pesquisa_nome=form.pesquisa_nome.data,
            data_inicio=form.data_inicio.data,
            data_fim=form.data_fim.data,
            ativo=form.ativo.data
        )
        db.session.add(nova_pesquisa)
        db.session.commit()
        flash('Pesquisa criada com sucesso!')
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

@app.route('/pesquisa/edit/<int:pesquisa_id>', methods=['GET', 'POST'])
def edit_pesquisa(pesquisa_id):
    pesquisa = Pesquisa.query.get_or_404(pesquisa_id)
    form = PesquisaForm(obj=pesquisa)
    if form.validate_on_submit():
        pesquisa.pesquisa_nome = form.pesquisa_nome.data
        pesquisa.data_inicio = form.data_inicio.data
        pesquisa.data_fim = form.data_fim.data
        pesquisa.ativo = form.ativo.data
        db.session.commit()
        flash('Pesquisa atualizada com sucesso!')
        return redirect(url_for('index'))
    return render_template('update.html', form=form, pesquisa=pesquisa)

@app.route('/pesquisa/delete/<int:pesquisa_id>')
def delete_pesquisa(pesquisa_id):
    pesquisa = Pesquisa.query.get_or_404(pesquisa_id)
    db.session.delete(pesquisa)
    db.session.commit()
    flash('Pesquisa deletada com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

