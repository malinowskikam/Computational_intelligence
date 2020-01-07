from data import *
import numpy as np


def relu(x):
    if x < 0:
        return 0
    return x


def apply_filter(target_image, filter_to_apply):
    result_image_row_count = (len(target_image)-len(filter_to_apply)+1)
    result_image_col_count = (len(target_image[0])-len(filter_to_apply[0])+1)

    result_image = np.ndarray([result_image_row_count, result_image_col_count])

    for i in range(len(result_image)):
        for j in range(len(result_image)):
            target_slice = target_image[i:i+len(filter_to_apply),j:j+len(filter_to_apply[0])]
            result_image[i][j] = relu(np.sum(target_slice*filter_to_apply))

    return result_image


def pool_max(target_image, x, y):
    assert len(target_image) % y == 0 and len(target_image[0]) % x == 0
    result_image_row_count = int(len(target_image)/y)
    result_image_col_count = int(len(target_image[0])/x)

    result_image = np.ndarray([result_image_row_count, result_image_col_count])

    for i in range(len(result_image)):
        for j in range(len(result_image)):
            target_slice = target_image[2*i:2*i+y,2*j:2*j+x]
            result_image[i][j] = np.max(target_slice)
    return result_image


def neural_network(first_input, second_input):
    return first_input*network[0][0]+second_input*network[1][0], first_input*network[0][1]+second_input*network[1][1]


first_6x6 = apply_filter(image, filters[0])
second_6x6 = apply_filter(image, filters[1])

print(first_6x6)
print(second_6x6)

first_3x3 = pool_max(first_6x6, 2, 2)
second_3x3 = pool_max(second_6x6, 2, 2)

print(first_3x3)
print(second_3x3)

input_1 = apply_filter(first_3x3, filters[2])
input_2 = apply_filter(second_3x3, filters[3])

print(f"{input_1} {input_2}")

print(neural_network(input_1[0][0],input_2[0][0]))
