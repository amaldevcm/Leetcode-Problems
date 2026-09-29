class Solution(object):
    def reverseWords(self, s):
        temp = []
        result = ''
        
        for i in s.split(' '):
            if(i != ''):
                temp.append(i)
        print(temp)
        for i in temp[::-1]:
            result += i+' '

        return result[:len(result)-1]


if __name__ == "__main__":
    sentence = input()
    print(Solution().reverseWords(sentence))