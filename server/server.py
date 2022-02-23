from flask import Flask, request, jsonify
import util

app = Flask(__name__)


# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    request_data = request.get_json()

    longitude = float(request_data['longitude'])
    latitude = float(request_data['latitude'])
    housing_median_age = float(request_data['housing_median_age'])
    households = float(request_data['households'])
    median_income = float(request_data['median_income'])
    # ocean_proximity = float([])

    response = jsonify({
        'estimated_price': util.get_estimated_price(longitude, latitude, housing_median_age,
                                                    households, median_income)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.set_data()

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
