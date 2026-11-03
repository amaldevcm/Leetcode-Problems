class Solution:
    def minSwapsToSort(self, arr):
        ones_seen = 0
        zeros_seen = 0
        swaps_zeros_first = 0
        swaps_ones_first = 0

        for value in arr:
            if value == 0:
                swaps_zeros_first += ones_seen
                zeros_seen += 1
            else:
                swaps_ones_first += zeros_seen
                ones_seen += 1

        return min(swaps_zeros_first, swaps_ones_first)

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    solution = Solution()
    print(f'output: {solution.minSwapsToSort(arr)}')