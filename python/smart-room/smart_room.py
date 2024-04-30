import json
from flask import Flask
from flask import jsonify
from flask import Response
from flask import render_template 

from model import SmartRoom

app = Flask(__name__)

# the model
smart_room = SmartRoom("kitchen")

@app.route('/lights/<string:light_id>/state',  methods=['GET'])
def getState(light_id):
    try:
        state = smart_room.getLightState(light_id)
        return jsonify({ 'result': 'ok', 'state': state })
    except:
        return jsonify({ 'result': 'error'})

@app.route('/lights/<string:light_id>/turnOn',  methods=['POST'])
def turnOn(light_id):
    try:
        smart_room.turnOn(light_id)
        return jsonify({ 'result': 'ok'})
    except:
        return jsonify({ 'result': 'error'})

@app.route('/lightswitches/<string:switch_id>/press',  methods=['POST'])
def press(switch_id):
    try:
        smart_room.press(switch_id)
        return jsonify({ 'state': 'ok' })
    except:
        return jsonify({ 'result': 'error'})


@app.route('/lock',  methods=['POST'])
def lock():
    smart_room.lock()
    print("locked")
    return jsonify({ 'result': 'ok' })


# serving the web (view) part

@app.route("/") 
def hello(): 
    message_of_the_day = "Hello, World"
    return render_template('index.html',  
                           message=message_of_the_day) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)