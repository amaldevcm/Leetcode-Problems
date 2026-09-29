class Solution(object):
    def maxArea(self, height):      
        first = 0
        last = len(height)-1
        result = 0
        water = 0
        
        while( first < last ):
            water = min(height[first], height[last]) * (last - first)
            if(water > result):
                result = water
            
            if(height[first] > height[last]):
                last -= 1
            else:
                first += 1
                
        return result


if __name__ == "__main__":
    height = list(map(int, input("Enter heights separated by spaces: ").split()))
    solution = Solution()
    print(solution.maxArea(height))


