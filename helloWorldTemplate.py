
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

in1 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, False)
try:
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])


    def hello():
        if request.method == 'POST':
            if request.form['light'] == "ON":
                #turn light on
                GPIO.output(in1, True)
            elif request.form['light'] == "OFF":
                #turn light off
                GPIO.output(in1, False)
        return render_template('index.html')

    if __name__ == "__main__":
            app.run(host='0.0.0.0', port=80, debug=True)

except KeyboardInterrupt:
    GPIO.cleanup()
