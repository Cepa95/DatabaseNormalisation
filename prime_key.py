import relations
for main in relations.dependencies:
    print(main,"=>")
    (main_key,main_value)=main.split("->")
    for i in range(len(relations.dependencies)):
        main_value+=main_key
        for e in relations.dependencies:
            (key,value)=e.split("->")
            if set(key).issubset(set(main_value)):
                main_value+=value
            else:
                continue
        flag=0
        for e in relations.relation:
            for k in relations.dependencies:
                (ky,v)=k.split("->")
                if e==ky and not(set(e).issubset(set(main_value))):
                    main_key+=ky
                    main_value+=v
                    flag=1
                    break
            if flag==1:
                break
        if flag==0:
            for e in relations.relation:
                if set(e).issubset(set(main_value)):
                    continue
                else:
                    main_key+=e
                    main_value+=e
                    break
    main_key=set(main_key)
    main_value=set(main_value)
    main_key="".join(main_key)
    main_value="".join(main_value)
    temp=main_key+"->"+main_value
    print(temp)
    relations.prime_key.append(temp)
print(relations.prime_key)
real_prime_key=[]
for e in relations.prime_key:
    (key,value)=e.split("->")
    real_prime_key.append("".join(sorted(key)))

real_prime_key = sorted(list(set(real_prime_key)))
print(sorted(real_prime_key, key=len))

