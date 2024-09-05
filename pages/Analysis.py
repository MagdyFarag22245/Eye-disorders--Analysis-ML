# import needed libraries
import numpy as np
import pandas as pd
import streamlit as st
import Meda as md
import sys
# Directing to MEDA file path to be able to read it
sys.path.append(r"C:\Users\DELL\Documents\GitHub\Eye-disorders--Analysis-ML\Meda.py") # Path of MEDA file

# Dividing our analysis into tabs, each tab contains information in one dimension and many facts.
tab_over_view,tab_prevalence,tab_category = st.tabs(['OverView','Prevalence','Category'])


# OverView tap
with tab_over_view:

    # first section
    st.header("Eye disorders prevalence ") 
    st.write("Vision and Eye Health Surveillance is a de-identified summary table of vision and eye health data indicators from Medicare claims, stratified by all available combinations of age group, race/ethnicity, gender, and state. Medicare claims for VEHSS includes beneficiaries who were fully enrolled in Medicare Part B Fee-for-Service (FFS) for the duration of the year. Medicare claims provide a convenience sample that includes approximately 30 million individuals annually, including persons disabled due to blindness.")
    # Create columns for metrics
    col1, col2, col3 = st.columns([1, 1, 2])  # Adjust column width as needed

    # Display metrics in the first two columns
    col1.metric("Total Records", md.Total_records)
    col2.metric("Features", md.num_columns)

    # Create a custom "metric" with a larger link in the third column
    col3.markdown(
        """
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
            <a href="https://catalog.data.gov/dataset/medicaid-claims-max-vision-and-eye-health-surveillance" 
            target="_blank" style="font-size: 20px; color: #1f77b4; text-decoration: none; font-weight: bold; display: inline-block; padding: 10px;">
                🔗 View Dataset
            </a>
            <h4 style="margin-top: 10px;">Data.GOV</h4>
        </div>
        """,
        unsafe_allow_html=True
    )



    # second section
    st.header("Distribution of the data")
    st.plotly_chart(md.plot_distribution())

    # third section
    agree= st.checkbox('Show heatmap correlation')
    if agree:
        st.header("Heatmap of the correlation matrix")
        st.pyplot(md.plot_correlation_heatmap())

    # fourth section
    st.header("Interactive map of eye disorders prevalence ")
    st.plotly_chart(md.cluster_map())


# Prevalence tap
with tab_prevalence:

    # first section
    st.header("1) Distribution of data_value(%)")
    st.plotly_chart(md.plot_data_value_distribution())

    # second section
    st.header("2) mean prevalence by:")
    par=st.radio("Options",("age","raceethnicity","gender","locationdesc"),horizontal=True)
    st.plotly_chart(md.plot_mean_prevalence(par))

    # third section
    st.header("3)Box Plot of Data_Value(%) by Eye Disorder")
    option=st.selectbox('Select..',('Cornea Disorders','Glaucoma','Diabetic Eye Diseases','Orbital and External Disease','Infectious and Inflammatory Diseases',
                                    'Age Related Macular Degeneration','Other Visual Disturbances','Injury, Burns and Surgical Complications of the Eye'
                                    ,'Disorders of Optic Nerve and Visual Pathways','Cancer and Neoplasms of the Eye','Retinal Detachment and Defects'
                                    ,'Other Retinal Disorders','Other Eye Disorders'))
    st.plotly_chart(md.plot_box_plot_for_category(option))

    st.header("Summary:")
    st.write("1- New jersey is the most prevalent state. It has a higher prevalence than other states. Wyoming is the least prevalent state. It has a lower prevalence than other states.")
    st.write("2- Those who are between the ages of 65:48 have the highest prevelance rate, while the ages of 18:39 are the least susceptible to this diseases.")
    st.write("3- The prevelance of the diseases in female is higher than males.")
    st.write("4- All races have similar ratiose of eye disorders, except North American Native ,which is the least.")

# Category tap
with tab_category:

    st.header("Eye Disorders Categories")
    st.write("Other retinal disorders are the most prevalence category.")
    st.write("Age Related Macular Degeneration is the highest disorderr prevalence with 13.3%")
    # first section
    # st.header("Eye Disorders Categories")
    category=st.radio("Options",("pie","bar"),horizontal=True)
    st.plotly_chart(md.plot_eye_disorders(category))

    # second section
    st.header("Distribution of Eye Disorders by:")
    opt=st.radio("Options",("age","gender","response"),horizontal=True)
    st.plotly_chart(md.eye_disorders_by(opt))
