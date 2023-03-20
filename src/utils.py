import os
import sys
import pandas as pd
import numpy as np
import dill

from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


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


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)  # Train model

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as f:
            return dill.load(f)
    except Exception as e:
        raise CustomException(e, sys)
