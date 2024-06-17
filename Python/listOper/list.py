List1 = [4, 2, 1, 5, 3]

# send back most big element
if List1[0] > List1[1]:
    List1[0], List1[1] = List1[1], List1[0]
    print(List1)
if List1[1] > List1[2]:
    List1[1], List1[2] = List1[2], List1[1]
    print(List1)
    print("List1[2] is " + str(List1[2]))
if List1[2] > List1[3]:
    List1[2], List1[3] = List1[3], List1[2]
    print(List1)
    print("List1[3] is " + str(List1[3]))
if List1[3] > List1[4]:
    List1[3], List1[4] = List1[4], List1[3]
    print(str(List1) + "!")

# send back big element
if List1[0] > List1[1]:
    List1[0], List1[1] = List1[1], List1[0]
    print(List1)
if List1[1] > List1[2]:
    List1[1], List1[2] = List1[2], List1[1]
    print(List1)
    print("List1[2] is " + str(List1[2]))
if List1[2] > List1[3]:
    List1[2], List1[3] = List1[3], List1[2]
    print(List1)
    print("List1[3] is " + str(List1[3]))

print(str(List1)+" is sorted!")
# [1, 2, 3, 4, 5]
