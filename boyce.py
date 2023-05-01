import relations
import printf

def check_key():
    big_string = "".join(sorted(relations.relation))
    for key in relations.prime_key:
        for element in relations.third_nf_optimisation:
            if set(key).issubset(set(element)):
                print("The given set of functional dependencies already includes a key for the relation, only adding:", big_string)    
                relations.third_nf_optimisation.add(big_string)
                return relations.third_nf_optimisation     
    for key in relations.prime_key:
        if set(key).issubset(set(big_string)):
            print("The given set of functional dependencies already includes a key for the relation, found in", big_string)
            big_string=sorted(big_string)
            temp = key
            for k in key:
                big_string.remove(k)
            temp += '->'+ "".join(big_string)
            print("adding:", temp)
            return relations.third_nf_optimisation.add(temp)
    print("The key is not specified in the functional dependencies. The following key will be added: [{}]".format(relations.prime_key[0]), "and the following relation: [{}]".format(big_string))
    relations.third_nf_optimisation.add(big_string)
    return relations.third_nf_optimisation.add(relations.prime_key[0])

def check_dependencies():
    processed = set()
    for element in relations.dependencies:
        key, value = element.split("->")
        temp = key + value
        # ako se nadje iti jedna vrijednost u chec_value, preskoci korak
        if any(check in temp for check in relations.check_value):
            continue
        temp = ''.join(sorted(temp))
        if temp in processed:
            continue
        processed.add(temp)
        relations.check_list.append(temp)
        relations.third_nf_optimisation.add(element)
        for element in value:
            if element in relations.relation:
                relations.relation.remove(element)
            relations.check_value.append(element)
    check_key()


printf.print_all()
check_dependencies()
print("p:", sorted(relations.third_nf_optimisation))

