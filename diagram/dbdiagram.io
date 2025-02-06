// Warsztat samochodowy database schema
// Docs: https://dbml.dbdiagram.io/docs

Table employees {
  id integer [primary key]
  first_name varchar
  last_name varchar
}

Table fuel_types {
  id integer [primary key]
  type varchar
}

Table vehicles {
  id integer [primary key]
  model varchar
  brand varchar
  production_year integer
  vin varchar [unique]
  engine_capacity integer
  registration_number varchar [unique]
  fuel_type_id integer
}

Table orders {
  id integer [primary key]
  description varchar
  creation_date timestamp
  employee_id integer
  vehicle_id integer
}

Table actions {
  id integer [primary key]
  name varchar
}

Table tasks {
  id integer [primary key]
  employee_id integer
  action_id integer
  order_id integer
  start_date timestamp
  end_date timestamp
}

// Relationships

Ref: vehicles.fuel_type_id > fuel_types.id 
Ref: orders.employee_id > employees.id 
Ref: orders.vehicle_id > vehicles.id 
Ref: tasks.employee_id > employees.id
Ref: tasks.action_id > actions.id 
Ref: tasks.order_id > orders.id 
