# Brian lesko
# 4/21/2024
# A simple UI for picking vacation days to request off
# sends an email to your manager requesting permission

import streamlit as st
from style import style, footer, header, make_title
from mysecrets import EMAIL, PASSWORD
from simpleEmailSender import SimpleEmailSender

# Set the page configuration
st.set_page_config(
    page_title="Deposit Return",
    page_icon='./elev.png',
    layout="wide"  # This sets the layout to wide format
)
style()
st.html(header)
st.html(make_title('Security Deposit Return Form'))
col1, col2, col3 = st.columns([1,3,1])

col2.write("**How do you want your security deposit returned?**")

name = col2.text_input("Enter your name")
email = col2.text_input("Enter your email")
if email: pass
else: st.stop()
choice = col2.radio("Return method",["Venmo","Zelle"])
if choice == "Venmo":
  payment_info = col2.text_input("Enter your Venmo")
else:
  payment_info = col2.text_input("Enter your Zelle information")
 
if payment_info: pass
else: st.stop()

col2.write(" ")
col2.write(" ")
if col2.button("submit"):
  with st.spinner("Sending your submission"):
    content1 = f"{name}, we have received your security deposit submission and will process it as soon as possible. You chose {choice} with your username/account as {payment_info}."
    SimpleEmailSender("Deposit Return Form", content1, email).send_email()
    content2 = f"{name} has submitted a security deposit return form and elected {choice} via the following account info: {payment_info}."
    SimpleEmailSender("Deposit Return Form", content2, "204EOakland@gmail.com").send_email()
    col2.info("Success! Check your email for a confirmation")
