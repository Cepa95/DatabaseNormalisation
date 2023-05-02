def fill_destination(dest,*args):
    if type(dest)==set:
        for x in args:
            dest.add(x)
    else:
        for x in args:
            dest.append(x)

