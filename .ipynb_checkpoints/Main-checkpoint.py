from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

def iot_data_collection():
    # assume this is the iot part where sensors and actuators come in to give data to our program
    start = datetime(2018, 1, 1)
    end = datetime(2018, 12, 31)

    vancouver = Point(49.2497, -123.1193, 70)
    print(id(end))

    data = Daily(vancouver, start, end)
    data = data.fetch()
    print(data)
    data.plot(y=['tavg', 'tmin', 'tmax'])
    plt.show()
    return

def predict_generation():
    # Do testing/training to give out a model which predicts the generation based on the weather data that we got
    return 

def optimize():
    # Do some optimization to get the best possible generation based on the model prediction
    return

iot_data_collection()