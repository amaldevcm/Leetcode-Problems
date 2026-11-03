class Solution:
    def lowestReliableNode(self, k, m, reliability):
        if(len(reliability) < k):
            return []

        m = min(m, len(reliability))
        result = []

        for i in range(len(reliability) - m + 1):
            window = reliability[i:i + m]
            window.sort()

            result.append(window[k - 1])

        return result

        

if __name__ == "__main__":
    k = int(input("Enter the value of k: "))
    m = int(input("Enter the value of m: "))
    reliability = list(map(int, input("Enter reliability values separated by spaces: ").split()))

    solution = Solution()
    print(solution.lowestReliableNode(k, m, reliability))