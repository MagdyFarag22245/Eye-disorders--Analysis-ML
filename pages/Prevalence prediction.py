import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import cross_val_score, KFold
import plotly.graph_objects as go
import plotly.express as px


st.markdown("<h1 style='text-align: center;'>Disease category Prediction</h1>", unsafe_allow_html=True)
st.write("This page is dedicated to predict the Disease category, using a GradientBoostingClassifier model traind and tested over our dataset. The model is making an accuracy of 98.3%  over the test set. ")
st.write("Enter the required data accurately for providing an accurate prediction. ")

st.markdown("<h5> INPUT DATA FOR CATEGORY PREDICTION</h5>", unsafe_allow_html=True)

col1, col2= st.columns([1,1])

with col1:

    category = st.selectbox('Select your disorder category',['Diabetic Eye Diseases', 'Cancer and Neoplasms of the Eye',
       'Cornea Disorders', 'Other Visual Disturbances',
       'Orbital and External Disease', 'Other Retinal Disorders',
       'Retinal Detachment and Defects',
       'Age Related Macular Degeneration',
       'Infectious and Inflammatory Diseases',
       'Injury, Burns and Surgical Complications of the Eye', 'Glaucoma',
       'Disorders of Optic Nerve and Visual Pathways',
       'Other Eye Disorders'])
    response = st.selectbox('select your response',['Proliferative diabetic retinopathy',
       'All Cancer and neoplasms of the eye diseases',
       'Other corneal disorders', 'Visual field defect',
       'Disorders of the globe', 'Corneal transplant',
       'All Other retinal disorders', 'Retinal detachment and defects',
       'Keratoconus', 'Choroidal neovascularization',
       'Occlusive retinal vascular disease',
       'Unspecified-age related macular degeneration',
       'Advanced GA or Inactive CNV', 'Severe non-proliferative',
       'Other/unspecified infectious and inflammatory diseases',
       'Ocular burns', 'Non-vision threatening stage',
       'Congenital anomalies', 'Vision threatening stage',
       'All Age-related macular degeneration (AMD)', 'Lacrimal diseases',
       'Other/unspecified glaucoma', 'Benign neoplasm',
       'Macular edema (Cystoid or non-diabetic)', 'Optic nerve disorders',
       'Other/unspecified other retinal disorders',
       'Dry-form age-related macular degeneration',
       'Central retinal vein occlusion',
       'Wet-form age-related macular degeneration', 'Other eye disorders',
       'Eyelid infection and inflammation', 'Ocular injury',
       'Early stage age-related macular degeneration', 'Keratitis',
       'Endophthalmitis', 'All Orbital and external disease',
       'Myopic degeneration', 'Secondary glaucoma', 'Infectious diseases',
       'Disorders of the visual pathway and visual cortex',
       'All Diabetic eye diseases', 'Night blindness', 'Dry eye syndrome',
       'Surgical complication of the eye',
       'Other/unspecified visual disturbances', 'All Cornea disorders',
       'Non-proliferative', 'Malignant neoplasm',
       'Other/unspecified orbital and external disease',
       'Suspect or unclassified glaucoma', 'Glaucoma suspect',
       'Eyelid disorders', 'Non-Occlusive retinal vascular disease',
       'Cornea disorder related to contact lens', 'Geographic atrophy',
       'Diabetic macular edema', 'All Other visual disturbances',
       'All Disorders of optic nerve and visual pathways',
       'Branch retinal vein occlusion', 'Lacrimal and orbit inflammation',
       'All Injury, burns and surgical complications of the eye',
       'Other diabetes related eye disorders',
       'All Infectious and inflammatory diseases',
       'Endothelial dystrophy (Fuchs)', 'Branch retinal artery occlusion',
       'Open-angle glaucoma', 'Hereditary chorioretinal dystrophy',
       'Color blindness', 'Retinopathy of prematurity', 'All Glaucoma',
       'Conjunctivitis', 'Primary angle-closure glaucoma',
       'Central retinal arterial occlusion', 'Specified glaucoma'])
    
    locationdesc = st.selectbox('select your location',[
    "New York","Wisconsin", "Georgia", "Arizona",  "Illinois", "National",
    "Virginia", "Mississippi", "California", "Pennsylvania", "Minnesota",
    "New Jersey", "North Carolina", "Hawaii", "Texas", "Maryland", "Nevada",
    "Michigan", "New Hampshire", "Nebraska", "Washington", "South Carolina",
    "Iowa", "Indiana", "Maine", "Kentucky", "Oklahoma", "Missouri",
    "Massachusetts", "Oregon", "Montana", "New Mexico", "District Of Columbia",
    "Connecticut", "Colorado", "Louisiana", "Florida", "Ohio", "Puerto Rico",
    "Delaware", "West Virginia", "Arkansas", "North Dakota", "South Dakota",
    "Idaho", "Wyoming", "Kansas", "Rhode Island", "Tennessee"])
    

    age = st.selectbox('Select your age group',['85 years and older', 'All ages', '65-84 years',
       '18 years and older', '40 years and older', '40-64 years',
       '18-39 years', '65 years and older', '0-17 years'])

    raceethnicity = st.selectbox('Select your race',['White, non-Hispanic', 'Hispanic, any race', 'Black, non-Hispanic',
       'North American Native', 'All races', 'Asian', 'Other', 'Unknown'])




with col2:

    gender = st.selectbox('Select your sex',['Male','Female','All genders'])
    low_confidence_limit = st.number_input('Enter the low_confidence_limit',min_value=0.0, max_value=12.17)
    high_confidence_limit = st.number_input('Enter the high_confidence_limit',min_value=0.0, max_value=36.44)
    numerator = st.number_input('Enter the numerator',min_value=0.0, max_value=18.75)
    sample_size = st.number_input('Enter the sample_size',min_value=0.0, max_value=18.75)    


input_data = pd.DataFrame({
    'locationdesc': [locationdesc],
    'response': [response],
    'age': [age],
    'gender': [gender],
    'raceethnicity': [raceethnicity],
    'low_confidence_limit': [low_confidence_limit],
    'high_confidence_limit': [high_confidence_limit],
    'category': [category],
    'numerator': [numerator],
    'sample_size': [sample_size],
    })


st.markdown("<h5> CLICK TO PREDICT</h5>", unsafe_allow_html=True)
# Load the saved pipeline
with open(r"./sources/best_model_2.pkl", 'rb') as file:
    model_pipeline = joblib.load(file)


# Use the pipeline to make predictions

prediction = model_pipeline.predict(input_data)

if st.button('Predict'):
    # Format the prediction with 2 decimal places and display it as a percentage
    formatted_prediction = f"The prevalence is: {prediction[0] * 100:.2f}%"
    st.write(formatted_prediction)
