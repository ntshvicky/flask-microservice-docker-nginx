from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

employees = [ {
        "empcode": "10001",
        "name": "ABCD",
        "CTC": 100000
    },{
        "empcode": "10002",
        "name": "PQRS",
        "CTC": 150000
    }]

@app.route('/get_employees')
def getEmployees():
    return jsonify({'status': True, 'data': employees})

@app.route('/get_employee/<empcode>')
def getEmployee(empcode):
    employee = [emp for emp in employees if emp['empcode'] == empcode]
    return jsonify({'status': True, 'data': employee})

if __name__ == '__main__':
     app.run(host="0.0.0.0",port=3002, threaded=True,debug=True)