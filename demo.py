from collections import deque

print("hello world")

x="xxx"
print(f"{x} ddd")
l=[1,2, "3", "456"]
print(l)
l.append("7")
l.remove(2)
print(l)

ln=deque(l)
ln.popleft()


print(l)
print(ln)