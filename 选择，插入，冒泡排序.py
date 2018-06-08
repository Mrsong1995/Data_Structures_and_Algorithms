#交换元素
def swap(lyst,i,j):
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] =temp 



#选择排序
def selectionSort(lyst):
	i = 0
	while i< len(lyst) -1:
		minIndex = i
		j = i+1
		while j<len(lyst):
			if lyst[j] < lyst[minIndex]:
				minIndex = j
			j += 1
			
		if minIndex != i:
			swap(lyst,minIndex,i)
		i +=1


#冒泡排序
def bubbleSort(lyst):
	n = len(lyst)
	while n > 1:
		i = 1
		while i<n:
			if lyst[i] < lyst[i-1]:
				swap(lyst,i,i-1)
			i += 1
		n -= 1
		
def bubbleSort2(L):
	for i in range(len(L)-1):
		for j in range(len(L)-i-1):
			if L[j] > L[j+1]:
				swap(L,j,j+1)
				
		

#插入排序
def insertionSort(lyst):
	i = 1
	while i< len(lyst):
		itemToInsert = lyst[i]
		j = i-1
		while j >= 0:
			if itemToInsert < lyst[j]:
				lyst[j+1] = lyst[j]
				j -=1
			else:
				break
		lyst[j+1] = itemToInsert
		i += 1
		
				
				
				 





