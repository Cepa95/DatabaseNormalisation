relation = set()
dependencies = []
prime_key = []
third_nf_optimisation = set()
check_list = []
# check_list.append(1)
# print(check_list)

#PRVI PRIMJER
relation.add("a")
relation.add("b")
relation.add("c")


dependencies.append("a->b")
dependencies.append("b->a")
dependencies.append("a->c")
dependencies.append("c->a")
dependencies = sorted(dependencies)

prime_key.append("a")

# print(prime_key)

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
# prime_key.add("ag")
# prime_key = sorted(prime_key)

# SESTI PRIMJER
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

# dependencies.add("a->d")
# dependencies.add("a->b") 
# dependencies.add("ag->b")
# dependencies.add("b->g")
# dependencies.add("b->e")
# dependencies.add("e->b")
# dependencies.add("e->f")
# dependencies.add("di->b")
# dependencies.add("aj->f")
# dependencies.add("gb->fje")
# dependencies.add("aj->hd")
# dependencies.add("i->cg")
# dependencies.add("a->j")
# dependencies = sorted(dependencies)

# prime_key.add("abc")
# prime_key.add("bai")
# prime_key.add("ace")
# prime_key = sorted(prime_key)



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

# prime_key.append("xut")
# prime_key.append("pqr")







def check_key(check_list):
    for key in prime_key:
        found_key = False
        for element in check_list:
            #iako je to vec sortirano, u ali u krajnjim slucajevima ako imamo  bg->fje, sto je sortirano befgj, 
            #a da nam je kljuc beg, sa .issubsetom to lako mozemo provjeriti
            if set(key).issubset(set(element)):
                found_key = True
        if found_key:
            print("The given set of functional dependencies already includes a key for the relation.")            
            return None
    print("The key is not specified in the functional dependencies. The following key will be added: [{}]".format(key))
    return key
   

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
    
#u slucaju da smo ubacili clan na primjer u petom primjeru
#a->b koji je podskup ag->b, a koji je naknadno ubacen, pa 
#kako jos nismo znali za ag->b pa imamo ovisnost viska u 
#zadnjem koraku cemo takve substringove maknuti
def check_before_elements(third_nf_optimisation):
    third_nf_optimisation = sorted(third_nf_optimisation)
    new_check = ["".join(sorted(substring.replace("->", ""))) if "->" in substring else substring for substring in third_nf_optimisation]
    # provjera za sta imamo uneseno
    # print(new_check)
    substring_indexes = []
    for i, item in enumerate(new_check):
        for j, other_item in enumerate(new_check):
            if i != j and (item in other_item or set(item).issubset(set(other_item))):
                substring_indexes.append(i)
    # print(substring_indexes)
    third_form = [element for i, element in enumerate(third_nf_optimisation) if i not in substring_indexes]
    check_prime_key=check_key(new_check)
    if check_prime_key is not None:
        third_form.append(check_prime_key)
        return third_form
    return third_form

def print_all():
    big_string = "".join(sorted(relation))
    #da se izbjegne razmak od zagrada
    print("Relation: [{}]".format(big_string))
    print("Dependencies:",dependencies)
    print("Prime key:", prime_key)
    print()
  
check_dependencies()
print_all()
third_nf_optimisation = check_before_elements(third_nf_optimisation)
print("p:", third_nf_optimisation)

