# FastAPI Employee Management API

A RESTful Employee Management API built using FastAPI. This project demonstrates CRUD operations, request validation using Pydantic, response models, HTTP status codes, and exception handling.

## Features

* Create Employee
* View Employee by ID
* Search Employee by ID or Name
* Update Employee Details
* Delete Employee
* Request Validation using Pydantic
* Response Models
* HTTP Status Codes
* Exception Handling with HTTPException
* Interactive Swagger Documentation

## Technologies Used

* Python 3
* FastAPI
* Pydantic
* Uvicorn

## Installation

Clone the repository:

```bash
git clone https://github.com/niharikakuchhal/fastapi-employee-management.git
cd fastapi-employee-management
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Get All Employees

```http
GET /employees
```

### Search Employee by ID

```http
GET /employees?id=101
```

### Search Employee by Name

```http
GET /employees?name=Niharika
```

### Get Employee by ID

```http
GET /employee/{id}
```

Example:

```http
GET /employee/101
```

### Add Employee

```http
POST /employee
```

Request Body:

```json
{
  "id": "103",
  "name": "Riya",
  "salary": 60000
}
```

### Update Employee

```http
PUT /employee/{id}
```

Example:

```http
PUT /employee/103
```

Request Body:

```json
{
  "name": "Riya Sharma",
  "salary": 70000
}
```

### Delete Employee

```http
DELETE /employee/{id}
```

Example:

```http
DELETE /employee/103
```

## Validation Rules

### Employee

* Name must contain at least 2 characters.
* Salary must be greater than 0.
* Employee ID must be unique.

### Update Employee

* Name must contain at least 2 characters if provided.
* Salary must be greater than 0 if provided.

## Sample Response

```json
{
  "name": "Niharika",
  "salary": 50000
}
```

## Learning Outcomes

This project helped me learn:

* REST API Development
* FastAPI Framework
* CRUD Operations
* Path Parameters
* Query Parameters
* Request Body Validation
* Response Models
* HTTP Status Codes
* Exception Handling
* API Testing using Swagger UI

## Future Improvements

* Store employee data in JSON files
* Integrate SQLite Database
* Use SQLAlchemy ORM
* Authentication and Authorization
* Unit Testing with Pytest
* Docker Support

## Author

Niharika Kuchhal
