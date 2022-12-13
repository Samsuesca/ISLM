import sympy as sp
import numpy as np
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
    
    def parameters(tab1,coll, colr):
        with coll:
            Gp = tab1.slider('Gasto (G)',0,10000,500)
            cp = tab1.slider('Propensión al consumo (c)',min_value=float(0), max_value=float(1),value=0.8,step=0.01)
            tp = tab1.slider('Tasa Impositiva (t)',min_value=float(0), max_value=float(1),value=0.2,step=0.01)
            bp = tab1.slider('Sensibilidad de la inversion (b)',0,10000,40)
            Trp = tab1.slider('Transferencias (Tr)',0,10000,100)
            Cap = tab1.slider('Consumo Autonomo (Ca)',0,10000,180)
            Tap = tab1.slider('Impuesto Autonomo (Ta)',0,10000,50)
            Iap = tab1.slider('Interes Autonomo (Ia)',0,10000,50)  
            NXp = tab1.slider('Exportaciones Netas (NX)',0,10000,50)
        with colr:
            Mp = tab1.slider('Oferta Monetaria (M)',0,10000,400)
            kp = tab1.slider('Sensibilidad a la Renta (k)',0,10000,4)
            hp = tab1.slider('Sensibilidad al tipo de interes (h)',0,10000,50)
            Pp = tab1.slider('Nivel de Precios (P)',0,10000,1)
        data = {'Oferta Monetaria':round(Mp,2), 'Nivel de Precios':round(Pp,2), 'Sensibilidad a la Renta':round(kp,2),
                                        'Sensibilidad al tipo de interes':round(hp,2), 'Pmg':round(cp,2), 'Tasa Impositiva':round(tp,2),
                                        'Sensibilidad de la inversion':round(bp,2), 'Consumo Autonomo':round(Cap,2),'Impuesto Autonomo':round(Tap,2),
                          'Inversión Autonoma':round(Iap,2),'Trasnferencias':round(Trp,2),'Gasto':round(Gp,2),'Exportaciones Netas':round(NXp,2)}
        feactures = pd.DataFrame(data,index=['Parameters'])
        return feactures

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
        DM_P = DM/DP 
        DY1 = DM_P/Dk + (Dh*i)/Dk
        D_A = DCa + DIa +DG + DNX + Dc*DTr - Dc*DTa 
        DY2 = (D_A-Db*i)/(1-Dc*(1-Dt))
        DC = np.array([[Dk,-Dh],[1-Dc*(1-Dt),Db]])
        DB = np.array([[DM_P],[D_A]])
        DX = np.linalg.inv(DC).dot(DB)
        Di1 = np.linspace(0,DX[0]*Dk/Dh+100)
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