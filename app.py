'''This code uses the streamlit library to create a interactive website that describes
 and demonstrates the IS-LM model in economics. It also imports the pandas, numpy, and 
 sympy libraries to perform mathematical operations and display equations in LaTeX format.
  The code defines the symbols used in the IS-LM model, and displays the mathematical 
  equations and graphs of the model. It also allows the user to input values for the 
  parameters of the model and see the resulting changes in the equilibrium.'''

import streamlit as st
from ISLM import ISLMProcess

def main():
    #CONGIGURACIÓN DEL SITIO 
    st.set_page_config(page_title='Blog Economia',
                    page_icon=':notebook:',
                    layout='wide')

    ## DESCRIPCÓN PRINCIPAL 
    st.markdown("""---""")
    st.title('BLOG:  Modelo IS-LM')
    st.markdown("""---""")
    st.markdown(f'''
        **GENERALIDADES DEL BLOG** \n
        En esta ocasión, tenemos un blog que se enfoca en el modelo IS-LM, uno de los modelos más importantes en la 
        macroeconomía. Este modelo, (Investment-Saving and Liquidity Preference-Money
        Supply) analiza la interacción entre el mercado de bienes y servicios y el mercado
        de dinero en una economía. Este sitio funciona como un infograma interactivo sobre
        el modelo, el cual se trabaja en los primeros cursos de macroeconomia, pues sirve 
        como introducción al análisis macro de una economía.''') 
    st.markdown('''Este infograma, 
        fue basado en el libro de Macroeconomía de Rudirger Dornbush, Stanley Fischer y 
        Richard Startz, especialmente en los capitulos 10, 11 y 12 de la  12va edición. 
        El blog ofrece una breve descripción del modelo y sus fundamentos
        teóricos, así como una explicación detallada de la "síntesis" matemática del modelo. 
        Además, ofrece una sección interactiva donde el usuario puede ingresar valores para
        los parámetros del modelo y observar los cambios en el equilibrio del mercado. 
        También ofrece enlaces a recursos adicionales, como un libro guía y una lista de 
        reproducción de youtube, para que los usuarios puedan profundizar en el tema.
        El blog es una herramienta valiosa para estudiantes y profesionales interesados
        en el modelo IS-LM y su aplicación en la economía.''')
    st.markdown("""---""")
    leftcol1,rightcol1 = st.columns([1.3,1],gap='large')
    with leftcol1:
        st.markdown('''**DESCRIPCIÓN DEL MODELO** \n''')
        st.markdown('''El modelo se basa en la teoría de la demanda y la oferta de dinero y 
        bienes, y se utiliza para examinar de manera general el impacto de las políticas
        monetarias y fiscales en el equilibrio general de la economía. En la siguiente imagen 
        podemos ver una breve definición:
        ''')
        st.image(ISLMProcess.img_definition(),use_column_width='always')
        

    with rightcol1:
        st.markdown('''
        Cómo se explicó previamente, el modelo IS-LM parte del análisis de
        dos mercados: el de bienes y el de dinero, y termina por explicar las principales 
        relaciones entre la política monetaria y la política fiscal. Es así como el modelo IS-LM se 
        compone de dos curvas, la curva IS y la curva LM. La curva IS representa la relación
        entre la tasa de interés y el producto real en el mercado 
        de bienes y servicios. La curva LM representa la relación entre la tasa de interés
        y la cantidad de dinero en el mercado de dinero. El equilibrio del mercado se
        encuentra en el punto de intersección de las dos curvas.''')
        st.write('---')
        st.markdown('''**NAVEGACIÓN EN EL SITIO** \n''')
        st.markdown('''
        En la parte derecha podrás encontrar la "síntesis" matemática del
        modelo, para después, en la parte inferior, entrar a la parte interactiva, donde
        podrás entrar los parámetros de un modelo IS-LM estático. Y obtener como resultado
        la gráfica del equilibrio de mercado. Tambien podras realizar desplazamientos de
        las curvas con la opción Desplazamiento, además  del planteamiento del modelo y rel procedimiento con la opción Ejecutar.''')
        st.write('---')
        st.markdown('''**RECURSOS ADICIONALES** \n''')
        st.download_button('Descarga el libro guía','./book.pdf','Macroeconomia_DFS.pdf')
        st.markdown(f'''Accede a esta lista de reproducción de youtube de la [Universidad 
        de Valladolid](https://www.youtube.com/watch?v=BgbQB3jRxOI&list=PLSbo9kXA_Lcx5baMlEVo4s60RODjZiwsW) 
        para acceder a un curso sobre IS-LM.
        ''')

    st.write('---')
    
    with open('equation.txt','r') as f:
            results1 = [line for line in f]
    leftcol1,rightcol1 = st.columns([1.4,1],gap='large')
    ##PROCEDIMIENTO GENERAL 
    with leftcol1:
        st.markdown('**DEMANDA AGREGADA Y LA CURVA IS**')
        st.markdown('''La curva IS se deriva del equilibrio en el 
        mercado de bienes, y permite mostrar la relación entre la tasa de interés y el nivel de 
        producción. Es así como en una sola curva se puede analizar la cantidad de bienes 
        y servicios que se producen en una economía en función de la tasa de interés. Por ejemplo,
        una tasa de interés más alta conduce a un nivel más bajo de inversión y un nivel más bajo de producción.''')
        st.markdown('''Para la construcción de la curva IS, es necesario utilizar el modelo de Demanda
        Agreagada de la economía, que se puede sintetizar así:''')
        st.markdown(''' - Ecuación de DA: DA = C + I + G + (X-M), donde C es el consumo,
        I es la inversión, G es el gasto gubernamental, X es el ingreso neto de 
        exportaciones y M es el ingreso neto de importaciones; el termino (X-M), puede expresarse
        como XN que significa las exportaciones netas de la economía. En la construcción detallada
        del modelo cada uno de los componentes de la DA tiene un componente autonómo (dado), 
        y tiene otras relaciones, como es el caso del consumo, que depende de los impuestos de 
        la economía y de las transferencias hechas por el estado.
        ''')
        st.write('''Sabemos de forma general que la Demanda Agregada de una economia 
                tiene ciertos componenetes autonomos que se expresan en la siguiente ecuación:''')
        st.latex(results1[3])
        st.write('''Cuando el mercado está en equilibrio, es decir, cuando
        la demanda agregada DA es igual al nivel de renta Y, se obtiene la recta IS a 
        partir de la siguiente expresión:''')
        st.latex(results1[4])
        st.markdown('''Como podemos observar, la pendiente de la curva IS está determinada por
        la propensión marginal a consumir (c), la sensibilidad de la inversión a la (b)
        tasa de interés y la tasa impositiva, mientras que el componente autonómo fija el 
        intercepto de la curva ''')
        
    with rightcol1:
    
        st.markdown('**MERCADO DE DINERO Y LA CURVA LM**')
        st.markdown('''La curva LM representa el mercado de dinero en la economía, asī, muestra 
        la relación entre la tasa de interés y la cantidad demandada de dinero. La teoría económica 
        nos dice que una tasa de interés más alta conduce a una menor demanda de dinero y viceversa.
        La pendiente de la curva LM está determinada por la preferencia de liquidez de los hogares y las 
        empresas, en la cuál, los parametros h y k (sensibilidad de la demanda de dinero a la renta y
        a la tasa de interés respectivamente) son fundamentales para definir la demanda de dinero.
        Ya entrados en el mercado del dinero, podemos introducirnos en la parte 
        matemática de dicho mercado:''')
        st.write('Tenemos la forma de la ecuación de demanda de dinero:')
        st.latex(results1[0])
        st.write('''Para construir la curva LM, el mercado de dinero debe estar en equilibrio, por lo tanto la oferta monetaria 
        (exógena para el modelo) real es igual a la demanda de dinero:''')
        st.latex(results1[1])
        st.write('De forma general, se obtiene igualando ambas L, y despejando para Y:')
        st.latex(results1[2])
        st.markdown('''Podemos ver que la curva LM es creciente, y su pendiente depende de las
        sensibilidades h y k.''')
        st.markdown('''''')
        
    st.markdown("""---""")
    st.markdown('**EQUILIBRIO IS-LM**')
    st.write('Se igualan las rectas IS y LM, de forma general:')
    st.latex(results1[5])
    st.write('Despejando se obtiene el nivel de renta de equilibrio:')
    st.latex(results1[6])
    st.write('Y ahora se pasa el nivel de renta a las rectas IS o LM:')
    st.latex(results1[7])
    ##BODY OF INTERACTIVE PART
    tab1, tab2 = st.tabs(["Entrada de Parámetros","Desplazamiento"])
    
    ##ENTRADA DE PARAMTROS
    with tab1:

        st.markdown("***Entrada de Parámetros***")
        leftcola,leftcolb,rightcola,rightcolb = st.columns(4)
        Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp = ISLMProcess.parameters(leftcola,leftcolb,rightcola,rightcolb)
        
    
        st.write('')

    #CODIGO SI ELIGE DESPLAZAMIENTOS EN EL MODELO
    with tab2:
        st.markdown("***Deltas***")
        leftcola,leftcolb,rightcola,rightcolb = st.columns(4)
        DMp,DPp,Dkp,Dhp,Dcp,Dtp,Dbp,DCap,DTap,DIap,DTrp,DGp,DNXp = ISLMProcess.deltas(leftcola,leftcolb,rightcola,rightcolb)
        st.write('')
 


    ##REALIZACIÓN DELA GRAFICA
    Col1,Col2,Col3 = st.columns([1.3,1.3,2])
    plt, plt1,plt2 = ISLMProcess.graficar(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp,
                            DMp,DPp,Dkp,Dhp,Dcp,Dtp,Dbp,DCap,DTap,DIap,DTrp,DGp,DNXp)
    
    with Col1: 
        st.subheader('Construcción IS')
        st.pyplot(plt1)
        st.markdown('''La gráfica de DA vs Y se muestra cómo cambia la DA cuando
        cambia el nivel de renta total en la economía. Se considera el
        equilibrio en el mercado de bienes DA=Y, es decir una recta que inicia en el origen es
        interceptada por la recta inclinada que representa diferentes valores en 
        las demás variables de la economía.''')

    with Col2:
        st.subheader('Construcción LM')
        st.pyplot(plt2)
        st.markdown('''En la gráfica del mercado de dinero vemos la relación entre la tasa
         de interés y la cantidad de dinero en la economía. Nos muestra cómo 
         cambia la tasa de interés a medida que cambia la cantidad de dinero en una economía. Esto
         se puede producir por cambios en la renta o en la oferta monetaria, asi como en P, h y k''')

    with Col3:
        st.subheader('Equilibrio de Mercado')
        st.pyplot(plt)
        st.markdown('''La gráfica muestra el punto de equilibrio/intercepción entre 
        ambos mercados, es decir de las rectas IS-LM. Dando el nivel de renta de equilibrio y la 
        tasa de interes de equilibrio''')


    ##RESULTADOS EJERCICIO
    tab1, tab2 = st.tabs(["Modelo","Procedimiento"])

    #Parámetros configurados
    tab1.subheader('Parametros Configurados')
    equations = ISLMProcess.get_description(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
    with tab1:
        lc1, rc1 = st.columns([1,1])
        with lc1:
            for i in range(len(equations)-5):
                st.latex(equations[i])
        with rc1:
            for i in range(5,len(equations)):
                st.latex(equations[i])


    #PROCEDIMIENTO
    tab2.subheader('Procedimiento')
    tab2.markdown('Puedes Ejecutar el procedimiento, dando click en el botón')
    if tab2.button('Ejecutar'):
    
        #PROCESO CURVA LM:
        results = ISLMProcess().make_exercise(Mp,Pp,kp,hp,cp,tp,bp,Cap,Tap,Iap,Trp,Gp,NXp)
        tab2.markdown('**Obtener la recta LM**')
        tab2.write('La demanda de dinero, como se vio anteriormente, quedaría:')
        tab2.latex(results[0])
        tab2.write('La oferta real de dinero:')
        tab2.latex(results[1])
        tab2.write('Si igualamos la oferta monetaria real con la demanda de liquidez, es decir:')
        tab2.latex(results[2])
        tab2.write('Despejando para Y,  la siguiente expresión representa la recta LM')
        tab2.latex(results[3])

        #PROCESO CURVA IS:
        tab2.markdown('**Obtener la recta IS**')
        tab2.write('Partiendo del equilibrio del mercado de dinero, es decir DA=Y,r tenemos que el componente autonomo y la recta IS de esta economía son:')
        tab2.latex(results[4])
        tab2.latex(results[5])
        tab2.markdown('**Equilibrio IS-LM**')
        tab2.write('Al igualar las rectas se obtiene:')
        tab2.latex(results[6])
        tab2.write('Si despejamos para Y, se obtiene la renta de equilibrio:')
        tab2.latex(results[7])
        tab2.write('Y por lo tanto una tasa de interes de:')
        tab2.latex(results[8])

    st.markdown("""---""")

if __name__ == '__main__':
    main()