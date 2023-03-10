import os
import sys
from src.exceptional import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataingestionConfig:
    train_data_path:str = os.path.join('artifects','train.csv')
    test_data_path :str= os.path.join('artifects','test.csv')
    raw_data_path :str = os.path.join('artifects','data.csv')

class DataIjestion:
    def __init__(self):
        self.Datainjestion_config = DataingestionConfig()

    def initiate_data_injetion(self):
        logging.info("enterd the data injetion method or components")

        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("exported dataset as dtaframes")

            os.makedirs(os.path.dirname(self.Datainjestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.Datainjestion_config.train_data_path,index=False,header = True)
            df.to_csv(self.Datainjestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initated")

            train_set ,test_set =train_test_split(df,test_size=2,random_state=42)
            train_set.to_csv(self.Datainjestion_config.train_data_path,index =False,header = True)
            test_set.to_csv(self.Datainjestion_config.test_data_path,index =False,header = True)
            logging.info("exported train and test set")

            return(self.Datainjestion_config.train_data_path,
                   self.Datainjestion_config.test_data_path,
                   self.Datainjestion_config.raw_data_path

                   )
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = DataIjestion()
    obj.initiate_data_injetion()
        





