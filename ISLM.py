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
        self.MPeq = ut.Equation(L,M_/P_)
        self.LM = ut.Equation(self.MPeq.rhs,self.Leq.rhs).solution_equals(Y,Y).evalf(3)
        self.Aeq = ut.Equation(A,Ca_ + Ia_ + G_ + NX_ + c_*(Tr_ - Ta_))
        self.LS = ut.Equation(Y,(self.Aeq.rhs-b_*i)/(1-c_*(1-t_)))
        self.iequ = ut.Equation(self.LM.rhs,self.LS.rhs)
        self.ieq = self.iequ.solution_equals(i,i)
        self.yeq = ut.Equation(Y,self.LS.subs(i,self.ieq.rhs).rhs)
        eq = [self.Leq,self.MPeq,self.LM,self.Aeq,self.LS,self.iequ,self.ieq,self.yeq]
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
        Leq = sp.Eq(L,k*Y-h*i)
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

    def graficar(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX):
        i = np.linspace(0,1000000)
        M_P = M/P 
        Y1 = M_P/k + (h*i)/k
        A = Ca + Ia + G + NX + c*Tr - c*Ta
        Y2 = (A-b*i)/(1-c*(1-t))
        C = np.array([[k,-h],[1-c*(1-t),b]])
        B = np.array([[M_P],[A]])
        X = np.linalg.inv(C).dot(B)
        fig, ax = plt.subplots()
        ax.plot(i, Y1)
        ax.plot(i,Y2)
        ax.set_xlim(0,float(X[1]) + 3)
        ax.set_ylim(0,int(X[0]+100))
        ax.set_xlabel('Interest Rate')
        ax.set_ylabel('Total Output')
        ax.set_title('IS-LM Model')  
        return fig, pd.DataFrame(X,index=['Nivel de Renta','Tasa de Interes'],columns=['Equilibrio Economía'])


if __name__ == '__main__':
    with open('ISLM/equation.txt','w') as f:
        for i in ISLMProcess().make_procces():
            f.write(i)
            f.write('\n')