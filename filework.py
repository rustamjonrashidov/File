a = int(input())
b = int(input())

s = open("002.txt", "a")
s.write(str(a))
s.close()

r = open("003.txt", "a")
r.write(str(b))
r.close()