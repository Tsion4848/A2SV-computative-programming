class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter1 = [1,2,3,4,5,6,7,8,9]
        num1 = ['a','b','c','d','e','f','g','h','i']
        
        aToz = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
        
        y = ""
        # x = s.split()
        # print(x)
        
#         for i in x:
#             y+=aToz.get(i)
            
#         print('\"' + y + '\"')
        
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                result.append(s[i-2:i])
                i -= 3
            else:
                result.append(s[i])
                i -= 1
        print("".join(reversed(result)))
        
        for i in result[::-1]:
            y+=aToz.get(i)
            
        print('\"' + y + '\"')
        return y