import math

def MGC_Queueing(Arrival_Mean,Service_Mean,No_of_server,ServiceVariance):
    lembda=1/Arrival_Mean
    meu=1/Service_Mean
    c=No_of_server
    p=lembda/(c*meu)
    idle=1-p
    #Ca=ArrivalVariance/((1/lembda)**2)
    Cs=ServiceVariance/((1/meu)**2)
    value=0
    for m in range(c):
        value=value+(((c*p)**m)/(math.factorial(m)))+(((c*p)**c)/(math.factorial(c)*(1-p)))
    Pnot=1/value
    Lq=(Pnot*p*(lembda/meu)**c)/(math.factorial(c)*((1-p)**2))
    Wq=Lq/lembda
    #Wq=Wq*((Ca+Cs)/2)
    Wq=Wq*Cs
    Lq=lembda*Wq
    Ws=Wq+(1/meu)
    Ls=Ws*lembda
    return Lq,Wq,Ws,Ls,idle

