import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, Response
from gpiozero import Robot
from gpiozero import Motor
from functools import wraps
from time import sleep
#from mpu6050 import mpu6050
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

TRANSMITTER    = 13
GPIO.setup(TRANSMITTER,GPIO.OUT)
GPIO.output(TRANSMITTER, False)

app = Flask(__name__)
handler = RotatingFileHandler('/var/log/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
robot = Robot(left=(22, 27), right=(17, 4))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor')
def sensor():
	return render_template('sensor.html')

@app.route('/robot_left', methods=['POST'])
def robot_left():
    #print 'robot_left'
    robot.left(1)
    sleep(0.75)
    robot.stop()
    return 'L'

@app.route('/robot_right', methods=['POST'])
def robot_right():
    #print 'robot_right'
    robot.right(1)
    sleep(0.75)
    robot.stop()
    return 'R'

@app.route('/robot_forward', methods=['POST'])
def robot_forward():
    #print 'robot_forward'
    robot.forward(1)
    sleep(3)
    robot.stop()  	
    #course_correct()
    return 'F'

@app.route('/robot_backward', methods=['POST'])
def robot_backward():
    #print 'robot_backward'
    robot.backward(1)
    sleep(2)
    robot.stop()
    return 'B'

@app.route('/fire_gun', methods=['POST'])
def fire_gun():
	GPIO.output(TRANSMITTER, True)
	sleep(.5)
	GPIO.output(TRANSMITTER, False)
	return '?'

@app.route('/power_off', methods=['POST'])
def powerOff():
    os.system("sudo poweroff")
    return 'OFF'



#request.args.get('username')

#
#
#def check_auth(username, password):
#    """This function is called to check if a username /
#    password combination is valid.
#    """
#    return username == 'admin' and password == 'secret'

#def authenticate():
#    """Sends a 401 response that enables basic auth"""
#    return Response(
#    'Could not verify your access level for that URL.\n'
#    'You have to login with proper credentials', 401,
#    {'WWW-Authenticate': 'Basic realm="Login Required"'})
#
#def requires_auth(f):
#    @wraps(f)
#    def decorated(*args, **kwargs):
#        auth = request.authorization
#        if not auth or not check_auth(auth.username, auth.password):
#            return authenticate()
#        return f(*args, **kwargs)
#    return decorated


#@app.route('/secret-page')
#@requires_auth
#def secret_page():
#    return render_template('secret_page.html')

@app.route('/robot_controller')
#@requires_auth
def robot_controller():
    return render_template('robot_controller.html')

@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')



'''
def accel_orientation():
        sensor = mpu6050(0x68)
        accel_data = sensor.get_accel_data()
        return accel_data
def check_x_acceleration():
    accel_data = accel_orientation()    	
    app.logger.error("y: " + str(accel_data['y']))
    app.logger.error("z: " + str(accel_data['z']))
def check_y_acceleration():
    accel_data = accel_orientation()    	
    app.logger.error("y: " + str(accel_data['y']))
    app.logger.error("z: " + str(accel_data['z']))

def course_correct():
	#drive_forward()
	drive_forward()
	robot.stop()
	return 'F'
def drive_forward():
    #robot.forward(.8)
    #check_y_acceleration()
    #check_x_acceleration()
    #sleep(.3)
	for num in range(1,20):
		robot.forward(.8)    	
		sleep(.12)
		veer = check_veer()
		app.logger.error("veer |"+str(veer)+"|")
		if int(veer) == -1:
			robot.left(.5)
			sleep(.04)
		elif int(veer) == -2:
			robot.left(.5)
			sleep(.07)   
		elif int(veer) == -3:
			robot.left(.6)
			sleep(.1)  
		elif int(veer) == 1:
			robot.right(.5)
			sleep(.04)
		elif int(veer) == 2:
			robot.right(.5)
			sleep(.07)   
		elif int(veer) == 3:
			robot.right(.6)
			sleep(.11)      
    	
def gyro_orientation():
        sensor = mpu6050(0x68)
        gyro_data = sensor.get_gyro_data()
        return gyro_data
def check_x_rotation():
        gyro_data = gyro_orientation()
        #app.logger.error("x: " + str(gyro_data['x']))
        return gyro_data['x']
def check_veer():
    x_rot = check_x_rotation()
    app.logger.error(x_rot)
    if x_rot < 8 and x_rot > -8:
        return 0
    elif x_rot > 8 and x_rot < 15:
        return 1
    elif x_rot < -8 and x_rot > -15:
        return -1
    elif x_rot > 15 and x_rot < 30:
        return 2
    elif x_rot < -15 and x_rot > -30:
        return -2
    elif x_rot > 30:
        return 3
    elif x_rot < 30:
        return -3

'''
