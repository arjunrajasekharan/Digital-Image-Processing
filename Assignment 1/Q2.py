import random
#User defined functions

def sums(m, r, c):
    sum_var= 0
    for i in range(r):
        for j in range(c):
            sum_var += int(m[i][j])
    return sum_var

def mean(m, r, c):
    sum_var = 0
    for i in range(r):
        for j in range(c):
            sum_var += int(m[i][j])
    mean = sum_var/(r*c)
    return mean

def maximum(m, r, c):
    test_arr = []
    for i in range(r):
        for j in range(c):
            test_arr.append(int(m[i][j]))
    maxi = max(test_arr)
    return maxi

def median(m, r, c):
    test_arr = []
    for i in range(r):
        for j in range(c):
            test_arr.append(int(m[i][j]))
    new_arr = sorted(test_arr)
    med = new_arr[13]
    return med

def freq_dist(m, r, c):
    test_arr = []
    for i in range(r):
        for j in range(c):
            test_arr.append(m[i][j])
    new_arr = sorted(test_arr)
    freq = {}
    for i in new_arr:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def std_dev(m, r, c):
    sum_var = 0
    for i in range(r):
        for j in range(c):
            sum_var += int(m[i][j])
    mean = sum_var/(r*c)
    std_sum = 0
    test_arr = []
    for i in range(r):
        for j in range(c):
            test_arr.append(int(m[i][j]))
    for k in range(r*c):
        std_sum += (test_arr[k] - mean)**2
    std_dev = (std_sum/(r*c))**0.5
    return std_dev
    
def mode(m, r, c):
    test_arr = []
    for i in range(r):
        for j in range(c):
            test_arr.append(m[i][j])
    new_arr = sorted(test_arr)
    freq = {}
    for i in new_arr:
        if freq.get(i):
            freq[i] += 1
        else:
            freq[i] = 1
    max_freq = 0
    for i in freq:
        if(freq[i] > max_freq):
            max_freq = freq[i]
    print("Mode = ", end="")
    for j in freq:
        if(freq[j] == max_freq):
            print(j,"   ", end="")
    print()
    

#Actual Program
            
matrix = []

rows = int(input("Enter row count:"))
cols = int(input("Enter column count:"))


for i in range(rows):
    var = []
    for j in range(cols):
        var.append(random.randint(0,10))
    matrix.append(var)

print(matrix)

print("Sum = ", sums(matrix, rows, cols))

print("Mean =", mean(matrix, rows, cols))

print("Max =", maximum(matrix, rows, cols))

print("Median =", median(matrix, rows, cols))

print("Frequecy Distribution = ", freq_dist(matrix, rows, cols))

mode(matrix, rows, cols)

print("Std Deviation = ", std_dev(matrix, rows, cols))
