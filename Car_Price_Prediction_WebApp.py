import numpy as np
import pickle
import streamlit as st

# Loading the saved model
model_file = 'car_price_prediction_model.sav'

try:
    loaded_model = pickle.load(open(model_file, 'rb'))
except FileNotFoundError:
    st.error(f"The model file {model_file} was not found. Please check the file path and try again.")
    st.stop()

# Creating a function for prediction
def car_price_prediction(input_data):
    # Changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    # Displaying an animated image at the top
    st.image("https://wallpaperaccess.com/full/6997512.gif", use_column_width=True)

    # Giving a title with colorful text
    st.markdown(
        "<h1 style='text-align: center; color: #ff6347;'>Car Price Prediction Web App</h1>", 
        unsafe_allow_html=True
    )

    # Highlighting input variables and additional information with different colors
    st.markdown(
        """
        <style>
        .highlight {
            background-color: #d1e7dd;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }
        .info {
            color: #17a2b8;
            font-size: 18px;
        }
        .section-title {
            color: #ff5733;
            font-size: 24px;
            font-weight: bold;
        }
        </style>
        <div class="highlight">
        <h2 class="section-title">Input Variables and Additional Information</h2>
        <p class="info"><strong>Year:</strong> Enter the year of the car model</p>
        <p class="info"><strong>Km-driven:</strong> Enter the total kilometers driven by the car</p>
        <p class="info"><strong>Fuel:</strong> Select the type of fuel used</p>
        <ul class="info">
            <li>'Diesel' : 0</li>
            <li>'Petrol' : 1</li>
            <li>'CNG' : 2</li>
            <li>'LPG' : 3</li>
            <li>'Electric' : 4</li>
        </ul>
        <p class="info"><strong>Seller-type:</strong> Select the type of seller</p>
        <ul class="info">
            <li>'Individual' : 0</li>
            <li>'Dealer' : 1</li>
            <li>'Trustmark Dealer' : 2</li>
        </ul>
        <p class="info"><strong>Transmission:</strong> Select the transmission type</p>
        <ul class="info">
            <li>'Manual' : 0</li>
            <li>'Automatic' : 1</li>
        </ul>
        <p class="info"><strong>Owner:</strong> Select the number of previous owners</p>
        <ul class="info">
            <li>'First Owner' : 0</li>
            <li>'Second Owner' : 1</li>
            <li>'Third Owner' : 2</li>
            <li>'Fourth & Above Owner' : 3</li>
            <li>'Test Drive Car' : 4</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    # Getting input data from user
    with col1:
        year = st.number_input("Year", min_value=1900, max_value=2024, step=1)
    with col2:
        km_driven = st.number_input("Km-driven", min_value=0, step=1)
    with col1:
        option1 = st.selectbox('Fuel', ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))
        if option1 == 'Diesel':
            fuel = 0
        elif option1 == 'Petrol':
            fuel = 1
        elif option1 == 'CNG':
            fuel = 2
        elif option1 == 'LPG':
            fuel = 3
        elif option1 == 'Electric':
            fuel = 4
    with col2:
        option2 = st.selectbox('Seller-type', ('Individual', 'Dealer', 'Trustmark Dealer'))
        if option2 == 'Individual':
            seller_type = 0
        elif option2 == 'Dealer':
            seller_type = 1
        elif option2 == 'Trustmark Dealer':
            seller_type = 2
    with col1:
        option3 = st.selectbox('Transmission', ('Manual', 'Automatic'))
        if option3 == 'Manual':
            transmission = 0
        elif option3 == 'Automatic':
            transmission = 1
    with col2:
        option4 = st.selectbox('Owner', ('First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'))
        if option4 == 'First Owner':
            owner = 0
        elif option4 == 'Second Owner':
            owner = 1
        elif option4 == 'Third Owner':
            owner = 2
        elif option4 == 'Fourth & Above Owner':
            owner = 3
        elif option4 == 'Test Drive Car':
            owner = 4

    # Code for prediction
    price = ''

    # Creating a button for Prediction
    if st.button('Predict Car Price'):
        price = car_price_prediction((year, km_driven, fuel, seller_type, transmission, owner))

    st.markdown(
        f"<h3 style='text-align: center; color: #007bff;'>The Predicted Price: {price}$</h3>", 
        unsafe_allow_html=True
    )

    # Feedback Mechanism
    st.subheader("Feedback")
    feedback_text = st.text_area("Please share your feedback:")
    if st.button("Submit Feedback"):
        # Code to store or process the feedback
        st.success("Thank you for your feedback!")

if __name__ == '__main__':
    main()
