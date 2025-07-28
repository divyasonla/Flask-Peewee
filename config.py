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
def invoice():
    return render_template("invoice-create.html")

@app.route("/invoices", methods=["POST",'GET'])
def invoices():
    if request.method == "POST":
        customer = int(request.form.get("customer_id"))
        customer = Customer.get_by_id(customer)
        invoice_date = request.form.get("invoice_date")
        total_amount = request.form.get("total_amount")
        created_at = request.form.get("created_at")
        invoice = Invoice(customer=customer,
                           invoice_date=invoice_date, 
                           total_amount=total_amount, 
                           created_at=created_at)
        invoice.save()
        return redirect("/invoices")
    else:
        invoices = Invoice.select()
        data = [{
                'invoice_id': i.id,
                'customer_id': i.customer.id,
                'invoice_date': i.invoice_date,
                'total_amount': i.total_amount,
                'created_at': i.created_at
            } for i in invoices]
        return jsonify(data)



# def get_all_users():
#     data = Customer.select()
#     for i in data:
#         print(i)



if __name__=="__main__":
    print("connecting to DB....")
    app.run(debug=True)
