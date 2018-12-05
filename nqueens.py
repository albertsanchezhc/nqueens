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

    
