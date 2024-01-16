#importing required libraries
import math
import pandas as pd
import random
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Graph plot Section
def entVsWT(s_no,WT):
    plt.bar(s_no, WT, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Wait Time')
    plt.title('Wait Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    plt.show()

def entVsTA(s_no,TA):
    plt.bar(s_no, TA, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Turn Around Time')
    plt.title('Turn Around Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    plt.show()
    

def entVsArrival(s_no,arrival):
    plt.bar(s_no, arrival, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Arrival Time')
    plt.title('Arrival Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    plt.show()

def entVsService(s_no,service):
    plt.bar(s_no, service, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Service Time')
    plt.title('Service Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    plt.show()
    return s_no,service
def ServerUtilization(Server_util):
    idleTime=1-Server_util
    #print(idleTime,Server_util)
    y = np.array([Server_util,idleTime])
    mylabels = ["Utilized Server", "Idle time"]

    plt.pie(y, labels = mylabels,autopct='%1.1f%%')
    plt.show() 

def GGC(lembda,meu,sigma,server_no):
    #initializing required lists
    s_no=[]
    cp=[]
    cpl=[0]
    int_arrival=[0]
    arrival=[]
    service=[]
    TA=[]
    WT=[]
    RT=[]
    cust_serv_no=[]
    all_curr_end_time=[]
    value=0
    C_count=-1
    global min_end

    #Generating values for serial number, cummulative probability and cummulative probability lookup
    x=0
    while cpl[-1]<1:
    #for x in range(0,ran_no):
        s_no.append(x)
        value=norm.cdf(x, meu, sigma)
        cp.append(float("%.6f"%value))
        cpl.append(cp[-1])
        x+=1
    cpl.pop(-1)

    #Generating values for inter-arrival time 
    for i in range(len(cp)):
        ran_var=float("%.6f"%random.uniform(0,1))
        #print(ran_var)
        for j in range(len(cp)):
            if cpl[j]<ran_var and ran_var<cp[j]:
                #print(cpl[j],ran_var,cp[j])
                int_arrival.append(j)

    #Generating values for arrival time
    arrival.append(int_arrival[0])
    for i in range(1,len(cp)):
        arrival.append(int_arrival[i]+arrival[i-1])
    int_arrival.pop(-1)

    #Generating values for service time
    for i in range(len(cp)):
        service.append(math.ceil(-meu*math.log(random.uniform(0,1))))

    #Initializing Servers
    S=[]
    E=[]
    Servers={}
    for i in range(1,server_no+1):
        Servers[i]=[[0],[0]]
    
    #Assigning customers to server
    for i in range(len(arrival)):
        for key, value in Servers.items():
            if arrival[i]>=value[1][-1]:
                C_count=C_count+1
                cust_serv_no.append(key)
                value[0].append(arrival[i])
                S.append(arrival[i])
                value[1].append(arrival[i]+service[i])
                E.append(arrival[i]+service[i])
                break
            all_curr_end_time.append(value[1][-1])
            min_end=min(all_curr_end_time)
            #print(min_end)
            
        all_curr_end_time.clear()
        #print(min_end)
        if i>C_count:
            C_count=C_count+1
            for key, value in Servers.items():
                if value[1][-1]==min_end:
                    cust_serv_no.append(key)
                    value[0].append(min_end)
                    S.append(min_end)
                    value[1].append(min_end+service[i])
                    E.append(min_end+service[i])
                    break

    #Generating values for TurnAround time,Wait time and Response Time
    for i in range(len(cp)):
        TA.append(E[i]-arrival[i])
        WT.append(TA[i]-service[i])
        RT.append(S[i]-arrival[i])

    #Server utilization calculation
    if lembda>=meu:
        Server_util=meu/lembda
    elif meu>=lembda:
        Server_util=lembda/meu

    #Avg values of the time given
    avg_interarrival=(np.sum(int_arrival))/len(cp)
    avg_service=(np.sum(service))/len(cp)
    avg_TA=(np.sum(TA))/len(cp)
    avg_WT=(np.sum(WT))/len(cp)
    avg_RT=(np.sum(RT))/len(cp)
    
    #printing simulation table and generating list for gantt chart
    result=[cp,cpl,int_arrival,arrival,service,S,E,cust_serv_no,TA,WT,RT]
    df=pd.DataFrame(result,index=["CP","CPL","Inter-arrival","Arrival","Service","Start","End","Server No","TurnAround","WaitTime","ResponseTime"])
    df=df.transpose()
    pd.set_option('display.max_columns', None)

    for key, value in Servers.items():
        print(f"Server: {key}")
        for nested in value:
            print(" ",nested)
    
    return print(df),print("Average Inter-Arrival Time=",avg_interarrival,"\nAverage Service Time=",avg_service,"\nAverage Turn-Around Time=",avg_TA,"\nAverage Wait Time=",avg_WT,"\nAverage Response Time=",avg_RT),ServerUtilization(Server_util),entVsService(s_no,service),entVsArrival(s_no,arrival),entVsTA(s_no,TA),entVsWT(s_no,WT)        

#testing
GGC(10,8,5,10)
                