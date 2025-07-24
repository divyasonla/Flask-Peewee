from flask import Flask
from peewee import *
from app import Customer 
from datetime import date

app = Flask(__name__)


# inserting the data 

# data = [
#     {'name':"A", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"D", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"C", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"E", 'join_date':'2000-9-23', 'salary':5000}
# ]
# Customer.insert_many(data).execute()
# p = Customer.create(name="A", join_date="2025-7-15", salary=5000)
# p.save()



# using if else



# pro = Customer.select()
# for i in pro:
#     # if i.salary < 5000:
#     if i.name == "A":
#        print(i.id, i.name, i.join_date, i.salary)



#read the records

r = Customer.select()
for i in r:
    print(i.id, i.name)



# with where 

# recentjoin = Customer.select().where(Customer.join_date > "2005-01-01" )

 
#  Updating data 


#  recentjoin = Customer.get(Customer.name == "A")
# recentjoin.name = "Divya"
# recentjoin.save()
# for i in recentjoin:
#     print(i.name)
# print(recentjoin)

# d = Customer.get(Customer.name =="Divya")
# print(d.id, d.name, d.join_date, d.salary)
  
# With count 




# total = Customer.select().count()

# print(total)


# total = Customer.select().where(Customer.name == "Divya").count()
# print(total)

# order = Customer.select().order_by(Customer.id.desc())
# for i in order:
#     print(i.id, i.name)
# print(order)
# total = Customer.select()


# Delete records

# p = Customer.select().where(Customer.name == "C")
# for i in p:
#     if i.name == "C":
#        print(f"deleteed: {i.id} ")
#        i.delete_instance()

# print(p)
# d = Customer.delete().where(Customer.name == "E").execute()
# print(d)




@app.route("/")
def Hello():
    return 'I am trying to make projec!'