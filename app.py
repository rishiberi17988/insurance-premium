import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

# Title of the Streamlit app
st.title("Premium insurance")

# Sidebar for user input
st.sidebar.header("Input Parameters")

def user_input_features():
    age = st.sidebar.number_input('age', min_value=0, value=25)
    bmi = st.sidebar.number_input('bmi', min_value=0, value=25)
    children = st.sidebar.number_input('children', min_value=0, value=0)
    
    sex = st.sidebar.selectbox('sex', ('male' , 'female'))
    smoker = st.sidebar.selectbox('Smoker', ('yes', 'no'))
    region = st.sidebar.selectbox('region', ('southeast', 'southwest', 'northeast', 'northwest'))

    data = {
        'age': age,
        'bmi': bmi,
        'children': children,
        'sex': sex,
        'smoker': smoker,
        'region': region
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display input features
st.subheader('User Input parameters')
st.write(input_df)

# Prediction
if st.button('Predict'):
    data = CustomData(
        age=input_df.at[0, 'age'],
        bmi=input_df.at[0, 'bmi'],
        children=input_df.at[0, 'children'],
        sex=input_df.at[0, 'sex'],
        smoker=input_df.at[0, 'smoker'],
        region=input_df.at[0, 'region']
    )
    
    final_data = data.get_data_as_dataframe()
    
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_data)
    result = round(pred[0], 2)
    
    st.subheader('Prediction')
    st.write(f'The predicted expense is ${result}')
