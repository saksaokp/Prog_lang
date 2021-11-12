import math
import numpy as np
import imageio
from scipy.spatial.distance import euclidean


# task 1
def diagonal_multi():
	x = np.array(
		[[1, 0, 1],
		 [2, 0, 2],
		 [3, 0, 3],
		 [4, 4, 4]])
	print(x.diagonal()[x.diagonal() != 0].prod())


# task 2
def get_subvector():
	x = np.array([[9, 4, 2], [6, 0, 0], [9, 9, 3]])
	i = np.array([1, 2, 1])
	j = np.array([1, 0, 1])

	print(x[i, j])


# task 3
def multi():
	x = np.array([1, 2, 2, 4])
	y = np.array([4, 2, 1, 2])
	x.sort()
	y.sort()
	print(all(x == y))


# task 4
def custom_max_element():
	x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
	print(x[1:][(x == 0)[:-1]].max())


# task 5
def image_processing():
	img = imageio.imread('1.png')
	coefs = [0.299, 0.587, 0.114]
	reshaped_image = img[:, :, :-1]  # trim last chanal
	new_img = reshaped_image * (([[coefs] * reshaped_image.shape[1]]) * reshaped_image.shape[0])  # use coefs

	print(new_img.sum(axis=2))
	imageio.imsave('test.png', new_img.sum(axis=2))  # sum all colors


# task 6
def run_len_encoding():
	x = np.array([2, 2, 2, 3, 3, 5])
	print(np.unique(np.array(x), return_counts=True))


# task 7
def euclidean_matrix():
	x = np.array([2, 7, 6, 6, 9, 6, 3, 4, 9])
	y = np.array([1, 0, 0, 7, 2, 2, 4, 3, 0])
	print(math.sqrt(((x - y) ** 2).sum()))
	print(np.linalg.norm(x - y))
	print(euclidean(x, y))


if __name__ == '__main__':
	image_processing()
