import math
theta_d1 = 0.1
theta_d2 = 0.2
px1 = 0.5
px2 = 0.5
x1 = [1,2]
x2 = [3,4]
x1f = [5,6]
x2f = [7,8]
ex_pdata = math.log(1/(1+math.exp(-(theta_d1*x1[0]-theta_d2*x1[1]-2))))*px1 +\
           math.log(1/(1+math.exp(-(theta_d1*x2[0]-theta_d2*x2[1]-2))))*px2
ez_pzdata = math.log(1-1/(1+math.exp(-(theta_d1*x1f[0]-theta_d2*x1f[1]-2))))*px1 +\
           math.log(1-1/(1+math.exp(-(theta_d1*x2f[0]-theta_d2*x2f[1]-2))))*px2
V_dg = ex_pdata+ez_pzdata
print ex_pdata,ez_pzdata,V_dg