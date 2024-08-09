import streamlit as st
def style():
    hide_st_style = """
                <style>
                html {
                    overflow: hidden;
                    overscroll-behavior: none;
                }
                overflow: hidden;
                overscroll-behavior: none;
                body {
                    margin: 40px auto;
                    line-height: 1.6;
                    font-size: 18px;
                    color: #444;
                    /* padding: 0 10px; */
                    background-color: rgb(255, 255, 255);
                    font-family: Arial;
                    font-weight: 300; /* font thickness */
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
                h1, h2, h3 {
                    font-family: Helvetica;
                    line-height: 1;
                    font-weight: 300; /* font thickness */
                }
                a.link {
                    margin-left: 20px;
                    text-decoration: none;
                    font-family: inherit;
                    color: #ff5b15;
                    transition: text-decoration 0.3s ease;
                }
                a.link:hover {
                    text-decoration: underline;
                }
                a.h2link {
                    margin-left: 20px;
                    text-decoration: none;
                    font-family: inherit;
                    color: #adadad;
                    transition: text-decoration 0.3s ease;
                }
                a.h2link:hover {
                    text-decoration: underline;
                }
                /* Media Queries for Mobile Devices */
                @media only screen and (max-width: 480px) {
                    body {
                        padding-left: 20px;
                        padding-right: 20px;
                    }
                }
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(
            """
            <style>
            .centered-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .stButton button {
                background-color: #ff5b15;  /* Original green color */
                color: rgb(244, 244, 244);
                border: none;
                padding: 10px 20px;
                border-radius: 24px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
            }
            .stButton button:hover {
                background-color: #f86526;  /* Change this color to your preferred hover state */
                color: #ffffff;  /* Set the hover text color */
            }
            </style>
            """,
            unsafe_allow_html=True)
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    div.st
    </style>""", unsafe_allow_html=True)

def make_title(title):
    return f"""
        <div id="content" style="max-width: 95%; max-width: 665px; margin: auto; z-index: 1000;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: -2px;">
            <img src="/docs/elev.png" alt="Your Alt Text" style="width: 80px; flex: 0.2; margin: 0;">
            <h1 style="text-align: center; flex: 1; margin: 0;">{title}</h1>
            <div style="flex: 0.2;"></div>
        </div>
        <hr style="margin-top: 10px;">
    """

header =   """
<div style="position: fixed; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; height: 40px; display: flex; justify-content: center; align-items: center; background-color: #f0f0f0; top: 0; overflow: auto; padding-left: 20px; padding-right: 20px; box-sizing: border-box; z-index: 1000;">
    <div class="link" style="text-align: center;">
    <a href="https://mystudentrental.co" class="link" style="font-size: 0.76em;">My Student Rental Co.</a>
    </div>

    <div class="link" style="text-align: right;">
    <a href="https://mystudentrental.co/tenants/" class="h2link" style="font-size: 0.76em;">Tenants</a>
    </div>
</div>
<div style="height: 50px;"></div>
<div id="content"></div>
"""

footer = """
<div style = "margin-top: 100px;">
    <div style="margin-bottom: -50vw; margin-left: -50vw; margin-right: -50vw; height: 200px; display: flex; justify-content: center; align-items: center; background-color: #f0f0f0; top: 0; top: 0; overflow: auto; padding-left: 20px; padding-right: 20px; box-sizing: border-box; z-index: 1000;">
            <div class="link" style="text-align: center;">
            <a href="https://cleanmybuilding.co" class="link" style="font-size: 0.76em;">Clean my building Co.</a>
            </div>

            <div class="link" style="text-align: right;">
            <a href="https://cleanmybuilding.co/employees/" class="h2link" style="font-size: 0.76em;">Employees</a>
            </div>
    </div>
"""
