f = open("001.txt", "a")
f.write("sardor")
f.close()

f = open("001.txt", "a")
f.write("\nRustam")
f.close()

k = open("001.txt", "r")
p = k.read()
print(p)
