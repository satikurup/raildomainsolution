# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:35:50 2021

@author: ATHIRA
"""

import time
import numpy as np
import cv2


import plot
import streamlit as st
import cv2
import webbrowser
from PIL import Image
import numpy as np 
import streamlit as st 
import argparse
import time
import numpy as np
import cv2
import moviepy.editor as moviepy
import argparse
import time
import numpy as np
import cv2


import plot

import plot
from PIL import Image
import numpy as np 
import tempfile

rad = st.sidebar.selectbox(
    " Platform ",
    ("CrowdAnalysis", "Unattended Baggage Detection","Blind person detection")
)   
st.title("Rail Platform Solutions")
if rad=="CrowdAnalysis":
   st.write("CrowdAnalysis")
   st.video("crowd.mp4")
   
if rad=="Unattended Baggage Detection":
   st.video("myvide.mp4")
if rad==("Blind person detection"):
    st.video("12-02-52.mp4")
