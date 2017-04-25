#coding=UTF-8
'''
Created on 2016年12月2日

@author: ZWT
'''
import Initialize
from Evaluation_Indicators import AUC

import MySQLdb
import numpy as np

SocialFile = u"Data/Social/Train.txt"
TestFile = u"Data/Social/Test.txt"
UserItemFile = u"Data/UserItem.csv"



Social_Data = np.loadtxt(SocialFile,delimiter=',')
Test_Data = np.loadtxt(TestFile,delimiter=',')
UserItem_Data = np.loadtxt(UserItemFile,delimiter=',',usecols = (1,2))

print "Social_Data's is Shape :"+str(Social_Data.shape)
print "Test_Data's is Shape :"+str(Test_Data.shape)
print "UserItem_Data's is Shape :"+str(UserItem_Data.shape)
print '\n'

MatrixAdjacency_Social,MaxNode_Social = Initialize.Initialize_Social(Social_Data)
MatrixAdjacency_Test = Initialize.Initialize_Test(Test_Data, MaxNode_Social)
MatrixAdjacency_UserItem = Initialize.Initialize_UserItem(UserItem_Data)
print 'MatrixAdjacency_Social'
print MatrixAdjacency_Social
print 'MatrixAdjacency_Test'
print MatrixAdjacency_Test
print 'MatrixAdjacency_UserItem'
print MatrixAdjacency_UserItem


T_MatrixAdjacency_UserItem = MatrixAdjacency_UserItem.T
array_Degree_User = sum(T_MatrixAdjacency_UserItem)
MatrixDegree_User = np.diag(array_Degree_User)
INV_MatrixDegree_User = np.linalg.inv(MatrixDegree_User)

array_Degree_Item = sum(MatrixAdjacency_UserItem)
MatrixDegree_Item = np.diag(array_Degree_Item)
INV_MatrixDegree_Item = np.linalg.inv(MatrixDegree_Item)

# MatrixNet_UserItem = np.dot(np.dot(np.dot(MatrixAdjacency_UserItem,INV_MatrixDegree_Item),T_MatrixAdjacency_UserItem),INV_MatrixDegree_User)

m1 = np.dot(MatrixAdjacency_UserItem,INV_MatrixDegree_Item)
m2 = np.dot(T_MatrixAdjacency_UserItem,INV_MatrixDegree_User)
MatrixNet_UserItem = np.dot(m1,m2)

print " \nW1:"
print "MatrixNet_UserItem's is Shape :"+str(MatrixNet_UserItem.shape)
print MatrixNet_UserItem




array_Degree_Social = sum(MatrixAdjacency_Social)
MatrixDegree_Social = np.diag(array_Degree_Social)
INV_MatrixDegree_Social = np.linalg.inv(MatrixDegree_Social)

# MatrixNet_Social = np.dot(np.dot(np.dot(MatrixAdjacency_Social,INV_MatrixDegree_Social),MatrixAdjacency_Social),INV_MatrixDegree_Social)

n1 = np.dot(MatrixAdjacency_Social,INV_MatrixDegree_Social)
MatrixNet_Social = np.dot(n1,n1)
print " \nW2:"
print "MatrixNet_Social's is Shape :"+str(MatrixNet_Social.shape)
print MatrixNet_Social


Params = 0.0
while Params < 1.01:
    print '*********'
    print '\nParams is '+str(Params)
    MatrixNet = Params * MatrixNet_UserItem + (1 - Params) * MatrixNet_Social
    Matrix = np.dot(MatrixNet,MatrixAdjacency_Social)
    print '\nSim:'
    print "MatrixNet's Shape is :"+str(Matrix.shape)
    print Matrix[0]
    print np.argsort(-Matrix)[0]
    
    
    AUC.Calculation_AUC(MatrixAdjacency_Social, MatrixAdjacency_Test, Matrix, MaxNode_Social)
    
    Params += 0.1


