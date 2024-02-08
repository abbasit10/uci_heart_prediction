import streamlit as st
import pandas as pd
from joblib import load




model = load(r"\heart_disease_model.joblib")

st.markdown("""
    <style>
    .title {
        color: red;
        text-align: center;
    }
    </style>
    <h1 class="title">UCI Heart Prediction Model</h1>
    """, unsafe_allow_html=True)

# image position
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("https://www.hsph.harvard.edu/nutritionsource/wp-content/uploads/sites/30/2016/04/CVD_NSHomepageWidget.jpg", use_column_width=True)

# result info
st.markdown("""
    <style>
    .title {
        color: red;
        text-align: center;
    }
    </style>
    <h2 class="title">What predicted attribute shows?</h2>
    """, unsafe_allow_html=True)
data = {
    "Predicted Attribute": ["0", "1", "2", "3", "4"],
    "Result": ["Normal", "Pre-Heart Failure", "Congestive Heart Failure", "Beginning of Advanced Heart Failure", "Severe Hearth Failure"]
}

df = pd.DataFrame(data)

# Display the table
st.table(df)

# header
st.header('Enter patient information')

age= st.number_input("Age in years", min_value=0, max_value=100,value=1)
sex= st.selectbox('Sex',("Male", "Female"))
dataset= st.selectbox("Area", ('Cleveland','Hungary', 'VA Long Beach','Switzerland'))
cp= st.selectbox("Chest Pain type",("asymptomatic", "non-anginal", "atypical angina", "typical angina"))
trestbps= st.number_input("Resting Blood Pressure", min_value=0.0, max_value=400.0, value= 0.0)
chol= st.number_input("Cholesterol", min_value=0.0, max_value=700.0, value=0.0)
fbs= st.selectbox("Fasting Blood Sugar", ("True", "False"))
restecg= st.selectbox("Resting Electrocardiographic Results", ("normal", "lv hypertrophy", "st-t abnormality"))
thalch= st.number_input("Maximum Heart Rate Achieved", min_value=0.0, max_value=300.0, value=0.0)
exang= st.selectbox("Exercise Induced Angina",("True", "False"))
oldpeak= st.number_input("ST Depression Measure", min_value=-0.0, max_value=10.0, value=0.0)
slope= st.selectbox("ST Segment Slope", ("flat", "upsloping", "downsloping"))
ca= st.selectbox("Number of Major Vessels", (0.0,1.0,2.0,3.0))
thal= st.selectbox("Thallium Stress Testing", ("normal", "fixed defect", "reversable defect"))

# sex
if sex == 'Male':
    sex_arr= [1,0]
else:
    sex_arr= [0,1]

# dataset
if dataset == 'Cleveland':
    dataset_arr= [0]
elif dataset == 'Hungary':
    dataset_arr= [1]
elif dataset == 'VA Long Beach':
    dataset_arr= [3]
else:
    dataset_arr= [2]

# cp
if cp== 'asymptomatic':
    cp_arr= [0]
elif cp== 'non-anginal':
    cp_arr= [2]
elif cp== 'atypical angina':
    cp_arr= [1]
else:
    cp_arr= [3]

# fbs
if fbs== 'True':
    fbs_arr= [1]
else:
    fbs_arr= [0]

# restecg
if restecg== 'normal':
    restecg_arr= [1]
elif restecg== 'lv hypertrophy':
    restecg_arr= [0]
else:
    restecg_arr= [2]

# exang
if exang== 'False':
    exang_arr= [0]
else:
    exang_arr= [1]

# slope
if slope== 'flat':
    slope_arr= [1]
elif slope== 'upsloping':
    slope_arr= [2]
else:
    slope_arr= [0]

# thal
if thal== 'reversable defect':
    thal_arr= [2]
elif thal== 'normal':
    thal_arr= [1]
else:
    thal_arr= [0]


input_arr= []
input_arr.append(age)
input_arr += sex_arr
input_arr += dataset_arr
input_arr += cp_arr
input_arr.append(trestbps)
input_arr.append(chol)
input_arr += fbs_arr
input_arr += restecg_arr
input_arr.append(thalch)
input_arr += exang_arr
input_arr.append(oldpeak)
input_arr += slope_arr
input_arr.append(ca)
input_arr += thal_arr

prediction= model.predict([input_arr])

if prediction[0]== 0:
    attribute= "Normal Heart Condition"
elif prediction[0]== 1:
    attribute= "Pre-Heart Failure"
elif prediction[0]== 2:
    attribute= "Congestive Heart Failure"
elif prediction[0]== 3:
    attribute= "Beginning of Advanced Heart Failure"
else:
    attribute= "Severe Heart Failure"

if st.button('See results!'):
    comment = "Thank You for the information!"

    st.write(comment)
    st.subheader("Result")
    st.success(attribute)

