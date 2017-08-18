import os
import numpy as np
import shutil

np.random.seed(2016)

root_train = '/Users/pengpai/Desktop/python/DeepLearning/Kaggle/NCFM/data/train_split'
root_val = '/Users/pengpai/Desktop/python/DeepLearning/Kaggle/NCFM/data/val_split'

root_total = '/Users/pengpai/Desktop/python/DeepLearning/Kaggle/NCFM/data/train'

FishNames = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']

nbr_train_samples = 0
nbr_val_samples = 0

# Training proportion
split_proportion = 0.8

for fish in FishNames:
    if fish not in os.listdir(root_train):
        os.mkdir(os.path.join(root_train, fish))
#http://www.cnblogs.com/niocai/p/3351587.html   
#http://www.runoob.com/python/att-string-join.html
#http://www.cnblogs.com/luhouxiang/archive/2012/05/22/2514081.html
    total_images = os.listdir(os.path.join(root_total, fish))

    nbr_train = int(len(total_images) * split_proportion)
#http://www.runoob.com/python/func-number-shuffle.html
    np.random.shuffle(total_images)
#range   http://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html

    train_images = total_images[:nbr_train]

    val_images = total_images[nbr_train:]

    for img in train_images:
        source = os.path.join(root_total, fish, img)
        target = os.path.join(root_train, fish, img)
    #http://blog.csdn.net/xmnathan/article/details/36217631
        shutil.copy(source, target)
        nbr_train_samples += 1

    if fish not in os.listdir(root_val):
        os.mkdir(os.path.join(root_val, fish))

    for img in val_images:
        source = os.path.join(root_total, fish, img)
        target = os.path.join(root_val, fish, img)
        shutil.copy(source, target)
        nbr_val_samples += 1

print('Finish splitting train and val images!')
print('# training samples: {}, # val samples: {}'.format(nbr_train_samples, nbr_val_samples))
