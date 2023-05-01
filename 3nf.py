import relations
import printf

def check_key(check_list):
    for key in relations.prime_key:
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
    for element in relations.dependencies:
        key, value = element.split("->")
        temp = key + value
        temp = ''.join(sorted(temp))
        for el in relations.check_list:
            if temp in el:
                break
        else:
            relations.check_list.append(temp)
            relations.third_nf_optimisation.add(element)
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

  
check_dependencies()
printf.print_all()
third_nf_optimisation = check_before_elements(relations.third_nf_optimisation)
print("p:", third_nf_optimisation)

