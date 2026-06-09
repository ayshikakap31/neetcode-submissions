class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_1 = {}
        if len(strs)<2:
            return [strs]
        else:
            final = []
            for ele in strs:
                ele_sort = sorted(ele)
                out = ''
                for chars in ele_sort:
                    out += chars
                if out in dict_1:
                    dict_1[out].append(ele)
                else:
                    dict_1[out] = [ele]
            for keys in dict_1:
                final.append(dict_1[keys])
            return final
        