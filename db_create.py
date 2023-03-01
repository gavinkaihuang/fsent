from fsent import app, db
from fsent.models import User, Bank

with app.app_context():
    # app.config.from_pyfile("config.cfg")

    # create the database and the db table
    db.create_all()

    # insert data
    db.session.add(User("gavin", "gavinkaihuang@gmail.com", "111111"))

    db.session.add(Bank("zsyh", "招商银行", "", ""))
    db.session.add(Bank("yayh", "平安银行", "", ""))
    db.session.add(Bank("jsyh", "建设银行", "", ""))
    db.session.add(Bank("xyyh", "兴业银行", "", ""))
    db.session.add(Bank("zgyh", "中国银行", "", ""))
    db.session.add(Bank("msyh", "民生银行", "", ""))
    db.session.add(Bank("alipay", "支付宝花呗", "", ""))
    db.session.add(Bank("jdbt", "京东白条", "", ""))

    # commit the changes
    db.session.commit()
