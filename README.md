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
###矩阵交换行与列
方法1
```
c=np.eye(3)
c
Out: 
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
c[[0,2],:]=c[[2,0],:]       #交换第一行与第三行，c[:,[1,2]]=c[:,[2,1]]则是交换第二列与第三列
c
Out: 
array([[ 0.,  0.,  1.],
       [ 0.,  1.,  0.],
       [ 1.,  0.,  0.]])
```
方法2：交换行与列等同于左乘或右乘一个矩阵
```
d=np.array([1,2,1,3,8,1,0,4,1]).reshape(3,3)
e=c=np.array([0,1,0,1,0,0,0,0,1]).reshape(3,3)
d
Out: 
array([[1, 2, 1],
       [3, 8, 1],
       [0, 4, 1]])
e
Out: 
array([[0, 1, 0],
       [1, 0, 0],
       [0, 0, 1]])
d.dot(e)
Out: 
array([[2, 1, 1],
       [8, 3, 1],
       [4, 0, 1]])
e.dot(d)
Out: 
array([[3, 8, 1],
       [1, 2, 1],
       [0, 4, 1]])
```
###矩阵某一行（列）乘以一个数字后再加到另一行上：也能转化为左乘或者右乘一个矩阵
```
a=np.eye(3)
a[0,1]=-3
b=np.array([1,2,1,3,8,1,0,4,1]).reshape(3,3)
Mul_b_a=b.dot(a)
b1=b.copy()
b1[:,1]=b1[:,0]*(-3)+b1[:,1]

a
Out: 
array([[ 1., -3.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
b
Out: 
array([[1, 2, 1],
       [3, 8, 1],
       [0, 4, 1]])
Mul_b_a
Out: 
array([[ 1., -1.,  1.],
       [ 3., -1.,  1.],
       [ 0.,  4.,  1.]])
b1
Out: 
array([[ 1, -1,  1],
       [ 3, -1,  1],
       [ 0,  4,  1]])
```
