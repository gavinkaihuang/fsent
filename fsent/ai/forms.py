from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class QuestionForm(FlaskForm):
    question = TextAreaField('question', validators=[DataRequired(), Length(max=200)])
    # question = TextAreaField(u'question', [validators.optional(), validators.length(max=200)])
    #  [validators.optional(), validators.length(max=200)]
    submit = SubmitField('Ask')