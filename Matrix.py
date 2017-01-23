import numpy as np
M1=np.arange(24).reshape(4,6)
#取行和列
for i in range(M1.shape[0]):
    print('row',i,':',M1[i])
print()
for i in range(M1.shape[1]):
    print('column',i,':',M1[:,i])
#矩阵乘法
M2=np.arange(30,0,-1).reshape(6,5)
#method1:
M1.dot(M2)
#method2:
Mul1=np.zeros([M1.shape[0],M2.shape[1]])
for i in range(M1.shape[1]):
    Mul1+=M1[:,i].reshape(M1.shape[0],1).dot(M2[i].reshape(1,-1))
#method3:
Mul2=[M1[i].reshape(1,-1).dot(M2[:,j].reshape(M2.shape[0],1)).item() for i in range(M1.shape[0]) for j in range(M2.shape[1])]
#乘法性质
a=np.eye(3)
a[0,1]=-3
b=np.array([1,2,1,3,8,1,0,4,1]).reshape(3,3)
Mul_b_a=b.dot(a)
b1=b.copy()
b1[:,1]=b1[:,0]*(-3)+b1[:,1]
#Mul_b_a==b1
#原矩阵b，如果a右乘b，非主对角元素a[i,j]=m,则影响b的列向量：b[:,j]=b[:,i]*m+b[:,j]，对角元素则b[:i]=b[:i]*m
#原矩阵b，如果a左乘b，非主对角元素a[i,j]=m,则影响b的行向量：b[i]=b[j]*m+b[i]，对角元素则b[i]=b[i]*m
#矩阵交换行与列,交换1,2行则c.dot(b),交换1,2列则b.dot(c)
c=np.array([0,1,0,1,0,0,0,0,1]).reshape(3,3)
b.dot(c)
c.dot(b)


