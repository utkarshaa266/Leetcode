class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            # Elements just before and after the partition
            if cut1 == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[cut1 - 1]

            if cut2 == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[cut2 - 1]

            if cut1 == m:
                right1 = float('inf')
            else:
                right1 = nums1[cut1]

            if cut2 == n:
                right2 = float('inf')
            else:
                right2 = nums2[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even number of elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # nums1 partition is too far right
            elif left1 > right2:
                right = cut1 - 1

            # nums1 partition is too far left
            else:
                left = cut1 + 1