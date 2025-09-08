#https://leetcode.com/problems/merge-similar-items/

#Brute Force Solution
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = items1 + items2
        print(ret)
        i = 0
        j = 0
        while i < len(ret) - 1:
            j = 0
            while j < len(ret) - i - 1:
                if ret[j][0] > ret[j+1][0]:
                    temp = ret[j]
                    ret[j] = ret[j+1]
                    ret[j+1] = temp
                if ret[j][0] == ret[j+1][0]:
                    ret[j][1] += ret[j+1][1]
                    ret.remove(ret[j+1])
                else:
                    j += 1
            i += 1
        return ret
    
#Better Solution
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        agg = defaultdict(int)
        for v, w in items1:
            agg[v] += w
        for v, w in items2:
            agg[v] += w
        return [[v, agg[v]] for v in sorted(agg)]

"""
Notes/Realizations
Brute Force Solution
 - When working with arrays of changing size, use while statements and dont increment forward if an element was removed or added to ensure positions aren't skipped.
 - Bubble sort works by comparing an element and it's successor, and "bubbling" the greater number upward until the largest number is found, and brought to the end of the array.
    :for i in range(len(array) - 1):
        for j in range(len(array) - i - 1): ---> This - i is because as we "bubble" the greatest number to the end, it's considered a sorted section of the array, so -i ensures j doesn't touch it again.

Better Solution
 - Trying to access a key that doesnt exist dict[key] will result in a KeyError
    :In order to populate a dictionary with this key:value format in mind, set dictionary = defaultdict(type) ---> defaultdict is the keyword from the collections library, and int is the data type of default keys
 - Sorted function in python can be used to sort a dictionary by its keys if they're int values
"""