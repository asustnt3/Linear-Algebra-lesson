# Linear-Algebra-lesson
##矩阵基本运算
###提取矩阵的行与列
考虑两个矩阵
```
M1=np.arange(24).reshape(4,6)
M2=np.arange(30,0,-1).reshape(6,5)
M1
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
M2
array([[30, 29, 28, 27, 26],
       [25, 24, 23, 22, 21],
       [20, 19, 18, 17, 16],
       [15, 14, 13, 12, 11],
       [10,  9,  8,  7,  6],
       [ 5,  4,  3,  2,  1]])
for i in range(M1.shape[0]):
       print('row', i, ':', M1[i])
for i in range(M1.shape[1]):
       print('column', i, ':', M1[:,i])
```
###矩阵相乘 Matrix Multiplication
方法1
```
M1.dot(M2)
```
方法2：M1的每一列与M2的每一行相乘得出一个矩阵，再把这些矩阵相加
```
Mul1=np.zeros([M1.shape[0],M2.shape[1]])
for i in range(M1.shape[1]):
       Mul1+=M1[:,i].reshape(M1.shape[0],1).dot(M2[i].reshape(1,-1))
```
ps:对于reshape的原因
```
M1[0,:]
Out: 
array([0, 1, 2, 3, 4, 5])
M1[:,0].reshape(1,-1)
Out: 
array([[ 0,  6, 12, 18]])
M1[:,0].reshape(4,1)
Out: 
array([[ 0],
       [ 6],
       [12],
       [18]])
```
方法3：M1的每一列与M2的每一行相乘得出一个数字，再合并为一个矩阵
```
Mul2=[M1[i].reshape(1,-1).dot(M2[:,j].reshape(M2.shape[0],1)).item() for i in range(M1.shape[0]) for j in range(M2.shape[1])]
```
