from collections import deque

print("hello world")

i=3
print(i)
j=2.5
print(j)
print(i * j)
print(i * j + i)
print(i * (j + i))

x='a'
y="BCD"
print(x)
print(y)
print(x.upper())
print(y.lower())

print(x + y)
print(x + " " + y)
print(f"{x} {y}")
print("{} {}".format(x, y))
print("{m} {n}".format(m=x, n=y))
print(y.split('C'))

number_list=[2, 3, 4, 5, 6, 3.5]
print(number_list)
print(number_list[0])
print(number_list[-1])
print(number_list[1:3])
print(number_list.sort())
print(number_list)

number_list.append(9)
print(number_list)
print(number_list.pop())
print(number_list)

number_queue=deque(number_list)
number_queue.append("m")
number_queue.append("n")
print(number_queue)
print(number_queue.popleft())
print(number_queue)

number_list=[x for x in range(10)]
print(number_list)
number_list=[x*10 for x in range(10)]
print(number_list)

number_set=set()
number_set.add('m')
number_set.add('abc')
print(number_set)
number_set.add("abc")
print(number_set)
number_set={"a", "b", "c"}
print(number_set)

element_tuple=2,"a"
print(element_tuple)
print(element_tuple[1])

element_dict={"a":1, "b": "bcd"}
print(element_dict)
element_dict["mn"]="mmmmmm"
print(element_dict)
print(element_dict.get("a"))
print(element_dict["a"])
print(element_dict.items())
print(element_dict.keys())
print(element_dict.values())
for k,v in element_dict.items():
    print("each")
    print(k)
    print(v)