import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from PIL import Image

def definition():
    image = Image.open('islm.jpg')
    return image

def ISLM(M,P,k,h,c,t,b,Ca=0,Ta=0,Ia=0,Tr=0,G=0,NX=0):
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

M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX,L,Y,i,DA,I,T,C = sp.symbols('M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX,L,Y,i,DA,I,T,C')

def to_symp(lista,a=0):
    result = sp.sympify(str(lista[a])) ##convert a solution of a sympify object (intermediate computations)
    return result

def ISLM_get_description(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX):
    ## get the equations of the model
    Leq = sp.Eq(L,k*Y-h*i)
    M_a = sp.Eq(sp.symbols('M_s'),M)
    Peq = sp.Eq(sp.symbols('P^_'),P)
    Treq = sp.Eq(sp.symbols('Tr^_'),Tr)
    Geq = sp.Eq(sp.symbols('G^_'),G)
    NXeq = sp.Eq(sp.symbols('NX^_'),NX)
    Teq = sp.Eq(T,Ta + t*Y)
    Yd = Y - Teq.rhs + Tr
    Ydeq = sp.Eq(sp.symbols('Y_d'),Yd)
    Ceq = sp.Eq(C,Ca+c*Yd)
    Ieq = sp.Eq(I,Ia-b*i)
    list = [Leq,M_a,Peq,Treq,Geq,NXeq,Teq,Ydeq,Ceq,Ieq]
    return [sp.latex(i) for i in list]

def ISLM_deploy(M_,P_,k_,h_,c_,t_,b_,Ca_,Ta_,Ia_,Tr_,G_,NX_): 
    Leq = sp.Eq(L,k*Y-h*i)
    Leq_ = sp.Eq(L,k_*Y-h_*i)
    MPeq = sp.Eq(L,M/P)
    MPeq_ = MPeq.subs(M/P,M_/P_)
    LM = sp.Eq(i,to_symp(sp.solve(sp.Eq(MPeq.rhs,Leq.rhs),i)))
    LM_ = sp.Eq(i,to_symp(sp.solve(sp.Eq(Leq_.rhs,MPeq_.rhs),i))).evalf(3)
    A = sp.Eq(sp.symbols('A'),Ca + Ia + G + NX + c*Tr - c*Ta)
    LS = sp.Eq(i,(A.lhs-(1-c*(1-t))*Y)/b)
    A_ = sp.Eq(sp.symbols('A'),
            A.rhs.subs(Ca,Ca_).subs(Ia,Ia_).subs(NX,NX_).subs(G,G_).subs(c,c_).subs(Tr,Tr_).subs(Ta,Ta_))
    LS_ = sp.Eq(i,LS.subs(sp.symbols('A'),A_.rhs).subs(c,c_).subs(t,t_).subs(b,b_).rhs).evalf(3)
    iequ = sp.Eq(LM.rhs,LS.rhs)
    iequ_ = sp.Eq(LM_.rhs,LS_.rhs)
    yeq = sp.Eq(Y,to_symp(sp.solve(iequ,Y)))
    yeq_ = sp.Eq(Y,to_symp(sp.solve(iequ_,Y)))
    ieq = sp.Eq(i,LS.subs(Y,yeq.rhs).rhs)
    ieq_ = sp.Eq(i,LM_.subs(Y,yeq_.rhs).rhs.evalf(3))
    list = [Leq,Leq_,MPeq,MPeq_,LM,LM_,A,A_,LS,LS_,iequ,iequ_,yeq,yeq_,ieq,ieq_]
    return [sp.latex(i) for i in list]


if __name__ == '__main__':
    ISLM_deploy(M,P,k,h,c,t,b,Ca,Ta,Ia,Tr,G,NX)