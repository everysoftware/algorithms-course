from functools import lru_cache


class hashTable:
    def __init__(self, q, p):
        self.q = q
        self.p = p
        self.table = {i: None for i in range(q)}

    @lru_cache(None)
    def getHash(self, s):
        result = 0
        p = self.p
        q = self.q
        for i, char in enumerate(s):
            result = (result + (ord(char) - ord("a") + 1) * pow(p, i, q)) % q

        return (result % q + q) % q

    def getFreeHash(self, h):
        newh = h
        i = 0
        q = self.q
        while self.table[newh] != None and self.table[newh][1] != None:
            # Нет свободного ключа
            if i == q - 1:
                return "-1" + str(newh)

            newh = ((newh + 1) % q + q) % q
            i += 1
        return newh

    def getCollisionHash(self, h, key):
        q = self.q
        flag = True
        for i in range(h, q):
            if self.table[i] == None:
                flag = False
                break
            elif self.table[i][0] == key and self.table[i][1] != None:
                return i
        if flag:
            for i in range(h):
                if self.table[i] == None:
                    break
                elif self.table[i][0] == key and self.table[i][1] != None:
                    return i

        return "-1" + str(i)

    def put(self, key, value):
        h = self.getHash(key)
        ch = self.getFreeHash(h)

        if h == ch:
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=PUT",
                "result=inserted",
                "value=" + str(value),
            )
        elif str(ch).startswith("-1"):
            print("key=" + key, "hash=" + str(h), "operation=PUT", "result=overflow")
            return
        else:
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=PUT",
                "result=collision",
                "linear_probing=" + str(ch),
                "value=" + str(value),
            )

        self.table[ch] = (key, value)

    def get(self, key):
        h = self.getHash(key)
        ch = self.getCollisionHash(h, key)

        if self.table[h] == None:
            print("key=" + key, "hash=" + str(h), "operation=GET", "result=no_key")
        elif h == ch:
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=GET",
                "result=found",
                "value=" + str(self.table[h][1]),
            )
        elif str(ch).startswith("-1"):
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=GET",
                "result=collision",
                "linear_probing=" + ch[2:],
                "value=no_key",
            )
        else:
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=GET",
                "result=collision",
                "linear_probing=" + str(ch),
                "value=" + str(self.table[ch][1]),
            )

    def delete(self, key):
        h = self.getHash(key)
        ch = self.getCollisionHash(h, key)

        if self.table[h] == None:
            print("key=" + key, "hash=" + str(h), "operation=DEL", "result=no_key")
        elif h == ch:
            self.table[h] = (self.table[h][0], None)
            print("key=" + key, "hash=" + str(h), "operation=DEL", "result=removed")
        elif str(ch).startswith("-1"):
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=DEL",
                "result=collision",
                "linear_probing=" + str(ch[2:]),
                "value=no_key",
            )
        else:
            self.table[h] = (self.table[h][0], None)
            print(
                "key=" + key,
                "hash=" + str(h),
                "operation=DEL",
                "result=collision",
                "linear_probing=" + str(ch),
                "value=removed",
            )


q, p, n = list(map(int, input().split()))
ht = hashTable(q, p)

for _ in range(n):
    i = input().split()
    if i[0] == "PUT":
        ht.put(i[1], int(i[2]))
    elif i[0] == "GET":
        ht.get(i[1])
    elif i[0] == "DEL":
        ht.delete(i[1])
