# import csv
# import pandas as pd
# from sqlalchemy import create_engine
# import sqlite3
# from flask import Flask, request, render_template, jsonify
# from sqlalchemy.orm import Session 

# from flask import Flask, render_template 
# import subprocess 

# app = Flask(__name__) 
    
# @app.route('/') 

# def index(): 
#     #Convert the Jupyter notebook to Voilà application 
#     subprocess.Popen(['voila', 'loan_prediction.ipynb', '--no-browser']) 
#     return render_template('index.html') 

# if __name__ == '__main__': 
#     app.run(debug=True) 


# ------------------------------------------------------
# from flask import Flask, render_template, request
# import subprocess
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# app = Flask(__name__)

# # Load the model and label encoder
# rf_model = None  # Load the trained RandomForestClassifier model here
# label_encoder = None  # Load the LabelEncoder used for categorical variables here

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_data = {}
#         for col in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']:
#             user_data[col] = [request.form[col]]

#         user_df = pd.DataFrame(user_data)
#         for col in ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']:
#             user_df[col] = label_encoder.transform(user_df[col])

#         # Ensure the columns in user_df match the columns used during training
#         missing_cols = set(X.columns) - set(user_df.columns)
#         for col in missing_cols:
#             user_df[col] = 0
#         user_df = user_df[X.columns]  # Reorder the columns to match the order used during training

#         # Make predictions
#         user_pred = rf_model.predict(user_df)
#         prediction = "Approved" if user_pred[0] == 1 else "Denied"

#         return render_template('index.html', prediction=prediction)

#     return render_template('index.html', prediction=None)

# if __name__ == '__main__':
#     app.run(debug=True)


    #--------------------------------------------------

import traceback
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv('Datasets/ETL_Completed_LoanApprovalPrediction.csv')

app = Flask(__name__)

rf_model = joblib.load('RandomForest/rf_model.pkl')  # Load the trained RandomForestClassifier model here
# label_encoder = joblib.load('RandomForest/label_encoder.pkl')  # Load the LabelEncoder used for categorical variables here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        user_data = {}
        form_keys = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        for col in form_keys:
            user_data[col] = request.form.get(col)
        user_df = {}  # Create a dictionary similar to pandas DataFrame
        # Convert categorical variables to numerical using the loaded label encoder
        label_encoder = LabelEncoder()
        categorical_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
        for col in categorical_columns:
            user_df[col] = label_encoder.fit_transform([user_data[col]])[0]
        # Convert other numeric fields to appropriate data types
        numeric_columns = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
        for col in numeric_columns:
            user_df[col] = float(user_data[col])
        # Ensure the properties in user_df match the properties used during training
        training_columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        for col in training_columns:
            if col not in user_df:
                user_df[col] = 0
        # Reorder the properties to match the order used during training
        ordered_columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        user_df = {col: user_df[col] for col in ordered_columns}
        # Make predictions
        user_pred = rf_model.predict([list(user_df.values())])
        prediction = "Approved" if user_pred[0] == 1 else "Denied"
        return jsonify({'prediction': prediction})
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message})

if __name__ == '__main__':
    app.run(debug=True)