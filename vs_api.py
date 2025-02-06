from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from vs_db import engine, Employee, Vehicle, FuelType, Order, Action, Task, Base

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Swagger setup
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Workshop API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Routes
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = session.query(Employee).all()
    return jsonify([{'id': e.id, 'first_name': e.first_name, 'last_name': e.last_name} for e in employees])

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = session.query(Vehicle).all()
    return jsonify([{'id': v.id, 'model': v.model, 'brand': v.brand, 'vin': v.vin, 'fuel_type_id': v.fuel_type_id} for v in vehicles])

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = session.query(Order).all()
    return jsonify([{'id': o.id, 'description': o.description, 'creation_date': o.creation_date.isoformat(), 'employee_id': o.employee_id, 'vehicle_id': o.vehicle_id} for o in orders])

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = session.query(Task).all()
    return jsonify([{'id': t.id, 'employee_id': t.employee_id, 'action_id': t.action_id, 'order_id': t.order_id, 'start_date': t.start_date.isoformat(), 'end_date': t.end_date.isoformat() if t.end_date else None} for t in tasks])

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(first_name=data['first_name'], last_name=data['last_name'])
    session.add(new_employee)
    session.commit()
    return jsonify({'message': 'Employee added successfully', 'id': new_employee.id}), 201

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.json
    new_order = Order(description=data['description'], employee_id=data['employee_id'], vehicle_id=data['vehicle_id'])
    session.add(new_order)
    session.commit()
    return jsonify({'message': 'Order added successfully', 'id': new_order.id}), 201

if __name__ == '__main__':
    app.run(debug=True)
