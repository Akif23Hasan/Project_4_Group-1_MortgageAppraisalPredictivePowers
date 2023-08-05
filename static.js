function predictLoanApproval() {
    if (request.method === 'POST') {
        try {
            var user_data = {};
                console.log(user_data)
            var formData = new FormData(document.getElementById('loanForm'));

            var formKeys = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'];
            formKeys.forEach(function(col) {
                user_data[col] = formData.get(col);
            });

            var user_df = {}; // Create a JavaScript object similar to pandas DataFrame
            // Convert categorical variables to numerical using the loaded label encoder
            var categoricalColumns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'];
            categoricalColumns.forEach(function(col) {
                user_df[col] = label_encoder.transform([user_data[col]])[0];
            });

            // Convert other numeric fields to appropriate data types
            var numericColumns = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History'];
            numericColumns.forEach(function(col) {
                user_df[col] = parseFloat(user_data[col]);
            });

            // Ensure the properties in user_df match the properties used during training
            var trainingColumns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'];
            trainingColumns.forEach(function(col) {
                if (!user_df.hasOwnProperty(col)) {
                    user_df[col] = 0;
                }
            });

            // Reorder the properties to match the order used during training
            var orderedColumns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'];
            user_df = orderedColumns.reduce(function(obj, col) {
                obj[col] = user_df[col];
                return obj;
            }, {});

            // Make predictions
            var user_pred = rf_model.predict([Object.values(user_df)]);
            var prediction = user_pred[0] === 1 ? 'Approved' : 'Denied';

            // Update your HTML with the prediction result
            document.getElementById('prediction').innerHTML = 'Prediction: ' + prediction;
        } catch (e) {
            console.error(e); // Print the error message for debugging
            var error_message = e.toString();
            document.getElementById('prediction').innerHTML = 'Prediction: Error';
            document.getElementById('error_message').innerHTML = 'Error: ' + error_message;
        }
    }
console.log(prediction)}