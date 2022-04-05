import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def app():
    st.title('HYPOTESIS TESTING')
    st.write('Berdasarkan dataset yang ada, saya akan menggunakan rating sebagai parameter pembanding antara ketiga branch.')

    df = pd.read_csv('supermarket_sales - Sheet1.csv')

    st.subheader('__ANOVA__')
    st.write('__Apakah rating kepuasan customer di setiap cabang memiliki perbedaan yang signifikan?__')
    st.write('Berikut ini adalah hipotesanya.')
    st.latex(''' H0: μ_A = μ_B = μ_C ''')
    st.latex(''' H1: μ_A != μ_B != μ_C ''')

    st.write('H0: perbedaan rating dari cabang A, B, dan C tidak signifikan')
    st.write('H1: perbedaan rating dari cabang A, B, dan C signifikan')
    
    cv = 0.05
    st.write('Critical value:', cv)

    A = df[df['Branch'] == 'A']
    B = df[df['Branch'] == 'B']
    C = df[df['Branch'] == 'C']

    with st.expander('Mean Value'):
        st.write('Rata-rata rating cabang A adalah', A['Rating'].mean())
        st.write('Rata-rata rating cabang B adalah', B['Rating'].mean())
        st.write('Rata-rata rating cabang C adalah', C['Rating'].mean())


    f_val,p_val = stats.f_oneway(A['Rating'], B['Rating'], C['Rating'])
    st.write('P-value:', p_val)
    st.write('F-value:', f_val)

    sns.boxplot(x='Branch',
                y='Rating',
                data=df,
                color='#99c2a2',
                showmeans=True,
                meanprops={"marker": "+",
                           "markeredgecolor": "red",
                           "markersize": "10"})

    with st.expander('Show Visualization'):
        st.pyplot(plt.gcf())

    st.subheader('Kesimpulan')
    st.write('P-value lebih besar dari 0.05, sehingga H0 diterima.')
    st.write('Artinya, perbedaan rating dari cabang A, B, dan C tidak signifikan atau memiliki nilai yang sama')