from flask import Flask, render_template, request, redirect
from app import db, Customer, Invoice, InvoiceItem
app = Flask(__name__)




# @app.route("/new-customer")
# def customer():
#     return render_template("create.html")

    
# @app.route('/customers', methods=['POST', 'GET'])
# def customers():
#     if request.method == "POST":
#         name = request.form.get("name")
#         join_date = request.form.get("join_date")
#         salary = request.form.get("salary")
#         customer = Customer(name=name, join_date= join_date, salary=salary)
#         customer.save()
#         return redirect("/customers")

#     else:
#         customers = Customer.select()
#         return render_template("create.html", customers=customers)



# data = [
#     {'name':"A", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"D", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"C", 'join_date':'2000-9-23', 'salary':5000},
#     {'name':"E", 'join_date':'2000-9-23', 'salary':5000}
# ]
# Customer.insert_many(data).execute()
# p = Customer.create(name="A", join_date="2025-7-15", salary=5000)
# p.save()



# for Customers 
# customer = Customer.create(
#     # id = int(input("enter a int : ")),
#     name = input("enter a Customers name :"),
#     join_date = input("enter a joining date (YYYY-MM-DD) :"),
#     salary = float(input("enter  a salary : "))
# )
# customer.save()

# for Invoice
# invoice = Invoice.create(
#     invoice_id=int(input("enter a invoice_id : ")), 
#     customer_id=int(input("enter customer_id : ")), 
#     invoice_date=input("enter a date (YYYY-MM-DD) : "), 
#     total_amount=float(input("input total amount : ")),
#     created_at=datetime.now()
# )
# invoice.save()

# for i in Invoice.select():
#     print(i.invoice_id, i.customer_id_id, i.total_amount)


# for InvoiceItem

# v = InvoiceItem.create(
#     item_id =int(input('enter item id :')),
#     invoice_id = int(input("enter invoice_id : ")),
#     description = input("enter description : "),
#     quantity = int(input("enter quantity :")),
#     unit_price = float(input("enter price : "))
# )
# v.save()


# @app.route('/api/invoice')
# def api_invoice():
#     g = Invoice.select()
#     data = [{
#         'invoice_id': i.invoice_id,
#         'customer_id': i.customer_id.id,
#         'invoice_date': i.invoice_date.isoformat(),
#         'total_amount': i.total_amount,
#         'created_at': i.created_at.isoformat()
#     } for i in g]
#     return jsonify(data)

# @app.route('/api/invoiceItem')
# def api_invoiceItem():
#     v = InvoiceItem.select()
#     data = [{'id':i.item_id, "description":i.description, "Quantity":i.quantity} for i in v]
#     return jsonify(data)




# @app.route("/invoice")
# def invoice():
#     return render_template('invoice-create.html')

# data = Customer.select()
# for i in data:
#     if i.id < 5:
#         i.delete_instance()
#     print(i.id, i.name)


if __name__=="__main__":
    print("customer....")
    app.run(debug=True)

