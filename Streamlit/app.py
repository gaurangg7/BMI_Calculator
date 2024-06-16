import streamlit as st
st.title('BMI Calculator')
with st.form('BMI Calculator'):
  col1,col2,col3 = st.columns([3,2,1])
  
  st.write('Enter your weight and height below:')
with col1:
  weight = st.number_input('Weight (kg)')
with col2:
  height = st.number_input('Height (m))')
with col3:
  submitted = st.form_submit_button('Calculate')

if submitted:
  bmi = round( weight / (height * height), 2)
  st.write('BMI:', bmi)

  if bmi <= 18.5:
    st.error('Underweight')
  elif bmi >= 18.5 and bmi <= 24.9:
    st.success('Normal & Healthy')
  elif bmi >= 25 and bmi <= 29.9:
    st.warning('Overweight')
  else:
    st.error('Obese')