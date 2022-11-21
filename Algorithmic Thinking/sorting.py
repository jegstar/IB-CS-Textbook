from random import randint
def makeRandom(length):
    return [randint(1,length) for _ in range(length) ]

def bubble(lst):
    swapped = True
    end = len(lst) - 1
    while swapped:
        swapped = False
        for i in range(1, end):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                swapped = True

def selection(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):

            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]


def insertion(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        index = i - 1
        while item < lst[index] and index >= 0:
            lst[index+1] = lst[index]
            index -= 1
        lst[index+1] = item


def merge(left, right):
    l = r = 0
    output = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    
    output += left[l:]
    output += right[r:]
    return output

def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

import time


lst = makeRandom(10000)
start = time.time()

print(start)

lst = selection(lst)

print(time.time()- start)