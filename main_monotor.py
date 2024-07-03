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
    #from credentials import cresas


    ##ads

    st.set_page_config(page_title="MAIN", layout="wide", initial_sidebar_state="expanded", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Welcome to our property listings. This is an *extremely* cool app!"
    })

    #import modules
    path = "/pages.toml"
    path = "/Users/christianheins/Documents/Coding/Projects/Personal_finance/modules/pages.toml"
    path = ".streamlit/pages.toml"

    show_pages_from_config(path)

    # Importing credentials
    with open('/Users/christianheins/Documents/Coding/Projects/Personal_finance/credentials/credentials.yaml') as file:
        credentials_config = yaml.load(file, Loader=SafeLoader)
        db_username = credentials_config['local_database']["user"]
        db_password = credentials_config['local_database']['password']
        db_host = credentials_config['local_database']['host']
        db_port = credentials_config['local_database']['port']
        db_Db = credentials_config['local_database']['database_m']

        supabase_url = credentials_config["supabase"]["url"]
        supabase_key = credentials_config["supabase"]["key"]
        supabase_database_m = credentials_config["supabase"]["database_m"]


    # Project modules
    #import sys
    #sys.path.insert(1, "/Users/christianheins/Documents/Coding/Projects/Personal_finance")
    #sys.path.insert(1, "/Users/christianheins/Documents/Coding/Projects/Personal_finance/modules")
    #from modules import module_login
    #from modules.expense_form import forms_expense



    # Set the time zone to Berlin
    berlin_timezone = pytz.timezone('Europe/Berlin')

    # Get the current time in Berlin
    now_berlin = datetime.now(berlin_timezone)

    # Format the timestamp as a string
    timestamp_berlin = now_berlin.strftime('%Y-%m-%d %H:%M:%S')

    cols = st.columns(2)
    with cols[0]:
        tabselection = ui.tabs(options=['Team', 'Each of'], default_value='Past 30 days', key="kanaries")

    with cols[1]:
        st.write(f"The time now in berlin is {timestamp_berlin}")

    # Login module
    with open('/Users/christianheins/Documents/Coding/Projects/Personal_finance/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    #hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
    #st.write(hashed_passwords)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login(location="main")

    if st.session_state["authentication_status"]:

        # Eliminate the need to check for ssl
        ssl._create_default_https_context = ssl._create_unverified_context

        def get_current_movements():
            try:
                mydb = connection.connect(
                    host=db_host,
                    database = db_Db,
                    user=db_username,
                    passwd=db_password, use_pure=True)
                print(mydb)
                query = "Select * from movements;"
                df = pd.read_sql(query,mydb)
                mydb.close() #close the connection
                return df

            except Exception as e:
                mydb.close()
                print(str(e))

        #df_movements_sql_server = get_current_movements()
        #df_movements_sql_server.sort_values(by=["Date", "Time_of_transaction"], ascending=[False, False], inplace=True)


        def get_current_movements_supabase():
            supabase: Client = create_client(supabase_url, supabase_key)
            response = supabase.table(supabase_database_m).select("*").execute()
            data = response.data
            df = pd.DataFrame(data)
            return df


        df_movements_supabase = get_current_movements_supabase()

        df_movements_sql_server = df_movements_supabase


        def format_df(df) -> pd.DataFrame:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.tz_localize(None)
            return df
        df_movements_sql_server = format_df(df_movements_sql_server)


        df_movements_sql_server.fillna("", inplace=True)

        df_movements_sql_server.sort_values(by=[
            "Date",
            "Time_of_transaction"
        ],
            ascending=[False, False],
            inplace=True
        )


        with st.sidebar:
            st.write(f'Welcome *{name}*')
            authenticator.logout('Logout', 'main')

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
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')



    with open(r'/Users/christianheins/Documents/Coding/Projects/Personal_finance/pages/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    try:
        plyer.notification.notify(title='Streamlit', message=str("Main page reloaded"), timeout=5)
    except:
        def sendslack():
            # Eliminate the need to check for ssl
            #ssl._create_default_https_context = ssl._create_unverified_context
            #Create a slack client and define todays date or moment date
            token_slack = "xoxb-5139171635815-6832465209141-MAnpqSCUStVzHxv65aGINVQ1"
            #client = slack.WebClient(token=token_slack)


            #slack_token = os.environ["SLACK_BOT_TOKEN"]
            client = WebClient(token=token_slack)

            #Tell the client to select a channel and include the specified text.
            client.chat_postMessage(channel='#page_reloads', text=f"Main page reloaded at: {timestamp_berlin}")
            print("Sending slack message")
        sendslack()


if __name__ == "__main__":
    main()
