from flask import Flask
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
    id = AutoField()  # cleaner primary key
    customer = ForeignKeyField(Customer, backref='invoices')
    invoice_date = DateField()
    total_amount = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db

class InvoiceItem(Model):
    item_id = IntegerField(primary_key=True)
    invoice_id = ForeignKeyField(Invoice, backref="item", lazy_load=False)
    description = CharField()
    quantity = IntegerField()
    unit_price = FloatField()
    
    class Meta:
        database = db



def create_tables():
    db.connect()
    db.create_tables([Customer, Invoice, InvoiceItem])
    db.close()


@app.route("/")
def home():
    return "app"

# config.run()
# create_customer.run()

if __name__ == "__main__":
    print("app runing successfully!")
    app.run(debug=True)
