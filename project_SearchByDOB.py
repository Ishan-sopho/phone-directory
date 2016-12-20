def SearchByDOB (date) :
    import pickle
    per=open(r'personal.dat','rb')
    tval=0
    while True :
        try:
            sp=pickle.load(per)
            if sp.Date==date :
                tval1=1
                print sp
        except EOFError :
            sp.close()
            break
    if tval :
        print 'no such contact with D.O.B',date,'was found'
