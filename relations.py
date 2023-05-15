import initialize
relation = []
dependencies = []
prime_key = []
third_nf_optimisation = set()
check_list = []
check_value = []

#PRVI PRIMJER
# initialize.fill_destination(relation,"a","b","c")
# initialize.fill_destination(dependencies,"a->b","b->a","a->c","c->a")

#DRUGI PRIMJER
initialize.fill_destination(relation,"a","b","c","d","e","f","g","h","i","j")
initialize.fill_destination(dependencies,"di->b","aj->f","gb->fje","aj->hd","i->cg")
# initialize.fill_destination(prime_key,"aji","adi","abi")

#TRECI PRIMJER
# initialize.fill_destination(relation,"a","b","c")
# initialize.fill_destination(dependencies,"a->b","c->a","b->c")
# initialize.fill_destination(prime_key,"a")

#CETVRTI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e","f","g")
# initialize.fill_destination(dependencies,"a->d","ag->b","b->g","b->e","e->b","e->f")
# initialize.fill_destination(prime_key,"acg","abc","ace")

#PETI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e","f","g")
# initialize.fill_destination(dependencies,"a->d","a->b","ag->b","b->g","b->e","e->b","e->f")
# initialize.fill_destination(prime_key,"acg","abc","ag")

# SESTI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e","f","g","h","i","j")
# initialize.fill_destination(dependencies,"a->d","a->b","ag->b","b->g","b->e","e->b","e->f","di->b","aj->f","gb->fje","aj->hd","i->cg","a->j")
# initialize.fill_destination(prime_key,"abc","bai","ace")

#SEDMI PRIMJER
# initialize.fill_destination(relation,"p","q","r","s","t","u","v","w","x","y")
# initialize.fill_destination(dependencies,"pq->r","p->st","u->vw","s->xy")
# initialize.fill_destination(prime_key,"xut","pqr")

#OSMI PRIMJER
# initialize.fill_destination(relation,"p","q","r","s","t","u","v","w","x","y")
# initialize.fill_destination(dependencies,"pq->r","p->st","u->vw","s->xy")
# initialize.fill_destination(prime_key,"qxw","usr","ytu")


#DEVETI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e","f","g","h","i","j")
# initialize.fill_destination(dependencies,"a->b","c->b","b->e","i->j","h->g","a->d","d->f","a->h" )

#ZA PRIMARNE DODATNO
#DESETI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e","f","g","h","i","j")
# initialize.fill_destination(dependencies,"a->b","c->b","b->e","i->j","h->g","a->d","d->f","a->h", "h->j" )

#JEDANAESTI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d","e")
# initialize.fill_destination(dependencies,"a->bc","b->d","c->d" )

#DVANAESTI PRIMJER
# initialize.fill_destination(relation,"a","b","c","d")
# initialize.fill_destination(dependencies,"ac->b","c->d")