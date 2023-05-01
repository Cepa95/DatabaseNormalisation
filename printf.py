import relations

def print_all():
    big_string = "".join(sorted(relations.relation))
    #da se izbjegne razmak od zagrada
    print("Relation: [{}]".format(big_string))
    print("Dependencies:",relations.dependencies)
    print("Prime key:", relations.prime_key)
    print()