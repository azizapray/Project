#import data_viz, hypo
import streamlit as st

st.set_page_config(
    page_title="Airbnb in NY City",
    page_icon="🙉",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "My Github Profile: https://github.com/azizapray",
    }
)

PAGES = {
    'Data Visualization': data_viz,
    'Hypotesis Testing': hypo
}

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Select a page:", list(PAGES.keys()))

page = PAGES[selection]

page.app()