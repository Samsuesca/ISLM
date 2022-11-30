import numpy as np
import matplotlib.pyplot as plt



def LM(M,P,k,h):
  i = np.linspace(0,10,num=100)
  M_P = M/P 
  Y = M_P/k + (h*i)/k #RECTA LM

def IS(c,t,r,Ca=0,Ta=0,Ia=0,G=0,Tr=0,NX=0):
  i = np.linspace(0,10,num=100)
  A = Ca + Ia + G + NX + c*Tr - c*Tr
  Y = (A-r*i)/(1-c*(1-t)) # RECTA IS

def ISLM(M,P,k,h,c,t,b,Ca=0,Ta=0,Ia=0,Tr=0,G=0,NX=0):
  i = np.linspace(0,10000000)
  M_P = M/P 
  Y1 = M_P/k + (h*i)/k
  A = Ca + Ia + G + NX + c*Tr - c*Ta
  Y2 = (A-b*i)/(1-c*(1-t))
  C = np.array([[k,-h],[1-c*(1-t),b]])
  B = np.array([[M_P],[A]])
  X = np.linalg.inv(C).dot(B)
  P1 = plt.plot(i, Y1)
  P2 = plt.plot(i, Y2)
  plt.xlim(0,float(X[1]) + 3)
  plt.ylim(0,int(X[0]+100))
  plt.xlabel('Interest Rate')
  plt.ylabel('Total Output')
  plt.title('IS-LM Model')  
  plt.show()
  return P1,P2,X
