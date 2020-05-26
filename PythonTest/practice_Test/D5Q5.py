roll_number = [47,64,69,37,76,83,97,7,5,3,4,1,9]
sampledict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}

new = []

for i in roll_number:
    if i in sampledict.values():
        new.append(i)

print(new)


