import streamlit as st
st.title("BMI Calculator")
with st.form("BMI Calculator"):
    col1,col2,col3=st.columns([2,2,1])
with col1:
    weight= st.number_input("enter your weight in KGs")
with col2:
    height= st.number_input("enter your height in Meters")
with col3:
    submit=st.form_submit_button("Calulate")
if submit:
    BMI=round((weight / (height**2)),2)
    if (BMI <= 18.5):
        st.error("Underweight")
    elif BMI>18.5 and BMI<=24.9:
        st.success("Healthy / Normal")
    elif BMI>=25 and BMI<=29.9:
        st.warning("Overweight")
    elif BMI>=30.0:
        st.error("Obese")
