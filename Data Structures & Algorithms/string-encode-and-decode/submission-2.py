class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for ele in strs:
            out = out + str(len(ele)) + '#' + ele 
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        index = 0
        while index < len(s):
            sep_pos = s.find('#', index)
            length = int(s[index:sep_pos])
            strin = s[sep_pos+1:sep_pos+1+length]
            out.append(strin)
            index = sep_pos+1+length
        return out
