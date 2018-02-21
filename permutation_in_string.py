from collections import Counter
class Solution():
	def checkInclusion(self, s1, s2):
		A = [ord(x) - ord('a') for x in s1]
		B = [ord(x) - ord('a') for x in s2]

		target = [0]*26
		for x in A:
			target[x]+=1

		window = [0]*26
		for i, x in enumerate(B):
			window[x]+=1
			if i >= len(A):
				window[B[i-len(A)]]-=1
			if window == target:
				return True
		return False
## Basically to keep track of the count of characters in substrings of s2 by offsetting that of s1. Beat 94% upon submission.
	def checkInclusion2(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""

		if not s1: return True
		if len(s2) < len(s1): return False

		m, n, a = len(s1), len(s2), ord('a')
		count = [0]*26
		for c in range(0, m):
			count[ord(s1[c]) - a]+=1
			count[ord(s2[c]) - a]-=1
		for i in range(m, n):
			if not any(count):
				return True
			count[ord(s2[i-m])-a]+=1
			count[ord(s2[i])-a]-=1
		return not any(count)


	def checkInclusion3(self, s1, s2):
		start, end, window_size = 0, 0, len(s1)
		count = Counter(s1)
		while end < len(s2):
			if s2[end] in count:
				count[s2[end]]-=1
			if end - start + 1 > window_size:
				if s2[start] in count:
					count[s2[start]]+=1
				start+=1
			if not list(filter(lambda x:x>0, count.values())):
				return True
			end+=1
		return False
    
## using dictionary to store the sliding window
    def checkInclusion4(self, s1, s2):
         """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        '''
        chack to see if s2 has permutation of string s1
        
        
        Algo:
        
        Need to use a sliding window of length the size of s1 in s2
        everytime, we enter the loop, check if the composition of s1 and that of the sliding window in s2 is same
        
        Main logic is to efficiently navigate throught that sliding window in s2, using the length of s1
        '''
        
        # Make dictionary for s1 with the counts
        
        dict_s1 = {}
        for char in s1:
            dict_s1[char] = dict_s1.get(char,0) + 1
        
        # BUt in the case of s2 , make the dictionary only upto the window size i.e len(s1)
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        dict_s2 = {}
        for char in s2[:len_s1]:
            dict_s2[char] = dict_s2.get(char,0) + 1
        
        
        # Now we need to go into the loop to check the freq of chars matches in s1 and the window size in s2
        # We move from left to right
        # As a char from the left is removed, -- by decrementing the count of that particular char in dict_s2, we can pop out the char from dict
        # Then a char from right is to be added to the dictionary --- as index in enumerate starts from 0
        
        for index,char in enumerate(s2):
            # everytime in the loop check if freq of chars in s1 and the <window in s2> is the same
            if (dict_s1 == dict_s2):
                return True
            
            #As we have already visited the char, decrement the count in dict_s2
            dict_s2[char] -= 1
            
            # Check if the desired window size can be fit in s2
            if (index+len_s1 < len_s2):
                if (dict_s2[char] == 0):
                    dict_s2.pop(char)
                #
                next_char = s2[index+len_s1]
                dict_s2[next_char] = dict_s2.get(next_char,0) + 1
        
        #Everything tried and nothing matches
        return False


	def checkInclusion5(self, s1, s2):
		return len(self.minWindow(s2, s1)) == len(s1)

    ###76. Minimum Window Substring
	def minWindow(self, s, t):
		need, missing = collections.Counter(t), len(t)
		i = I = J = 0
		for j, c in enumerate(s, 1):
			missing-=need[c]>0
			need[c]-=1
			if not missing:
				while i < j and need[s[i]]<0:
					need[s[i]]+=1
					i+=1
				if not J or j-i<=J-I:
					I, J = i, j
		return s[I:J]

if __name__=="__main__":
	s1 = "ab" 
	s2 = "eidbaooo"
	print(Solution().checkInclusion2(s1,s2))
	print(Solution().checkInclusion3(s1,s2))