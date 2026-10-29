class Solution:

    def encode(self, strs: List[str]) -> str:
        final_output=''
        for word in strs:
            final_output=final_output+str(len(word))+'#'+word
        return final_output

    def decode(self, s: str) -> List[str]:
        print(s)
        res=[]
        i=0
        word=''
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            print(s[i-1:j+1])
            length=int(s[i:j])
            start_of_word=j+1
            end_of_word=start_of_word+length
            res.append(s[start_of_word:end_of_word])
            i=end_of_word
  
        return res
            

