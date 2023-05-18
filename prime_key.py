import relations
import printf

printf.print_all()

# Potraga primarnih kljuceva preko funkcionalnih ovisnosti
for dependency in relations.dependencies:
    print(dependency, "=>")
    main_key, main_value = dependency.split("->")
    #Petlja za provodenje algoritma za pronalazenje primarnog kljuca n puta 
    #radi rasirivanja i drugih teorema
    for _ in relations.dependencies:
        #Primjena refleksivnosti
        main_value += main_key

        #Pretrazivanje da li postoji tranzitivnost i primjenjivanje unije ako je pronadena tranzitivnost
        for entry in relations.dependencies:
            key, value = entry.split("->")

            #Provjera ako A->B I B->C POTOME A->C i primjena unije A->B U A->C |=A->BC
            # if set(key).issubset(set(main_value)):
            if set(key) <= set(main_value):
                main_value += value

        found_match = False
        #Primjena Prosirivanja 
        for entry in relations.relation:
            for dependency in relations.dependencies:
                key, value = dependency.split("->")
                #Provjera da li postoji clan koji je ujedno kljuc neke funkcionalne osvisnosti
                # jer je njega optimalno prvog nadodati
                if entry == key and not set(entry) <= set(main_value):
                    main_key += key
                    main_value += value
                    found_match = True
                    break
            if found_match:
                break
        #ako nismo nasli clan koji je ujedno kljuc funkcionalne ovisnosti dodajemo
        # redom clan koji se ne nalazi s lijeve strane ograde relacije tj algoritma za primarni kljuc 
        if not found_match:
            for entry in relations.relation:
                if set(entry) <= set(main_value):
                    continue
                else:
                    main_key += entry
                    main_value += entry
                    break
    #Postavljanje lijeve i desne strane u SET da se izbrisu clanovi koji su duplikati
    #npr. aabba->abcaacab |= ab->abc
    main_key = "".join(set(main_key))
    main_value = "".join(set(main_value))
    #stvaranje te relacije da se vidi da je kljuc pokrio sve clanove relacije
    temp = main_key + "->" + main_value
    print(temp)
    relations.prime_key.append(temp)

# print(relations.prime_key)

#Sortiranje liste kljuceva po velicini tako da ide od najmanjeg prema najvecemu
real_prime_key = sorted(set("".join(sorted(set(entry.split('->')[0])))
                            for entry in relations.prime_key
                            if '->' in entry), key=len)
#Ispis primarnih kljuceva relacije
print('Prime key:', real_prime_key)
