import mahotas as B
from mahotas import imresize as A
import numpy as C
def D():B=C.repeat(C.arange(100),10).reshape((100,10));assert A(B,(1024,104)).shape==(1024,104);assert A(B,(10.0,10.0)).shape==(1000,100);assert A(B,0.2).shape==(20,2);assert A(B,(10.0,2.0)).shape==(1000,20)
def E():C=B.demos.load('lena');A=B.resize.resize_rgb_to(C,[256,256]);assert A.shape==(256,256,3);A=A.max(2);A=B.resize.resize_to(A,[512,256]);assert A.shape==(512,256)