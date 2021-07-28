import cv2
import glob
import os
files = glob.glob('./chim/*.jpg',  recursive = True)
# files = glob.glob('./shamp/*.txt',  recursive = True)
print(files)
# os.mkdir('./underwear')
filenames = "./chimneys/chimney"
print(files)
count=190
for file in files:
    image = cv2.imread(file)
# image = cv2.imread("./images/00000355.jpg")
# # print(image.shape)
    row , col ,piz= image.shape
    if row >=450 and col >=450:
        filename = filenames+str(count)+'.jpg'
        cv2.imwrite(filename,image)
        # dst = "shaving_brush" + str(count)+ "jpg"
        # src = file
        # dst ='./images' + dst
        # os.rename(src,dst)
        print(file)
        # print(dst)
        count+=1
    pass
# print('hekko')

# # files = glob.glob('./New_folder/*.txt',recursive = True)
# # for file in files:
# #     os.remove(file)
# print('Done')

# rename txt file
# files = glob.glob('./shamp/*.txt',  recursive = True)
# print(files)
# filenames = "./images/shampoo"
# count=1
# for file in files:
#     # filename = filenames+str(count)+'.txt'
#     new_file = os.path.join('./images/', str(count)+".txt")
#     os.rename(file,new_file)
#     count+=

print('done')

