from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PesquisaForm(FlaskForm):
    pesquisa_nome = StringField('Nome da Pesquisa', validators=[DataRequired()])
    data_inicio = DateTimeField('Data de Início', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    data_fim = DateTimeField('Data de Fim', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    ativo = BooleanField('Ativo')
    submit = SubmitField('Salvar')
