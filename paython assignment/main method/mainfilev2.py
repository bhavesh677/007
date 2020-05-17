import mainfilev1
print("start of v2 file")

def main():
    print("start of main v2")
    print("end of mainv2")

print("this is end of v2 file")

if __name__=='__main__':
    print("name has:",__name__,"---->v2")
    mainfilev1.main()
    main()



