import streamlit as st
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp = """ 
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black;text-align:center;"> Yopnalyst Car Price Prediction Web App </h2>
    </div>
    """
    
    model = xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write ('')
    st.write ('')
    
    st.markdown("##### Are You Planning To Sell Your Car!?\n##### Let's Try Evaluating The Price")
    
    p1 = st.number_input ('What is the current ex-showroom price of the car (In Dollars)', 3000, 37500, step = 1500)
    
    p2 = st.number_input('What is the distance completed by the car in kilometers?', 100, 5000000, step = 100)
    
    s1 = st.selectbox ('What is the fuel type of the car?', ('Petrol', 'Diesel', 'CNG'))
    
    if s1 == 'Petrol':
        p3 = 0
    elif s1 == 'Diesel':
        p3 = 1
    elif s1 == 'CNG':
        p3 = 2
    s2 = st.selectbox ('Are you a dealer or an individual?', ('Dealer', 'Individual'))
    
    if s2 == 'Dealer':
        p4 = 0
    else:
        p4 = 1
    
    s3 = st.selectbox ('What is the transmission type?', ('Manual', 'Automatic'))
    
    if s3 == 'Manual':
        p5 = 0
    else:
        p5 = 1
    
    p6 = st.slider ('Number Previous of Owners', 0,3)
    
    date_time = datetime.datetime.now()
    years = st.number_input ('In which year was the car purchased?', 1990,date_time.year)
    p7 = date_time.year - years
    
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try:
        if st.button ('Predict'):
            pred = model.predict(data_new)
            if pred > 0:
                st.balloons()
                st.success('You can sell your car for {:.2f} Dollars'.format (pred[0]))
            else:
                st.Warning ("You can't be able to sell this car")
    except:
        st.warning('Something Went Wrong,Try again')

if __name__ == '__main__':
    main()