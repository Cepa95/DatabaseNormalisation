relation = set()
dependencies = []
prime_key = []
third_nf_optimisation = set()
check_list = []
check_value = []

# check_list.append(1)
# print(check_list)

#PRVI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")

# dependencies.append("a->b")
# dependencies.append("b->a")
# dependencies.append("a->c")
# dependencies.append("c->a")

# prime_key.append("a")

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

# dependencies.append("di->b")
# dependencies.append("aj->f")
# dependencies.append("gb->fje")
# dependencies.append("aj->hd")
# dependencies.append("i->cg")

# prime_key.append("abi")
# prime_key.append("aji")
# prime_key.append("adi")

#TRECI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")

# dependencies.append("a->b")
# dependencies.append("c->a")
# dependencies.append("b->c")

# prime_key.append("a")

#CETVRTI PRIMJER
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


#PETI PRIMJER
# relation.add("a")
# relation.add("b")
# relation.add("c")
# relation.add("d")
# relation.add("e")
# relation.add("f")
# relation.add("g")

# dependencies.append("a->d")
# dependencies.append("a->b") 
# dependencies.append("ag->b")
# dependencies.append("b->g")
# dependencies.append("b->e")
# dependencies.append("e->b")
# dependencies.append("e->f")

# prime_key.append("acg")
# prime_key.append("abc")
# prime_key.append("ag")


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

# dependencies.append("a->d")
# dependencies.append("a->b") 
# dependencies.append("ag->b")
# dependencies.append("b->g")
# dependencies.append("b->e")
# dependencies.append("e->b")
# dependencies.append("e->f")
# dependencies.append("di->b")
# dependencies.append("aj->f")
# dependencies.append("gb->fje")
# dependencies.append("aj->hd")
# dependencies.append("i->cg")
# dependencies.append("a->j")

# prime_key.append("abc")
# prime_key.append("bai")
# prime_key.append("ace")

#SEDMI PRIMJER
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


#OSMI PRIMJER
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
