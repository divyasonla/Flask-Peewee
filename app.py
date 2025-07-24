from flask import Flask
from peewee import *

app = Flask (__name__)
db = SqliteDatabase('./people.db') 

class Customer(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    join_date = DateField()
    salary = FloatField()

    class Meta:
        database = db 

# class 

p = Customer(name = "A", join_date = "2000-9-23",salary = 50000)

def create_tables():
    db.connect()
    db.create_tables([Customer])
    db.close()


@app.route("/")
def app():
    return "app"


if __name__ == "__main__":
    print("app runing successfully!")
    app.run(debug = True)