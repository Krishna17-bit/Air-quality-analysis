from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        # Assuming you are sending some parameters to predict air quality
        humidity = request.form.get('humidity')
        temperature = request.form.get('temperature')
        # Generate a random prediction for simplicity
        prediction = random.randint(1, 500)  # AQI ranges arbitrarily set from 1 to 500

    # Render a simple form to input humidity and temperature
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
