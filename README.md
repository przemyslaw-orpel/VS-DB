# Vehicle Service Database API Example

## Overview
This project is a **Vehicle Service Database** API built with **Python, Flask, SQLite, and SQLAlchemy**. It provides a RESTful API to manage employees, vehicles, orders, tasks, and actions in a vehicle workshop. The API also includes **Swagger UI** for easy documentation and testing.

## Features
- **CRUD operations** for employees, vehicles, orders, and tasks.
- **SQLite database** with SQLAlchemy ORM.
- **Flask REST API** for interacting with the database.
- **Swagger UI** for API documentation (`/api/docs`).
- **CORS enabled** for external requests.

## Technologies Used
- Python
- Flask
- SQLAlchemy
- SQLite
- Flask-CORS
- Flask-Swagger-UI

## Installation
### Clone the repository
```bash
git clone https://github.com/przemyslaw-orpel/VS-DB.git
cd VS-DB
```

### Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Running the API
```bash
python vs_api.py
```
By default, the API runs on `http://localhost:5000/`

## API Endpoints
| Method | Endpoint        | Description                   |
|--------|----------------|-------------------------------|
| GET    | /employees      | Get all employees            |
| GET    | /vehicles       | Get all vehicles             |
| GET    | /orders         | Get all orders               |
| GET    | /tasks          | Get all tasks                |
| POST   | /add_employee   | Add a new employee           |
| POST   | /add_order      | Add a new order              |

## Swagger UI
The API documentation is available at:
```
http://localhost:5000/api/docs
```

## Database Schema
The SQLite database includes the following tables:
- **employees**: Stores workshop employees.
- **vehicles**: Stores vehicle details.
- **orders**: Stores service orders.
- **tasks**: Tracks tasks assigned to employees.
- **actions**: Defines available service actions.
- **fuel_types**: Stores fuel type details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
