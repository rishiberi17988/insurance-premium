import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logging import logging
from src.utils.utils import load_object


class PredictPipeline:

    
    def __init__(self):
        print("init.. the object")

    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_fea=preprocessor.transform(features)
            pred=model.predict(scaled_fea)

            return pred

        except Exception as e:
            raise customexception(e,sys)


class CustomData:
    def __init__(self,
                 age:int,
                 bmi:float,
                 children:int,
                 sex:str,
                 smoker:str,
                 region:str):
        
        self.age=age
        self.bmi=bmi
        self.children=children
        self.sex = sex
        self.smoker = smoker
        self.region = region
            
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'age':[self.age],
                'bmi':[self.bmi],
                'children':[self.children],
                'sex':[self.sex],
                'smoker':[self.smoker],
                'region':[self.region]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customexception(e,sys)