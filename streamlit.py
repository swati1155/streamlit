import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import urllib.request
# import osascript
import time
# import applescript
from streamlit.components.v1 import html



# button = st.button('Click Here')
url='https://www.youtube.com/shorts/wIsQpQ8fLSs'

# if button:
#     # osascript.osascript("set volume output volume 100")
#     for i in range(1):
#         webbrowser.open_new_tab(url)
#         # urllib.urlopen(url)
#         # with urllib.request.urlopen(url) as url:
#         #     s = url.read()
#         time.sleep(2)



if 'open_count' not in st.session_state:
    st.session_state.open_count = 0

def open_page(url):
    open_script= f"""
        <script type="text/javascript">
            window.open('%s', "new_window_{st.session_state.open_count}", "popup").focus();
        </script>
    """ % (url)
    for i in range(15):
        html(open_script)
        # st.session_state.open_count += 1
        time.sleep(2)

# st.button('test', on_click=open_page, args=(url,))
button = st.button('Click Here')

if button:
    for i in range(1):
        open_page(url)
        time.sleep(2)