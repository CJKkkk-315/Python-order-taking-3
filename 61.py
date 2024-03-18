def compareLists(list1,list2,list3):
    max = list1[0]
    min = list1[0]
    for i in list1[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    sp1 = max - min
    max = list2[0]
    min = list2[0]
    for i in list2[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    sp2 = max - min
    max = list3[0]
    min = list3[0]
    for i in list3[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    sp3 = max - min
    if sp1 < sp2:
        if sp2 < sp3:
            print('The order for spread from lowest to highest is: one two three')
        else:
            if sp1 < sp3:
                print('The order for spread from lowest to highest is: one three two')
            else:
                print('The order for spread from lowest to highest is: three one two')
    else:
        if sp2 < sp3:
            if sp1 < sp3:
                print('The order for spread from lowest to highest is: two one three')
            else:
                print('The order for spread from lowest to highest is: two three one')
        else:
            print('The order for spread from lowest to highest is: three two one')
    su1 = 0
    n = 0
    for i in list1:
        n += 1
        su1 += i
    su1 /= n
    su2 = 0
    n = 0
    for i in list2:
        n += 1
        su2 += i
    su2 /= n
    su3 = 0
    n = 0
    for i in list3:
        n += 1
        su3 += i
    su3 /= n
    if su1 < su2:
        if su2 < su3:
            print('The order for average from lowest to highest is: one two three')
        else:
            if su1 < su3:
                print('The order for average from lowest to highest is: one three two')
            else:
                print('The order for average from lowest to highest is: three one two')
    else:
        if su2 < su3:
            if su1 < su3:
                print('The order for average from lowest to highest is: two one three')
            else:
                print('The order for average from lowest to highest is: two three one')
        else:
            print('The order for average from lowest to highest is: three two one')