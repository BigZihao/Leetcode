

# 86 / 86 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# 84.03%
#Just like the Lomuto partition algorithm usually used in quick sort. 
#We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s 
#sorted in place for [0,k). Here ")" means exclusive. 
#We don't need to swap because we know the values we want.


## two pointer

def sortColors(self, nums):
    i = j = 0
    for k in xrange(len(nums)):
        tmp = nums[k]
        nums[k] = 2
        if tmp < 2:
            nums[j] = 1
            j += 1
        if tmp == 0:
            nums[i] = 0
            i += 1



This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. If the white pointer is blue, we swap with the latest unclassified element.

def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1
    
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1