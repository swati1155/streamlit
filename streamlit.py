import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import urllib
# import osascript
import time
# import applescript

button = st.button('Click Here')

if button:
    # osascript.osascript("set volume output volume 100")
    for i in range(1):
        # webbrowser.open_new_tab('https://www.youtube.com/shorts/wIsQpQ8fLSs')
        urllib.urlopen('https://www.youtube.com/shorts/wIsQpQ8fLSs')
        time.sleep(2)