phrase = "Don't Panic!"
plist = list(phrase)
print(phrase)
print(plist)

# def dummy():
    # Print "on taP"
    # for x in range(4):
    #     plist.pop()
    #     print(plist)
    # plist.pop(0)
    # print(plist)
    # plist.remove("'")
    # print(plist)
    # plist.extend([plist.pop(),plist.pop()])
    # print(plist)
    # plist.insert(2,plist.pop(3))

# def dummy():
    # # print "Panic not!"
    # plist.pop() #Don't Panic
    # print(plist)
    # plist.remove("'")
    # print(plist)
    # plist.pop(0)
    # for x in range(3,0,-1):
    #     plist.append(plist.pop(x))
    # plist.append(plist.pop(0))
    # plist.append(plist.pop(-3))
    # new_phrase = ''.join(plist)
    # print(plist)
    # print(new_phrase)

new_list = ''.join(plist[1:3])
new_list = new_list + ''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_list)