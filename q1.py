#!/usr/bin/env python

inversion = 0

def merge(left, right):
	global inversion
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			inversion += len(left) - i
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def mergesort(lst):
	if len(lst) <= 1:
		return lst
	mid = int(len(lst) / 2)
	left = mergesort(lst[:mid])
	right = mergesort(lst[mid:])
	return merge(left, right)

if __name__ == "__main__":
    mergesort([int(x) for x in open('IntegerArray.txt')])
    print inversion
    