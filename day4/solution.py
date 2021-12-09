import numpy as np


if __name__ == '__main__':
    # r_nums = np.loadtxt('test_rand.txt', delimiter=',')
    f = open('puzzle.dat')
    first_line = f.readline().strip()
    f.close()
    r_nums = np.array(first_line.split(','),dtype='int')

    data = np.loadtxt('puzzle.dat', skiprows=1)
    print(data)
    print(np.shape(data))
    #print(np.shape(data))
    data = data.reshape((100,5,5))
    tracker = np.zeros(np.shape(data))
    print(tracker)
    print(data)

    for r in r_nums:
        print(r)
        coords = np.where(data==r)
        # print(coords)
        tracker[coords] =1

        # print(tracker)
        # for board in data:
        print("tracker sum: ")
        # these are the column sums
        column_sums = np.sum(tracker, axis=1)
        print(np.sum(tracker, axis=1))

        # These are the row sums
        row_sums = np.sum(tracker, axis=2)
        print(np.sum(tracker,axis=2))
        complete_column = np.where(column_sums == 5)
        complete_row = np.where(row_sums == 5)
        print(len(complete_row[0]))
        print(len(complete_column[0]))
        if len(complete_row[0])>0:
            print('Bingo Row')
            print(complete_row[0])
            # compute reminding board sum:
            board = data[complete_row[0]]
            mask = tracker[complete_row[0]]
            print(board)
            print(mask)
            not_found = np.where(mask==0)
            print('======================')
            print(not_found)
            print(np.sum(board[not_found])*r)
            break
        elif len(complete_column[0]) >0:

            print('Bingo in Column')
            board = data[complete_column[0]]
            mask = tracker[complete_column[0]]
            print(board)
            print(mask)
            not_found = np.where(mask==0)
            print('======================')
            print(not_found)
            print(np.sum(board[not_found])*r)
            break

