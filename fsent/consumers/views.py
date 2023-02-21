from flask import flash, redirect, render_template, request, url_for, Blueprint, session, jsonify
from fsent import app, db
from fsent.models import Consume
from flask_login import login_required
import json
from datetime import datetime


consumers_blueprint = Blueprint(
    'consumer', __name__,
    template_folder='templates'
)

@consumers_blueprint.route('/consumer/list', methods=['GET', 'POST'])
# @login_required
def consumer_list():
    item = request.get_json()
    # user_id = item['user_id']

    consumers = Consume.query.filter_by(user_id=item['user_id'])
    # return jsonify(banks)
    return jsonify([b.to_dict() for b in consumers])

@consumers_blueprint.route('/consumer/add', methods=['POST'])
# @login_required
def consumer_add():
    item = request.get_json()

    consume = Consume(user_id=item['user_id'], 
                      bank_id=item['bank_id'], 
                      price=item['price'],
                      month=item['month'],
                      year=item['year'],
                      note=item['note']
                      )
    
    if item['account_date'] is not None:
        account_date = datetime.strptime(item['account_date'], "%Y-%m-%d %H:%M:%S")
        consume.account_date = account_date
        # print("account_date date is " + consume.account_date)
    if item['finish_date'] is not None:
        finish_date = datetime.strptime(item['finish_date'], "%Y-%m-%d %H:%M:%S")
        consume.finish_date = finish_date
        # print("finish date is " + consume.finish_date)

    db.session.add(consume)
    db.session.commit()
    # return jsonify({'message': 'Bank created successfully!'})
    return jsonify({"status":"200", "msg": "Consumer created successfully!"})


@consumers_blueprint.route('/consumer/delete', methods=['POST'])
# @login_required
def consumer_delete():
    item = request.get_json()
    consumer = Consume.query.filter_by(id=item['id']).first()
    if consumer is not None:
        db.session.delete(consumer)
        db.session.commit()
    # return redirect('/consumer/list')#mathod 1: redirct to a url
    return jsonify({"status":"200", "msg": "Consumer delete successfully!"})



@consumers_blueprint.route('/consumer/update', methods=['POST'])
# @login_required
def consumer_update():
    item = request.get_json()
    consumer = Consume.query.filter_by(id=item['id']).first()
    
    if consumer is not None:
        consumer.bank_id = item['bank_id'] if item['bank_id'] is not None else ""
        consumer.price = item['price'] if item['price'] is not None else 0.0
        consumer.month = item['month'] if item['month'] is not None else ""
        consumer.year = item['year'] if item['year'] is not None else ""
        consumer.note = item['note'] if item['note'] is not None else ""
        consumer.account_date =  datetime.strptime(item['account_date'], "%Y-%m-%d %H:%M:%S") if item['account_date'] is not None else ""
        consumer.finish_date =  datetime.strptime(item['finish_date'], "%Y-%m-%d %H:%M:%S") if item['finish_date'] is not None else ""

        db.session.commit()
    # return redirect('/consumer/list')#mathod 2: redirect to a function
    # return jsonify(consumer.to_dict())
    return jsonify({"status":"200", "msg": "", "data" : consumer.to_dict()})
