import sympy as sp

def to_symp(lista):
    result = sp.sympify(str(lista[0])) ##convert a solution of a sympify object (intermediate computations)
    return result

class Equation(sp.Eq):
    def solve(self, i):
        sol = to_symp(sp.solve(self,i))
        return sol
    def solution_equals(self, i,eq):
        sol = sp.Eq(eq,to_symp(sp.solve(self,i)))
        return sol 