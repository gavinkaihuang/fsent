from codes import app, db
from codes.models import User, Bank

with app.app_context():
    # create the database and the db table
    db.create_all()

    # insert data
    db.session.add(User("gavin", "gavinkaihuang@gmail.com", "111111"))

    db.session.add(Bank("招商银行", "", ""))
    db.session.add(Bank("平安银行", "", ""))
    db.session.add(Bank("建设银行", "", ""))
    db.session.add(Bank("兴业银行", "", ""))
    db.session.add(Bank("支付宝花呗", "", ""))
    db.session.add(Bank("京东白条", "", ""))

    # commit the changes
    db.session.commit()
