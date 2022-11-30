import streamlit as st
import pandas as pd 
import numpy as np
from is_lm import ISLM

def main():
    st.set_page_config(page_title='Blog Economia',
                    page_icon=':notebook:',
                    layout='wide')
    st.title('Modelo IS-LM')
    st.sidebar.header('Entrada de parametros modelo')

    def user_input_parameters():
        M = st.sidebar.slider('Oferta Monetaria',0,10000,400)
        P = st.sidebar.slider('Nivel de Precios',0,10000,1)
        k = st.sidebar.slider('Sensibilidad a la Renta',0,10000,4)
        h = st.sidebar.slider('Sensibilidad al tipo de interes',0,10000,50)
        c = st.sidebar.slider('Propensión al consumo',min_value=float(0), max_value=float(1),value=0.8,step=0.01)
        t = st.sidebar.slider('Tasa Impositiva',min_value=float(0), max_value=float(1),value=0.2,step=0.01)
        b = st.sidebar.slider('Sensibilidad de la inversion',0,10000,40)
        Ca = st.sidebar.slider('Consumo Autonomo',0,10000,180)
        Ta = st.sidebar.slider('Impuesto Autonomo',0,10000,50)
        Ia = st.sidebar.slider('Interes Autonomo',0,10000,50)
        Tr = st.sidebar.slider('Transferencias',0,10000,100)
        G = st.sidebar.slider('Gasto',0,10000,500)
        NX = st.sidebar.slider('Exportaciones Netas',0,10000,50)
        data = {'Oferta Monetaria':round(M,2), 'Nivel de Precios':round(P,2), 'Sensibilidad a la Renta':round(k,2),
                'Sensibilidad al tipo de interes':round(h,2), 'Pmg':round(c,2), 'Tasa Impositiva':round(t,2),
                'Sensibilidad de la inversion':round(b,2), 'Consumo Autonomo':round(Ca,2),'Impuesto Autonomo':round(Ta,2),
                'Interes Autonomo':round(Ia,2),'Trasnferencias':round(Tr,2),'Gasto':round(G,2),'Exportaciones Netas':round(NX,2)}
        feactures = pd.DataFrame(data,index=['Parameters'])
        return feactures
    
    
    #M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX = tuple(user_input_parameters().loc['Parameters'])
    st.dataframe(user_input_parameters())
    #st.success(ISLM(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX)[0])

    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['2', 'b', 'c'])
    st.line_chart(chart_data)

    
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

if __name__ == '__main__':
    main()