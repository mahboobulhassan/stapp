import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Title and subheaders
st.title('Data Analysis')
st.header('Data Analysis Using Pithon  and streamlit')
# upload data set
upload=st.file_uploader('upload data file(csv)')
if upload is not None:
    df=pd.read_csv(upload)
    
# data description    
if upload is not None:
    if st.checkbox('Head'):
        st.write(df.head())
    if st.checkbox('Tail'):
        st.write(df.tail())
    if st.checkbox('Data type'):
        st.write(df.dtypes)

# check data type of each columns
if upload is not None:
    rc=st.radio('Check Shape of Dataset',('Columns','Rows'))
    if rc=='Columns':
        st.text('No of Columns')
        st.write(df.shape[1])
    if rc=='Rows':
        st.text('No of Rows')
        st.write(df.shape[0])

# null values in dataset
if upload is not None:
    nv=df.isnull().values.any()
    if nv==True:
        st.text('Summary of Null Values in the Dataset')
        st.write(df.isnull().sum())
        fig=plt.figure()
        sns.heatmap(df.isnull())
        st.pyplot(fig)
    else:
        st.success ('Congratulation!!! Trere is no null value in dataset' )
# Duplicated records in dataset
if upload is not None:
    test=df.duplicated().any()
    if test==True:
        st.warning('Dataset contains duplicated records')
        st.write(df.duplicated().sum())
        rdr=st.selectbox('Remove duplicated records ? ',('select one','Yes','No'))
        if rdr=='Yes':
            df=df.drop_duplicates()
            st.write('duplicated record removed')
        if rdr=='No':
            st.text('OK')
    else:
        st.text('No duplicated record found')
# statistics of dataset
if upload is not None:
    if st.checkbox('Summary of Dataset Statistics'):
        st.text('Statistics of Dataset (Numbers Only)')
        st.write(df.describe(include='number'))
        st.text('Statistics of Dataset (objects Only)')
        st.write(df.describe(include='object'))


if st.button('About App'):
    st.write('Built with streamlit')
    st.write('Thanks to streamlit')
if st.button('By'):
    st.write('MH Chaudhry')
            
            
    
    



        
