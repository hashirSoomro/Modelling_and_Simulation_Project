import math

def MMC_Queueing(Arrival_Mean,Service_Mean,No_of_server):
    lembda=1/Arrival_Mean
    meu=1/Service_Mean
    c=No_of_server
    p=lembda/(c*meu) #utlization factor
    idle=1-p
    value=0
    m=0
    for i in range(c):
        value=value+(((c*p)**m)/(math.factorial(m)))+(((c*p)**c)/(math.factorial(c)*(1-p)))
        
    Pnot=1/value
    Lq=(Pnot*p*(lembda/meu)**c)/(math.factorial(c)*((1-p)**2))
    Wq=Lq/lembda
    Ws=Wq+(1/meu)
    Ls=Ws*lembda
    return Lq,Wq,Ws,Ls,idle
