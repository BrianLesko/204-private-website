# Brian lesko
# 4/21/2024
# A simple UI for picking vacation days to request off
# sends an email to your manager requesting permission

import streamlit as st
from style import style, footer, header, make_title
#from mysecrets import EMAIL, PASSWORD
#from simpleEmailSender import SimpleEmailSender

# Set the page configuration
st.set_page_config(
    page_title="WIP Application page",
    #page_icon='./elev.png',
    layout="wide"  # This sets the layout to wide format
)
style()
st.html(header)
st.html(make_title('Rental Application'))
col1, col2, col3 = st.columns([1,3,1])


@st.experimental_dialog("Supply Check")
def submit(site,supplies):
    st.write(f"besides, {supplies} how many other 'cleaning items' are there?")
    number = st.number_input("Insert a number",step=1)
    if number:
        st.session_state.submission = {"jobsite": site, "request_supplies": supplies, "survery_supplies": number}
        if st.button("Submit"):
            st.rerun()


if "submission" not in st.session_state:
    scol1, scol2 = col2.columns([1, 1])
    # get the information from the user about what supplies they require
    input = scol1.text_input("Why are you interested in living here?")
    email = f"""
        <html>
            <body>
                <p>{input}<p>
        """

    manager_email = f"""
        <html>
            <body>
                <p> is requesting supplies.<p>
                <p>Jobsite</p>
                <p>Requesting Supplies:</p>
                <div style="text-align: center;">
                    <a href="mailto:{operations_email}&subject=Supplies Request&body={operations_email}" style="display: inline-block; margin: 10px; padding: 10px 20px; color: white; background-color: #4CAF50; text-decoration: none; border-radius: 5px;">Approve</a>
                </div>
        """
    if st.button(f'Submit'):
        st.write("submisson")
else: 
    st.html('</div><div style="padding-top: 85px;"></div>')
    #jobsite = st.session_state.submission['jobsite']
    #supplies = st.session_state.submission['request_supplies']
    #survery_item_number = st.session_state.submission['survery_supplies']

    scol1, scol2, scol3 = col2.columns([1, 2, 1])
    with col2:
        with st.spinner('Please wait, do not navigate away...'):
                st.write('Sending Application...')
                #SimpleEmailSender("Supplies Request", email, manager).send_email()
                # send the request 1 level up

                #e = em.email_sequence(key, name, email, manager_email, dates, n_daysoff)
                #e.confirmation_of_request()
                #e.request_approval()
                #st.write('')
                st.write('Done')

st.html('</div><div style="padding-top: 85px;"></div>')
st.html(footer)
