class CName:
        def __init__(self,FName,MName,LName):
            self.FName = FName
            self.MName = MName
            self.LName = LName
        def __eq__(self,other):
            if self.FName == other.FName and self.MName == other.MName and self.LName== other.LName:
               return True
            else:
                return False
        def __str__(self):
            s = 'Name'+str(self.FName) + str(self.MName) + str(self.LName)
            return s
        def display(self):
            print 'Name:',self.Fname,self.Mname,self.Lname

class Address:
        def __init__(self,BldgNum,StreetName,City,Pin):
                self.BldgNum = BldgNum
                self.StreetName = StreetName
                self.City = City
                self.Pin = Pin
        def __str__(self):
                s1 ='Address:'+ str(self.BldgNum)+str(self.StreetName)+str(self.City)+str(self.Pin)
                return s1
        def display(self):
            print 'Address:',self.BldgNum,self.StreetName,self.City,self.Pin
class Date:
        def __init__(self,Day,Month,Year):
            self.Day = Day
            self.Month = Month
            self.Year = Year
        def __eq__(self,other):
            if self.Day == other.Day and self.Month == other.Month and self.Year == other.Year:
               return True
            else:
               return False
        def __str__(self):
            s ='Date of birth:'+str(self.Day)+' '+str(self.Month)+' '+str(self.Year)
            return s
class PContact:
    PCount = 0
    def __init__(self,PName,HomeAddr,PMobile,DOB):
        self.PName = PName
        self.HomeAddr = HomeAddr
        self.PMobile = PMobile
        self.DOB = DOB
        PContact.PCount += 1
    def display(self) :
            print str(self.PName)
            print str(self.HomeAddr)
            print 'mobile number:',self.PMobile
            print str(self.DOB)
          

class OContact:
    OCount = 0
    def __init__(self,OName,OMobile,OfficeName,OfficeAddr):
        self.OName = OName
        self.OMobile = OMobile
        self.OfficeName = OfficeName
        self.OfficeAddr = OfficeAddr
        OContact.OCount += 1
    def display(self):
            print str(self.OName)
            print str(self.OfficeAddr)
            print 'Mobile number:',self.OMobile
            print 'Office Name:',str(self.OfficeName)
def add_contact():
        print 'ENTER DETAILS FOR A NEW CONTACT'
        x=int(raw_input('Enter 1 for Personal Contact and 2 for Official Contact:'))
        fname=raw_input('Enter First name:')
        mname=raw_input('Enter Middle name:')
        lname=raw_input('Enter Last name:')
        bldgnum=raw_input('Enter building number:')
        streetname=raw_input('Enter Street name:')
        city=raw_input('Enter name of City:')
        pin=raw_input('Enter city PIN Code:')
        mobile=raw_input('Enter your 10 digit Mobile Phone Number:')
        if x==1:
                day=raw_input('Enter Day:')
                month=raw_input('Enter Month:')
                year=raw_input('Enter Year:')
                pname=CName(fname,mname,lname)
                address=Address(bldgnum,streetname,city,pin)
                DOB=Date(day,month,year)
                a=PContact(pname,address,mobile,DOB)
        elif x==2:
                officename=raw_input('Enter name of office:')
                Oname=CName(fname,mname,lname)
                address=Address(bldgnum,streetname,city,pin)         
                a=OContact(Oname,mobile,officename,address)
        import pickle
        if x==1:
                per=open(r'personalcontact.dat','ab')
                pickle.dump(a,per)
                per.close()
        elif x==2:
                off=open(r'officialcontact.dat','ab')
                pickle.dump(a,off)
                off.close()
                

def modify():
    import os
    import pickle
    x=int(raw_input('Enter 1 to modify a personal contact ; Enter 2 to modify an official contact:'))
    print 'Enter contact name to modify address:'
    fname=raw_input('Enter First name:')
    mname=raw_input('Enter Middle name:')
    lname=raw_input('Enter Last name:')
    A=CName(fname,mname,lname)#A is the name (CName type object) to be modified
    if x==1:
            
        #TAKING CName input to modify personal contact
        per=open(r'personalcontact.dat','rb')    
        tval1=0
        while True:
            try:
                pc=pickle.load(per)
                if pc.PName==A:
                    tval1=1
                    break
            except EOFError :
                per.close()
                break
    if x==2:
        #TAKING CName input to modify official contact
        off=open(r'officialcontact.dat','rb')    
        tval2=0
        while True:
            try:
                oc=pickle.load(off)
                if oc.OName==A:
                    tval2=1
                    break
            except EOFError :
                off.close()
                break
    #Taking input for modified address ('Address' type object)
    nbldgnum=raw_input('Enter new building number:')
    nstreetname=raw_input('Enter new street name:')
    ncity=raw_input('Enter new city:')
    npin=raw_input('Enter new pin code:')
    addr=Address(nbldgnum,nstreetname,ncity,npin)
    if x==1 and tval1==1:
        per=open(r'personalcontact.dat','rb')    
        temppers=open(r'personal_temp.dat','wb')
        while True :
            try:
                pc=pickle.load(per)
                if pc.PName==A :
                    name=pc.PName
                    dob=pc.DOB
                    mob=pc.PMobile
                    mod=PContact(name,addr,mob,dob)
                    pickle.dump(mod,temppers)
                else:
                    pickle.dump(pc,temppers)
            except EOFError :
                per.close()
                break
        temppers.close()
        os.remove(r'personalcontact.dat')
        os.rename(r'personal_temp.dat',r'personalcontact.dat')
    elif x==2 and tval2==1:
        off=open(r'officialcontact.dat','rb')    
        tempoff=open(r'off_temp.dat','wb')
        while True :
            try:
                oc=pickle.load(off)
                if oc.OName==A :
                    name=oc.OName
                    offnam=oc.OfficeName
                    mob=oc.OMobile
                    mod=OContact(name,mob,offnam,addr)
                    pickle.dump(mod,tempoff)
                else:
                    pickle.dump(oc,tempoff)
            except EOFError :
                off.close()
                break
        tempoff.close()
        os.remove(r'officialcontact.dat')
        os.rename(r'off_temp.dat',r'officialcontact.dat')
    else: print 'Contact Not Found'

def delete_contact (name) :
    import os
    import pickle
    per=open(r'personalcontact.dat','rb')
    off=open(r'officialcontact.dat','rb')
    tval1,tval2=0,0
    while True :
        try:
            sp=pickle.load(per)
            if sp.PName==name :
                tval1=1
                break
            if tval1!=1:
                    so=pickle.load(off)
                    if so.OName==name :
                        tval2=1
                        break 
        except EOFError :
            per.close()
            off.close()
            break

    if tval1==1 :
        temppers=open(r'personal_temp.dat','wb')
        while True :
            try:
                sp=pickle.load(per)
                if not sp.PName==name :
                    pickle.dump(sp,temppers)
            except EOFError :
                per.close()
                break
        temppers.close()
        os.remove(r'personalcontact.dat')
        os.rename(r'personal_temp.dat',r'personalcontact.dat')
        print 'Contact has been deleted from personalcontact file'
    if tval2==1 :
        tempoff=open(r'official_temp.dat','wb')
        while True :
            try :
                so=pickle.load(off)
                if not so.OName==name :
                    pickle.dump(so,tempoff)
            except EOFError :
                off.close()
                break
        tempoff.close()
        os.remove(r'officialcontact.dat')
        os.rename(r'official_temp.dat',r'officialcontact.dat')
        print 'Contact has been deleted from official contact file'
    if tval1==0 and tval2==0 :
        print 'Contact Not Found'
                
def SearchByPName(name):
    import pickle
    fopen=open(r'personalcontact.dat','rb')
    tval=1
    while True :
        try:
            contact=pickle.load(fopen)
            if contact.PName==name:
                contact.display()
                tval=0
                break
        except EOFError :
            fopen.close()
            break
    if tval==1 :
        print 'Contact Not Found'

def SearchByOName(offname):
    import pickle
    off=open(r'officialcontact.dat','rb')
    tval1=1
    while True :
        try:
            so=pickle.load(off)
            if so.OName==offname :
                tval1=0
                so.display()
                break
        except EOFError :
            off.close()
            break
    if tval1==1 :
        print 'No employee in this office. Please check the office name!'
        
def SearchByDOB(date) :
    import pickle
    per=open(r'personalcontact.dat','rb')
    tval2=1
    while True :
        try:
            sp=pickle.load(per)
            if sp.DOB==date :
                tval2=0
                sp.display()
                break
        except EOFError :
            per.close()
            break
    if tval2==1:
        print 'Contact Not Found'
def SearchByOffName(offname):
    import pickle
    off=open(r'officialcontact.dat','rb')
    tval=0
    while True :
        try:
            so=pickle.load(off)
            if so.OfficeName==offname :
                tval=1
                so.display()
                break
        except EOFError :
            so.close()
            break
    if tval==0 :
        print 'No employee in this office. Please check the office name!'
        
def SearchByMobile(mobile):
    import pickle
    per=open(r'personalcontact.dat','rb')
    off=open(r'officialcontact.dat','rb')
    tval=0    
    while True:
        try:
            sp=pickle.load(per)
            if sp.PMobile==mobile:
                print 'Contact found in Personal Contacts'
                sp.display()
                print
                tval=1
                break
            if tval!=1:
                so=pickle.load(off)
                if so.OMobile==mobile:
                  print 'Contact found in Official Contacts'
                  so.display()
                  print
                  tval=2
                  break
        except:
                per.close()
                off.close()
    if tval==0:            
        print 'Contact Not Found'



#Main Code
print '1=Add a contact'
print '2=Modify a contact'
print '3=Delete a contact'
print '4=Enter a personal name to view details of a Personal Contact'
print '5=Enter an official name to view details of an Official Contact'
print '6=Enter a Mobile Phone Number to view details of a Contact'
print '7=Enter DOB to show the contact details of employees with same DOB'
print '8=Views contact details of employess of a particular office'
print 'E=Ends Program'
while True:
    n=raw_input('Enter option number to execute task or E to end program:')
    if n=='1':
        add_contact()
    elif n=='2':
        modify()
    elif n=='3' or n=='4' or n=='5':
        fname=raw_input('Enter First name:')
        mname=raw_input('Enter Middle name:')
        lname=raw_input('Enter Last name:')
        name=CName(fname,mname,lname)
        if n=='3':
            delete_contact(name)
        elif n=='4':
            SearchByPName(name)
        elif n=='5':
            SearchByOName(name)
    elif n=='6':
        mobile=raw_input('Enter your 10 digit Mobile Phone Number:')
        SearchByMobile(mobile)
    elif n=='7':
        day=raw_input('Enter Day:')
        month=raw_input('Enter Month:')
        year=raw_input('Enter Year:')
        date=Date(day,month,year)
        SearchByDOB(date)
    elif n=='8':
        offname=raw_input('Enter name of office:')
        SearchByOffName(offname)
    elif n=='E' or n=='e':
        print 'Thank You.'
        print 'Program Ending'
        print '-'*40
        break
    elif n not in ['1','2','3','4','5','6','7','8','e','E']:
        print 'You have entered an Invalid Option.'
        print 'Re-Enter Option.'



