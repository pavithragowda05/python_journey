#user defined library
#to use external library or user defined library we need import the libray
#  into program

#import library_name as alias_name


def fn_addnums(a=0,b=0):
    tot=a+b
    return tot

def fn_dname(dno):
    if dno==11:
        dname="admin"
    elif dno==12:
        dname="finance"   
    elif dno==13:
        dname="devlopment"
    elif dno==14:
        dname="marketing"
    elif dno==15:
        dname="hardwere"
    else:
        dname="others"  
    return dname   
def fn_gender(gn):
    if gn=="m" or gn=="M":
        dn="male"
    elif gn=="f" or gn=="F":
        dn="female" 
    else:
        dn="others" 
    return dn

def def_name(name):
    x=name.capitalize()
    return x  

def fn_grade(s1,s2,s3,s4,s5,s6,avg):
    if s1>=35 and s2>=35 and  s3>=35 and s4>=35 and s5>=35 and s6>=35:
        if avg>=75:
            p="distinction" 
        elif avg<75 and avg>=60:
            p="firstclass"
        elif avg<60 and avg>=50:
            p="secondclass" 
        elif avg<50 and avg>=35:
            p="thirdclass" 
        else:
            p="faile"
    else:
        p="faile" 
    return p
