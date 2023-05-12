import relations

for dependency in relations.dependencies:
    print(dependency, "=>")
    main_key, main_value = dependency.split("->")

    for _ in relations.dependencies:
        main_value += main_key

        for entry in relations.dependencies:
            key, value = entry.split("->")
            if set(key) <= set(main_value):
                main_value += value

        found_match = False
        for entry in relations.relation:
            for dependency in relations.dependencies:
                key, value = dependency.split("->")
                if entry == key and not set(entry) <= set(main_value):
                    main_key += key
                    main_value += value
                    found_match = True
                    break
            if found_match:
                break

        if not found_match:
            for entry in relations.relation:
                if set(entry) <= set(main_value):
                    continue
                else:
                    main_key += entry
                    main_value += entry
                    break

    main_key = "".join(set(main_key))
    main_value = "".join(set(main_value))
    temp = main_key + "->" + main_value
    print(temp)
    relations.prime_key.append(temp)

print(relations.prime_key)
real_prime_key = sorted(set("".join(sorted(set(entry.split('->')[0])))
                            for entry in relations.prime_key
                            if '->' in entry), key=len)

print(real_prime_key)
