# importing libraries
import streamlit as st

# Page content
st.markdown("<h1 style='text-align: center;'>Eye disorders </h1>", unsafe_allow_html=True)
st.markdown('''<h6 style='text-align: center;'>
    (category / prevalence)</h6>''', unsafe_allow_html=True)
st.write('Created by streamlit')
st.header('About dataset:')
st.write('This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the Medicaid Analytic eXtract (MAX) data. Medicaid MAX are a set of de-identified person-level data files with information on Medicaid eligibility, service utilization, diagnoses, and payments.')
# Link of Data
st.markdown('<a href="https://catalog.data.gov/dataset/medicaid-claims-max-vision-and-eye-health-surveillance"> <center> Link to Dataset  </center> </a> ', unsafe_allow_html=True)

st.header('About Analysis:')
st.write('the analysis page contains 3 taps: (OverView ,Category ,Prevalence), each tab contains greate analysis about its section. ')

st.header('About Models:')
st.write('this application contains 2 (ML models) 1- To predict eye disorder category. 2- To predict the prevalence of eye disorders.')