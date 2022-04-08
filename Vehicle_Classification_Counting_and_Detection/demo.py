import streamlit as st
import numpy as np

from cv2 import VideoWriter
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2


def app():
    st.markdown("<h1 style='text-align: center; color: yellow;'>DEMO PREDICTION</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center'>Web-app ini merupakan visualisasi dari hasil project yang telah kami buat mengenai <b>Object Detection<b>.<br>Dataset yang digunakan dalam project ini dapat dilihat pada <a href='https://www.kaggle.com/datasets/rishabkoul1/vechicle-dataset'>Kaggle</a>.</p>", unsafe_allow_html=True)
    st.write('---')

    model_v5 = load_model('model_vehicle_v5.h5')
    
    st.subheader('Video Uploader')
    video = st.file_uploader('Upload:', type=['mp4'])
    if video is not None:
        st.video(video)
    else:
        st.write('Please upload the correct format file.')