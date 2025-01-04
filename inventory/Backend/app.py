from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database connection configuration
app.config['MYSQL_HOST'] = 'localhost'  # or your database host
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'Sabitha@2004'  # MySQL password
app.config['MYSQL_DB'] = 'TelecomInventory'  # Your database name

mysql = MySQL(app)

# Route to get data from the 'User' table
@app.route('/api/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM User")  # Table name: User
    users = cursor.fetchall()
    return jsonify(users)

# Route to get data from the 'Product' table
@app.route('/api/products', methods=['GET'])
def get_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product")  # Table name: Product
    products = cursor.fetchall()
    return jsonify(products)

# Route to insert data into the 'User' table
@app.route('/api/users', methods=['POST'])
def insert_user():
    user_data = request.get_json()  # Expecting JSON data
    username = user_data['UserName']
    password = user_data['Password']
    first_name = user_data['FirstName']
    last_name = user_data['LastName']
    role = user_data['Role']
    phone = user_data['Phone']
    email = user_data['Email']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO User (UserName, Password, FirstName, LastName, Role, Phone, Email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (username, password, first_name, last_name, role, phone, email))
    
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"message": "User added successfully!"}), 201

# Route to insert data into the 'Product' table
@app.route('/api/products', methods=['POST'])
def insert_product():
    product_data = request.get_json()  # Expecting JSON data
    product_name = product_data['ProductName']
    description = product_data['Description']
    product_image = product_data['ProductImage']
    category = product_data['Category']
    model_number = product_data['ModelNumber']
    serial_number = product_data['SerialNumber']
    stock_level = product_data['StockLevel']
    reorder_point = product_data['ReorderPoint']
    supplier_name = product_data['SupplierName']
    supplier_mail = product_data['SupplierMail']
    supplier_contact = product_data['SupplierContact']
    order_date = product_data['OrderDate']
    quantity = product_data['Quantity']
    order_status = product_data['OrderStatus']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO Product (ProductName, Description, ProductImage, Category, ModelNumber, SerialNumber, StockLevel, ReorderPoint, SupplierName, SupplierMail, SupplierContact, OrderDate, Quantity, OrderStatus)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (product_name, description, product_image, category, model_number, serial_number, stock_level, reorder_point, supplier_name, supplier_mail, supplier_contact, order_date, quantity, order_status))
    
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"message": "Product added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)

