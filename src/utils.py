import os
import sys
import pandas as pd
import numpy as np
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(obj_file_path, obj):

    try:
        
        dir_path = os.path.dirname(obj_file_path)

        os.makedirs(dir_path, exist_ok=True)

        logging.info(f"Trying to save the pickle file to path {obj_file_path}")

        with open(obj_file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Successfully saved the pickle file to path {obj_file_path}")

            
    except Exception as e:
        raise CustomException(e, sys)