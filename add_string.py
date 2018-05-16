class Solution():

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

	def addString(self, nums1, nums2):
		nums1, nums2 = list(nums1), list(nums2)
		carry, res = 0, []
		while len(nums2)>0 or len(nums1)>0:
			n1 = ord(nums1.pop()) - ord('0') if len(nums1)>0 else 0
			n2 = ord(nums2.pop()) - ord('0') if len(nums2)>0 else 0

			temp = n1 + n2 + carry
			res.append(temp % 10)
			carry = temp//10
		if carry:
			res.append(carry)
		return ''.join([str(i) for i in res])[::-1]


