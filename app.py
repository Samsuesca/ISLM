import streamlit as st
import pandas as pd 
import numpy as np
import sympy as sp
from is_lm import ISLM, ISLM_deploy, ISLM_get_description, definition, parameters

M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX = sp.symbols('M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX')

def main():
    st.set_page_config(page_title='Blog Economia',
                    page_icon=':notebook:',
                    layout='wide')

    ##PRINCIPAL 
    st.markdown("""---""")
    st.title('Modelo IS-LM')
    st.markdown("""---""")
    leftcol1,rightcol1 = st.columns([1.5,1],gap='medium')
    with leftcol1:
        st.markdown('**GENERALIDADES**')
        st.markdown('''Este sitio es un infograma interactivo sobre el modelo
        IS-LM. Este modelo se trabaja en los primeros cursos de Macroeconomia, pues sirve como
        introducción al análisis macro de una economía. En la siguiente imagen podemos ver una breve definición''')
        st.image(definition())
        st.markdown('''El modelo IS-LM (Investment-Saving and Liquidity Preference-Money Supply) parte del análisis de dos mercados, el de bienes y el de dinero, 
        y termina por explicar las principales relaciones entre la política monetaria y la política fiscal. Este infograma, fue basado en el libro de 
        Macroeconomía de Rudiger Dornbush, Stanley Fischer y Richard Startz, especialmente en los capitulos 10, 11 y 12 de la  12va edición
        ''')
        st.markdown('''En la parte derecha podrás encontrar la "sintexis" matemática del modelo,
        para después, en la parte inferior, entrar a la parte interactiva, donde podrás entrar los parámetros de un modelo IS-LM estático. Y
        obtener como resultado la gráfica del equilibrio de mercado, el planteamiento del modelo y  el procedimiento''')
        st.markdown("""  """)
        st.markdown("""  """)
        st.download_button('Descarga el libro guía','book.pdf','Macroeconomia_DFS.pdf')
        st.write('''Accede a esta lista de reproducción de youtube de la [Universidad de 
        Valladolid](https://www.youtube.com/watch?v=BgbQB3jRxOI&list=PLSbo9kXA_Lcx5baMlEVo4s60RODjZiwsW) para acceder a un curso sobre IS-LM.''')
        st.markdown("""  """)
       

    with rightcol1:
        results1 = ISLM_deploy(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX)
        st.markdown('**MERCADO DE DINERO Y LA RECTA LM**')
        st.write('Tenemos la forma de la ecuación de demanda de dinero:')
        st.latex(results1[0])
        st.write('''El mercado de dinero debe estar en equilibrio, por lo tanto la oferta monetaria 
                real es igual a la demanda de dinero:''')
        st.latex(results1[2])
        st.write('De forma general, se obtiene igualando:')
        st.latex(results1[4])
        st.markdown('**DEMANDA AGREGADA Y LA RECTA IS**')
        st.write('''Sabemos de forma general que la Demanda Agregada de una economia 
                tiene ciertos componenetes autonomos que se expresan en la sigueinte ecuación:''')
        st.latex(results1[6])
        st.write('''Cuando el mercado está en equilibrio, es decir, cuando
            la demanda agregada DA es igual al nivel de renta Y, se obtiene la recta IS a partir
                de la siguiente expresión:''')
        st.latex(results1[8])
        st.markdown('**EQUILIBRIO IS-LM**')
        st.write('Se igualan las rectas IS y LM, de forma general:')
        st.latex(results1[10])
        st.write('Despejando se obtiene el nivel de renta de equilibrio:')
        st.latex(results1[12])
        st.write('Y ahora se pasa el nivel de renta a las rectas IS o LM:')
        st.latex(results1[14])
      
    

    st.markdown("""---""")
    ##BODY OF INTERACTIVE PART
    leftcol, rightcol = st.columns([2,1])

    with leftcol:
        tab1, tab2 = st.tabs(["Parámetros","📈 Gráficos"])
        tab1.subheader('Entrada de Parámetros')
        feactures = parameters(tab1)
        Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp = tuple(feactures.loc['Parameters'])
        plt, xresults = ISLM(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
        tab2.subheader('Grafica de Equilibrio de Mercado')
        tab2.pyplot(plt)
        tab2.markdown('''La gráfica muestra el punto de equilibrio/intercepción entre 
        ambos mercados, es decir de las rectas IS-LM. Dando el nivel de renta de equilibrio y la 
        tasa de interes de equilibrio''')

    with rightcol:
        tab1, tab2 = st.tabs(["Modelo","Procedimiento"])
        tab1.subheader('Parametros Configurados')
        equations = ISLM_get_description(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
        for i in equations:
            tab1.latex(i)

        tab2.subheader('Procedimiento')
        tab2.markdown('Puedes Ejecutar el procedimiento, dando click en el botón')
        if tab2.button('Ejecutar'):
            results = ISLM_deploy(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
            tab2.markdown('**Obtener la recta LM**')
            tab2.write('La demanda de dinero, como se vio anteriormente, quedaría:')
            tab2.latex(results[1])
            tab2.write('Si igualamos la oferta monetaria real con la demanda de liquidez:')
            tab2.latex(results[3])
            tab2.latex(results[5])
            tab2.write('La última expresión representa la recta LM')
            tab2.markdown('**Obtener la recta IS**')
            tab2.write('Partiendo de DA=Y, tenemos que el componente autonomo y la recta IS de esta economía son:')
            tab2.latex(results[7])
            tab2.latex(results[9])
            tab2.markdown('**Equilibrio IS-LM**')
            tab2.write('Al igualar las rectas se obtiene:')
            tab2.latex(results[11])
            tab2.write('Si despejamos para Y, se obtiene la renta de equilibrio:')
            tab2.latex(results[13])
            tab2.write('Y por lo tanto una tasa de interes de:')
            tab2.latex(results[15])

    st.markdown("""---""")

   
    
   

if __name__ == '__main__':
    main()