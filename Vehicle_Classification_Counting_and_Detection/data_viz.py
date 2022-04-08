import streamlit as st

def app():
    st.markdown("<h1 style='text-align: center; color: yellow;'>VEHICLE DETECTOR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center'>Web-app ini merupakan visualisasi dari hasil project VECTOR yang telah kami buat mengenai <b>Object Detection<b>.<br>Dataset yang digunakan dalam project ini dapat dilihat pada <a href='https://www.kaggle.com/datasets/rishabkoul1/vechicle-dataset'>Kaggle</a>.</p>", unsafe_allow_html=True)
    st.write('---')

    # -------- Klasifikasi Dataset ---------
    st.header('About the Dataset')
    st.subheader('Classification')
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
 
    with col1:
        st.subheader('🛵Bike')
        with st.expander('See data train class and sample'):
            st.image('bike.png','Bike')
            st.write('Ciri-ciri sepeda motor:')
            st.write('- Digerakkan dengan mesin.')
            st.write('- Mempunyai dua roda yang sebaris lurus.')
            st.write('- Mempunyai setang untuk mengendalikan arah jalannya motor.')
            st.write('- Termasuk transportasi darat.')

    with col2:
        st.subheader('🚗Car')
        with st.expander('See data train class and sample'):
            st.image('car.png','Car')
            st.write('Ciri-ciri mobil:')
            st.write('- Digerakkan dengan mesin.')
            st.write('- Mempunyai dua roda depan dan dua roda belakang.')
            st.write('- Mobil mempunyai ruang dalam yang berisikan kursi.')
            st.write('- Mempunyai setir untuk mengendalikan arah jalan mobil.')
            st.write('- Mempunyai pintu.')
            st.write('- Termasuk transportasi darat.')

    with col3:
        st.subheader('🚌Bus')
        with st.expander('See data train class and sample'):
            st.image('bus.png','Bus')
            st.write('Ciri-ciri bus:')
            st.write('- Digerakkan dengan mesin.')
            st.write('- Memiliki dua roda depan dan dua roda belakang.')
            st.write('- Ukuran bus umumnya lebih besar daripada mobil.')
            st.write('- Bisa mengangkut banyak penumpang.')
            st.write('- Mempunyai setir untuk mengendalikan arah jalan bus.')
            st.write('- Mempunyai pintu.')
            st.write('- Termasuk transportasi darat.')

    with col4:
        st.subheader('🚚Truck')
        with st.expander('See data train class and sample'):
            st.image('truck.png','Truck')
            st.write('Ciri-ciri truk:')
            st.write('- Digerakkan dengan mesin.')
            st.write('- Memiliki dua roda depan dan dua roda belakang.')
            st.write('- Umumnya memiliki ukuran yang besar dibanding mobil.')
            st.write('- Mempunyai ruang pengankut barang di bagian belakang truk.')
            st.write('- Ruang depan berisikan kursi supir dan penumpang.')
            st.write('- Mempunyai pintu.')
            st.write('- Termasuk transportasi darat.')