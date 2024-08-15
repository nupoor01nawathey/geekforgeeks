# Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. 
# The array is a permutation of size n with one element missing. Return the missing element.

# Examples:
# Input: n = 5, arr[] = [1,2,3,5]
# Output: 4
# Explanation : All the numbers from 1 to 5 are present except 4.

# Input: n = 2, arr[] = [1]
# Output: 2
# Explanation : All the numbers from 1 to 2 are present except 2.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ n ≤ 106
# 1 ≤ arr[i] ≤ 106


# Company Tags
# Flipkart  Morgan Stanley  Accolite  Amazon  Microsoft  D-E-Shaw  Ola Cabs  Payu  Visa  Intuit  Adobe  Cisco  Qualcomm  TCS


def missingNumber(self, n, arr):
    expected_sum = (n * (n+1)) // 2    
    actual_sum = sum(arr)
    return expected_sum - actual_sum


print(missingNumbers(5, [1,2,3,5])) # 4
print(missingNumbers(2, [1]))       # 2



