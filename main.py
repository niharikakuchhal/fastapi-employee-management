from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel, Field
import json, os
app = FastAPI()

filename = "Employee_data.json"

def save_json(data, filename=filename):
    try:
        with open(filename, 'w',encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except (OSError, TypeError) as e:
            print(f"Error saving data: {e}")
            return False

def load_json(filename=filename):
    if not os.path.exists(filename):
        print("Employee data not present")
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            emp = json.load(file)
            return emp
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return {}

# emp = {"101":{"name":"Niharika", "salary":50000},"102":{"name":"Ani", "salary":100000}}

class Employee(BaseModel):
    id: str
    name: str = Field(min_length=2, examples=["Niharika"])
    salary: int = Field(gt=0, examples=[50000])

class EmployeeResponse(BaseModel):
    name: str
    salary: int

class UpdateEmployee(BaseModel):
    name: Optional[str] = Field(None, min_length=2)
    salary: Optional[int] = Field(None, gt=0)

@app.get("/employees")
def search_employee(id: Optional[str] = None, name: Optional[str] = None):
    emp = load_json()
    if id:
        if id not in emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"id": id, "details": emp[id]}
    elif name:
        for emp_id, details in emp.items():
            if details["name"].lower() == name.lower():
                return {"id": emp_id, "details": details}
        raise HTTPException(status_code=404, detail="Employee not found with that name")
    else:
        return emp

@app.get("/employee/{id}",response_model=EmployeeResponse)
def employee(id:str):
    emp = load_json()
    if id in emp:
        return emp[id]
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employee",status_code=status.HTTP_201_CREATED,response_model=Employee)
def add_employee(employee: Employee):
    emp = load_json()
    if employee.id in emp:
        raise HTTPException(status_code=400, detail="Employee already exists")
    emp[employee.id] = {"name":employee.name, "salary":employee.salary}
    save_json(emp)
    return employee

@app.delete("/employee/{id}", status_code=status.HTTP_200_OK)
def delete_employee(id:str):
    emp = load_json()
    if id in emp:
        del emp[id]
        save_json(emp)
        return {"message":"Successfully deleted employee"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employee/{id}", response_model=EmployeeResponse)
def update_employee(id:str, update:UpdateEmployee):
    emp = load_json()
    if id in emp:
        if update.name is not None:
            emp[id]["name"] = update.name
        if update.salary is not None:
            emp[id]["salary"] = update.salary
        save_json(emp)
        return emp[id]
    raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/")
def home():
    return {"message": "Welcome to Employee API"}