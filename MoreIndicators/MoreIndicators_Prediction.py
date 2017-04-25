#coding=UTF-8
'''
Created on 2016年12月1日

@author: ZWT
'''
import Initialize
import time
import os
import numpy as np
import csv

import similarity_indicators.CommonNeighbor

import Evaluation_Indicators.AUC

startTime = time.clock()

NetFile = u"Data/Social.csv"
NetName = 'Social'
Auxiliaryfile = u"Data/UserItem.csv"


print("\nLink Prediction start：\n")
TrainFile_Path = 'Data\\'+NetName+'\\Train.txt'
if os.path.exists(TrainFile_Path):
    Train_File = 'Data\\'+NetName+'\\Train.txt'
    Test_File = 'Data\\'+NetName+'\\Test.txt'
    MatrixAdjacency_Train,MatrixAdjacency_Test,MaxNodeNum = Initialize.Init2(Test_File, Train_File)
else:
    MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
    MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)



AuxiliarySet = csv.reader(file(Auxiliaryfile,'rb'))
AuxiliaryData_list = []
Auxiliary_list_A = []
Auxiliary_list_B = []
for line in AuxiliarySet:
    Auxiliary_list_A.append(int(line[1]))
    Auxiliary_list_B.append(int(line[2]))
    AuxiliaryData_list.append([int(line[1]),int(line[2])])
Auxiliary_list_A = set(Auxiliary_list_A)
Auxiliary_list_B = set(Auxiliary_list_B)
MatrixAdjacency_Auxiliary = np.zeros([len(Auxiliary_list_A),len(Auxiliary_list_B)])
for n in range(len(AuxiliaryData_list)):
    i = int(AuxiliaryData_list[n][0]) - 1
    j = int(AuxiliaryData_list[n][1]) - 1
    MatrixAdjacency_Auxiliary[i,j] = 1 
print(MatrixAdjacency_Auxiliary.shape)
Matrix_Auxiliary = np.dot(MatrixAdjacency_Auxiliary,MatrixAdjacency_Auxiliary.T)
print(Matrix_Auxiliary.shape)
Matrix_similarity = similarity_indicators.CommonNeighbor.Cn(MatrixAdjacency_Train)
print(Matrix_similarity.shape)

Param = 0.8
Matrix_similarity = Param * Matrix_similarity + (1 - Param) * Matrix_Auxiliary

Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)



endTime = time.clock()
print("\nRunTime: %f s" % (endTime - startTime))