class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s = list()
        for ch in s:
            list_s.append(ch)
        #list_s = re.split('( )', s)
        #list_s = [s.split("")]
        for ch in t:
            if ch in list_s:
                list_s.remove(ch)
            else:
                return False
        return True
        