#coding=UTF-8
'''
Created on 2016��12��2��

@author: ZWT
'''
import numpy as np

def Initialize_Social(Data_ndarray):
    print 'Data To MatrixAdjacency_Soial ......'
    set_A = set(Data_ndarray[:,0])
    set_B = set(Data_ndarray[:,1])
    if 0 not in set_A:
        if 0 not in set_B:
            length_A = len(set_A)
            maxNode_A = int(max(set_A))
            print "    The first col's node length is :"+str(length_A)
            print "    The first col's max node is :"+str(maxNode_A)
            length_B = len(set_B)
            maxNode_B = int(max(set_B))
            print "    The second col's node length is :"+str(length_B)
            print "    The second col's max node is :"+str(maxNode_B)
            maxNode = int(max(maxNode_A,maxNode_B))
            MatrixAdjacency = np.zeros([maxNode,maxNode])
        
            for row in Data_ndarray:
                i = int(row[0]) - 1
                j = int(row[1]) - 1
                MatrixAdjacency[i,j] = 1
                MatrixAdjacency[j,i] = 1
    else:
        length_A = len(set_A)
        maxNode_A = int(max(set_A))
        print "    The first col's node length is :"+str(length_A)
        print "    The first col's max node is :"+str(maxNode_A)
        length_B = len(set_B)
        maxNode_B = int(max(set_B))
        print "    The second col's node length is :"+str(length_B)
        print "    The second col's max node is :"+str(maxNode_B)
        maxNode = int(max(maxNode_A,maxNode_B)) + 1

        MatrixAdjacency = np.zeros([maxNode,maxNode])
    
        for row in Data_ndarray:
            i = int(row[0])
            j = int(row[1])
            MatrixAdjacency[i,j] = 1
            MatrixAdjacency[j,i] = 1
        
    print "MatrixAdjacency_Social's Shape is :"+str(MatrixAdjacency.shape)
    
    return MatrixAdjacency,maxNode

def Initialize_UserItem(Data_ndarray):
    print 'Data To MatrixAdjacency_UserItem ......'
    set_A = set(Data_ndarray[:,0])
    set_B = set(Data_ndarray[:,1])
    if 0 not in set_A:
        if 0 not in set_B:
            length_A = len(set_A)
            maxNode_A = int(max(set_A))
            print "    The first col's node length is :"+str(length_A)
            print "    The first col's max node is :"+str(maxNode_A)
            length_B = len(set_B)
            maxNode_B = int(max(set_B))
            print "    The second col's node length is :"+str(length_B)
            print "    The second col's max node is :"+str(maxNode_B)
            
            MatrixAdjacency = np.zeros([maxNode_A,maxNode_B])
        
            for row in Data_ndarray:
                i = int(row[0]) - 1
                j = int(row[1]) - 1
                MatrixAdjacency[i,j] = 1
        else:
            length_A = len(set_A)
            maxNode_A = int(max(set_A)) + 1
            print "    The first col's node length is :"+str(length_A)
            print "    The first col's max node is :"+str(maxNode_A)
            length_B = len(set_B)
            maxNode_B = int(max(set_B)) + 1
            print "    The second col's node length is :"+str(length_B)
            print "    The second col's max node is :"+str(maxNode_B)
            
            MatrixAdjacency = np.zeros([maxNode_A,maxNode_B])
        
            for row in Data_ndarray:
                i = int(row[0])
                j = int(row[1])
                MatrixAdjacency[i,j] = 1
    else:
        length_A = len(set_A)
        maxNode_A = int(max(set_A)) + 1
        print "    The first col's node length is :"+str(length_A)
        print "    The first col's max node is :"+str(maxNode_A)
        length_B = len(set_B)
        maxNode_B = int(max(set_B)) + 1
        print "    The second col's node length is :"+str(length_B)
        print "    The second col's max node is :"+str(maxNode_B)
        
        MatrixAdjacency = np.zeros([maxNode_A,maxNode_B])
    
        for row in Data_ndarray:
            i = int(row[0])
            j = int(row[1])
            MatrixAdjacency[i,j] = 1
        
    print "MatrixAdjacency_UserItem's Shape is :"+str(MatrixAdjacency.shape)
    
    return MatrixAdjacency

def Initialize_Test(Data_ndarray,maxNode):
    print 'Data To MatrixAdjacency_Test ......'
    MatrixAdjacency = np.zeros([maxNode,maxNode])
#     
    for row in Data_ndarray:
        i = int(row[0]) - 1
        j = int(row[1]) - 1
        MatrixAdjacency[i,j] = 1
        MatrixAdjacency[j,i] = 1


#     set_A = set(Data_ndarray[:,0])
#     set_B = set(Data_ndarray[:,1])
#     if 0 not in set_A:
#         if 0 not in set_B:
#             for row in Data_ndarray:
#                 i = int(row[0]) - 1
#                 j = int(row[1]) - 1
#                 MatrixAdjacency[i,j] = 1
#                 MatrixAdjacency[j,i] = 1
#     else:
#         for row in Data_ndarray:
#             i = int(row[0])
#             j = int(row[1])
#             MatrixAdjacency[i,j] = 1
#             MatrixAdjacency[j,i] = 1
        
    print "MatrixAdjacency_Test's Shape is :"+str(MatrixAdjacency.shape)
    
    return MatrixAdjacency
    
    