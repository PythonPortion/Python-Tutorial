
def testIfFlow():
    tmp = 90
    if tmp>90 :
        print("excellent grade")
    elif tmp==90 :
        print("an ordinary grade")
    else:
        print("poor grade")

# testIfFlow()

def testMatchCaseFlow():
    tmp = 89
    match tmp:
        case 89:
            print("not bad")
        case _:
            print("no matched value")


testMatchCaseFlow()
            