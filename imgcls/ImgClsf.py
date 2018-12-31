import cv2
import os
import imageio
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
def reshape(matrix):
    flaggy=[]
    for i in range(0,127):
        for j in range(0,127):
            for k in range(0,3):
                troo=matrix[i,j,k]
                flaggy.append(troo)
    return flaggy
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
print("Please enter the number of distinguishing classifications (it should be between 2-5) i.e. number of folders")
classif= int(input())
if(classif>1):
    classific1=load_images_from_folder("classif1")
    classific2=load_images_from_folder("classif2")
if (classif>2):
    classific3=load_images_from_folder("classif3")
if(classif>3):
    classific4=load_images_from_folder("classif4")
if(classif==5):
    classific5=load_images_from_folder("classif5")
n1=len(classific1)
n2=len(classific2)
if(classif>2):
    n3=len(classific3)
if(classif>3):
    n4=len(classific4)
if(classif==5):
    n5=len(classific5)
#creal=0
#for kl in range(0,n1):
#    classificationt[kl]=classific1[creal]
#    creal=creal+1
#c1=0
#for kz in range(n1,n2+n1):
#    classificationst[kz]=classific2[c1]
#    c1=c1+1
#c2=0
#if(classif>2):
#    for kz in range(n1+n2),n1+n2+n3):
#            classificationst[kz]=classific3[c2]
#            c2=c2+1
#c3=0
#if(classif>3):
#    for kz in range(n1+n2+n3,n1+n2+n3+n4):
#        classificationst[kz]=classific3[c3]
#        c3=c3+1
#c4=0
#if(classif>4):
#    for kz in range(len(classific2)+len(classific1)+len(classific3)+len(classific4),len(classific2)+len(classific1)+len(classific3)+len(classific4)+len(classific5)):
#       classificationst[kz]=classific3[c4]
#        c4=c4+1
classificationst=classific1+classific2
if(classif>2):
    classificationst=classificationst+classif3
if(classif>3):
    classificationst=classificationst+classif4
if(classif>4):
    classificationst=classificationst+classif5
features=[]
for i in range(0,len(classificationst)):
    t=reshape(classificationst[i])
    features.append(t)
lis1=[]
lis2=[]
lis3=[]
lis4=[]
lis5=[]
for io in range(0,n1):
    lis1.append(1)
for ip in range(0,n2):
    lis2.append(2)
if(classif>2):
    for ia in range(0,n3):
        lis3.append(3)
if(classif>3):
    for id in range(0,n4):
        lis4.append(4)
if(classif>4):
    for ig in range(0,n5):
        lis5.append(5)
labels=lis1+lis2
if(classif>2):
    labels=labels+lis3
if(classif>3):
    labels=labels+lis4
if(classif>4):
    labels=labels+lis5
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
testmatrix=imageio.imread(str(sys.argv[1]))
listinput=reshape(testmatrix)
x=clf.predict([listinput])
print("The test image belongs to class number:")
print(x)
