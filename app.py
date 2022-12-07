import streamlit as st
import pandas as pd 
import numpy as np
import sympy as sp
from ISLM import ISLMProcess
from streamlit_option_menu import option_menu

M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX = sp.symbols('M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX')


def main():
    #CONGIGURACIÓN DEL SITIO 
    st.set_page_config(page_title='Blog Economia',
                    page_icon=':notebook:',
                    layout='wide')

    ## DESCRIPCÓN PRINCIPAL 
    st.markdown("""---""")
    st.title('                 Modelo IS-LM                ')
    st.markdown("""---""")
    leftcol1,rightcol1 = st.columns([1,1],gap='large')
    with leftcol1:
        st.markdown(f'''
        **GENERALIDADES** \n
        Este sitio es un infograma interactivo sobre el modelo
        IS-LM. Este modelo se trabaja en los primeros cursos de Macroeconomia, pues sirve como
        introducción al análisis macro de una economía. En la siguiente imagen podemos ver una breve definición''')
        st.image(ISLMProcess.img_definition(),use_column_width='always')
        st.markdown('''El modelo IS-LM (Investmenrt-Saving and Liquidity Preference-Money Supply) parte del análisis de dos mercados, el de bienes y el de dinero, 
        y termina por explicar las principales relaciones entre la política monetaria y la política fiscal. Este infograma, fue basado en el libro de 
        Macroeconomía de Rudirger Dornbush, Stanley Fischer y Richard Startz, especialmente en los capitulos 10, 11 y 12 de la  12va edición.''')
        st.markdown('''En la parte derecha podrás encontrar la "sintexis" matemática del modelo,
        para después, en la parte inferior, entrar a la parte interactiva, donde podrás entrar los parámetros de un modelo IS-LM estático. Y
        obtener como resultado la gráfica del equilibrio de mercado. Tambien podras realizar desplazamientos de las curvas con la opción Desplazamiento, además  del planteamiento del modelo y  el procedimiento con la opción Ejecutar.''')
        st.download_button('Descarga el libro guía','./book.pdf','Macroeconomia_DFS.pdf')
        st.markdown(f'''Accede a esta lista de reproducción de youtube de la [Universidad de 
        Valladolid](https://www.youtube.com/watch?v=BgbQB3jRxOI&list=PLSbo9kXA_Lcx5baMlEVo4s60RODjZiwsW) para acceder a un curso sobre IS-LM.
        ''')
       
    ##PROCEDIMIENTO GENERAL 
    with rightcol1:
        with open('equation.txt','r') as f:
            results1 = [line for line in f]
        st.markdown('**MERCADO DE DINERO Y LA RECTA LM**')
        st.write('Tenemos la forma de la ecuación de demanda de dinero:')
        st.latex(results1[0])
        st.write('''El mercado de dinero debe estar en equilibrio, por lo tanto la oferta monetaria 
                real es igual a la demanda de dinero:''')
        st.latex(results1[1])
        st.write('De forma general, se obtiene igualando ambas L, y despejando para YR:')
        st.latex(results1[2])
        st.markdown('**DEMANDA AGREGADA Y LA RECTA IS**')
        st.write('''Sabemos de forma general que la Demanda Agregada de una economia 
                tiene ciertos componenetes autonomos que se expresan en la siguiente ecuación:''')
        st.latex(results1[3])
        st.write('''Cuando el mercado está en equilibrio, es decir, cuando
            la demanda agregada DA es igual al nivel de renta Y, se obtiene la recta IS a partir
                de la siguiente expresión:''')
        st.latex(results1[4])
        st.markdown('**EQUILIBRIO IS-LM**')
        st.write('Se igualan las rectas IS y LM, de forma general:')
        st.latex(results1[5])
        st.write('Despejando se obtiene el nivel de renta de equilibrio:')
        st.latex(results1[6])
        st.write('Y ahora se pasa el nivel de renta a las rectas IS o LM:')
        st.latex(results1[7])

    st.markdown("""---""")
    ##BODY OF INTERACTIVE PART
    options = option_menu(None, ["Parámetros", "Gráfica","Procedimiento"], 
        icons=['list', 'graph-up','check2-square'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    st.markdown("""---""")
    
    data = {'Oferta Monetaria':400, 'Nivel de Precios':1, 'Sensibilidad a la Renta':1,
                                    'Sensibilidad al tipo de interes':1, 'Pmg':0.8, 'Tasa Impositiva':0.2,
                                    'Sensibilidad de la inversion':1, 'Consumo Autonomo':0,'Impuesto Autonomo':0,
                        'Inversión Autonoma':0,'Trasnferencias':0,'Gasto':0,'Exportaciones Netas':0}
    feactures = pd.DataFrame(data,index=['Parameters'])
    Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp = tuple(feactures.loc['Parameters'])
    ##ENTRADA DE PARAMTROS
    if options == 'Parámetros':
            
        st.markdown("***Entrada de Parámetros***")
        leftcola,leftcolb,rightcola,rightcolb = st.columns(4)
        with leftcola:
            st.write('')
            kp = st.number_input('Sensldad.-Renta (k)',0,10000,1)
            hp = st.number_input('Sensldad.-t_rinteres (h)',0,10000,1)
            Mp = st.number_input('Oferta Monetaria (M)',0,10000,400)
            Pp = st.number_input('Nivel de Precios (P)',0,10000,1)
            
        with leftcolb:
            st.write('---')
            Trp = st.number_input('Transferencias (Tr)',0,10000,0)
            st.write('')
            Gp = st.number_input('Gasto (G)',0,10000,1000)
            st.write('')
            NXp = st.number_input('Export. Netas (NX)',0,10000,0)
            
        with rightcola:
            st.write('---')
            Cap = st.number_input('Cons. Autonomo (Ca)',0,10000,0)
            st.write('')
            Tap = st.number_input('Impuesto Autonomo (Ta)',0,10000,0)
            st.write('')
            Iap = st.number_input('Interes Autonomo (Ia)',0,10000,0)  
        with rightcolb:
            st.write('---')
            cp = st.number_input('Prop. al consumo (c)',min_value=float(0), max_value=float(1),value=0.8,step=0.01)
            st.write('')
            tp = st.number_input('Tasa Impositiva (t)',min_value=float(0), max_value=float(1),value=0.2,step=0.01)
            st.write('')
            bp = st.number_input('Senbldad.-inversion (b)',0,10000,1)
            
        data = {'Oferta Monetaria':round(Mp,2), 'Nivel de Precios':round(Pp,2), 'Sensibilidad a la Renta':round(kp,2),
                                    'Sensibilidad al tipo de interes':round(hp,2), 'Pmg':round(cp,2), 'Tasa Impositiva':round(tp,2),
                                    'Sensibilidad de la inversion':round(bp,2), 'Consumo Autonomo':round(Cap,2),'Impuesto Autonomo':round(Tap,2),
                        'Inversión Autonoma':round(Iap,2),'Trasnferencias':round(Trp,2),'Gasto':round(Gp,2),'Exportaciones Netas':round(NXp,2)}
        feactures = pd.DataFrame(data,index=['Parameters'])
        Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp = tuple(feactures.loc['Parameters'])
            
        st.write('')
        desplazamiento = st.checkbox('Desplazamiento')
        ##CODIGO SI ELIGE DESPLAZAMIENTOS EN EL MODELO
        if desplazamiento:
            ### CODIGO DE DESPLAZAMIENTO:
            pass

    

    ##REALIZACIÓN DELA GRAFICA
    if options == 'Grafica':
        plt, xresults = ISLMProcess.graficar(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
        st.subheader('Grafica de Equilibrio de Mercado')
        st.pyplot(plt)
        st.markdown('''La gráfica muestra el punto de equilibrio/intercepción entre 
        ambos mercados, es decir de las rectas IS-LM. Dando el nivel de renta de equilibrio y la 
        tasa de interes de equilibrio''')

    
    if options == 'Procedimiento':
        tab1, tab2 = st.tabs(["Modelo","Procedimiento"])
        tab1.subheader('Parametros Configurados')
        equations = ISLMProcess.get_description(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
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