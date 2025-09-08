'''
    Merge sort is a divide and conquer algorithm.
    follows divide and conqure paradigm 
        divide      -   Divide the array into 2 subarrays
        Conqure     -   no need as cobiner(merge) will do its job
        Combine     -   Combine(merge) the divided subarrays


'''

import csv
import ast 

def mergearr(arr, l1,h1,l2,h2):
    i = l1
    j = l2
    mer = []
    while(i<=h1 and j<=h2):
        if arr[i]<arr[j]:
            mer.append(arr[i])
            i+=1
        elif arr[i]==arr[j]:
            mer.append(arr[i])
            mer.append(arr[j])
            i+=1
            j+=1
        else:
            mer.append(arr[j])
            j+=1
    
    while i<=h1:
        mer.append(arr[i])
        i+=1

    while j <= h2:
        mer.append(arr[j])
        j+=1

    for k in range(len(mer)):
        arr[l1+k] = mer[k]
    

def merge_sort(arr, l,h):
    if l>=h:
        return

    mid = (l+h)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,h)
    mergearr(arr,l,mid,mid+1,h)



def run_csv_tests(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        k = 0
        for row in reader:
            k+=1
            input_arr = ast.literal_eval(row['InputArray'])
            expected = ast.literal_eval(row['ExpectedOutput'])
            if input_arr:  # Avoid calling merge_sort on empty list
                merge_sort(input_arr, 0, len(input_arr)-1)
            result = input_arr
            count += 1 if result == expected else 0
            print(f"Test {row['TestCaseID']}: {'PASS' if result == expected else 'FAIL'}")
            print(f" Input: {row['InputArray']}")
            print(f" Output: {result}")
            print(f" Expected: {expected}\n")

    print(f'Test case passed : {count}/{k}')

# Run tests
run_csv_tests("merge_sort_test_cases_extended.csv")
