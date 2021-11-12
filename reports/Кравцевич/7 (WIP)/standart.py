import PIL
import math
import imageio


# task 1
def diagonal_multi():
	x = [[1, 0, 1],
		 [2, 0, 2],
		 [3, 0, 3],
		 [4, 4, 4]]

	prod = 1
	diagonal = [x[i][i] for i in range(min(len(x), len(x[0]))) if x[i][i] != 0]
	for x in diagonal:
		prod *= x
	print(prod)


# task 2
def get_subvector():
	x = [[9, 4, 2], [6, 0, 0], [9, 9, 3]]
	i = [1, 2, 1]
	j = [1, 0, 1]

	print([x[i[index]][j[index]] for index in range(len(i))])


# task 3
def multi():
	x = [1, 2, 2, 4]
	y = [4, 2, 1, 2]
	print(x.sort() == y.sort())


# task 4
def custom_max_element():
	x = [6, 2, 0, 3, 0, 0, 5, 7, 0]

	print(max([x[i] for i in range(1, len(x)) if x[i - 1] == 0]))


# task 5
def image_processing():
	img = imageio.imread('1.png')
	coefs = [0.299, 0.587, 0.114]
	# print(img)
	re_img = []
	for line in img:
		new_line = []
		for pixel in line:
			pixel = [*pixel[:-1]]
			pixel = [pixel[i] * coefs[i] for i in range(len(pixel))]
			new_line.append(sum(pixel))
		re_img.append(new_line)
	imageio.imsave('py_processing.png', re_img)


# task 6
def run_len_encoding():
	x = [2, 2, 2, 3, 3, 5]
	values = list(set(x))
	counts = [x.count(value) for value in values]
	print([values, counts])


# task 7
def euclidean_matrix():
	x = [2, 7, 6, 6, 9, 6, 3, 4, 9]
	y = [1, 0, 0, 7, 2, 2, 4, 3, 0]
	print(math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))])))


if __name__ == '__main__':
	euclidean_matrix()
