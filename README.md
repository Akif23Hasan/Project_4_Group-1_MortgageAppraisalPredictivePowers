# Project_4_Group-1_

# UNVEILING THE FUTURE… Predicting Home Loan Approvals using Machine Learning
By Pedro Azpurua, Akif Hasan, Henry Leighton, Graham Meadon

## Overview
Loans are important for people who need money for things like education, buying a home, or other things they want. For financial institutions, lending plays a pivotal role, serving as a significant source of profitability. However, the conventional loan evaluation process is often intricate and time-consuming, requiring meticulous consideration of numerous factors. To address these time-consuming processes and improve the efficiency of home loan assessments, our project uses Machine Learning to simplify and streamline the home loan lending process, enabling real-time decisions through data-driven insights and predictive analytics.

Our Project Objective is to develop a comprehensive loan eligibility model that considers both historical loan data and key features (Applicant Income, Co-applicant Income, Loan Amount, Loan Amount Term, Credit History) as well as demographics (Gender, Dependents, Marital Status, Education). 

The purpose of the model is to promote financial inclusion and reduce biases, ensuring fair access to loans for individuals from diverse backgrounds.

## Goals
1) Build and evaluate predictive models using historical loan data and important factors like income, loan amount, and credit history to determine loan eligibility.
2) Create a fair loan eligibility model considering demographics like gender, education, etc., to ensure unbiased access to loans.
3) Use machine learning to uncover location-based patterns affecting loan approval for different property areas.
4) Develop a user-input tool that assesses education, dependents, and income to provide personalized loan approval insights for better financial decisions.

## Data source
* https://www.geeksforgeeks.org/loan-approval-prediction-using-machine-learning/
* https://drive.google.com/file/d/1LIvIdqdHDFEGnfzIgEh4L6GFirzsE3US/view 

## Requirements
* Find a problem worth solving, analysing, or visualizing.
* Use machine learning (ML) with the technologies we’ve learned.
* Must use Scikit-learn and/or another machine learning library.
* Must be powered by a dataset with at least 100 records.
* Must use at least two of the following: Python Pandas, Python Matplotlib, HTML/CSS/Bootstrap, JavaScript Plotly, JavaScript Leaflet, SQL Database, MongoDB Database, Google Cloud SQL, Amazon AWS, Tableau.

## Project Steps
**Data Cleaning - ETL Process**
* Imported the data from SQL
* Dropped lines where we had empty values (NaN) 
    * Reduced data sample from 598 to 505
* Dropped columns that were irrelevant
    * Loan_ID
* Converted categorical variables to one-hot encoding (0 or 1)
    * Gender, Married, Education, Self_Employed, Property_Area
* Exported to CSV for Machine Learning models
* The data was scaled before training and testing

**Machine Learning**
* Tested two Supervised Machine Learning models: Random Forest and Logistic Regression 
    * Random Forest model produced an accuracy score of 89.11%
    * Logistic Regression model produced an accuracy score of 89.11%
* We also tested the data using a Neural Network model with 3 Hidden Layers with 140 neurons
    * The Neural Network model produced an accuracy score of 70.08%

**Model Selected**
* The Neural Network was discarded due to its low accuracy score
* In deciding between the two models, both models have the same accuracy, but they exhibit different trade-offs in terms of precision and recall for different classes. 
    * Random Forest: This model seems to have balanced performance for both classes, with relatively high precision and recall for both.
    * Logistic Regression: This model achieves very high precision for class 0 (denied), indicating that when it predicts class 0, it's usually correct. However, it has a lower recall for class 0, meaning it might miss some instances of class 0. It excels in classifying instances of class 1 (approved).
* Model selected: Random Forest
    * The Random Forest model achieves a balanced performance, lowers overfitting risk, and maintains a favourable precision-recall trade-off for both classes. On the other hand, the Logistic Regression model's high precision for class 0 is compromised by a lower recall, which could hinder accurate identification of class 0 instances. For a dependable and adaptable classification outcome, the Random Forest model is the recommended option.

**Building the User interface: Loan Eligibility Prediction**
1) User Input Form: The interface features a form where users provide information for loan eligibility prediction. The form includes checkboxes, text fields, and number inputs to capture various parameters like gender, marital status, dependents, education, income, loan amount, credit history, and property area.
2) Form Submission: Upon form submission, the provided data is sent to a server endpoint ("/predict") using the POST method. The data is collected using FormData to handle multipart/form-data, ensuring accurate transmission.
3) Prediction Results Display: The UI includes a div element ("prediction_result") to display prediction results. When the prediction is available, it dynamically updates the UI to show the prediction outcome.
4) JavaScript Interaction: The JavaScript code handles form submission and prediction result updates. It prevents the form from submitting normally, sends data to the server, receives a JSON response, and updates the UI accordingly.
5) Separation of Concerns: The script is enclosed within a script tag, enabling separation from the HTML for cleaner code organization. It attaches a form submission event listener to trigger the data submission process.

**To Run the User interface:**
* In the terminal, run the app.py file by typing in: "python app.py"
* This will create a remote server on http://127.0.0.1:5000 which will allow you to access the interface

## Conclusion
Loan approval prediction using machine learning can improve the efficiency and accuracy of loan processing in financial institutions. 

By building a robust predictive model that considers key features and demographics, banks can better assess the risk associated with loan applicants and make informed decisions about loan approvals. 

This project demonstrates the potential of machine learning in the finance industry to streamline the loan approval process and promote financial inclusion.

Project Presentation<https://github.com/Akif23Hasan/Project_4_Group-1_MortgageAppraisalPredictivePowers/blob/main/Homeloan%20Machine%20Learning%20Presentation_Final.pdf?
