import random

f = open("attribute values.txt", "a+")
content = f.read()
attribute_vals_stored = content.split(", ")
m = []
for i in range(5): 
     j = random.randint(1000, 1800)
     if j not in m and j not in attribute_vals_stored:
        m.append(j)

print(m)
for j in m:
    f.write(str(j) + ", ")
f.close()