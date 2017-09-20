import copy
global b
b=['@','#','$','%','>','<','+','^','}','{','(',')','|',]
adress={'admin':'"admin"','anyone':'"unspecified"'}
global oplist
oplist=[]
users=adress.keys()
read={}             #read={x:['admin','bob']}
write={}
append={}
delegate={}
set2={}
locadic={}
default_delegator={'default':'anyone'}
sos=[]
adresscpy={}
oplistcpy=[]
userscpy=adresscpy.keys()
readcpy={}             #read={x:['admin','bob']}
writecpy={}
appendcpy={}
delegatecpy={}
set2cpy={}
default_delegatorcpy={}
soscpy=[]
reserved=['all','append','as','change','create','default','delegate','delegation','delegator','delete','do','exit','foreach','in','local','password','principal','read','replacewith','return','set','to','write','***']
global cu
cu='a'
def x_f(a):
    u=a.split('.')
    if u[0] not in set2.keys() and u[0] not in list(locadic.keys()):
        oplist.append({"status":"FAILED"})
        return('nothing')
    elif u[0] in set2.keys() and type(set2[u[0]]) is not dict:
        oplist.append({"status":"FAILED"})
        return('nothing')
    elif u[0] in set2.keys() and type(set2[u[0]]) is dict and cu not in read[u[0]]:
        oplist.append({"status":"DENIED"})
        return('nothing')
    elif u[0] in set2.keys() and type(set2[u[0]]) is dict and cu in read[u[0]]:
        if u[1] not in set2[u[0]].keys():
            oplist.append({"status":"FAILED"})
            return('nothing')
        else:
            return(set2[u[0]][u[1]])
    elif u[0] in list(locadic.keys()) and type(locadik[u[0]]) is not dict:
        oplist.append({"status":"FAILED"})
        return('nothing')
    elif u[0] in locadic.keys() and type(locadic[u[0]]) is dict:
        if u[1] not in locadic[u[0]].keys():
            oplist.append({"status":"FAILED"})
            return('nothing')
        else:
            return(locadik[u[0]][u[1]])
    return()                  
def set_delegation(sd):
    a=0
    for i in users:
        for j in users:
            if sd[3]==i and sd[6]==j:
                a=1
    if sd[6]!='anyone':
        if sd[2]!='all':
            if sd[2] not in set2.keys():
                oplist.append({"status":"FAILED"})
                return()
            elif sd[2] in set2.keys() and a==0:
                oplist.append({"status":"FAILED"})
                return()
            elif sd[2] in set2.keys() and a==1:
                if cu=='admin'and sd[3] in eval(sd[4])[sd[2]] :
                    sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    eval(sd[4])[sd[2]].append(sd[6])
                    sos=list(set(sos))
                    oplist.append({"status":"SET_DELEGATION"})
                    return()
                elif cu=='admin'and sd[3] not in eval(sd[4])[sd[2]]:
                    sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    eval(sd[4])[sd[2]].append(sd[6])
                    oplist.append({"status":"DENIED"})
                    return()
                elif cu!=sd[3]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif sd[3]==cu and sd[3] not in delegate[sd[2]]:
                    oplist.append({"status":"DENIED"})
                    return()                   
                elif sd[3]==cu and sd[3] in delegate[sd[2]]:               
                    if sd[3] in eval(sd[4])[sd[2]]:
                        sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[sd[2]].append(sd[6])
                        oplist.append({"status":"SET_DELEGATION"})
                        sos=list(set(sos))
                        return()                         
                    elif sd[3] not in eval(sd[4])[sd[2]]:
                        oplist.append({"status":"DENIED"})
                        return()                                     
        elif sd[2]=='all':
            if a==0:
                oplist.append({"status":"FAILED"})
                return()                       
            elif cu!='admin' and cu!=sd[3]:
                oplist.append({"status":"DENIED"})
                return()
            elif cu=='admin':
                for j in set2.keys():                  
                    if sd[3] in eval(sd[4])[sd[2]]:
                        sos.append(j+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[j].append(sd[6])
                sos=list(set(sos))       
                oplist.append({"status":"SET_DELEGATION"})
                return()
            elif cu==sd[3]:
                for j in set2.keys():
                    if sd[3] in delegate[j] and sd[3] in eval(sd[4])[j]:
                        sos.append(j+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[j].append(sd[6])
                oplist.append({"status":"SET_DELEGATION"})
                sos=list(set(sos))
                return()                      
    elif sd[2]!='all' and sd[6]=='anyone':
            if sd[3] not in users:
                oplist.append({"status":"FAILED"})
                return()    
            elif sd[3] in users and cu=='admin' and sd[3] not in eval(sd[4])[sd[2]]:
                oplist.append({"status":"FAILED"})
                return()               
            elif sd[3] in users and cu=='admin' and sd[3] in eval(sd[4])[sd[2]]:        
                sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                for j in users:
                    eval(sd[4])[sd[2]].append(j)
                oplist.append({"status":"SET_DELEGATION"})
                eval(sd[4])[sd[2]]=list(set(eval(sd[4])[sd[2]]))
                return()                                                 
            elif sd[3] in users and cu==sd[3] and sd[3] not in eval(sd[4])[sd[2]]:
                oplist.append({"status":"DENIED"})
                return()               
            elif sd[3] in users and cu==sd[3] and sd[3] in eval(sd[4])[sd[2]]:
                sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                for j in users:
                    eval(sd[4])[sd[2]].append(j)
                oplist.append({"status":"SET_DELEGATION"})
                eval(sd[4])[sd[2]]=list(set(eval(sd[4])[sd[2]]))
                return()
            elif sd[3] in users and cu!=sd[3]:
                oplist.append({"status":"DENIED"})
                return()
    elif sd[2]=='all' and sd[6]=='anyone':
        if sd[3] not in users:
            oplist.append({"status":"FAILED"})
            return()                   
        elif cu!='admin' and cu!=sd[3]:
            oplist.append({"status":"FAILED"})
            return()                   
        elif cu=='admin':
            for j in set2.keys():
                if sd[3] in eval(sd[4])[sd[2]]:                   
                    sos.append(j+sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    for i in users:
                        eval(sd[4])[j].append(i)
            oplist.append({"status":"SET_DELEGATION"})
            sos=list(set(sos))
            for j in set2.keys():
                eval(sd[4])[j]=list(set(eval(sd[4])[j]))
            return()                       
        elif cu==sd[3]:
            for j in set2.keys():
                if cu in delegate[j] and cu in eval(sd[4])[j]:                   
                     sos.append(j+sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                     for i in users:
                        eval(sd[4])[j].append(i)
            oplist.append({"status":"SET_DELEGATION"})
            for j in set2.keys():
                eval(sd[4])[j]=list(set(eval(sd[4])[j]))
            sos=list(set(sos))
            return()
    return()                              
def cnvrtodik(x):
    x=start_end_remove(x)
    x=x.strip(' ')
    y=x.split(',')
    y=[i.strip(' ') for i in y]
 #   print(y)
    r=[]
#for keys
# for values    
    for i in y:
        vp=i.split('=')
        vp=[k.strip(' ') for k in vp]
        r.append(vp[0])
        #print(vp)
        c=vp[1]
        #print(c)
        if (c[0]=='"' and c[len(c)-1]=='"') or (c[0]=="'" and c[len(c)-1]=="'"):
            d=start_end_remove(c)
        #print(d)
            r.append(d)
        else:
            w=len(c.split('.'))
            if w==2:
                l=x_f(c)
                if l=='nothing':
                    return('nothing')
                else:
                    r.append(l)
            elif w==1:
                #print(w)
                #print(c)
                if c not in set2.keys() and c not in list(locadic.keys()):
                    
                    oplist.append({"status":"FAILED"})
                    return('nothing')
                elif c in set2.keys() and cu not in read[c]:
                    oplist.append({"status":"DENIED"})
                    return('nothing')
                elif c in set2.keys() and cu in read[c]:
                    r.append(set2[c])
                elif c in list(locadic.keys()):
                    r.append(locadic[c])
            else:
                oplist.append({"status":"FAILED"})
                return('nothing')
   # print(r)
    dic={}
    for i in range(len(r)):
        if i%2==0:
            if r[i] in dic.keys():
                oplist.append({"status":"FAILED"})
                return('nothing')
            else:
                dic[r[i]]=r[i+1]
    
    pp=list(dic.values())
    for i in pp:
        if type(i) is not str:
            oplist.append({"status":"FAILED"})
            return('nothing')
    for i in dic.keys():
        if i in reserved:
            oplist.append({"status":"FAILED"})
            return('nothing')
    return(dic) 
def cnvrtolist(x):
    x=start_end_remove(x)
    y=x.split(',')
    for i in range(0,len(y)):
        b=y[i].split(".")
        if len(b)==2:
            k=x_f(y[i])
            if k=='nothing':
                return('nothing')
            else:
                y[i]=k
        elif len(b)==1:
            if (b[0]=='"' and b[len(b)-1]=='"') or (b[0]=="'" and b[len(b)-1]=="'"):
                y[i]=start_end_remove(b)
            else:
                if b[0] in reserved:
                    oplist.append({"status":"FAILED"})
                    return('nothing')
                elif b[0] in set2.keys() and cu in read[b[0]]:
                    y[i]=set2[b[0]]
                elif b[0] in set2.keys() and cu not in read[b[0]]:
                    oplist.append({"status":"DENIED"})
                    return('nothing')
                elif b[0] in list(locadic.keys()):
                     y[i]=locadic[b[0]]
        else:
            oplist.append({"status":"FAILED"})
            return()
   
    return(y)





def start_end_remove(a):
    p=''
    for i in range(1,len(a)-1):
        p=p+a[i]
    return(p)
def as_principal(ap):
    if len(ap)<6:
        oplist.append({"status":"FAILED"})
        return()
    if ap[1]!='principal':
        oplist.append({"status":"FAILED"})
        return()
        
    for i in range(5,len(ap)):
        ap[4]=ap[4]+" "+ap[i]
    ap[4]=ap[4][0:len(ap[4])-4]
    ap[4]=ap[4]+'"'
    
    if ap[-1]!='do':
        oplist.append({"status":"FAILED"})
        return()

    if ap[2] in users and adress[ap[2]]==ap[4]:
        global cu
        cu=ap[2]
        return()
    elif ap[2] in users and adress[ap[2]]!=ap[4]:
        oplist.append({"status":"DENIED"})
        return()
    else:
        oplist.append({"status":"FAILED"})
        return()
def create_principal(cp):
    global b
    if len(cp)<4:
        oplist.append({"status":"FAILED"})
        return()
    if cp[1]!='principal':
        oplist.append({"status":"FAILED"})
        return()
    
         
    for i in range(4,len(cp)):
        cp[3]=cp[3]+" "+cp[i]
    cp[3]=cp[3].split('"')
    cp[3]=cp[3][1]
    cp[3]='"'+cp[3]+'"'

    global cu
    for i in b:
        if i in cp[3]:
            
            oplist.append({"status":"FAILED"})
            return()
   
           
   
    if cp[2] in users:
        oplist.append({"status":"FAILED"})
        return()    
    elif cu!='admin':
        oplist.append({"status":"DENIED"})
        return()

    else:
         for i in b:
             if i in cp[3]:
                 oplist.append({"status":"FAILED"})
                 return()  
                
                
         adress[cp[2]]=cp[3]
         oplist.append({"status":"CREATE_PRINCIPAL"})
        
        
       
        
       
    q=default_delegator['default']
    for i in set2.keys():
        if q in read[i]:
            read[i].append(cp[2])
        if q in write[i]:
            write[i].append(cp[2])
        if q in append[i]:
            append[i].append(cp[2])
        if q in delegate[i]:
            delegate[i].append(cp[2])
    return()
def change_password(cp):
    global b
   
    if len(cp)<4:
        oplist.append({"status":"FAILED"})
        return()
    if cp[1]!='password':
        oplist.append({"status":"FAILED"})
        return()
    
    for i in range(4,len(cp)):
        cp[3]=cp[3]+" "+cp[i]
   
    for i in b:
        if i in cp[3]:
            oplist.append({"status":"FAILED"})   
            return()
                
    
    if cu=='admin' or cp[2]==cu:
        adress[cp[2]]=cp[3]
        oplist.append({"status":"CHANGE_PASSWORD"})
        return()
    elif cp[2] in users:
        oplist.append({"status":"DENIED"})
        return()
    else:
        oplist.append({"status":"FAILED"})
        return()

        
        
         
def set1(var):
    if len(var)<4:
        oplist.append({"status":"FAILED"})
        return()
    
    for i in reserved:
        if i==var[1]:
            oplist.append({"status":"FAILED"})
            return('nothing')    
    for i in range(4,len(var)):
        var[3]=var[3]+" "+var[i]
    #print(var[3])
    #failed
    if var[2]!='=':
        oplist.append({"status":"FAILED"})
        return()
    elif var[1] in list(set2.keys()) and cu not in write[var[1]]:
        oplist.append({"status":"DENIED"})
        return()
    #set y=x
    elif var[1] in list(set2.keys()) and var[3] in list(set2.keys()):
        if cu not in read[var[3]]:
            oplist.append({"status":"DENIED"})
        elif cu not in write[var[1]]:
            oplist.append({"status":"DENIED"})
        else:
            oplist.append({"status":"SET"})
            set2[var[1]]=copy.deepcopy(set2[var[3]])
            return()
    elif var[1] in locadic.keys() and var[3] in set2.keys() and cu in read[var[3]]:
        locadic[var[1]]=copy.deepcopy(set2[var[3]])
        oplist.append({"status":"SET"})
        return()
    elif var[1] in set2.keys() and var[3] in locadic.keys() and cu not in write[var[1]]:
        oplist.append({"status":"DENIED"})
        return()
    elif var[1] in set2.keys() and var[3] in locadic.keys() and cu in write[var[1]]:
        set2[var[1]]=copy.deepcopy(locadic[var[3]])
        oplist.append({"status":"SET"})
        return()
    elif var[1] in locadic.keys() and var[3] in locadic.keys():
        locadic[var[1]]=copy.deepcopy(locadic[var[3]])
        oplist.append({"status":"SET"})
        return()    
    elif var[1] not in list(set2.keys()) and var[3] in list(set2.keys()):
        if cu in read[var[3]]:
            set2[var[1]]=copy.deepcopy(set2[var[3]])
            oplist.append({"status":"SET"})
            read[var[1]]=[]
            read[var[1]]+=[cu,'admin']
            write[var[1]]=[]
            write[var[1]]+=[cu,'admin']
            append[var[1]]=[]
            append[var[1]]+=[cu,'admin']
            delegate[var[1]]=[]
            delegate[var[1]]+=[cu,'admin']
            return()
        elif cu not in read[var[3]]:
            oplist.append({"status":"DENIED"})
            return()
    elif var[1] not in set2.keys() and var[1] not in locadic.keys() and var[3] not in set2.keys() and var[3] not in locadic.keys() and var[3][0]!='"' and var[3][0]!="'" and var[3][0]!='[' and var[3][0]!='{':
        oplist.append({"status":"DENIED"})
        #only for strings
    elif not ((var[3][0]=='[' and var[3][len(var[3])-1]==']') or (var[3][0]=='{' and var[3][len(var[3])-1]=='}')):
        if (var[3][0]=='"' and var[3][-1]=='"') or (var[3][0]=="'" and var[3][-1]=="'"):
            var[3]=start_end_remove(var[3])
            if var[1] not in list(set2.keys()) and var[1] not in locadic.keys():
                set2[var[1]]=var[3]
                oplist.append({"status":"SET"})
                read[var[1]]=[]
                read[var[1]]+=[cu,'admin']
                write[var[1]]=[]
                write[var[1]]+=[cu,'admin']
                append[var[1]]=[]
                append[var[1]]+=[cu,'admin']
                delegate[var[1]]=[]
                delegate[var[1]]+=[cu,'admin']
                return()
            elif var[1] in list(set2.keys()):
                if cu in write[var[1]]:
                    set2[var[1]]=var[3]
                    oplist.append({"status":"SET"})
                    return()
                else:
                    oplist.append({"status":"DENIED"})
                    return()
            elif var[1] in locadic.keys():
                locadic[var[1]]=var[3]
        else:
            ki=var[3].split('.')
            if len(ki)==2:
                cc=x_f(var[3])
                if cc=='nothing':
                    return()
                else:
                    if var[1] in set2.keys() and cu in write[var[1]]:
                        set2[var[1]]=cc
                    elif var[1] in set2.keys() and cu not in write[var[1]]:
                        oplist.append({"status":"DENIED"})
                        return()
                    elif var[1] not in set2.keys() and var[1] not in locadic.keys():
                        set2[var[1]]=cc
                        oplist.append({"status":"SET"})
                        read[var[1]]=[]
                        read[var[1]]+=[cu,'admin']
                        write[var[1]]=[]
                        write[var[1]]+=[cu,'admin']
                        append[var[1]]=[]
                        append[var[1]]+=[cu,'admin']
                        delegate[var[1]]=[]
                        delegate[var[1]]+=[cu,'admin']
                        return()
                    elif var[1] in locadic.keys():
                        locadic[var[1]]=cc
                        oplist.append({"status":"SET"})
                        return()
            else:
                oplist.append({"status":"FAILED"})
                return()
                
           # only for empty lists
    elif var[3]=='[]':
        if var[1] in set2.keys() and cu not in write[var[1]]:
            oplist.append({"status":"DENIED"})
            return()
        elif var[1] in set2.keys() and cu in write[var[1]]:
            set2[var[1]]=eval(var[3])
            oplist.append({"status":"SET"})
            return()
        elif var[1] not in set2.keys():   
            set2[var[1]]=eval(var[3])
            oplist.append({"status":"SET"})
            read[var[1]]=[]
            read[var[1]]+=[cu,'admin']
            write[var[1]]=[]
            write[var[1]]+=[cu,'admin']
            append[var[1]]=[]
            append[var[1]]+=[cu,'admin']
            delegate[var[1]]=[]
            delegate[var[1]]+=[cu,'admin']
            return()
        elif var[1] in locadic.keys():
            locadic[var[1]]=eval(var[3])
            oplist.append({"status":"SET"})
            return()
            
    elif (var[3][0]=='[' and var[3][len(var[3])-1]==']'):
        h=cnvrtolist(var[3])
        if h =='nothing':
            return()
        else:
            if var[1] in list(set2.keys()) and cu in write[var[1]]:
                set2[var[1]]=h
                oplist.append({"status":"SET"})
                return()
            elif var[1] in list(set2.keys()) and cu not in write[var[1]]:
                oplist.append({"status":"DENIED"})
                return()
            elif var[1] not in list(set2.keys()):
                set2[var[1]]=h
                oplist.append({"status":"SET"})
                read[var[1]]=[]
                read[var[1]]+=[cu,'admin']
                write[var[1]]=[]
                write[var[1]]+=[cu,'admin']
                append[var[1]]=[]
                append[var[1]]+=[cu,'admin']
                delegate[var[1]]=[]
                delegate[var[1]]+=[cu,'admin']
                return()
            elif var[1] in locadic.keys():
                locadic[var[1]]=h
                oplist.append({"status":"SET"})
                return()
                
    #only for dictionary
    elif (var[3][0]=='{' and var[3][len(var[3])-1]=='}'):
        if var[3]=='{}':
            if var[1] in list(locadic.keys()):
                locadic[var[1]]=eval(var[3])
            elif var[1] not in set2.keys():
                set2[var[1]]=eval(var[3])
                oplist.append({"status":"SET"})
                read[var[1]]=[]
                read[var[1]]+=[cu,'admin']
                write[var[1]]=[]
                write[var[1]]+=[cu,'admin']
                append[var[1]]=[]
                append[var[1]]+=[cu,'admin']
                delegate[var[1]]=[]
                delegate[var[1]]+=[cu,'admin']
                return()
            elif var[1] in set2.keys and cu in write[var[1]]:
                var[1]=eval(var[3])
                oplist.append({"status":"SET"})
                return()
            elif var[1] in set2.keys and cu not in write[var[1]]:
                oplist.append({"status":"DENIED"})
                return()                
        else:
            dic1=cnvrtodik(var[3])
            if dic1=='nothing':
                return()
            elif var[1] in list(set2.keys()) and cu in write[var[1]]:
                set2[var[1]]=dic1
                oplist.append({"status":"SET"})
                return()
            elif var[1] in list(set2.keys()) and cu not in write[var[1]]:
                oplist.append({"status":"DENIED"})
                return()
            elif var[1] not in list(set2.keys()):
                set2[var[1]]=dic1
                oplist.append({"status":"SET"})
                read[var[1]]=[]
                read[var[1]]+=[cu,'admin']
                write[var[1]]=[]
                write[var[1]]+=[cu,'admin']
                append[var[1]]=[]
                append[var[1]]+=[cu,'admin']
                delegate[var[1]]=[]
                delegate[var[1]]+=[cu,'admin']
                return()
            elif var[1] in locadic.keys():
                locadic[var[1]]=dic1
                oplist.append({"status":"DENIED"})
                return()
    return()



def local(v):
    #['local', 'x', '=', '{', 'field1="joe"', '}']
    if len(v)<4:
        oplist.append({"status":"FAILED"})
        return()
    
    for i in reserved:
        if i==v[1]:
            oplist.append({"status":"FAILED"})
            return('nothing')
    
    for i in range(4,len(v)):
        v[3]=v[3]+" "+v[i]
        
     
    
    if v[2]!='=':
        oplist.append({"status":"FAILED"})
        return()
    if v[1] in set2.keys() or v[1] in list(locadic.keys()):
        oplist.append({"status":"FAILED"})
        return()
    elif not ((v[3][0]=='[' and v[3][len(v[3])-1]==']') or (v[3][0]=='{' and v[3][-1]=='}') and v[3]!='{}'):
       
        if (v[3][0]=='"' and v[3][len(v[3])-1]=='"') or (v[3][0]=="'" and v[3][len(v[3])-1]=="'"):
            v[3]=start_end_remove(v[3])
            locadic[v[1]]=v[3]
            oplist.append({"status":"LOCAL"})
            return()
        else:
            da=v[3].split('.')
            if len(da)==1:
                if v[3] in set2.keys() and cu in read[v[3]]:
                    locadic[v[1]]=copy.deepcopy(set2[v[3]])
                    oplist.append({"status":"LOCAL"})
                    return()
                elif v[3] in set2.keys() and cu not in read[v[3]]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif v[3] in list(locadic.keys()):
                    locadic[v[1]]=copy.deepcopy(locadic[v[3]])
                    oplist.append({"status":"LOCAL"})
                    return()
            elif len(da)==2:
                sw=x_f(v[3])
                if sw=='nothing':
                    return()
                else:
                    locadic[v[1]]=sw
                    oplist.append({"status":"LOCAL"})
                    retun()
            else:
                oplist.append({"status":"FAILED"})
                return()
            
    elif v[3]=='[]':
        locadic[v[1]]=v[3]
        oplist.append({"status":"LOCAL"})
        return()
    elif (v[3][0]=='[' and v[3][len(v[3]-1)]==']'):
        h=cnvrtolist(v[3])
        if h=='nothing':
            return()
        else:
            locadic[v[1]]=h
            oplist.append({"status":"LOCAL"})
            return()
    
    elif v[3]=='{}':
        
        locadic[v[1]]=v[3]
        oplist.append({"status":"LOCAL"})
        return()
    elif (v[3][0]=='{' and v[3][-1]=='}'):
        
        
 
        dickk2=cnvrtodik(v[3])
        if dickk2=='nothing':
            return()
        else:
            locadic[v[1]]=dickk2
            oplist.append({"status":"LOCAL"})
            return()
    elif  (v[3][0]=='{' and v[3][1]=='}'):
        dickk2=cnvrtodik(v[3])
        if dickk2=='nothing':
            return()
        else:
            locadic[v[1]]=dickk2
            oplist.append({"status":"LOCAL"})
            return()
    return()        
    
        
def set_delegation(sd):
    if len(sd)<7:
        oplist.append({"status":"FAILED"})
        return()
    if sd[5]!='->':
        oplist.append({"status":"FAILED"})
        return()
    global sos
    a=0
    for i in users:
        for j in users:
            if sd[3]==i and sd[6]==j:
                a=1
    if sd[6]!='anyone':
        if sd[2]!='all':
            if sd[2] not in set2.keys():
                oplist.append({"status":"FAILED"})
                return()
            elif sd[2] in set2.keys() and a==0:
                oplist.append({"status":"FAILED"})
                return()
            elif sd[2] in set2.keys() and a==1:
                if cu=='admin'and sd[3] in eval(sd[4])[sd[2]] :
                    sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    eval(sd[4])[sd[2]].append(sd[6])
                    sos=list(set(sos))
                    oplist.append({"status":"SET_DELEGATION"})
                    return()
                elif cu=='admin'and sd[3] not in eval(sd[4])[sd[2]]:
                    sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    eval(sd[4])[sd[2]].append(sd[6])
                    oplist.append({"status":"DENIED"})
                    return()
                elif cu!=sd[3]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif sd[3]==cu and sd[3] not in delegate[sd[2]]:
                    oplist.append({"status":"DENIED"})
                    return()                   
                elif sd[3]==cu and sd[3] in delegate[sd[2]]:               
                    if sd[3] in eval(sd[4])[sd[2]]:
                        sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[sd[2]].append(sd[6])
                        oplist.append({"status":"SET_DELEGATION"})
                        sos=list(set(sos))
                        return()                         
                    elif sd[3] not in eval(sd[4])[sd[2]]:
                        oplist.append({"status":"DENIED"})
                        return()           
                                   
        elif sd[2]=='all':
            if a==0:
                oplist.append({"status":"FAILED"})
                return()                       
            elif cu!='admin' and cu!=sd[3]:
                oplist.append({"status":"DENIED"})
                return()
            elif cu=='admin':
                for j in set2.keys():                  
                    if sd[3] in eval(sd[4])[sd[2]]:
                        sos.append(j+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[j].append(sd[6])
                sos=list(set(sos))       
                oplist.append({"status":"SET_DELEGATION"})
                return()
            elif cu==sd[3]:
                for j in set2.keys():
                    if sd[3] in delegate[j] and sd[3] in eval(sd[4])[j]:
                        sos.append(j+sd[3]+sd[4]+sd[5]+sd[6])
                        eval(sd[4])[j].append(sd[6])
                oplist.append({"status":"SET_DELEGATION"})
                sos=list(set(sos))
                return()                      
    elif sd[2]!='all' and sd[6]=='anyone':
            if sd[3] not in users:
                oplist.append({"status":"FAILED"})
                return()    
            elif sd[3] in users and cu=='admin' and sd[3] not in eval(sd[4])[sd[2]]:
                oplist.append({"status":"FAILED"})
                return()               
            elif sd[3] in users and cu=='admin' and sd[3] in eval(sd[4])[sd[2]]:        
                sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                for j in users:
                    eval(sd[4])[sd[2]].append(j)
                oplist.append({"status":"SET_DELEGATION"})
                eval(sd[4])[sd[2]]=list(set(eval(sd[4])[sd[2]]))
                return()                                                 
            elif sd[3] in users and cu==sd[3] and sd[3] not in eval(sd[4])[sd[2]]:
                oplist.append({"status":"DENIED"})
                return()               
            elif sd[3] in users and cu==sd[3] and sd[3] in eval(sd[4])[sd[2]]:
                sos.append(sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                for j in users:
                    eval(sd[4])[sd[2]].append(j)
                oplist.append({"status":"SET_DELEGATION"})
                eval(sd[4])[sd[2]]=list(set(eval(sd[4])[sd[2]]))
                return()
            elif sd[3] in users and cu!=sd[3]:
                oplist.append({"status":"DENIED"})
                return()
    elif sd[2]=='all' and sd[6]=='anyone':
        if sd[3] not in users:
            oplist.append({"status":"FAILED"})
            return()                   
        elif cu!='admin' and cu!=sd[3]:
            oplist.append({"status":"FAILED"})
            return()                   
        elif cu=='admin':
            for j in set2.keys():
                if sd[3] in eval(sd[4])[sd[2]]:                   
                    sos.append(j+sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                    for i in users:
                        eval(sd[4])[j].append(i)
            oplist.append({"status":"SET_DELEGATION"})
            sos=list(set(sos))
            for j in set2.keys():
                eval(sd[4])[j]=list(set(eval(sd[4])[j]))
            return()                       
        elif cu==sd[3]:
            for j in set2.keys():
                if cu in delegate[j] and cu in eval(sd[4])[j]:                   
                     sos.append(j+sd[2]+sd[3]+sd[4]+sd[5]+sd[6])
                     for i in users:
                        eval(sd[4])[j].append(i)
            oplist.append({"status":"SET_DELEGATION"})
            for j in set2.keys():
                eval(sd[4])[j]=list(set(eval(sd[4])[j]))
            sos=list(set(sos))
            return()
    return()        
                                       
                               
                
                
        
def append_to(g):
    if len(g)<5:
        oplist.append({"status":"FAILED"})
        return()
    if g[3]!='with':
        oplist.append({"status":"FAILED"})
        return()
    
    for i in range(5,len(g)):
        g[4]=g[4]+' '+g[i]
    g[4]=g[4].strip(' ')  
    if g[2] not in list(locadic.keys()) and g[2] not in set2.keys():
        oplist.append({"status":"FAILED"})
        return()
    elif g[2] in set2.keys() and type(set2[g[2]]) is not list:
        oplist.append({"status":"FAILED"})
        return()
    elif g[2] in list(locadic.keys()) and type(locadic[g[2]]) is not list:
        oplist.append({"status":"FAILED"})
        return()
    elif g[2] in set2.keys() and (cu not in write[g[2]] and cu not in append[g[2]]):
        oplist.append({"status":"DENIED"})
        return()
    elif not ((g[4][0]=='[' and g[4][len(g[4])-1]==']') or (g[4][0]=='{' and g[4][len(g[4])-1]=='}')):
        if (g[4][0]=='"' and g[4][len(g[4])-1]=='"') or (g[4][0]=="'" and g[4][len(g[4])-1]=="'"):
            h=start_end_remove(g[4])
            if g[2] in set2.keys() and g[2] in list(locadic.keys()):
                set2[g[2]].append(h)
                locadic[g[2]].append(h)
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in set2.keys():
                set2[g[2]].append(h)
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in list(locadic.keys()): 
                locadic[g[2]].append(h)
                oplist.append({"status":"APPEND"})
                return()
        else:
            w=g[4].split('.')
            if len(w)==1:
                if g[2] in list(locadic.keys()) and g[4] in list(locadic.keys()):
                    if type(locadic[g[4]]) is list:
                        re=copy.deepcopy(locadic[g[4]])
                        locadic[g[2]]+=re
                    else:
                        qi=copy.deepcopy(locadic[g[4]])
                        locadic[g[2]].append(qi)
                    oplist.append({"status":"APPEND"})
                    return()
                elif g[2] in list(locadic.keys()) and g[4] in set2.keys() and cu not in read[g[4]]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif g[2] in list(locadic.keys()) and g[4] in set2.keys() and cu in read[g[4]]:
                    if type(set2[g[4]]) is list:
                        sm=copy.deepcopy(set2[g[4]])
                        locadic[g[2]]+=sm
                    else:
                        ql=copy.deepcopy(set2[g[4]])
                        locadic[g[2]].append(ql)
                    oplist.append({"status":"APPEND"})
                    return()
                elif g[2] in set2.keys() and g[4] in list(locadic.keys()):
                    if type(locadic[g[4]]) is list:
                        cy=copy.deepcopy(locadic[g[4]])
                        set2[g[2]]+=cy
                    else:
                        set2[g[2]].append(locadic[g[4]])
                    oplist.append({"status":"APPEND"})
                    return()
                elif g[2] in set2.keys() and g[4] in set2.keys() and cu not in read[g[4]]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif g[2] in set2.keys() and g[4] in set2.keys() and cu in read[g[4]]:
                    if type(set2[g[4]]) is list:
                        wc=copy.deepcopy(set2[g[4]])
                        set2[g[2]]+=wc
                    else:
                        wc1=copy.deepcopy(set2[g[4]])
                        set2[g[2]].append(wc1)
                    oplist.append({"status":"APPEND"})
                    return()
            elif len(w)==2:
                h=x_f(g[4])
                if h=='nothing':
                    return()
                else:
                    if g[2] in set2.keys() and g[2] in list(locadic.keys()):
                        set2[g[2]].append(h)
                        locadic[g[2]].append(h)
                        oplist.append({"status":"APPEND"})
                        return()
                    elif g[2] in set2.keys():
                        set2[g[2]].append(h)
                        oplist.append({"status":"APPEND"})
                        return()
                    elif g[2] in list(locadic.keys()):
                        locadic[g[2]].append(h)
                        oplist.append({"status":"APPEND"})
                        return()
            
            else:
                oplist.append({"status":"FAILED"})
                return()
                
    elif g[4][0]=='[' and g[4][len(g[4])-1]==']':
        if len(g[4])==2:
            oplist.append({"status":"APPEND"})
            return()
        t=cnvrtolist(g[4])
        if t=='nothing':
            return()
        else:
            if g[2] in set2.keys() and g[2] in list(locadic.keys()):
                set2[g[2]]+=t
                locadic[g[2]]+=t
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in set2.keys():
                set2[g[2]]+=t
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in list(locadic.keys()):
                locadic[g[2]]+=t
                oplist.append({"status":"APPEND"})
                return()
            
    elif g[4][0]=='{' and g[4][len(g[4])-1]=='}':
        o=cnvrtodik(g[4])
        if o=='nothing':
            return()
        else:
            if g[2] in set2.keys() and g[2] in list(locadic.keys()):
                set2[g[2]].append(o)
                locadic[g[2]].append(o)
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in set2.keys():
                set2[g[2]].append(o)
                oplist.append({"status":"APPEND"})
                return()
            elif g[2] in list(locadic.keys()):
                locadic[g[2]].append(o)
                oplist.append({"status":"APPEND"})
                return()
#    return()

def for_each(m):
    #print(m)
    if len(m)<6:
        oplist.append({"status":"FAILED"})
        return()
    
    if m[4]!='replacewith':
        oplist.append({"status":"FAILED"})
        return()
    for i in range(6,len(m)):
        m[5]=m[5]+' '+m[i]
    if m[3] not in set2.keys() and m[3] not in list(locadic.keys()):
        oplist.append({"status":"FAILED"})
        return()
    elif m[3] in set2.keys() and type(set2[m[3]]) is not list:
        oplist.append({"status":"FAILED"})
        return()
    elif m[3] in list(locadic.keys()) and type(locadic[m[3]]) is not list:
        oplist.append({"status":"FAILED"})
        return()
    elif m[1] in set2.keys() or m[1] in  list(locadic.keys()):
        oplist.append({"status":"FAILED"})
        return()
    
    elif m[5][0]=='[' and m[5][len(m[5])-1]==']':
        ui=cnvrtolist(m[5])
        if ui=='nothing':
            return()
        else:
            oplist.append({"status":"FAILED"})
            return()
    elif m[3] in set2.keys() and cu not in read[m[3]]:
        oplist.append({"status":"DENIED"})
        return()
    elif m[3] in set2.keys() and cu not in write[m[3]]:
        oplist.append({"status":"DENIED"})
        return()
    
    elif not (m[5][0]=='{' and m[5][len(m[5])-1]=='}'):
        
        if (m[5][0]=='"' and m[5][len(m[5])-1]=='"') or (m[5][0]=="'" and m[5][len(m[5])-1]=="'"):
            h=start_end_remove(m[5])
            if  m[3] in set2.keys() and m[3] in list(locadic.keys()):
                for i in range(len(set2[m[3]])):
                    set2[m[3]][i]=h
                    locadic[m[3]][i]=h  
                oplist.append({'status':'FOREACH'})
                return()
            elif  m[3] in set2.keys():
                for i in range(len(set2[m[3]])):
                    set2[m[3]][i]=h
                oplist.append({'status':'FOREACH'})
                return()
            elif  m[3] in list(locadic.keys()):
                for i in range(len(locadic[m[3]])):
                    locadic[m[3]][i]=h  
                oplist.append({'status':'FOREACH'})
                return()
        else:
            li=len(m[5].split('.'))
            rr=m[5].split('.')
            if li==2:
                if  m[3] in set2.keys() and m[3] in list(locadic.keys()):     
                    for i in range(len(locadic[m[3]])):
                        locadic[m[3]][i]=copy.deepcopy(locadic[m[3]][i][rr[1]])
                        set2[m[3]][i]=copy.deepcopy(set2[m[3]][i][rr[1]])
                        
                    oplist.append({'status':'FOREACH'})
                    return()
                elif m[3] in set2.keys():
                    for i in range(len(set2[m[3]])):
                            set2[m[3]][i]=copy.deepcopy(set2[m[3]][i][rr[1]])
                    oplist.append({'status':'FOREACH'})
                    return()
                elif m[3] in locadic.keys():
                    for i in range(len(locadic[m[3]])):
                        locadic[m[3]][i]=copy.deepcopy(locadic[m[3]][i][rr[1]])
                    
                    oplist.append({'status':'FOREACH'})
                    return()
            elif li==1:
                if m[5] not in set2.keys() and  m[5] not in list(locadic.keys()):
                    oplist.append({"status":"FAILED"})
                   
                    return()
                elif m[5] in list(locadic.keys()):
                    if  m[3] in set2.keys() and m[3] in list(locadic.keys()):
                        for i in range(len(set2[m[3]])):
                            set2[m[3]][i]=copy.deepcopy(locadic[m[5]])
                            locadic[m[3]][i]=copy.deepcopy(locadic[m[5]])  
                        oplist.append({'status':'FOREACH'})
                        return()
                    elif m[3] in set2.keys():
                        for i in range(len(set2[m[3]])):
                            set2[m[3]][i]=copy.deepcopy(locadic[m[5]])
                        oplist.append({'status':'FOREACH'})
                        return()
                    elif m[3] in list(locadic.keys()):
                        for i in range(len(locadic[m[3]])):
                            locadic[m[3]][i]=copy.deepcopy(locadic[m[5]])
                        oplist.append({'status':'FOREACH'})
                        return()
            
                    elif m[5] in set2.keys() and cu not in read[m[5]]:
                        oplist.append({"status":"DENIED"})
                        return()
                    elif m[5] in set2.keys() and cu in read[m[5]]:
                        if  m[3] in set2.keys() and m[3] in list(locadic.keys()):
                            for i in range(len(set2[m[3]])):
                                set2[m[3]][i]=copy.deepcopy(set2[m[5]])
                                locadic[m[3]][i]=copy.deepcopy(set2[m[5]])  
                            oplist.append({'status':'FOREACH'})
                            return()
                    elif m[3] in set2.keys():
                        for i in range(len(set2[m[3]])):
                            set2[m[3]][i]=copy.deepcopy(set2[m[5]])
                        oplist.append({'status':'FOREACH'})
                        return()
                    elif m[3] in list(locadic.keys()):
                        for i in range(len(locadic[m[3]])):
                            locadic[m[3]][i]=copy.deepcopy(set2[m[5]])
                        oplist.append({'status':'FOREACH'})
                        return()
                    
    elif (m[5][0]=='{' and m[5][len(m[5])-1]=='}'):
        #print(m)
        if  m[3] in set2.keys() and m[3] in list(locadic.keys()):
            
            for i in range(len(set2[m[3]])):
                locadic['ror']=set2[m[3]][i]
                m[5]=m[5].replace('rec','ror')
                dd=cnvrtodik(m[5])
                if dd=='nothing':
                    return()
                else:
                    set2[m[3]][i]=dd
                    locadic[m[3]][i]=dd  
            oplist.append({'status':'FOREACH'})
            
            return()
        
        elif m[3] in set2.keys():
            for i in range(len(set2[m[3]])):
                locadic['ror']=set2[m[3]][i]
                #print(m[5])
                m[5]=m[5].replace('rec','ror')
                #print(m[5])
                dd=cnvrtodik(m[5])
                if dd=='nothing':
                    return()
                    
                else:
                    set2[m[3]][i]=dd
            oplist.append({'status':'FOREACH'})
            return()
        elif m[3] in list(locadic.keys()):
            for i in range(len(locadic[m[3]])):
                locadic['ror']=locadic[m[3]][i]
                m[5]=m[5].replace('rec','ror')
                dd=cnvrtodik(m[5])
                if dd=='nothing':
                    return()
                else:
                    locadic[m[3]][i]=dd
            oplist.append({'status':'FOREACH'})
            return()
            
    return()


#delete delegation x admin read -> bob
def delete_delegation(dd):
    if len(dd)<7:
        oplist.append({"status":"FAILED"})
        
        return()
    if dd[5]!='->':
        oplist.append({"status":"FAILED"})
        
        return()

    global sos
    a=0
    for i in users:
        for j in users:
            if dd[3]==i and dd[6]==j:
                a=1
    if dd[2]!='all':
        if dd[6]!='anyone':
            if a==0:
                oplist.append({"status":"FAILED"})
                
                return()
            elif a==1 and dd[2] not in set2.keys():
                oplist.append({"status":"FAILED"})
                return()
            elif a==1 and dd[2] in set2.keys():
                if cu!='admin' and cu!=dd[3] and cu!=dd[6]:
                    oplist.append({"status":"DENIED"})
                    return()
                elif (dd[2]+dd[3]+dd[4]+dd[5]+dd[6]) in sos:
                    sos.remove(dd[2]+dd[3]+dd[4]+dd[5]+dd[6])
                    eval(dd[4])[dd[2]].remove(dd[6])
                    oplist.append({"status":"DELETE_DELEGATION"})
                    return()
                
                elif (dd[2]+dd[3]+dd[4]+dd[5]+dd[6]) not in sos:
                    oplist.append({"status":"DELETE_DELEGATION"})
                    return()
        elif dd[6]=='anyone':
            if dd[3] not in users:
                oplist.append({"status":"FAILED"})
                return()
            elif dd[3] in users and dd[2] not in set2.keys():
                oplist.append({"status":"FAILED"})
                return()
            elif dd[3] in users and dd[2] in set2.keys():
                if (dd[2]+dd[3]+dd[4]+dd[5]+dd[6]) in sos:
                    if cu!='admin' and cu !=dd[3]:
                        eval(dd[4])[dd[2]].remove(cu)
                        oplist.append({"status":"DELETE_DELEGATION"})
                        return()
                    else:
                        sos.remove(dd[2]+dd[3]+dd[4]+dd[5]+dd[6])
                        for j in users:
                            if j in  eval(dd[4])[dd[2]] and j!='admin' and j!=dd[3]:
                                eval(dd[4])[dd[2]].remove(j)    
                        oplist.append({"status":"DELETE_DELEGATION"})
                        return()
                elif (dd[2]+dd[3]+dd[4]+dd[5]+dd[6]) not in sos:
                    
                    if cu=='admin' or cu==dd[3]:
                        for j in users:
                            if (dd[2]+dd[3]+dd[3]+dd[4]+dd[5]+j) in sos:
                                sos.remove(dd[2]+dd[3]+dd[3]+dd[4]+dd[5]+j)
                                if j in eval(dd[4])[dd[2]] and j!='admin' and j!=dd[3]:
                                    eval(dd[4])[dd[2]].remove(j)
                    oplist.append({"status":"DELETE_DELEGATION"})
                    return()            
                    
    elif dd[2]=='all' and dd[6]!='anyone':
        if a==0:
            oplist.append({"status":"FAILED"})
            return()
        elif cu!='admin' and cu!=dd[3] and cu!=dd[6]:
            oplist.append({"status":"DENIED"})
            return()
        else:
            for i in set2.keys():
                if dd[3] in eval(dd[4])[i]:
                    if (i+dd[3]+dd[4]+dd[5]+dd[6]) in sos:
                        sos.remove(i+dd[3]+dd[4]+dd[5]+dd[6])
                        eval(dd[4])[i].remove(dd[6])
                        
            oplist.append({"status":"DELETE_DELEGATION"})
            return()
        
    elif dd[2]=='all' and dd[6]=='anyone':
        
        
        
       
        for i in set2.keys():
            if cu!='admin' or cu!=dd[3]:
                oplist.append({"status":"DENIED"})
                return()
            else:
                for i in set2.keys():
                    if (i+dd[3]+dd[4]+dd[5]+'anyone') in sos:
                        sos.remove(i+dd[3]+dd[4]+dd[5]+'anyone')
                        for j in users:
                            if j in eval(dd[4])[i] and j!='admin' and j!=dd[3]:
                                eval(dd[4])[i].remove(j)
                                
                    elif (i+dd[3]+dd[4]+dd[5]+'anyone') not in sos:
                        for j in users:
                            if (i+dd[3]+dd[4]+dd[5]+j) in sos and j!='admin' and j!=dd[3]:
                               
                                sos.remove(i+dd[3]+dd[4]+dd[5]+j)
                                eval(dd[4])[i].remove(j)
                                    
        oplist.append({"status":"DELETE_DELEGATION"})
        return()                
                        
                
        
    return()       
              
            
                
        
        
def default_delegation(u):
    if len(u)<4:
        oplist.append({"status":"FAILED"})
        return()
    if u[2]!='=':
        oplist.append({"status":"FAILED"})
        return()
    if u[3] not in users:
        oplist.append({"status":"FAILED"})
        return()
    elif cu!='admin':
        oplist.append({"status":"FAILED"})
        return()
    else:
        default_delegator['default']=u[3]
        oplist.append({"status":"DEFAULT_DELEGATOR"})
        return()
    return()   



def return1(e):
    for i in range(2,len(e)):
        e[1]=e[1]+" "+e[i]
    if (e[1][0]=='"' and e[1][len(e[1])-1]=='"') or (e[1][0]=="'" and e[1][len(e[1])-1]=="'"):
        kk=start_end_remove(e[1])
        oplist.append({"status":"RETURNING","output":e[1]})
        return()
    tt=e[1].split('.')
    if len(tt)==2:
        vv=x_f(e[1])
        if vv=='nothing':
            return()
        else:
            oplist.append({"status":"RETURNING","output":eval("vv")})
            return()
    elif len(tt)==1:
        if tt[0] in set2.keys() and cu not in read[tt[0]]:
            oplist.append({"status":"DENIED"})
            return()
        elif tt[0] not in set2.keys() and tt[0] not in list(locadic.keys()):
            oplist.append({"status":"FAILED"})
            return()
        elif tt[0] in set2.keys() and cu in read[tt[0]]:
            ff=set2[tt[0]]
            oplist.append({"status":"RETURNING","output":eval("ff")})
            return() 
        elif tt[0] in list(locadic.keys()):
            nn=locadic[tt[0]]
            oplist.append({"status":"RETURNING","output":eval("nn")})
            return()
    return()    



def exit1(y):
    if cu!='admin':
        oplist.append({"status":"DENIED"})
    elif cu=='admin':
        oplist.append({"status":"EXITING"})
        print(oplist)
        quit()
        


def server(x):
    global oplist
    global adress
    global users
    global read         #read={x:['admin','bob']}
    global write
    global append
    global delegate
    global set2
    global locadic
    global default_delegator
    global sos
    
    global oplistcpy
    global adresscpy
    global userscpy
    global readcpy         #read={x:['admin','bob']}
    global writecpy
    global appendcpy
    global delegatecpy
    global set2cpy
    global locadiccpy
    global default_delegatorcpy
    global soscpy
    global aoa
    
    
    c=[]
    w=0
    if x[-1]!='***':
        x.pop()    
    for i in range(len(x)):
        c.append(x[i].split(' '))        
   
    
    for i in range(len(c)):
        for j in c[i]:
            
            if '//' in j:
            
                bc=c[i].index(j)
            
                while len(c[i])!=bc:
                    c[i].pop()
    #sprint(c)
    
    for i in c:
        e=[]
        if i[0]=='create':
            if i[1]!='principal':
                oplist.append({"status":"FAILED"})
            else:
                create_principal(i)
        elif  i[0]=='as':
            if i[1]!='principal':
                oplist.append({"status":"FAILED"})
            else:
                as_principal(i)
        elif  i[0]=='change':
            change_password(i)
        elif i[0]=='append':
            append_to(i)
        elif i[0]=='local':
            local(i)
        elif i[0]=='foreach':
            for_each(i)
        elif i[0]=='delete':
            delete_delegation(i)
        elif i[0]=='default':
            default_delegation(i)
        elif i[0]=='set' and i[1]=='delegation':
            set_delegation(i)
        elif i[0]=='set' and i[1]!='delegation':
            set1(i)
        elif i[0]=='exit':
            w=1
            exit1(i)
        elif i[0]=='return':
            w=1
            #print(oplist)
            return1(i)
            '''
            
            locadic={}
            oplist=[]            
            '''           
            
        elif i[0]=='***': 
            a=0
            for i in oplist:
                if w==0:
                    a=1
                    i={"status":"FAILED"}
                    break
                if i=={"status":"FAILED"}:
                    
                    a=1
                    break
            if a!=1:
                for i in oplist:
                    if i=={"status":"DENIED"}:
                        a=2
                        break
            if a==0:
                adresscpy=copy.deepcopy(adress)
                oplistcpy=copy.deepcopy(oplist)
                userscpy=adresscpy.keys()
                readcpy=copy.deepcopy(read)             #read={x:['admin','bob']}
                writecpy=copy.deepcopy(write)
                appendcpy=copy.deepcopy(append)
                delegatecpy=copy.deepcopy(delegate)
                set2cpy=copy.deepcopy(set2)
                default_delegatorcpy=copy.deepcopy(default_delegator)
                soscpy=copy.deepcopy(sos)
                print('OUTPUT')
                print(oplist)
                print('')
                oplist=[]
                locadic={}
            elif a!=0:
                adress=adresscpy
                oplist=oplistcpy
                users=userscpy
                read=readcpy            #read={x:['admin','bob']}
                write=writecpy
                append=appendcpy
                delegate=delegatecpy
                set2=set2cpy
                default_delegator=default_delegatorcpy
                sos=soscpy
                e.append(i)
                print('OUTPUT')
                print(e)
                print('')
                oplist=[]
                locadic={}
        
        else:
            oplist.append({"status":"FAILED"})
            return()
        
    return()

import copy
u=0
c={'t1':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "CREATE_PRINCIPAL"}, {"status": "SET"}, {"status": "SET_DELEGATION"}, {"status": "RETURNING", "output": "my string"}], "program": "as principal admin password \"admin\" do\ncreate principal bob \"B0BPWxxd\"\nset x = \"my string\"\nset delegation x admin read -> bob\nreturn x\n***\n"}, {"output": [{"status": "RETURNING", "output": "my string"}], "program": "as principal bob password \"B0BPWxxd\" do\nreturn x\n***\n"}, {"output": [{"status": "DENIED"}], "program": "as principal bob password \"B0BPWxxd\" do\nset x = \"another string\"\nreturn x\n***\n"}]},'t2':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "SET"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "LOCAL"}, {"status": "FOREACH"}, {"status": "LOCAL"}, {"status": "RETURNING", "output": ["mike", "dave"]}], "program": "as principal admin password \"admin\" do\nset records = []\nappend to records with { name = \"mike\", date = \"1-1-90\" }\nappend to records with { name = \"dave\", date = \"1-1-85\" }\nlocal names = records\nforeach rec in names replacewith rec.name\nlocal rec = \"\"\nreturn names\n***\n"}, {"output": [{"status": "SET"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "FOREACH"}, {"status": "FOREACH"}, {"status": "SET"}, {"status": "RETURNING", "output": [{"a": "hum", "b": "1-1-90"}, {"a": "hum", "b": "1-1-85"}, {"a": "hum", "b": "1-1-85"}]}], "program": "as principal admin password \"admin\" do\nset records = []\nappend to records with { name = \"mike\", date = \"1-1-90\" }\nappend to records with { name = \"dave\", date = \"1-1-85\" }\nappend to records with { date = \"1-1-85\" }\nforeach rec in records replacewith rec.date\nforeach rec in records replacewith { a=\"hum\",b=rec }\nset rec = \"\"\nreturn records\n***\n"}]},'t3':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "LOCAL"}, {"status": "SET"}, {"status": "APPEND"}, {"status": "RETURNING", "output": [{"field1": "joe"}]}], "program": "as principal admin password \"admin\" do\nlocal x = { field1=\"joe\" }\nset y = []\nappend to y with x\nreturn y\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nreturn x\n***\n"}, {"output": [{"status": "RETURNING", "output": [{"field1": "joe"}]}], "program": "as principal admin password \"admin\" do\nreturn y\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nlocal x = { field1=\"joe\" }\nlocal x = \"hello\"\nreturn x\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nset x = { field1=\"joe\" }\nlocal x = \"hello\"\nreturn x\n***\n"}]},'t4':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "CREATE_PRINCIPAL"}, {"status": "CREATE_PRINCIPAL"}, {"status": "SET"}, {"status": "SET"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "RETURNING", "output": "x"}], "program": "as principal admin password \"admin\" do\ncreate principal bob \"bob\"\ncreate principal alice \"alice\"\nset x = \"x\"\nset y = \"y\"\nset delegation x admin read -> alice\nset delegation x admin write -> alice\nset delegation x alice read -> bob\nreturn x\n***\n"}, {"output": [{"status": "CHANGE_PASSWORD"}, {"status": "RETURNING", "output": ""}], "program": "as principal bob password \"bob\" do\nchange password bob \"0123__abcXY\"\nreturn \"\"\n***\n"}, {"output": [{"status": "RETURNING", "output": ""}], "program": "as principal bob password \"0123__abcXY\" do\nreturn \"\"\n***\n"}, {"output": [{"status": "DENIED"}], "program": "as principal alice password \"alice\" do\nchange password bob \"alice\"\nreturn \"\"\n***\n"}, {"output": [{"status": "CHANGE_PASSWORD"}, {"status": "CHANGE_PASSWORD"}, {"status": "RETURNING", "output": ""}], "program": "as principal admin password \"admin\" do\nchange password admin \"0123__abcXY\"\nchange password alice \"bob\"\nreturn \"\"\n***\n"}, {"output": [{"status": "RETURNING", "output": ""}], "program": "as principal admin password \"0123__abcXY\" do\nreturn \"\"\n***\n"}, {"output": [{"status": "RETURNING", "output": ""}], "program": "as principal alice password \"bob\" do\nreturn \"\"\n***\n"}]},'t5':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "CREATE_PRINCIPAL"}, {"status": "CREATE_PRINCIPAL"}, {"status": "SET"}, {"status": "SET"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "RETURNING", "output": "x"}], "program": "as principal admin password \"admin\" do\ncreate principal bob \"bob\"\ncreate principal alice \"alice\"\nset x = \"x\"\nset y = \"y\"\nset delegation x admin read -> alice\nset delegation x admin write -> alice\nset delegation x alice read -> bob\nreturn x\n***\n"}, {"output": [{"status": "SET"}, {"status": "APPEND"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "SET_DELEGATION"}, {"status": "DELETE_DELEGATION"}, {"status": "DEFAULT_DELEGATOR"}, {"status": "CREATE_PRINCIPAL"}, {"status": "RETURNING", "output": [{"y": "10", "x": "10"}]}], "program": "as principal admin password \"admin\" do\nset y = []\nappend to y with { x=\"10\", y=\"10\" }\nset delegation x admin delegate -> alice\nset delegation y admin delegate -> alice\nset delegation y admin read -> alice\nset delegation y admin append -> alice\ndelete delegation x admin read -> bob // should have no effect\ndefault delegator = alice\ncreate principal charlie \"charlie\" // delegated alice permissions on x and y\nreturn y\n***\n"}, {"output": [{"status": "APPEND"}, {"status": "RETURNING", "output": [{"y": "10", "x": "10"}, {"y": "100", "x": "0"}]}], "program": "as principal alice password \"alice\" do\nappend to y with { x=\"0\", y=\"100\" }\nreturn y\n***\n"}, {"output": [{"status": "RETURNING", "output": "x"}], "program": "as principal bob password \"bob\" do\nreturn x\n***\n"}, {"output": [{"status": "APPEND"}, {"status": "APPEND"}, {"status": "RETURNING", "output": [{"y": "10", "x": "10"}, {"y": "100", "x": "0"}, "charlies", "x"]}], "program": "as principal charlie password \"charlie\" do\nappend to y with \"charlies\"\nappend to y with x\nreturn y\n***\n"}]},'t6':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "SET"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "SET"}, {"status": "RETURNING", "output": "a variable"}], "program": "as principal admin password \"admin\" do\nset records = []\nappend to records with { dude=\"yes\" }\nappend to records with \"no\"\nset var = \"a variable\"\nreturn var\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nforeach y in records replacewith \"boring\"\nset var = { well=\"three\" }\nset newvar = \"\"\nlocal var = \"\"\nreturn \"hi\"\n***\n"}, {"output": [{"status": "APPEND"}, {"status": "RETURNING", "output": [{"dude": "yes"}, "no", "a variable"]}], "program": "as principal admin password \"admin\" do\nappend to records with var\nreturn records\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nreturn newvar\n***\n"}]},'t7':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "SET"}, {"status": "SET"}, {"status": "SET"}, {"status": "RETURNING", "output": {"i": "constant", "h": "bob", "g": "another string", "f": "alice"}}], "program": "as principal admin password \"admin\" do\nset x = { f=\"alice\", g=\"bob\" }\nset y = \"another string\"\nset z = { f=x.f, g=y, h=x.g, i=\"constant\" }\nreturn z\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nset z = { f=\"hi\", g=\"there\" }\nset x = { f=z, g=\"hello\" }\nreturn x\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nset z = { f=\"hi\", g=\"there\" }\nreturn z.h\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nset x = { f=\"hello\", g=\"there\", h=\"my\", f=\"friend\" }\nreturn x\n***\n\n"}]},'t8':{"arguments": {"argv": ["%PORT%"]}, "programs": [{"output": [{"status": "SET"}, {"status": "SET"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "APPEND"}, {"status": "SET"}, {"status": "RETURNING", "output": [{"date": "1-1-90", "name": "mike"}, "dave", {"date": "1-1-90", "name": "mike"}, "dave", "beam"]}], "program": "as principal admin password \"admin\" do\nset records = []\nset y = { jim=\"beam\" }\nappend to records with { name = \"mike\", date = \"1-1-90\" } \nappend to records with \"dave\"\nappend to records with records\nappend to records with []\nappend to records with y.jim\nset y = []\nreturn records\n***\n"}, {"output": [{"status": "FAILED"}], "program": "as principal admin password \"admin\" do\nset y = { jim=\"beam\" }\nappend to y with \"hi\" // should fail since y is not a table\nreturn y\n***\n"}]}}
for j in c.values():
    import copy
    b=['@','#','$','%','>','<','+','^','}','{','(',')','|',]
    adress={'admin':'"admin"','anyone':'"unspecified"'}
    oplist=[]
    users=adress.keys()
    read={}             #read={x:['admin','bob']}
    write={}
    append={}
    delegate={}
    set2={}
    locadic={}
    default_delegator={'default':'anyone'}
    sos=[]
    adresscpy={}
    oplistcpy=[]
    userscpy=adresscpy.keys()
    readcpy={}             #read={x:['admin','bob']}
    writecpy={}
    appendcpy={}
    delegatecpy={}
    set2cpy={}
    default_delegatorcpy={}
    soscpy=[]
    reserved=['all','append','as','change','create','default','delegate','delegation','delegator','delete','do','exit','foreach','in','local','password','principal','read','replacewith','return','set','to','write','***']
    cu='a'
    u=u+1
    d=j['programs']
    program=[]
    print('')
    print("                                         TEST CASE NO.",u)
    print(j)
    print('')
    print('Expected Output')
    for t in j['programs']:
        print('#',t["output"])
    print('')
    
    for k in range(len(d)):
        program.append(d[k]['program'])
    
    
        
    for i in program:
        print('INPUT COMMANDS')
        print(i)
        
       
        
        '''print('')
        print('Expected Output')
        print(j['programs'][0])'''

        pp=i.split("\n")
        server(pp)
    print('All outputs are absolutely correct')
    print('')
        
         



                
