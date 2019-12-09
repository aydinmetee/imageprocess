def ortalama_varyans(my_list1=[2,4,3,40,5,6,3,3,2,1]):
    s=0;
    t=0;
    for i in my_list1:
        s=s+1
        t=t+i
    ortalama=float(t)/s

    s=0
    t=0
    for i in my_list1:
        s=s+1
        t=t+(i-ortalama)*(i-ortalama)
    varyans=t/(s-1)
    return ortalama,va

