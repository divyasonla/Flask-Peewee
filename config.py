from flask import Flask, jsonify, request, render_template,redirect
from peewee import *
from app import db, Customer, Invoice, InvoiceItem  # your actual model file
from datetime import datetime
from markupsafe import escape

app = Flask(__name__)

# for Customers
# inserting the data 

@app.route("/new-customer")
def customer():
    return render_template("create.html")

#inserting data from Bruno 

@app.route('/customerss', methods=['POST', 'GET'])
def create_customers():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    try:
        data = request.get_json()
        customer = Customer.create(
            name=data['name'],
            join_date=data['join_date'],
            salary=data['salary']
        )
        return jsonify({'message': "Customer created", "id": customer.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# inserting data  from form 

@app.route('/customers', methods=['POST', 'GET'])
def customers():
    if request.method == "POST" :
        name = request.form.get('name')
        join_date = request.form.get('join_date')
        salary = request.form.get('salary')
        customer = Customer.create(
            name = name,
            join_date=join_date,
            salary=salary
        )
        return jsonify({"message": "Customer created", "id": customer.id}), 201
    else:
        customers = Customer.select()
        data = [{"id":d.id, "name":d.name, "join_date":d.join_date, "salary":d.salary} for d in customers ]
        return jsonify(data)
        # return render_template("list-customers.html", customers=customers)


# update the data with specific id with all data updating 
@app.route("/update/<int:id>")
def update(id):
    try :
        customer = Customer.get(Customer.id == id)
        
        return render_template('update.html', customer=customer)
    except Customer.DoesNotExist:

        return "Customer not found", 404

@app.route('/update_customers/<int:id>' , methods = ['POST','GET'])
def update_customers(id):
    try :
        update = Customer.get(Customer.id == id)

        if request.method == "POST":
            update.name = request.form.get("name")
            update.join_date = request.form.get("join_date")
            update.salary = request.form.get("salary")
            update.save()
            return jsonify({"message": "Customer updated", "id":update.id}), 201
        return jsonify({
            "id": update.id,
            "name": update.name,
            "join_date":update.join_date,
            "salary":update.salary
        })
    except:
        return "Customer not found"


# Delete the data with specific id 
@app.route('/delete/<int:id>')  
def delete(id):
    customer = Customer.get(Customer.id == id)
    customer.delete_instance()
    return f"Deleted the {customer}"


@app.route("/new-invoice")
def new_invoice():
    return render_template("invoice-create.html")

# @app.route('/invoice', methods=['POST', 'GET'])
# def invoice():
#     if request.method == "POST":
#         customer = request.form.get("customer_id")
#         invoice_date = request.form.get("invoice_date")
#         total_amount = request.form.get("total_amount")
#         # create_at = request.form.get("created_at")
#         created_at = datetime.now()
#         with db.atomic():
#             Invoices = Invoice.create(customer=customer, invoice_date=invoice_date, total_amount=total_amount, created_at=created_at)
#             Invoices.save()
#         return jsonify({'message': 'Invoice created successfully'}), 201

#     else:
#         Invoices = Invoice.select()
#         data = [{
#                 'invoice_id': i.id,
#                 'customer': i.customer.id,
#                 'invoice_date': i.invoice_date,
#                 'total_amount': i.total_amount,
#                 'created_at': i.created_at
#             } for i in Invoices]
#         return jsonify(data)


# getting data and inserting the data from invoice

@app.route('/invoice', methods=['POST', 'GET'])
def invoice():
    if request.is_json and request.method == "POST":
        data = request.get_json()
        customer = data.get("customer")
        invoice_date = data.get("invoice_date")
        created_at = datetime.now()
        items_data = data.get("items", [])
    
        # ✅ Corrected total calculation
        total = sum(item["quantity"] * item["unit_price"] for item in items_data)
    
        invoice = Invoice.create(
            customer=customer,
            invoice_date=invoice_date,
            total_amount=total,
            created_at=created_at
        )
    
        for item in items_data:
            InvoiceItem.create(
                invoice=invoice,
                quantity=item["quantity"],
                unit_price=item["unit_price"]
            )
        return jsonify({'message': 'Invoice created successfully'}), 201

    else:
        Invoices = Invoice.select()
        data = [{
                'invoice_id': i.id,
                'customer': i.customer.id,
                'invoice_date': i.invoice_date,
                'total_amount': i.total_amount,
                'created_at': i.created_at
            } for i in Invoices]
        return jsonify(data)
    

# deleting the data from invoice

@app.route("/invoice/<int:id>", methods=["DELETE"])
def d_invoice(id):
    # invoice_id = request.get_json()
    try :
        invoice = Invoice.get_by_id(id)
        invoice.delete_instance()
        return jsonify({"message": f"Invoice {id} deleted successfully"}), 200
    except Invoice.DoesNotExist:
        return "Invoice not found"


# updating the data from invoice

@app.route("/invoice/<int:id>", methods=["PUT"])
def d_in(id):
    try :
        data = request.get_json()
        invoice = Invoice.get_by_id(id)
        invoice.invoice_date = data.get("invoice_date", invoice.invoice_date)
        invoice.total_amount = data.get("total_amount", invoice.total_amount)
        invoice.customer = data.get("customer", invoice.customer)
        invoice.save()
        return jsonify({"message":"Invoice Update Successful"})
    except:
        return jsonify({"error":"Invoice not found"})

@app.route("/item", methods=['GET', 'POST'])
def item():
    if request.is_json and request.method == 'POST':
        data = request.get_json()
        item_name= data.get("item_name")
        invoice= data.get("invoice")
        # amount = data.get("amount")
        quantity =  data.get("quantity")
        unit_price = data.get("unit_price")

        item = InvoiceItem.create(
            item_name=item_name,
            invoice = invoice,
            amount = quantity * unit_price,
            quantity = quantity,
            unit_price = unit_price
        )
        item.save()
        return jsonify({'message':"Successful created InvoiceItem! "})
    else:
        Item = InvoiceItem.select()
        data = [{
            "item_name":i.item_name,
            "invoice":i.invoice,
            "amount":i.amount,
            "quantity": i.quantity,
            "unit_price":i.unit_price
        } for i in Item]

        return jsonify(data)
    


    # n = Invoice.select()
    # data = [{"invoice_id" : d.id, "customer":d.customer,"total_amount" :d.total_amount} for d in n]
    # return jsonify(data)
# # Creating the invoice 
# @app.before_request
# def before_request():
#     if db.is_closed():
#         db.connect()

# @app.teardown_request
# def teardown_request(exception):
#     if not db.is_closed():
#         db.close()
# @app.route("/new-invoice")
# def invoice():
#     return render_template("invoice-create.html")

# @app.route("/invoices", methods=["POST",'GET'])
# def invoices():
#     if request.method == "POST":
#         customer_id = request.form.get("customer_id")
#         # customer = Customer.get_by_id(customer)
#         invoice_date = request.form.get("invoice_date")
#         total_amount = request.form.get("total_amount")
#         created_at = request.form.get("created_at")
#         invoice = Invoice(customer=customer_id,
#                            invoice_date=invoice_date, 
#                            total_amount=total_amount, 
#                            created_at=created_at)
#         invoice.save()
#         return redirect("/invoices")
#     else:
#         invoices = Invoice.select()
#         data = [{
#                 'invoice_id': i.id,
#                 'customer': i.customer.id,
#                 'invoice_date': i.invoice_date,
#                 'total_amount': i.total_amount,
#                 'created_at': i.created_at
#             } for i in invoices]
#         return jsonify(data)


# @app.route('/update_invoice/<int:id>')
# def update_invoice(id):
#     try :
#         invoi = Invoice.get(Invoice.id == id )
#         if request.method == "POST":
#             invoi.customer_id = request.form.get("customer_id")
#             invoi.invoice_date = request.form.get("invoice_date")
#             invoi.total_amount = request.form.get("total_amount")
#             invoi.created_at = request.form.get("created_at")

#             invoi.save()
#             return jsonify({"message": "Customer updated", "id":update.id}), 201
#         return jsonify({
#             'invoice_id': invoi.id,
#                 'customer_id': invoi.customer.id,
#                 'invoice_date': invoi.invoice_date,
#                 'total_amount': invoi.total_amount,
#                 'created_at': invoi.created_at
#         })
#     except:
#         return "Invoice is not found"


# 

# def get_all_users():
#     data = Customer.select()
#     for i in data:
#         print(i)



if __name__=="__main__":
    print("connecting to DB....")
    app.run(debug=True)
