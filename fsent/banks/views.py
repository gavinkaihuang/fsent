from flask import flash, redirect, render_template, request, url_for, Blueprint, session, jsonify
from fsent import app, db
from fsent.models import Bank
from flask_login import login_required
import json


banks_blueprint = Blueprint(
    'banks', __name__,
    template_folder='templates'
)

@banks_blueprint.route('/bank/list', methods=['GET', 'POST'])
# @login_required
def bank_list():
    # user = session.get("user")
    # user_id = user.id
    banks = Bank.query.all()
    # return jsonify(banks)
    return jsonify([b.to_dict() for b in banks])

@banks_blueprint.route('/bank/add', methods=['POST'])
# @login_required
def bank_add():
    item = request.get_json()
    bank = Bank(bankname=item['bankname'], icon_url=item['icon_url'], note=item['note'])
    db.session.add(bank)
    db.session.commit()
    return jsonify({'message': 'Bank created successfully!'})

@banks_blueprint.route('/bank/delete', methods=['POST'])
# @login_required
def bank_delete():
    item = request.get_json()
    bank = Bank.query.filter_by(id=item['id']).first()
    if bank is not None:
        db.session.delete(bank)
        db.session.commit()
    return redirect('/bank/list')#mathod 1: redirct to a url

@banks_blueprint.route('/bank/update', methods=['POST'])
# @login_required
def bank_update():
    item = request.get_json()
    bank = Bank.query.filter_by(id=item['id']).first()
    if bank is not None:
        bank.bankname = item['bankname']
        bank.icon_url = item['icon_url']
        bank.note = item['note']
        db.session.commit()
    return redirect(url_for('banks.bank_list'))#mathod 2: redirect to a function
