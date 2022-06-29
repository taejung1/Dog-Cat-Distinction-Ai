import tensorflow as tf
import numpy as np
import shutil


from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pylab as plt

#압축파일 위치
file_path = "C:\Users\timki\Desktop\딥러닝\dog-cat/dataset/cat-dog.zip"
data_set = "data/"

#압축파일 압축해제

shutil.unpack_archive(file_path, data_set) 
