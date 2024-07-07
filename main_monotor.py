def main():

    from fake_useragent import UserAgent
    import urllib
    from bs4 import BeautifulSoup
    import ssl
    import requests
    from datetime import datetime, timedelta
    import time
    import pytz
    import slack
    #from slack import WebClient
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError

    # Data Management
    import os
    import random
    import time
    #import pyodbc
    #import mysql
    #import mysql.connector as connection
    import sqlalchemy
    from supabase import create_client, Client
    from sqlalchemy import create_engine
    import pandas as pd
    from pandas.tseries.offsets import MonthBegin, MonthEnd

    # Front End
    import streamlit as st
    import streamlit.components.v1 as components

    #from streamlit_option_menu import option_menu
    #from streamlit_extras.stylable_container import stylable_container
    from st_pages import Page, show_pages, add_page_title, show_pages_from_config
    #from st_aggrid import AgGrid
    #from st_aggrid.grid_options_builder import GridOptionsBuilder
    #from streamlit_card import card
    #import streamlit_authenticator as stauth
    #import streamlit_shadcn_ui as ui
    import yaml
    from yaml.loader import SafeLoader
    #import plyer
    import altair as alt
    import plotly.express as px
    import json
    #from credentials import cre


    ##ads

    st.set_page_config(page_title="MAIN", layout="wide", initial_sidebar_state="collapsed", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Welcome to our property listings. This is an *extremely* cool app!"
    })
    
    with open(r'styles/main_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    


    html = """

    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body {font-family: Arial, Helvetica, sans-serif;}

    /* The Modal (background) */
    .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    -webkit-animation-name: fadeIn; /* Fade in the background */
    -webkit-animation-duration: 0.4s;
    animation-name: fadeIn;
    animation-duration: 0.4s
    }

    /* Modal Content */
    .modal-content {
    position: fixed;
    bottom: 0;
    background-color: #fefefe;
    width: 100%;
    -webkit-animation-name: slideIn;
    -webkit-animation-duration: 0.4s;
    animation-name: slideIn;
    animation-duration: 0.4s
    }

    /* The Close Button */
    .close {
    color: white;
    float: right;
    font-size: 28px;
    font-weight: bold;
    }

    .close:hover,
    .close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
    }

    .modal-header {
    padding: 2px 16px;
    background-color: #5cb85c;
    color: white;
    }

    .modal-body {padding: 2px 16px;}

    .modal-footer {
    padding: 2px 16px;
    background-color: #5cb85c;
    color: white;
    }

    /* Add Animation */
    @-webkit-keyframes slideIn {
    from {bottom: -300px; opacity: 0} 
    to {bottom: 0; opacity: 1}
    }

    @keyframes slideIn {
    from {bottom: -300px; opacity: 0}
    to {bottom: 0; opacity: 1}
    }

    @-webkit-keyframes fadeIn {
    from {opacity: 0} 
    to {opacity: 1}
    }

    @keyframes fadeIn {
    from {opacity: 0} 
    to {opacity: 1}
    }
    </style>
    </head>
    <body>

    <h2>Bottom Modal</h2>

    <!-- Trigger/Open The Modal -->
    <button id="myBtn">Open Modal</button>

    <!-- The Modal -->
    <div id="myModal" class="modal">

    <!-- Modal content -->
    <div class="modal-content">
        <div class="modal-header">
        <span class="close">&times;</span>
        <h2>Modal Header</h2>
        </div>
        <div class="modal-body">
        <p>Some text in the Modal Body</p>
        <p>Some other text...</p>
        </div>
        <div class="modal-footer">
        <h3>Modal Footer</h3>
        </div>
    </div>

    </div>

    <script>
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal 
    btn.onclick = function() {
    modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }
    </script>

    </body>
    </html>



    """

    st.html(html)

    with st.sidebar:
        #st.write(f'Welcome *{name}*')
        #authenticator.logout('Logout', 'main')

        ft = """
        <style>
        a:link , a:visited{
        color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
        background-color: transparent;
        text-decoration: none;
        }
        
        a:hover,  a:active {
        color: #0283C3; /* theme's primary color*/
        background-color: transparent;
        text-decoration: underline;
        }
        
        #page-container {
            position: relative;
            min-height: 0vh;
            display:flex;
            flex-direction: column;
            justify-content: center;
        
        }
        
        footer{
        visibility:hidden;
        }
        
        .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #808080; /* theme's text color hex code at 50 percent brightness*/
        text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
        }
        </style>
        
        <div id="page-container">
        
        <div class="footer">
        <hr>
        <p style='font-size: 0.875em;'>Powered by: <a style='display: inline; text-align: center;' href="https://streamlit.io/" target="_blank">Streamlit.</a><br 'style= top:3px;'>
        With <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "20"/> by: <a style='display: inline; text-align: center;' href="https://github.com/sape94" target="_blank">El Mono.</a></p>
        <hr>
        </div>
        
        </div>
        """
        st.write(ft, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
