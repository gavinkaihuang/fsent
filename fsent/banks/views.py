from flask import flash, redirect, render_template, request, url_for, Blueprint, session, jsonify
from fsent import app, db
from fsent.models import Bank
import json


banks_blueprint = Blueprint(
    'banks', __name__,
    template_folder='templates'
)

@banks_blueprint.route('/bank/list', methods=['GET', 'POST'])
def bank_list():
    # user = session.get("user")
    # user_id = user.id
    banks = Bank.query.all()
    # return jsonify(banks)
    return jsonify([b.to_dict() for b in banks])

@banks_blueprint.route('/bank/add', methods=['POST'])
def bank_add():
    item = request.get_json()
    bank = Bank(bankname=item['bankname'], icon_url=item['icon_url'], note=item['note'])
    db.session.add(bank)
    db.session.commit()
    return jsonify({'message': 'Bank created successfully!'})
    
    # # user = session.get("user")
    # # user_id = user.id
    # # banks = Bank.query.all()
    # return jsonify(item)
    # # return jsonify([b.to_dict() for b in banks])
    # banks = Bank.query.all()
    # return jsonify(item)
    # return jsonify([b.to_dict() for b in banks])

