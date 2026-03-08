class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Step 1: Merge the two arrays
        merged = sorted(nums1 + nums2)
        
        # Step 2: Find the middle index
        n = len(merged)
        mid = n // 2
        
        # Step 3: Return median
        if n % 2 == 0:  # even length
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:           # odd length
            return float(merged[mid])
