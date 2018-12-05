from itertool import permutations
import sys

n = int (sys.argv[1])

def check_equality(combo = None, clos=None, n_queens=None):

    #for each index i in the columns, finds the row value of that index and adds 1 to it
    results_1 = list()
    for i in cols:
        res = combo[i]+i
        results_1.append(res)

    #calculates length of the unique values from the previous step
    val1 = len(set(results_1))

    #for each index i in the columns, finds the row value of that index and subtracts 1 from it
    results_2 = list()
    for i in cols:
    res = combo[i]-i
    results_2.append(res)

    val2 = len(set(results_2))

    #checks if all values are check_equal
    if val1 == val2m == num_queens:
        return True
    else:
        return False

  
