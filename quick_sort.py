def swap(lyst,i,j):
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] = temp



def quicksort(lyst):
	quicklySortHelper(lyst,0,len(lyst)-1)

def quicklySortHelper(lyst,left,right):
	if left < right:
		pivotLocation = partition(lyst, left, right)
		quicklySortHelper(lyst, left, pivotLocation - 1)
		quicklySortHelper(lyst, pivotLocation + 1, right)


def partition(lyst,left,right):
	#find middle pivot and exchange
	middle = (left+right) // 2
	pivot = lyst[middle]
	lyst[middle] = lyst[right]	
	lyst[right] = lyst[middle]
	
	#set bounddry to first pisition
	boundary = left
	
	#move items less than picot to the left
	for index in range(left,right):
		if lyst[index] < lyst[right]:
			swap(lyst,index,boundary)
			boundary += 1
	
	#exchange the pivot item and the boundary item
	swap(lyst,right,boundary)
	return boundary
	
import random

def main(size =20,sort = quicksort):
	lyst = []
	for count in range(size):
		lyst.append(random.randint(1,size+1))
	
	print(lyst)
	sort(lyst)
	print(lyst)

if __name__ == '__main__':
	main()
			
		
		
		
		
