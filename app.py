# Importing Modules
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from xgboost import XGBRegressor
import pickle
import numpy

# Set page configuration
st.set_page_config(page_title="FitTrack",page_icon="heart")

# Loading Models
with open("Diabetes_Classification_pickle","rb") as f:
  diabetes_predict_model=pickle.load(f)

with open("Heart_Disease_Prediction_pickle","rb") as g:
  heart_disease_predict_model=pickle.load(g)

with open("Breast_Cancer_Classification_pickle","rb") as h:
  breast_cancer_predict_model=pickle.load(h)

with open("Calories_prediction_pickle","rb") as i:
  calories_burnt_predict_model=pickle.load(i)

# Building UI

# Building Sidebar
with st.sidebar:
  selected=option_menu("Your HealthCare Dashboard",
                       ["Calorie Burnt",
                       "Heart Health",
                       "Diabetes Diagnosis",
                       "Breast Cancer Diagnosis"],icons=["fire","heart-pulse-fill","bandaid-fill","gender-female"],menu_icon="person-hearts",default_index=0)

col1, col2 = st.columns(2)

with col1:
   title = '<p style="font-size:70px; color:#eb7971">FitTrack</p>'
   st.markdown(title, unsafe_allow_html=True)
   #st.title('FitTrack')
   tagline = '<p style="font-family:sans-serif; font-size: 35px;">Your Health Companion</p>'
   st.markdown(tagline, unsafe_allow_html=True)

with col2:
   st.image("/home/kunalgoel/Desktop/Hackathon_Data/HealthCare_App/Fitz - Morning Routine.png")


# Calories Burnt 
if selected=="Calorie Burnt":

  # Page Title
  st.title("Calorie Burnt")

  # Getting user data
  col1,col2,col3=st.columns(3)

  with col1:
     Gender=st.text_input("Gender")

  with col2:
     Age=st.text_input("Age")
  
  with col3:
     Height=st.text_input("Height")

  with col1:
     Weight=st.text_input("Weight")

  with col2:
     Duration=st.text_input("Duration")

  with col3:
     Heart_Rate=st.text_input("Heart Rate")

  with col1:
     Body_Temp=st.text_input("Body Temp")


  # creating a button for Prediction

  if st.button('Calories Burnt'):

      user_input =[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]

      user_input = [float(x) for x in user_input]

      cal_burnt_predict = calories_burnt_predict_model.predict([user_input])

      st.success(f"Total Calories Burnt {cal_burnt_predict}")



# Diabetes Prediction Page
if selected=="Diabetes Diagnosis":

  # Page Title
  st.title("Diabetes Diagnosis")

  # getting the input data from the user
  col1, col2, col3 = st.columns(3)

  with col1:
      Pregnancies = st.text_input('Number of Pregnancies')

  with col2:
      Glucose = st.text_input('Glucose Level')

  with col3:
      BloodPressure = st.text_input('Blood Pressure value')

  with col1:
      SkinThickness = st.text_input('Skin Thickness value')

  with col2:
      Insulin = st.text_input('Insulin Level')

  with col3:
      BMI = st.text_input('BMI value')

  with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

  with col2:
      Age = st.text_input('Age of the Person')

  # code for Prediction
  diab_diagnosis = ''

  # creating a button for Prediction

  if st.button('Diabetes Test Result'):

      user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                    BMI, DiabetesPedigreeFunction, Age]

      user_input = [float(x) for x in user_input]

      diab_prediction = diabetes_predict_model.predict([user_input])

      if diab_prediction[0] == 1:
          diab_diagnosis = 'You have Diabetic'
      else:
          diab_diagnosis = 'You dont have Diabetic'

  st.success(diab_diagnosis)


# Heart Health
if selected=="Heart Health":

  # Page Title
  st.title("Heart Health")

  col1, col2, col3 = st.columns(3)

  with col1:
    age = st.text_input('Age')

  with col2:
      sex = st.text_input('Sex')

  with col3:
      cp = st.text_input('Chest Pain types')

  with col1:
      trestbps = st.text_input('Resting Blood Pressure')

  with col2:
      chol = st.text_input('Serum Cholestoral in mg/dl')

  with col3:
      fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

  with col1:
      restecg = st.text_input('Resting Electrocardiographic results')

  with col2:
      thalach = st.text_input('Maximum Heart Rate achieved')

  with col3:
      exang = st.text_input('Exercise Induced Angina')

  with col1:
      oldpeak = st.text_input('ST depression induced by exercise')

  with col2:
      slope = st.text_input('Slope of the peak exercise ST segment')

  with col3:
      ca = st.text_input('Major vessels colored by flourosopy')

  with col1:
      thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

  # code for Prediction
  heart_diagnosis = ''

  # creating a button for Prediction

  if st.button('Heart Disease Test Result'):

      user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

      user_input = [float(x) for x in user_input]

      heart_prediction = heart_disease_predict_model.predict([user_input])

      if heart_prediction[0] == 1:
          heart_diagnosis = 'The person is having heart disease'
      else:
          heart_diagnosis = 'The person does not have any heart disease'

  st.success(heart_diagnosis)


# Breast Cancer
if selected=="Breast Cancer Diagnosis":

  # Page Title
  st.title("Breast Cancer Diagnosis")

  # Getting user data
  col1, col2, col3 = st.columns(3)

  with col1:mean_radius=st.text_input('mean radius')
  with col2:mean_texture=st.text_input('mean texture')
  with col3:mean_perimeter=st.text_input('mean perimeter')
  with col1:mean_area=st.text_input('mean area')
  with col2:mean_smoothness=st.text_input('mean smoothness')
  with col3:mean_compactness=st.text_input('mean compactness')
  with col1:mean_concavity=st.text_input('mean concavity')
  with col2:mean_concave_points=st.text_input('mean concave points')
  with col3:mean_symmetry=st.text_input('mean symmetry')
  with col1:mean_fractal_dimension=st.text_input('mean fractal dimension')
  with col2:radius_error=st.text_input('radius error')
  with col3:texture_error=st.text_input('texture error')
  with col1:perimeter_error=st.text_input('perimeter error')
  with col2:area_error=st.text_input('area error')
  with col3:smoothness_error=st.text_input('smoothness error')
  with col1:compactness_error=st.text_input('compactness error')
  with col2:concavity_error=st.text_input('concavity error')
  with col3:concave_points_error=st.text_input('concave points error')
  with col1:symmetry_error=st.text_input('symmetry error')
  with col2:fractal_dimension_error=st.text_input('fractal dimension error')
  with col3:worst_radius=st.text_input('worst radius')
  with col1:worst_texture=st.text_input('worst texture')
  with col2:worst_perimeter=st.text_input('worst perimeter')
  with col3:worst_area=st.text_input('worst area')
  with col1:worst_smoothness=st.text_input('worst smoothness')
  with col2:worst_compactness=st.text_input('worst compactness')
  with col3:worst_concavity=st.text_input('worst concavity')
  with col1:worst_concave_points=st.text_input('worst concave points')
  with col2:worst_symmetry=st.text_input('worst symmetry')
  with col3:worst_fractal_dimension=st.text_input('worst fractal dimension')

  # code for Prediction
  bc_diagnosis = ''

  # creating a button for Prediction

  if st.button('Breast Cancer Diagnosis'):

      user_input =[mean_radius,
 mean_texture,
 mean_perimeter,
 mean_area,
 mean_smoothness,
 mean_compactness,
 mean_concavity,
 mean_concave_points,
 mean_symmetry,
 mean_fractal_dimension,
 radius_error,
 texture_error,
 perimeter_error,
 area_error,
 smoothness_error,
 compactness_error,
 concavity_error,
 concave_points_error,
 symmetry_error,
 fractal_dimension_error,
 worst_radius,
 worst_texture,
 worst_perimeter,
 worst_area,
 worst_smoothness,
 worst_compactness,
 worst_concavity,
 worst_concave_points,
 worst_symmetry,
 worst_fractal_dimension]

      user_input = [float(x) for x in user_input]

      bc_prediction = breast_cancer_predict_model.predict([user_input])

      if bc_prediction[0] == 1:
          bc_diagnosis = 'The Breast Cancer is Benign'
      else:
          bc_diagnosis = 'The Breast cancer is Malignant'

  st.success(bc_diagnosis)



