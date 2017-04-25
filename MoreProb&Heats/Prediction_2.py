#coding=UTF-8
'''
Created on 2016��12��7��

@author: ZWT
'''
import Initialize
from Evaluation_Indicators import AUC

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
# print 'MatrixAdjacency_Social'
# print MatrixAdjacency_Social
# print 'MatrixAdjacency_Test'
# print MatrixAdjacency_Test
# print 'MatrixAdjacency_UserItem'
# print MatrixAdjacency_UserItem

print "\nStart………………………………"
Param_Q = 0.0

while Param_Q <1.01:
    
    array_Degree_Social = sum(MatrixAdjacency_Social)
    #### INV_Degree_Social 为 Ds^-1 INV_Degree_Social_Q 为(Ds^-1)^q    INV_Degree_Social_Qsub 为(Ds^-1)^(1-q)
#     MatrixDegree_Social = np.diag(array_Degree_Social)
#     INV_Degree_Social = np.linalg.inv(MatrixDegree_Social)
    MatrixDegree_Social_Q = np.diag(array_Degree_Social ** Param_Q)
    INV_Degree_Social_Q = np.linalg.inv(MatrixDegree_Social_Q)
    MatrixDegree_Social_Qsub = np.diag(array_Degree_Social ** (1 - Param_Q))
    INV_Degree_Social_Qsub = np.linalg.inv(MatrixDegree_Social_Qsub)

    
    T_MatrixAdjacency_UserItem = MatrixAdjacency_UserItem.T
    array_Degree_User = sum(T_MatrixAdjacency_UserItem)
    #### INV_Degree_User 为Du^-1    INV_Degree_Uesr_Q 为(Du^-1)^q    INV_Degree_User_Qsub 为(Du^-1)^(1-q)
    MatrixDegree_User = np.diag(array_Degree_User)
    INV_Degree_User = np.linalg.inv(MatrixDegree_User)
    MatrixDegree_User_Q = np.diag(array_Degree_User ** Param_Q)
    INV_Degree_User_Q = np.linalg.inv(MatrixDegree_User_Q)
    MatrixDegree_User_Qsub = np.diag(array_Degree_User ** (1 - Param_Q))
    INV_Degree_User_Qsub = np.linalg.inv(MatrixDegree_User_Qsub)
    
    array_Degree_Item = sum(MatrixAdjacency_UserItem)
    #### INV_Degree_Item 为Di^-1    INV_Degree_Item_Q 为(Di^-1)^q    INV_Degree_Item_Qsub 为(Di^-1)^(1-q)
    MatrixDegree_Item = np.diag(array_Degree_Item)
    INV_Degree_Item = np.linalg.inv(MatrixDegree_Item)
    MatrixDegree_Item_Q = np.diag(array_Degree_Item ** Param_Q)
    INV_Degree_Item_Q = np.linalg.inv(MatrixDegree_Item_Q)
    MatrixDegree_Item_Qsub = np.diag(array_Degree_Item ** (1 - Param_Q))
    INV_Degree_Item_Qsub = np.linalg.inv(MatrixDegree_Item_Qsub)
    
    
    # W1 = (Ds^-1)^(1-q) * S * (Ds^-1)^q * (Du^-1)^(1-q) * A * (Di^-1) * B * (Du^-1)^q
    MatrixNet_W1 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(INV_Degree_Social_Qsub,MatrixAdjacency_Social),INV_Degree_Social_Q),INV_Degree_User_Qsub),MatrixAdjacency_UserItem),INV_Degree_Item),T_MatrixAdjacency_UserItem),INV_Degree_User_Q) 
    
    print " \nW1:"
    print "MatrixNet_W1's is Shape :"+str(MatrixNet_W1.shape)
#     print MatrixNet_W1
    
    # W2 = (Du^-1)^(1-q) * A * (Di^-1) * B * (Du^-1)^q * (Ds^-1)^(1-q) * S * (Ds^-1)^q
    MatrixNet_W2 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(INV_Degree_User_Qsub,MatrixAdjacency_UserItem),INV_Degree_Item),T_MatrixAdjacency_UserItem),INV_Degree_User_Q),INV_Degree_Social_Qsub),MatrixAdjacency_Social),INV_Degree_Social_Q)
    print " \nW2:"
    print "MatrixNet_W2's is Shape :"+str(MatrixNet_W2.shape)
#     print MatrixNet_W2
    
    
    Param_P = 0.0
    while Param_P < 1.01:
        print '*********'
        print 'Param_Q is '+str(Param_Q)
        print '    Param_P is '+str(Param_P)
        
        MatrixNet = Param_P * MatrixNet_W1 + (1 - Param_P) * MatrixNet_W2
        Matrix = np.dot(MatrixNet,MatrixAdjacency_Social)
#         print "Matrix's Shape is :"+str(Matrix.shape)
#         print Matrix[0]
#         print np.argsort(-Matrix)[0]
        
        
        AUC.Calculation_AUC(MatrixAdjacency_Social, MatrixAdjacency_Test, Matrix, MaxNode_Social)
        
        Param_P += 0.1
        
    Param_Q += 0.1