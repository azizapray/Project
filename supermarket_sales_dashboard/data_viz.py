import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title('SUPERMARKET SALES DASHBOARD')
    st.write('Berikut ini merupakan Dataset history penjualan oleh suatu supermarket yang tercatat di 3 cabang berbeda selama 3 bulan.')
    
    df = pd.read_csv('supermarket_sales - Sheet1.csv')
    
    show = st.checkbox('Show Dataset')
    if show:
        st.write(df)
    
    ##--- Figure 1
    st.subheader('__Best Selling Product__')
    fig1,ax1 = plt.subplots(figsize=(6,3))
    
    df.groupby('Product line')['Quantity'].apply(sum).plot(kind='barh', ax=ax1)
    
    ax1.set_xlabel('Total Spending by Customers')
    ax1.set_ylabel('Product Line')
    
    st.pyplot(fig1)
    
    ##--- Figure 2
    st.subheader('__Customers Favorite Payment Method__')
    fig2,ax2 = plt.subplots()
    
    df.groupby('Payment')['Total'].sum().plot(kind='pie', figsize=(5,4), autopct='%1.1f%%', startangle=90, labels=None)
    plt.legend(labels=df.Payment, loc='upper left')
    
    st.pyplot(fig2)
    
    ##--- Figure 3
    payment_select = st.radio('Choose Payment Method :',['Cash', 'Ewallet', 'Credit card'])
    fig3,ax3 = plt.subplots(figsize=(6,3))
    
    payment = df[df['Payment'] == payment_select]
    group_pay = payment['Product line'].value_counts().sort_index()
    group_pay.plot(kind='barh', ax=ax3)
    
    ax3.set_xlabel('Number of transactions')
    ax3.set_ylabel('Product Line')
    
    st.write('Payment by', payment_select)
    st.pyplot(fig3)

    with st.expander('Data Insight'):
        st.write('1. Pembayaran dengan metode __cash__ untuk pembelian __aksesoris elektronik__ memiliki jumlah transaksi yang tertinggi. Sehingga ada peluang untuk penawaran diskon jika menggunakan metode pembayaran tersebut.')
        st.write('2. Pembayaran dengan metode __e-wallet__ untuk pembelian __aksesoris fashion__ memiliki jumlah transaksi yang tertinggi. Sehingga ada peluang untuk penawaran diskon jika menggunakan metode pembayaran tersebut.')