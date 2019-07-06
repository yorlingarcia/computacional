from numpy import zeros, array

fun = []
fun.append('y[0]+2')
fun.append('y[1]+4')
funx = 'y[0]+1'
print(type(funx),funx)
y = array(zeros((2,1)),float)
for i in range(len(fun)):
    y[i] = i+1
    funeval = str(fun[i])
    print(y[i],funeval)
    print(eval(funeval))
