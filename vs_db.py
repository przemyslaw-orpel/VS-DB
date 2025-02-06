from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Creating database
engine = create_engine('sqlite:///vs_db.sqlite', echo=True)
Base = declarative_base()

# Table definitions
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="employee")
    orders = relationship("Order", back_populates="employee")

class FuelType(Base):
    __tablename__ = 'fuel_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    vehicles = relationship("Vehicle", back_populates="fuel_type")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    production_year = Column(Integer, nullable=False)
    vin = Column(String, unique=True, nullable=False)
    engine_capacity = Column(Integer, nullable=False)
    registration_number = Column(String, unique=True, nullable=False)
    fuel_type_id = Column(Integer, ForeignKey('fuel_type.id'))
    fuel_type = relationship("FuelType", back_populates="vehicles")
    orders = relationship("Order", back_populates="vehicle")

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    employee = relationship("Employee", back_populates="orders")
    vehicle = relationship("Vehicle", back_populates="orders")
    tasks = relationship("Task", back_populates="order")

class Action(Base):
    __tablename__ = 'action'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="action")

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    action_id = Column(Integer, ForeignKey('action.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)
    employee = relationship("Employee", back_populates="tasks")
    action = relationship("Action", back_populates="tasks")
    order = relationship("Order", back_populates="tasks")

# Creating tables
Base.metadata.create_all(engine)

# Creating session
Session = sessionmaker(bind=engine)
session = Session()

print("Database 'vs_db' has been created.")