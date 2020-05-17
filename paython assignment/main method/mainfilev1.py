print("start of v1 file")

def main():
    print("start of main")
    print("end of main")

print("this is end of v1 file")

if __name__=='__main__':#will call only when the current file gets run not when imported by someone
    print("name has:",__name__,"v1")
    main()
