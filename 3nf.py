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
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation.add("d")
# relation.add("e")
# relation.add("f")
# relation.add("g")
# relation = sorted(relation)

# dependencies.add("a->d")
# dependencies.add("a->d") 
# dependencies.add("ag->b")
# dependencies.add("b->g")
# dependencies.add("b->e")
# dependencies.add("e->b")
# dependencies.add("e->f")
# dependencies = sorted(dependencies)

# prime_key.add("acg")
# prime_key.add("abc")
# prime_key.add("ace")
# prime_key = sorted(prime_key)


#PETI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation.add("d")
# relation.add("e")
# relation.add("f")
# relation.add("g")
# relation = sorted(relation)

# dependencies.add("a->d")
# dependencies.add("a->b") 
# dependencies.add("ag->b")
# dependencies.add("b->g")
# dependencies.add("b->e")
# dependencies.add("e->b")
# dependencies.add("e->f")
# dependencies = sorted(dependencies)

# prime_key.add("acg")
# prime_key.add("abc")
# prime_key.add("ace")
# prime_key = sorted(prime_key)

#SESTI PRIMJER
relation.add("a")
relation.add("b")
relation.add("c")
relation.add("d")
relation.add("e")
relation.add("f")
relation.add("g")
relation.add("i")
relation.add("j")
relation = sorted(relation)

dependencies.add("a->d")
dependencies.add("a->b") 
dependencies.add("ag->b")
dependencies.add("b->g")
dependencies.add("b->e")
dependencies.add("e->b")
dependencies.add("e->f")
dependencies.add("di->b")
dependencies.add("aj->f")
dependencies.add("gb->fje")
dependencies.add("aj->hd")
dependencies.add("i->cg")
dependencies = sorted(dependencies)

prime_key.add("acg")
prime_key.add("abc")
prime_key.add("ace")
prime_key = sorted(prime_key)


def check_key(check_list):
    for key in prime_key:
        key = sorted(key)
        key = ''.join(key)
        for element in check_list:
            if element.find(key) != -1 and check_list[-1]:
                return
            elif element.find(key) != -1:
                continue
    print("There is no key in the dependencies, adding:", key)
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
    # print(third_nf_optimisation)
    # print(check_list)
    check_key(check_list)
    
#u slucaju da smo ubacili clan na primjer u petom primjeru
#a->b koji je podskup ag->b, a koji je naknadno ubacen, pa 
#kako jos nismo znali za ag->b pa imamo ovisnost viska u 
#zadnjem koraku cemo takve substringove maknuti
def check_before_elements(third_nf_optimisation):
    third_nf_optimisation = sorted(third_nf_optimisation)
    new_check = ["".join(sorted(substring.replace("->", ""))) if "->" in substring else substring for substring in third_nf_optimisation]
    # print(new_check)
    substring_indexes = []
    for i, item in enumerate(new_check):
        for j, other_item in enumerate(new_check):
            if i != j and item in other_item:
                substring_indexes.append(i)
    # print(substring_indexes)
    third_form = [element for i, element in enumerate(third_nf_optimisation) if i not in substring_indexes]
    return third_form

     
check_dependencies()
print(check_before_elements(third_nf_optimisation))
