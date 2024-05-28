from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            age=int(request.form.get('age')),
            bmi=float(request.form.get('bmi')),
            children=int(request.form.get('children')),
            sex=request.form.get('sex'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )
        # this is my final data
        final_data = data.get_data_as_dataframe()
        
        predict_pipeline = PredictPipeline()
        
        pred = predict_pipeline.predict(final_data)
        
        result = round(pred[0], 2)
        
        return render_template("result.html", final_result=result)

# Execution begins
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
