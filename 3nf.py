relation = set()
dependencies = set()
prime_key = set()
third_nf_optimisation = set()
check_list = []
# check_list.append(1)
# print(check_list)

#PRVI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation = sorted(relation)
# # print(relation)

# dependencies.add("a->b")
# dependencies.add("b->a")
# dependencies.add("a->c")
# dependencies.add("c->a")
# dependencies = sorted(dependencies)
# # print(dependencies)

# prime_key.add("a")
# prime_key = sorted(prime_key)
# # print(prime_key)

#DRUGI PRIMJER
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

# dependencies.add("di->b")
# dependencies.add("aj->f")
# dependencies.add("gb->fje")
# dependencies.add("aj->hd")
# dependencies.add("i->cg")

# prime_key.add("abi")
# prime_key.add("aji")
# prime_key.add("adi")

#TRECI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")

# dependencies.add("a->b")
# dependencies.add("c->a")
# dependencies.add("b->c")

# prime_key.add("a")

#CETVRTI PRIMJER
relation.add("a")
relation.add("b")
relation.add("c")
relation.add("d")
relation.add("e")
relation.add("f")
relation.add("g")
relation = sorted(relation)

dependencies.add("a->d")
dependencies.add("a->b") #ad
dependencies.add("ag->b")
dependencies.add("b->g")
dependencies.add("b->e")
dependencies.add("e->b")
dependencies.add("e->f")
dependencies = sorted(dependencies)

prime_key.add("acg")
prime_key.add("abc")
prime_key.add("ace")
prime_key = sorted(prime_key)

def check_key(check_list):
    for key in prime_key:
        key=sorted(key)
        key="".join(key)
        for element in check_list:
            if element.find(key) != -1 and check_list[-1]:
                return
            elif element.find(key) != -1:
                continue
    third_nf_optimisation.add(key)

def check_dependencies():
    for element in dependencies:
        key, value = element.split("->")
        temp = key + value
        temp = ''.join(sorted(temp))
        for el in check_list:
            if temp in el:
                break
        else:
            check_list.append(temp)
            third_nf_optimisation.add(element)
    check_key(check_list)


check_dependencies()
third_nf_optimisation = sorted(third_nf_optimisation)
print(third_nf_optimisation)
# print(check_list)
