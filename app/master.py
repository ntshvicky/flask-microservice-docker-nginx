import requests

from flask_cors import CORS
from flask_openapi3 import Info, Tag, Server, OpenAPI
from pydantic import BaseModel, Field


#openapi configuartion
info = Info(title="Testing Microservice With Docker Scaled Load Balancing", version="1.0.1")
info.description = "This API for testing Flask Microservice integration with Docker"

# list of server 
servers = [
    Server(url='http://127.0.0.1')
]

app = OpenAPI(__name__, info=info, servers=servers)
app.config["VALIDATE_RESPONSE"] = True
CORS(app)


class MessageResponseModel(BaseModel):
    message: str 
    code: int = Field(0, description="Response status code")

class EmpCodeModel(BaseModel):
    empcode: str

@app.get("/api/get_employees/", 
    summary="This api returns list of employees.",
    responses={"200": MessageResponseModel}, 
    tags=[Tag(name="Return list of employees")])
def getEmployees():
    response = requests.get("http://employee:3002/get_employees")
    return response.json()


@app.get("/api/get_employee/<empcode>", 
    summary="This api returns employee details by employee code passed on path",
    responses={"200": MessageResponseModel}, 
    tags=[Tag(name="Return employee details")])
def getEmployee(path: EmpCodeModel):
    empcode = path.dict()['empcode']
    response = requests.get("http://employee:3002/get_employee/"+empcode)
    return response.json()

@app.get("/api/get_salary/<empcode>", 
    summary="This api returns employee salary details by employee code passed on path",
    responses={"200": MessageResponseModel}, 
    tags=[Tag(name="Return employee salary details")])
def getSalary(path: EmpCodeModel):
    empcode = path.dict()['empcode']
    response = requests.get("http://payroll:3003/get_salary/"+empcode)
    return response.json()


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3001,debug=True,threaded=True)