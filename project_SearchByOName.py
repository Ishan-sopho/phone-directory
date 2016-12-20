def SearchByOName(name) :
    import pickle
    off=open(r'official.dat','rb')
    tval=1
    while True :
        try:
            so=pickle.load(off)
            if so.CName==name :
                tval1=0
                print so
                off.close()
                break
        except EOFError :
            off.close()
            break
    if tval :
        print 'no such contact with name',name,'was found'
        
