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

    #import modules
    path = "/pages.toml"
    path = "/Users/christianheins/Documents/Coding/Projects/Personal_finance/modules/pages.toml"
    path = ".streamlit/pages.toml"

    #show_pages_from_config(path)

    # Importing credentials
    #with open('/Users/christianheins/Documents/Coding/Projects/Personal_finance/credentials/credentials.yaml') as file:
    #    credentials_config = yaml.load(file, Loader=SafeLoader)
    #    db_username = credentials_config['local_database']["user"]
    #    db_password = credentials_config['local_database']['password']
    #    db_host = credentials_config['local_database']['host']
    #    db_port = credentials_config['local_database']['port']
    #    db_Db = credentials_config['local_database']['database_m']

    #    supabase_url = credentials_config["supabase"]["url"]
    #    supabase_key = credentials_config["supabase"]["key"]
    #    supabase_database_m = credentials_config["supabase"]["database_m"]


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

    #cols = st.columns(2)
    #with cols[0]:
    #    tabselection = ui.tabs(options=['Team', 'Each of'], default_value='Past 30 days', key="kanaries")

    #with cols[1]:
    #    st.write(f"The time now in berlin is {timestamp_berlin}")

    # Login module
    #with open('/Users/christianheins/Documents/Coding/Projects/Personal_finance/config.yaml') as file:
    #    config = yaml.load(file, Loader=SafeLoader)
    #hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
    #st.write(hashed_passwords)
    #authenticator = stauth.Authenticate(
    #    config['credentials'],
    #    config['cookie']['name'],
    #    config['cookie']['key'],
    #    config['cookie']['expiry_days'],
    #    config['preauthorized']
    #)
    #name, authentication_status, username = authenticator.login(location="main")
    urls = [
                "https://www.youtube.com/watch?v=CDArwuz6Uic",
                "https://soundcloud.com/ackssek/gorillaz-clint-eastwood-jack-essek-edit?si=21ebd52700cc4b6db9ab68ef11f71d6c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
            ]
    #url = "https://soundcloud.com/ackssek/gorillaz-clint-eastwood-jack-essek-edit?si=21ebd52700cc4b6db9ab68ef11f71d6c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
    #@st.experimental_fragment
    #def return_music_player(url):
    #    st.subheader("Track of the week")
    #    st_player(url)
        #st_player("https://soundcloud.com/ackssek/gorillaz-clint-eastwood-jack-essek-edit?si=21ebd52700cc4b6db9ab68ef11f71d6c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
    #return_music_player(url=url)
    #st.divider()
    st.subheader("Track o the Week.")
    
    hide_streamlit_style = """
            <style>
                /* Hide the Streamlit header and menu */
                header {visibility: hidden;}
                /* Optionally, hide the footer */
                .streamlit-footer {display: none;}
                /* Hide your specific div class, replace class name with the one you identified */
                .st-emotion-cache-uf99v8 {display: none;}
            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    @st.experimental_fragment
    def return_soundcloudembed():
        html = """
        <iframe 
            width="100%"
            height="220" 
            scrolling="yes" 
            frameborder="no" 
            allow="autoplay" 
            src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1671680115&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            >
        </iframe>
        <div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/tellel" title="Tellel" target="_blank" style="color: #cccccc; text-decoration: none;">Tellel</a> · <a href="https://soundcloud.com/tellel/turu-anasi-bamboo" title="Turu Anasi - Bamboo" target="_blank" style="color: #cccccc; text-decoration: none;">Turu Anasi - Bamboo</a></div>
        """
        components.html(html, height=250)
        #st.divider()
    return_soundcloudembed()
    # right
    link2 = "https://soundcloud.com/ackssek/gorillaz-clint-eastwood-jack-essek-edit?si=21ebd52700cc4b6db9ab68ef11f71d6c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
    #with cols[1]:
    #    components.iframe(link2, height=400, width=500)
    @st.experimental_fragment
    def return_music_player(url):
        with elements("media_player"):

            # Play video from many third-party sources: YouTube, Facebook, Twitch,
            # SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, DailyMotion and Kaltura.
            #
            # This element is powered by ReactPlayer (GitHub link below).

            from streamlit_elements import media

            media.Player(url=url, controls=True)
    #return_music_player(url=urls[1])
    image = "images/verguerete4-RED.png"

    html_css_template = """
    <style>
    * {{
        box-sizing: border-box;
    }}
    
    :root {{
        --gold: #ffb338;
        --light-shadow: #77571d;
        --dark-shadow: #3e2904;
    }}
    body {{
        margin: 0;
    }}
    .wrapper {{
        background: transparent;
        display: grid;
        grid-template-areas: 'overlap';
        place-content: center;
        margin-left:3%;
        text-transform: uppercase;
    }}
    .wrapper > div {{
        background-clip: text;  
        -webkit-background-clip: text;
        color: #363833;
        font-family: 'Poppins', sans-serif;
        font-weight: 900;
        font-size: 60px;
        grid-area: overlap;
        letter-spacing: 4px;
        -webkit-text-stroke: 4px transparent;
    }}
    div.bg {{
        background-image: repeating-linear-gradient( 105deg, 
        var(--gold) 0% , 
        var(--dark-shadow) 5%,
        var(--gold) 12%);
        color: transparent;
        filter: drop-shadow(5px 15px 15px black);
        transform: scaleY(1.05);
        transform-origin: top;
        text-align: left;
    }}
    div.fg{{
        background-image: repeating-linear-gradient( 5deg,  
        var(--gold) 0% , 
        var(--light-shadow) 23%, 
        var(--gold) 31%);
        color: #1e2127;
        transform: scale(1);
        text-align: left;
    }}
    </style>
    
    <div class="wrapper">
        <div class="bg"> {} </div>
        <div class="fg"> {} </div>
    </div>
    """

    # Word to be inserted as variable
    variable_word = "MonoTor Presents"

    # Format the HTML string with the variable word
    html_css = html_css_template.format(variable_word, variable_word)
    st.html(html_css)


    html = """
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Artists Showcase</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 20px;
                }

                .artists-container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 240px;
                }

                .artist-card {
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                    width: 300px;
                    transition: transform 0.2s;
                }

                .artist-card:hover {
                    transform: scale(1.3);
                }

                .artist-image {
                    width: 100%;
                    height: 200px;
                    object-fit: cover;
                }

                .artist-info {
                    padding: 20px;
                    text-align: center;
                }

                .artist-name {
                    font-size: 1.5em;
                    margin: 10px 0;
                    color: #333;
                }

                .artist-description {
                    color: #777;
                    line-height: 1.6;
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">Artists Showcase</h1>
            <div class="artists-container">
                <div class="artist-card">
                    <img src="https://github.com/christianheins/monotor/blob/main/images/46022236_270547913605848_7412623757248725390_n.jpg?raw=true" alt="Artist 1" class="artist-image">
                    <div class="artist-info">
                        <h2 class="artist-name">Mono Heins</h2>
                        <p class="artist-description">
                        
                        Deep House, Tech House, Progressive House, Minimal, Tropical and Afrobeats. 
                        <br>
                        <br> 
                        Rangeing all the tempos, from low beats to high highs...</p>
                    
                    </div>
                </div>

                <div class="artist-card">
                    <img src="https://github.com/christianheins/monotor/blob/main/images/355400358_655713002694553_2090091328426271917_n.jpg?raw=true" alt="Artist 2" class="artist-image">
                    <div class="artist-info">
                        <h2 class="artist-name">Tomeitou</h2>
                        <p class="artist-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor.</p>
                    </div>
                </div>

                <div class="artist-card">
                    <img src="https://github.com/christianheins/monotor/blob/main/images/435039739_339982482390138_4821613555573842117_n.jpg?raw=true" alt="Artist 3" class="artist-image">
                    <div class="artist-info">
                        <h2 class="artist-name">Maniak</h2>
                        <p class="artist-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
    """
    st.html(html)
    #
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Gig Listings</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 20px;
                }

                h1 {
                    text-align: center;
                    color: black;
                }

                .gigs-table {
                    width: 90%;
                    margin: 20px auto;
                    border-collapse: collapse;
                    background-color: #fff;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 10px;
                    overflow: hidden;
                }

                .gigs-table th, .gigs-table td {
                    padding: 15px;
                    text-align: left;
                }

                .gigs-table th {
                    background-color: #333;
                    color: yellow;
                    text-transform: uppercase;
                    font-weight: normal;
                }

                .gigs-table td {
                    border-bottom: 1px solid #ddd;
                    color: orange;
                }

                .gigs-table tr:last-child td {
                    border-bottom: none;
                }

                .gigs-table tr:nth-child(even) {
                    background-color: #f9f9f9;
                }

                .gigs-table tr:hover {
                    background-color: #f1f1f1;
                }

                .gigs-table td:first-child {
                    font-weight: bold;
                    color: green;
                }
            </style>
        </head>
        <body>
            <h1>Gig Listings</h1>
            <table class="gigs-table">
                <thead>
                    <tr>
                        <th>Event Name</th>
                        <th>Venue Name</th>
                        <th>Date and Time</th>
                        <th>City</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Rock Night</td>
                        <td>The Big Arena</td>
                        <td>2024-07-16 20:00</td>
                        <td>New York</td>
                    </tr>
                    <tr>
                        <td>Jazz Festival</td>
                        <td>City Park</td>
                        <td>2024-08-05 18:00</td>
                        <td>Chicago</td>
                    </tr>
                    <tr>
                        <td>Indie Vibes</td>
                        <td>The Underground Club</td>
                        <td>2024-09-10 21:00</td>
                        <td>Los Angeles</td>
                    </tr>
                    <tr>
                        <td>Country Classics</td>
                        <td>Grand Hall</td>
                        <td>2024-10-22 19:30</td>
                        <td>Nashville</td>
                    </tr>
                </tbody>
            </table>
        </body>
        </html>

    """

    st.html(html)
    #

    st.image(image, use_column_width=True)

    st.html("""

        <img src="images/verguerete4-RED.png>

    """)

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


        #with open(r'/Users/christianheins/Documents/Coding/Projects/Personal_finance/pages/style.css') as f:
        #    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
