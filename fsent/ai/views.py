from flask import flash, redirect, render_template, request, url_for, Blueprint, session, jsonify
from fsent import app, db
from .forms import QuestionForm
from fsent.models import Bank
from flask_login import login_required
import json
import openai
from configparser import ConfigParser


ai_blueprint = Blueprint(
    'ai', __name__,
    template_folder='templates'
)




@ai_blueprint.route('/ai/prompt', methods=['GET', 'POST'])
def ai_prompt():
    error = None
    form = QuestionForm(request.form)
    return render_template('prompt.html', form=form, error=error)
    # return jsonify({"status":"200", "msg": "", "data" : response})



@ai_blueprint.route('/ai/search', methods=['POST'])
def ai_search():
    content = request.form.get('question')
    # print(request.get_data())
    # request.get_data()
    # item = request.get_json()
    # content = item['content']

    app.config.from_pyfile('ai_config.py')
    # print(app.config['ORG'])
    # print(app.config['OPEN_AI_KEY'])
    openai.api_key = app.config['OPEN_AI_KEY']

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=content,
        temperature=1,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    
    return jsonify({"status":"200", "msg": "", "data" : response})
    # # return redirect(url_for('banks.bank_list'))#mathod 2: redirect to a function
    # return jsonify({"status":"200", "msg": "", "data" : response.choices[0].text})
    # banks = Bank.query.all()
    # # return jsonify(banks)
    # # return jsonify([b.to_dict() for b in banks])
    # return jsonify({"status":"200", "msg": "", "data" : [b.to_dict() for b in banks]})
