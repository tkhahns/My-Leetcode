class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            i += "]"
            out += i
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        a = ""
        for i in s:
            if i != "]":
                a += i
            else:
                out.append(a)
                a = ""
                continue
        return out
