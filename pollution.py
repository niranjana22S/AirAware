import pickle
import streamlit as st
import numpy as np
file=open(r"C:\Users\NIRANJAN\main_project",'rb')

reg=pickle.load(file)
file.close()


st.title("AirAware")
a=st.number_input("CO")
b=st.number_input("Ozone")
c=st.number_input("NO2")
d=st.number_input("SO2")
e=st.number_input("PM2.5")
f=st.number_input("PM10")



if st.button('predict'):
    input_data=np.array([[a,b,c,d,e,f]])
    result=reg.predict(input_data)
    st.write("predicted value:",result[0])
    if result<=50:
        label="High"
        color="red"
    elif result<=100:
        label="moderate"
        color="orange"
    else:
        label="low"

if label == "Low":
    color = "green"
elif label == "High":
    color = "red"
else:
    color = "orange"         
st.markdown(f"### Predicted Pollution Result:<span style='color:{color};font-weight:bold'>{label}</span>",unsafe_allow_html=True)             