import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
print(a,b)
print(c)

d = b**2
print(d)

e = np.sin(a)
print(e)

print(b<3)
print(b == 3)
print("*"*50)

c = np.array([[1,1],
             [0,1]])
d = np.arange(4).reshape((2,2))
print(c)
print(d)
a = c*d          ##逐个相乘
a_dot = np.dot(c,d)  ###矩阵乘法
a_dot_2 = c.dot(d)
print(a)
print(a_dot)
print(a_dot_2)

print("#"*40)

f = np.random.random((2,4))
print(f)

print(np.sum(f))
print(np.sum(f,axis = 1))  ##每一行
print(np.min(f))
print(np.min(f,axis = 0))  ##每一列
print(np.max(f))

print("$"*50)

A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))  #最小值索引
print(np.argmax(A))  #最大值索引
print(np.mean(A))  #平均值 也可以用average
print(A.mean())     #平均值
print(np.median(A))  # 中位数
print(np.cumsum(A))  # 累加
print(np.diff(A))  #累差
print(np.sort(A))
print(np.transpose(A)) #矩阵反向
print((A.T).dot(A))

print(np.clip(A,5,9))  #所有小于5的数为5，所有大于9的数为9
print(np.mean(A,axis=0))##对于行或者列计算平均值 axis=0列  axis=1行
