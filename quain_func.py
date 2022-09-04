class Quain():
    def solving(self,line):
        s = line.split("+")
        for i in range(len(s)):
            s[i] = s[i].strip().strip("()")
            s[i] = s[i].split("\u00B7")
            for j in range(len(s[i])):
                s[i][j] = s[i][j].strip()

        for i in range(len(s)):
            for k in range(len(s)):
                count = 0
                index = 0
                for j in range(len(s[k])):
                    if s[i][j] == s[k][j] or s[i][j] not in s[k][j]:
                        count += 1
                    else:
                        index = j
                if count == len(s[k])-1:
                    temp = []
                    for i in range(len(s[k])):
                        if i != index:
                            temp.append(s[k][i])
                    s.append(temp)
        dlist = []
        for k in range(len(s)):
            for i in range(len(s)):
                count = 0
                if len(s[k]) < len(s[i]):
                    for j in range(len(s[k])):
                        if s[k][j] in s[i]:
                            count += 1
                    if count == len(s[k]):
                        if dlist.count(s[i]) == 0:
                            dlist.append(s[i])

        for i in range(len(dlist)):
            s.remove(dlist[i])



        result = []
        for i in range(len(s)):
            if result.count(s[i]) == 0:
                result.append(s[i])



        for i in range(len(result)):
            result[i] = "\u00B7".join(result[i])
            result[i] = "("+result[i]+")"
        result = " + ".join(result)

        return result