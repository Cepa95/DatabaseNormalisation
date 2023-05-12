import relations
for main in relations.dependencies:
    print(main,"=>:")
    (main_key,main_value)=main.split("->")
    for i in range(len(relations.dependencies)):
        #print(set(main_key),"->",set(main_value))
     #   print("rel len:",len(relations.relation))
      #  print("main val len:",len(main_value))
       # print("main:",main_key+""+main_value) 
        # for el in main_key:
        #     if set(el).issubset(set(main_value)):
        #         continue
        #     else:
        main_value+=main_key
        # print("main value:",main_value)
        # print("main key:",main_key)
        for e in relations.dependencies:
            (key,value)=e.split("->")
            # print("value:",value)
            # print("val:",val)
            # print("value:",value
            if set(key).issubset(set(main_value)):
                main_value+=value
            else:
                continue
        flag=0
        #print(main_key,"->",main_value)
        #potraga optimalnog clana za prosirivanje
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

# for e in real_prime_key:
#     e=sorted(e)
#     e="".join(e)

# print(set(sorted(real_prime_key)))
real_prime_key = sorted(list(set(real_prime_key)))
# print(sorted(real_prime_key))
print(sorted(real_prime_key, key=len))

