from flask import Flask, jsonify
import pyglet
import math
import threading

class GameController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        # Initialize Pyglet Joystick
        joysticks = pyglet.input.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            pyglet.input.Joystick
            # Register event handlers
            self.joystick.on_joybutton_press = self.on_joybutton_press
            self.joystick.on_joybutton_release = self.on_joybutton_release
            self.joystick.on_joyaxis_motion = self.on_joyaxis_motion
        else:
            print("No joystick/gamepad found.")
            self.joystick = None

    def read(self): # return the buttons/triggers that you care about in this method
        lJoyStickX = self.LeftJoystickX
        lJoyStickY = self.LeftJoystickY
        lt = self.LeftTrigger
        rt = self.RightTrigger
        lb = self.LeftBumper
        rb = self.RightBumper
        a = self.A
        b = self.B
        x = self.X
        y = self.Y
        return [lJoyStickX, lJoyStickY, lt, rt, a, b, lb, rb, x, y]

    def on_joybutton_press(self, joystick, button):
        # Handle button press event
        print(f'button {button} pressed')
        if str(button) == '0':
            self.X = 1
        elif str(button) == '2':
            self.A = 1
        elif str(button) == '3':
            self.B = 1
        elif str(button) == '4':
            self.Y = 1
        elif str(button) == '5':
            self.LeftBumper = 1
        elif str(button) == '6':
            self.RightBumper = 1
        elif str(button) == '7':
            self.LeftTrigger = 1
        elif str(button) == '8':
            self.RightTrigger = 1
        print(joystick,button)
        pass

    def on_joybutton_release(self, joystick, button):
        # Handle button release events
        print(f'button {button} pressed')
        if str(button) == '0':
            self.X = 0
        elif str(button) == '2':
            self.A = 0
        elif str(button) == '3':
            self.B = 0
        elif str(button) == '4':
            self.Y = 0
        elif str(button) == '5':
            self.LeftBumper = 0
        elif str(button) == '6':
            self.RightBumper = 0
        elif str(button) == '7':
            self.LeftTrigger = 0
        elif str(button) == '8':
            self.RightTrigger = 0
        print("no button")
        pass

    def on_joyaxis_motion(self, joystick, axis, value):
        # Handle joystick movement events
        if axis == 'y':
            self.LeftJoystickY = value
        elif axis == 'x':
            self.LeftJoystickX = value
        elif axis == 'rz':
            self.RightJoystickY = value
        elif axis == 'z':
            self.RightJoystickX = value
        # print(f"Joystick {axis} moved to {value} on {joystick}")
        print("joystick")
        pass

# Flask app setup
app = Flask(__name__)

@app.route('/controller')
def controller():
    print("HEILLO")
    print(joy.LeftJoystickX)
    return jsonify(joy.read())

@app.route('/health')
def health_check():
    return jsonify({"status": "Server is running"})

# Function to run Flask app
def run_flask_app():
    app.run(debug=True, port=5001, use_reloader=False)

# Initialize GameController
joy = GameController()

# Run Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.start()

# Run the Pyglet app
if __name__ == "__main__":
    print("running app")
    pyglet.app.run()
