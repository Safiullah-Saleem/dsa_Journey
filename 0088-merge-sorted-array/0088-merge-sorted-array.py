class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Pointer for the last valid element of nums1
        j = n - 1  # Pointer for the last element of nums2
        k = m + n - 1  # Pointer for the last position in nums1 (end of array)

        while j >= 0:  # Keep merging until all elements of nums2 are placed in nums1
            if i >= 0 and nums1[i] > nums2[j]:  
                nums1[k] = nums1[i]  # Move the larger element to nums1[k]
                i -= 1  # Move nums1 pointer left
            else:
                nums1[k] = nums2[j]  # Move the nums2 element to nums1[k]
                j -= 1  # Move nums2 pointer left
            k -= 1  # Move merged array pointer left