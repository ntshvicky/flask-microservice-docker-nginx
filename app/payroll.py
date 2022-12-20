from flask import Flask, jsonify
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

empPayroll = [ {
        "empcode": "10001",
        "basic": 6000,
        "HRA": 2000,
        'MED': 2000
    },{
        "empcode": "10002",
        "basic": 11000,
        "HRA": 3000,
        'MED': 2000
    }]


@app.route('/get_salary/<empcode>')
def getSalary(empcode):
    payroll = [emp for emp in empPayroll if emp['empcode'] == empcode]
    return jsonify({'status': True, 'data': payroll})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3003,threaded=True,debug=True)