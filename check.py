# import sqlite3

# conn = sqlite3.connect('people.db')
# cursor = conn.cursor()

# # Show list of tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("Tables:", tables)

# # Check table schema (columns of Person table)
# cursor.execute("PRAGMA table_info(Person);")
# columns = cursor.fetchall()
# print("Person table columns:", columns)

# conn.close()
from app import Invoice, Customer  # Make sure 'app.py' defines models and database connection
from datetime import datetime, date

# Step 1: Create a customer
customer = Customer.create(
    name="John Doe",
    join_date=date.today(),
    salary=50000.0
)
print("Customer created with ID:", customer.id)

# Step 2: Create invoice for that customer
invoice = Invoice.create(
    customer=customer,  # Use the object instead of fetching again
    invoice_date='2025-07-27',
    total_amount=5000.0,
    created_at=datetime.now()
)
print("Invoice created with ID:", invoice.invoice_id)


# Fetch and print invoice IDs
invoices = Invoice.select()
for i in invoices:
    print(i.invoice_id) 