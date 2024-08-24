import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Law Buddy - Login/Signup",
    page_icon="logo.png",
    layout="centered",  
)

st.image("logo.png", width =170)
st.title("Welcome to Law Buddy")
st.subheader("Please login or sign up to continue")


option = st.radio("Choose an option", ('Login', 'Sign Up'))

if option == 'Login':

    with st.form(key='login_form'):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button(label="Login")
   
    if login_button:
        if email == "admin@example.com" and password == "password":
            st.success("Login successful!")
        else:
            st.error("Invalid email or password. Please try again.")
else:
    with st.form(key='signup_form'):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        signup_button = st.form_submit_button(label="Sign Up")
    

    if signup_button:
        if name and email and password:
            st.success(f"Account created for {name}!")
        else:
            st.error("Please fill out all fields.")

st.markdown("---")
st.markdown("Already have an account? Select **Login** above.")
st.markdown("New user? Select **Sign Up** above.")
