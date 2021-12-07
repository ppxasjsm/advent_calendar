import numpy as np


def get_binary_array_count(array):
    print(array)
    zeros = np.count_nonzero(array == 0)
    ones = np.count_nonzero(array == 1)
    binary_counts = {'zeros':zeros,'ones':ones}

    return binary_counts


def compute_rates(report_data):

    gamma = ''
    epsilon = ''
    array_shape = np.shape(report_data)
    for i in range(array_shape[1]):
        binary_count = get_binary_array_count(report_data[:,i])
        if binary_count['ones'] > binary_count['zeros']:
            gamma = gamma+'1'
            epsilon = epsilon+'0'
        else:
            gamma = gamma+'0'
            epsilon = epsilon+'1'
    print('gammae is {gamma}')
    print ('epsilon is {epsilon}')
    print(f'gamma as integer is {int(gamma, 2)}')
    print(f'epsilon as integer is {int(epsilon, 2)}')
    multiplied = int(gamma, 2)*int(epsilon, 2)
    print(f'muliplied rates: {multiplied}')


if __name__ == '__main__':

    f = open('data.txt')
    lines = f.readlines()
    f.close()

    line_list = []
    for line in lines:
        line = line.strip()
        binary_string = []
        for digit in line:
            binary_string.append(int(digit))
        binary_string = np.array(binary_string)
        line_list.append(binary_string)
    line_list = np.array(line_list)
    compute_rates(line_list)


