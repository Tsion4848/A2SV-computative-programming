class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        comment = False
        modified = ''

        for line in source:
            i = 0
            while i < len(line):
                if i + 1 == len(line):
                    if not comment:
                        modified += line[i]
                    i += 1
                    break
                twoChars = line[i:i + 2]
                if twoChars == '/*' and not comment:
                    comment = True
                    i += 2
                elif twoChars == '*/' and comment:
                    comment = False
                    i += 2
                elif twoChars == '//':
                    if not comment:
                        break
                    else:
                        i += 2
                else:
                    if not comment:
                        modified += line[i]
                    i += 1
            if modified and not comment:
                res.append(modified)
                modified = ''

        return res