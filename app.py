from flask import Flask
from datetime import date
from peewee import *
# import config
# import create_customer


app = Flask (__name__)
db = SqliteDatabase('./people.db') 

class Customer(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    join_date = DateField()
    salary = FloatField()

    class Meta:
        database = db 

class Invoice(Model):
    id = AutoField()
    customer = ForeignKeyField(Customer)
    invoice_date = DateField(default=date.today) 
    total_amount = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db


class InvoiceItem(Model):
    item_name = CharField(200, unique=True)
    invoice = ForeignKeyField(Invoice, backref="items", lazy_load=False)
    quantity = IntegerField()
    unit_price = FloatField()
    amount = FloatField()
    
    class Meta:
        database = db

# Invoice.create_table()
# db.connect()
# db.create_tables([Invoice]) 

def create_tables():
    db.connect()
    db.create_tables([InvoiceItem])
    db.close()

# @app.before_request
# def before_request():
#     if db.is_closed():
#         db.connect()

# def create_tables():
#     db.connect(reuse_if_open=True)
#     db.create_tables([Customer, Invoice, InvoiceItem])
#     print("Tables created successfully!")

@app.route("/")
def home():
    return "app"
# Invoice.drop_table()
# InvoiceItem.drop_table()

# config.run()
# create_customer.run()
# Invoice.create_table()
# InvoiceItem.create_table()

print(db.get_tables())
if __name__ == "__main__":
    print("app runing successfully!")
    app.run(debug=True)
