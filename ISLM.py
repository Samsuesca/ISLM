import sympy as sp
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
from PIL import Image
from Utils import utils_sp as ut

#Definir Simbolos del modelo
M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX,L,Y,DA,I,T,C,A,i,Yd = sp.symbols('M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX,L,Y,DA,I,T,C,A,i,Yd')

        
#Clase del modelo
class ISLMProcess:

    def __init__(self):

        self.Leq = None
        self.MPeq = None
        self.LM = None
        self.Aeq = None
        self.LS = None
        self.iequ = None
        self.yeq = None
        self.ieq = None 
    
    #agregar parametros
    def parameters(leftcola,leftcolb,rightcola,rightcolb):

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
        
        return feactures.loc['Parameters']

    #agregar deplazamientos
    def deltas(leftcola,leftcolb,rightcola,rightcolb):
        with leftcola:
            st.write('')
            Dkp = st.number_input('Delta (k)',-10000,10000,0)
            Dhp = st.number_input('Delta (h)',-10000,10000,0)
            DMp = st.number_input('Delta (M)',-100000,100000,0)
            DPp = st.number_input('Delta (P)',-100000,100000,0)
            
        with leftcolb:
            st.write('---')
            DTrp = st.number_input('Delta (Tr)',-100000,100000,0)
            st.write('')
            DGp = st.number_input('Delta (G)',-100000,100000,0)
            st.write('')
            DNXp = st.number_input('Delta (NX)',-100000,10000,0)
            
        with rightcola:
            st.write('---')
            DCap = st.number_input('Delta (Ca)',-100000,100000,0)
            st.write('')
            DTap = st.number_input('Delta (Ta)',-100000,100000,0)
            st.write('')
            DIap = st.number_input('Delta (Ia)',-100000,100000,0)  

        with rightcolb:
            st.write('---')
            Dcp = st.number_input('Delta (c)',min_value=float(-1), max_value=float(1),value=float(0),step=0.01)
            st.write('')
            Dtp = st.number_input('Delta (t)',min_value=float(-1), max_value=float(1),value=float(0),step=0.01)
            st.write('')
            Dbp = st.number_input('Delta (b)',-10000,10000,0)
            
        Ddata = {'Oferta Monetaria':round(DMp,2), 'Nivel de Precios':round(DPp,2), 'Sensibilidad a la Renta':round(Dkp,2),
                                    'Sensibilidad al tipo de interes':round(Dhp,2), 'Pmg':round(Dcp,2), 'Tasa Impositiva':round(Dtp,2),
                                    'Sensibilidad de la inversion':round(Dbp,2), 'Consumo Autonomo':round(DCap,2),'Impuesto Autonomo':round(DTap,2),
                        'Inversión Autonoma':round(DIap,2),'Trasnferencias':round(DTrp,2),'Gasto':round(DGp,2),'Exportaciones Netas':round(DNXp,2)}
        Dfeactures = pd.DataFrame(Ddata,index=['Parameters'])
        return Dfeactures.loc['Parameters']


    #Print de image definition
    def img_definition():
        image = Image.open('islm.jpg')
        return image

    #Obtener procedimiento general
    def make_procces(self):

        self.Leq = ut.Equation(L,k*Y-h*i)
        self.MPeq = ut.Equation(L,M/P)
        self.LM = ut.Equation(self.MPeq.rhs,self.Leq.rhs).solution_equals(Y,Y)
        self.Aeq = ut.Equation(A,Ca + Ia + G + NX + c*(Tr - Ta))
        self.LS = ut.Equation(Y,(self.Aeq.lhs-b*i)/(1-c*(1-t)))
        self.iequ = ut.Equation(self.LM.rhs,self.LS.rhs)
        self.ieq = self.iequ.solution_equals(i,i)
        self.yeq = ut.Equation(Y,self.LS.subs(i,self.ieq.rhs).rhs)
        eq = [self.Leq,self.MPeq,self.LM,self.Aeq,self.LS,self.iequ,self.ieq,self.yeq]
        return [sp.latex(e) for e in eq]

    #Realizar un ejercicio dado los parametros
    def make_exercise(self,M_,P_,k_,h_,c_,t_,b_,Ca_,Ta_,Ia_,Tr_,G_,NX_):
        self.Leq = ut.Equation(L,k_*Y-h_*i)
        self.MPeq = ut.Equation(M/P,M_/P_)
        inter = ut.Equation(self.Leq.rhs,self.MPeq.rhs).evalf(3)
        self.LM = ut.Equation(self.MPeq.rhs,self.Leq.rhs).solution_equals(Y,Y).evalf(3)
        self.Aeq = ut.Equation(A,Ca_ + Ia_ + G_ + NX_ + c_*(Tr_ - Ta_)).evalf(3)
        self.LS = ut.Equation(Y,(self.Aeq.rhs-b_*i)/(1-c_*(1-t_))).evalf(3)
        self.iequ = ut.Equation(self.LM.rhs,self.LS.rhs)
        self.ieq = self.iequ.solution_equals(i,i).evalf(3)
        self.yeq = ut.Equation(Y,self.LS.subs(i,self.ieq.rhs).rhs).evalf(3)
        eq = [self.Leq,self.MPeq,inter,self.LM,self.Aeq,self.LS,self.iequ,self.ieq,self.yeq]
        return [sp.latex(e) for e in eq]

    #Realiza desplazamiento de mercados por cambios de factores
    def desplazamiento(self,M_,P_,k_,h_,c_,t_,b_,Ca_,Ta_,Ia_,Tr_,G_,NX_):
        self.Leq0 = ut.Equation(L,k_*Y-h_*i)
        self.MPeq0 = ut.Equation(L,M_/P_)
        self.LM0 = ut.Equation(self.MPeq0.rhs,self.Leq0.rhs).solution_equals(Y,Y).evalf(3)
        self.Aeq0 = ut.Equation(A,Ca_ + Ia_ + G_ + NX_ + c_*Tr_ - c_*Ta_)
        self.LS0 = ut.Equation(Y,(self.Aeq0.rhs-b_*i)/(1-c_*(1-t_)))
        self.iequ0 = ut.Equation(self.LM0.rhs,self.LS0.rhs)
        self.ieq0 = self.iequ0.solution_equals(i,i)
        self.yeq0 = ut.Equation(Y,self.LS0.subs(i,self.ieq0.rhs).rhs)
        eq = [self.Leq0,self.MPeq0,self.LM0,self.Aeq0,self.LS0,self.iequ0,self.ieq0,self.yeq0]
        return [sp.latex(e) for e in eq]

    #DESCRIPCIÓN DEL MODELO
    def get_description(M_,P_,k_,h_,c_,t_,b_,Ca_,Ta_,Ia_,Tr_,G_,NX_):
    ## get the equations of the model
        Leq = sp.Eq(L,k_*Y-h_*i)
        M_a = sp.Eq(M,M_)
        Peq = sp.Eq(P,P_)
        Treq = sp.Eq(Tr,Tr_)
        Geq = sp.Eq(G,G_)
        NXeq = sp.Eq(NX,NX_)
        Teq = sp.Eq(T,Ta_ + t_*Y)
        Yd_ = Y - Teq.rhs + Tr_
        Ydeq = sp.Eq(Yd,Yd_)
        Ceq = sp.Eq(C,Ca_+c_*Yd_)
        Ieq = sp.Eq(I,Ia_-b_*i)
        list = [Leq,M_a,Peq,Treq,Geq,NXeq,Teq,Ydeq,Ceq,Ieq]
        return [sp.latex(i) for i in list]


    #GRAFICOS
    def graficar(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX,
                DM,DP,Dk,Dh,Dc,Dt,Db,DCa,DTa,DIa,DTr,DG,DNX):

        #entradas normales - rectas 

        plt.rcParams.update({'font.size': 22})
        i = np.linspace(0,10000)
        M_P = M/P 
        Y1 = M_P/k + (h*i)/k
        A = Ca + Ia + G + NX + c*Tr - c*Ta 
        Y2 = (A-b*i)/(1-c*(1-t))
        C = np.array([[k,-h],[1-c*(1-t),b]])
        B = np.array([[M_P],[A]])
        X = np.linalg.inv(C).dot(B)
        i1 = np.linspace(0,X[0]*k/h+100)
        Y = np.linspace(0,X[0]+X[0]*0.3)

        #deltas: son la configuración de los desplazamientos
        deltasIS = np.array([Dc,Dt,Db,DCa,DTa,DIa,DTr,DG,DNX])
        deltasLM = np.array([DM,DP,Dk,Dh])
        DM_P = (DM+M)/(DP+P) 
        DY1 = (DM_P+M_P)/(Dk+k) + (Dh+h)*(i)/(Dk+k)
        D_A =  (Ia+ DIa)+(G+DG) + (DNX+NX)+ (c*Tr+Dc*DTr) - (Dc*DTa+c*Ta)+(DCa+Ca)
        DY2 = (D_A+A-Db*i-b*i)/(1-(Dc+c)*(1-(Dt+t)))
        DC = np.array([[(Dk+k),-(Dh+h)],[1-(c+Dc)*(1-(t+Dt)),(Db+b)]])
        DB = np.array([[(DM_P+P)],[(A+D_A)]])
        DX = np.linalg.inv(DC).dot(DB)
        Di1 = np.linspace(0,DX[0]*(Dk+k)/(h+Dh)+100)
        DY = np.linspace(0,DX[0]+DX[0]*0.3)

        ##grafica equilibrio mercado

        fig1, ax = plt.subplots(figsize=(10, 8))
        ax.plot(i, Y1)
        ax.plot(i,Y2)
        ax.set_xlim(0,float(X[1]) + X[1]*0.2)
        ax.set_ylim(0,int(X[0]+X[0]*0.2))
        ax.set_xlabel('Tasa de Interés')
        ax.set_ylabel('Producto Total')
        ax.set_title('EQUILIBRIO IS-LM') 
        
        if np.any(deltasIS != 0):
            ax.plot(i,DY2)
           
            if np.any(deltasLM != 0):
                ax.plot(i,DY1)
                ax.legend(['IS-1', 'LM-1','IS-2','LM-2'])
            else:
                ax.legend(['IS-1', 'LM-1','IS-2'])
        
        elif np.any(deltasLM != 0):
            ax.plot(i,DY1)
            ax.legend(['IS-1', 'LM-1','LM-2'])
        
        else:
            ax.legend(['IS-1', 'LM-1'])

        ##grafica IS

        fig2, ax2 = plt.subplots(figsize=(10, 8))
        ax2.plot(Y,A+c*(1-t)*Y-b*X[1])
        
        ax2.plot(Y,Y)
        ax2.legend(['Producto Total', 'Demanda Agregada = Y'])
        ax2.set_xlabel('Y')
        ax2.set_ylabel('Demanda Agregada')
        ax2.set_xlim(0,float(X[0]) + X[0]*0.2)
        ax2.set_ylim(0,int(X[0]+X[0]*0.2))

        ##grafica LM

        fig3, ax3 = plt.subplots(figsize=(10, 8))
        ax3.plot(k*X[0]-h*i1,i1)
        mp = np.array([M_P for i in range(len(i1))])
        ax3.plot(mp,i1)
        ax3.legend(['Demanda de Dinero', 'Oferta de Dinero'])
        ax3.set_xlabel('Dinero')
        ax3.set_ylabel('Tasa de Interes')
        ax3.set_xlim(0,M_P + M_P*0.2)
        ax3.set_ylim(0,int(X[0]+X[0]*0.2))
        
        #pd.DataFrame(X,index=['Nivel de Renta','Tasa de Interes'],columns=['Equilibrio Economía'])
        return fig1,fig2,fig3


if __name__ == '__main__':
    with open('ISLM/equation.txt','w') as f:
        for i in ISLMProcess().make_procces():
            f.write(i)
            f.write('\n')