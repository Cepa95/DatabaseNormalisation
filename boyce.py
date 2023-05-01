relation = set()
dependencies = []
prime_key = []
third_nf_optimisation = set()
check_list = []
remove_value = []

# PRVI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation.add("d")
# relation.add("e")
# relation.add("f")
# relation.add("g")
# relation.add("h")
# relation.add("i")
# relation.add("j")

# dependencies.append("di->b")
# dependencies.append("aj->f")
# dependencies.append("gb->fje")
# dependencies.append("aj->hd")
# dependencies.append("i->cg")

# prime_key.append("abi")
# prime_key.append("aji")
# prime_key.append("adi")

# DRUGI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation.add("d")
# relation.add("e")
# relation.add("f")
# relation.add("g")

# dependencies.append("a->d") 
# dependencies.append("ag->b")
# dependencies.append("b->g")
# dependencies.append("b->e")
# dependencies.append("e->b")
# dependencies.append("e->f")

# prime_key.append("acg")
# prime_key.append("abc")
# prime_key.append("ace")

#TRECI PRIMJER
# relation.add("p")
# relation.add("q")
# relation.add("r")
# relation.add("s")
# relation.add("t")
# relation.add("u")
# relation.add("v")
# relation.add("w")
# relation.add("x")
# relation.add("y")

# dependencies.append("pq->r") 
# dependencies.append("p->st")
# dependencies.append("q->u")
# dependencies.append("u->vw")
# dependencies.append("s->xy")

# prime_key.append("qxw")
# prime_key.append("usr")
# prime_key.append("ytu")

#CETVRTI PRIMJER
relation.add("p")
relation.add("q")
relation.add("r")
relation.add("s")
relation.add("t")
relation.add("u")
relation.add("v")
relation.add("w")
relation.add("x")
relation.add("y")

dependencies.append("pq->r") 
dependencies.append("p->st")
dependencies.append("q->u")
dependencies.append("u->vw")
dependencies.append("s->xy")

# prime_key.append("xut")
# prime_key.append("pqr")
prime_key.append("ab")



def check_key():
    big_string = "".join(sorted(relation))
    for key in prime_key:
        for element in third_nf_optimisation:
            if set(key).issubset(set(element)):
                print("The given set of functional dependencies already includes a key for the relation, only adding:", big_string)    
                third_nf_optimisation.add(big_string)
                return third_nf_optimisation     
    for key in prime_key:
        if set(key).issubset(set(big_string)):
            print("The given set of functional dependencies already includes a key for the relation, found in", big_string)
            big_string=sorted(big_string)
            temp = key
            for k in key:
                big_string.remove(k)
            temp += '->'+ "".join(big_string)
            print("adding:", temp)
            return third_nf_optimisation.add(temp)
    print("The key is not specified in the functional dependencies. The following key will be added: [{}]".format(prime_key[0]), "and the following relation: [{}]".format(big_string))
    third_nf_optimisation.add(big_string)
    return third_nf_optimisation.add(prime_key[0])

   

# def check_dependencies():
#     for element in dependencies:
#         key, value = element.split("->")
#         flag = False
#         temp = key + value
#         for remove in remove_value:
#             if remove in temp:
#                 flag = True
#                 break
#         if flag:
#             continue
#         temp = ''.join(sorted(temp))
#         for el in check_list:
#             if temp in el:
#                 break
#         else:
#             check_list.append(temp)
#             third_nf_optimisation.add(element)
#             for e in value:
#                 remove_value.append(e)
#                 if e in relation:
#                     relation.remove(e)
#     check_key()
def check_dependencies():
    # keep track of processed dependencies
    processed = set()
    # iterate over dependencies
    for element in dependencies:
        key, value = element.split("->")
        # combine key and value to check if they should be skipped
        temp = key + value
        # check if temp contains any values to remove
        if any(remove in temp for remove in remove_value):
            continue
        # sort and combine key and value for checking against previous dependencies
        temp = ''.join(sorted(temp))
        # check if temp has already been processed
        if temp in processed:
            continue
        # mark temp as processed and add to check_list
        processed.add(temp)
        check_list.append(temp)
        # add dependency to third_nf_optimisation
        third_nf_optimisation.add(element)
        # remove any values in value from relation and add to remove_value
        for e in value:
            if e in relation:
                relation.remove(e)
            remove_value.append(e)
    check_key()


def print_all():
    big_string = "".join(sorted(relation))
    print("Relation: [{}]".format(big_string))
    print("Dependencies:",dependencies)
    print("Prime key:", prime_key)
    print()

print_all()
check_dependencies()
print("p:", sorted(third_nf_optimisation))

