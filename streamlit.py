import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import osascript
import time

# st.link_button("Go to gallery", "https://streamlit.io/gallery")

button = st.button('View')

if button:
    osascript.osascript("set volume output volume 10")
    for i in range(10):
        webbrowser.open_new_tab('https://www.youtube.com/shorts/wIsQpQ8fLSs')
        time.sleep(2)