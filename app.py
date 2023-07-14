import joblib
import streamlit as st
import pandas as pd
import xgboost
import sklearn

def app():
    model = joblib.load('Final_Model.h5')
    st.set_page_config(page_title=" Loan Status Classifier ")
    st.title(" Loan Classifier ")
    st.header(" Epsilon Training Project ")

    st.write("This project predicts Loan Status based on some features")

    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Married = st.selectbox('Married ?', ['Yes', 'No'])
    Dependents = st.radio('Any Dependents ?', ['0','1','2','3 or more'])
    Education = st.selectbox('Educational Status', ['Not Graduated', 'Graduated'])
    Self_Employed = st.selectbox('Self_Employed ?', ['Yes', 'No'])
    ApplicantIncome = st.number_input("Enter Primary Income ", value=0)
    CoapplicantIncome = st.number_input("Enter Secondary Income", value=0)
    LoanAmount = st.number_input("Enter Loan Amount that wish to be taken", value=0)
    Loan_Amount_Term = st.number_input("How Much Months will you take to return the Loan", value=0)
    Credit_History = st.selectbox('Your History with Banks ?', ['Good', 'Bad'])
    Property_Area = st.radio('Select the Area', ['Urban','Semiurban','Rural'])
    
    
    
    
    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'Gender':[0 if Gender == 'Male' else 1],
                'Married':[0 if Married == 'No' else 1],
                'Dependents	':[0 if Dependents == '0' else (1 if Dependents == '1' else  (2 if Dependents == '2' else  '3' ))],
                'Education':[0 if Education == 'Not Graduated' else 1],
                'Self_Employed':[0 if Self_Employed == 'No' else 1],
                'ApplicantIncome':[ApplicantIncome],
                'CoapplicantIncome':[CoapplicantIncome],
                'LoanAmount':[LoanAmount],
                'Loan_Amount_Term':[Loan_Amount_Term],
                'Credit_History':[0 if Credit_History == 'Bad' else 1],
                'Property_Area':[0 if Property_Area == 'urban' else (1 if Property_Area == 'Semiurban' else 2 )],
            }
        )


        st.write("Input Data: ")
        st.dataframe(df)

        pred = model.predict(df)
        
        if pred == 1:
            st.write(F"Prediction: Loan Will be Accepted ")

        else:
            st.write(F"Prediction: Loan Will be Rejected ")         

app()
