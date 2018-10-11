

app_val = [[[1, 2], 1], [[2, 3], 2], [[1, 3], 3], [[3, 4], 1], [[2, 4], 4]]

print(app_val)

app_val_loc = []

val = []

for i in range(len(app_val)):
    val.append(app_val[i][1])
val.sort()
print(val)

tmp = app_val

for i in range(len(val)):
    print(i," : ")
    for j in range(len(tmp)):
        if tmp[j][1] == val[i]:
            app_val_loc.append(tmp[j])
            tmp[j][1] == -1
            print(tmp[j])
            break

print(app_val_loc)