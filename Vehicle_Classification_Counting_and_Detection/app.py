import data_viz, demo
import streamlit as st

st.set_page_config(
    page_title="Vehicle Detection Counter",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Our Github Profile: https://github.com/lutfiadam97, https://github.com/azizapray, https://github.com/sandikaaplg",
    }
)

PAGES = {
    'Data Visualization': data_viz,
    'Demo Prediction': demo
}

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Select a page:", list(PAGES.keys()))

page = PAGES[selection]

page.app()