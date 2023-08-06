from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import threading
model = LinearRegression()

def iot_data_collection():
    # assume this is the iot part where sensors and actuators come in to give data to our program
    start = datetime(2022, 1, 1)
    end = datetime(2023, 12, 31)
    vancouver = Point(49.2497, -123.1193, 70)
    hyderabad = Point(17.3616, 78.4747, 545)
    data = Daily(hyderabad, start, end)
    data = data.fetch()
    gen_thread = threading.Thread(target=predict_generation, args=(data,))
    gen_thread.start()
    data.plot(y=['tavg', 'tmin', 'tmax'])
    plt.show()

def predict_generation(data):
    # Do testing/training to give out a model which predicts the generation based on the weather data that we got
    # Split the data into training/testing sets
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X = [[i.timestamp()] for x, i in enumerate(data.index)] # Features ie the date in unixtime
    y = data['tavg'] # Target variable ie the temperature
    model.fit(X, y)
    tomorrow = datetime.today() + timedelta(days=1)
    prediction = model.predict([[tomorrow.timestamp()]])  # Assume tavg=20, tmin=15, tmax=25
    print(f"Prediction for {tomorrow.date()}: {prediction[0]:.1f} degrees Celsius")
    optimize_thread = threading.Thread(target=optimize, args=(prediction,))
    optimize_thread.start()

def optimize(tomorrow_prediction):
    # Do some optimization to get the best possible generation based on the model prediction
    if tomorrow_prediction >= model.predict([[datetime.today().timestamp()]]):
        print("Increase generation")
        def turn_solar_on():
            print("Solar on")
            return
    else:
        print("Decrease generation")
        def turn_solar_off():
            print("Solar off")
            return

iot_data_collection()