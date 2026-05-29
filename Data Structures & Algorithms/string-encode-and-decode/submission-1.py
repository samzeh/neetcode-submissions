class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for s in strs:
            str_length = len(s)
            temp_string = str(len(s)) + "#" + s
            new_string += temp_string
        return new_string

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            j+=1

            word = s[j:j+length]
            result.append(word)    

            i=j+length
    
        return result

