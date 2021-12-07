import numpy as np


# Part 1
data = np.loadtxt('data.csv')

def get_number_of_times_count_increased(data):
    increased_counter = 0
    for i in range(len(data)-1):
        if data[i+1]>data[i]:
            increased_counter +=1
    return increased_counter

data = np.loadtxt('data.csv')
increased_counter = get_number_of_times_count_increased(data)
print(f'{increased_counter} of times is the number larger than before')

# Part II
window_size = 3

window_sums = []
for i in range(len(data) - window_size + 1):
    print(data[i: i + window_size])
    window_sum = np.sum(data[i: i+window_size])
    print(window_sum)
    
    window_sums.append(window_sum)

increased_counter_window = get_number_of_times_count_increased(window_sums)
print(f'{increased_counter_window} of times is the number larger than before')
    
