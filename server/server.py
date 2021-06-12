from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    print(util.get_location_name())
    response = jsonify({
        'locations':util.get_location_name()
    })
    print(response)
    response.headers.add('Access-Control-Allow-Origin',"*")

    return response


@app.route("/predict_home_price",methods = ['POST'])
def predict_home_price():
    sqft = float(request.form.get('total_sqft'))
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))


    response = jsonify({
        'estimated_price':util.get_estimated_price(location,sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

if __name__ == '__main__':
    util.load_saved_artifcats()
    app.run(debug=True)