class Lagrange:
   
    def funcion(self, x, y, xi):
        n = len(x)
        yinterp = []
        for i in range(len(xi)):
            L = 0.
            for j in range(n):
                m = 0
                lj = 1.
                while m < n:
                    if m != j:
                        lj *= (xi[i] - x[m])/(x[j]-x[m])
                    m += 1
                L +=y[j]*lj
            yinterp.append(L)
        return (yinterp)