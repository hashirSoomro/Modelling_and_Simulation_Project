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

def MMC(lembda,meu,server_no):
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
    priority=[]
    all_curr_priority=[]
    end_now=[]
    pending=[]
    
    value=0
    C_count=-1
    global min_end
    global min_priority
    
    #Generating values for serial number, cummulative probability and cummulative probability lookup
    x=0
    while cpl[-1]<1:
        s_no.append(x)
        value=value+(((math.exp(-lembda))*lembda**x)/math.factorial(x))
        cp.append(float("%.6f"%value))
        cpl.append(cp[-1])
        x+=1
    cpl.pop(-1)

    #Generating priority
    for i in range(len(cp)):
        ran_prior=random.randint(1,3)
        priority.append(ran_prior)

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
        Servers[i]=[[0],[0],[0],[],[]]
    
    service=[2, 1, 5, 4, 2, 3, 8, 1, 1, 3, 2, 2]
    arrival=[0, 4, 5, 6, 7, 8, 8, 11, 12, 13, 16, 17]
    priority=[1, 1, 1, 3, 2, 3, 3, 2, 2, 3, 2, 1]
    #Assigning customers to server
    for i in range(len(arrival)):
        for key, value in Servers.items():
            if len(value[3]) != 0: #S1:value[3]=[[1,6,2],[1,4,3]] S2:value[3]=[[]]
                    for k in range(len(value[3])):
                        if arrival[i]>value[1][-1]: #13>16
                            if priority[i]<value[3][0][0]:
                                value[0].append(value[1][-1])
                                value[1].append(value[1][-1]+value[3][0][-1])
                            else:
                                curr_service=arrival[i]-value[1][-1] #curr_service=17-10=7
                                if curr_service> value[3][0][-1]: #3>2
                                    value[1].append(value[1][-1]+value[3][0][-1])
                                elif curr_service <= value[3][0][-1]: #2<=2
                                    value[1].append(value[1][-1]+curr_service) 
                            value[2].append(value[3][0][0])
                            value[4].append(value[3][0][1])
                            value[3].pop(0)
            if arrival[i]>=value[1][-1]: #3.3>=5 and 3>=4
                

                C_count=C_count+1   #C_count=11
                cust_serv_no.append(key) #cust_serv_no=[]
                value[0].append(arrival[i]) #value[0]=[]
                value[1].append(arrival[i]+service[i]) #value[1]=[]
                value[2].append(priority[i]) # value[2]=[]
                value[4].append(s_no[i]) # value[4]= []
                
                
                break
            
            all_curr_end_time.append(value[1][-1])  # all_curr_end_time=[16,16]
            min_end=min(all_curr_end_time) #min_end=16
            
            all_curr_priority.append(value[2][-1]) #all_curr_priority=[2,3]
            min_priority=min(all_curr_priority) #min_priority=2
        for key, value in Servers.items():
            if i==(len(arrival)-1): #S1:value[3]=[[]] S2:value[3]=[[]]
                for k in range(len(value[3])):
                    if arrival[i]>value[1][-1]: #16>16
                        value[0].append(value[1][-1]) 
                        curr_service=arrival[i]-value[1][-1] #curr_service=20-17=3
                        if curr_service> value[3][0][-1]: #3>2
                            value[1].append(value[1][-1]+value[3][0][-1])
                        elif curr_service <= value[3][0][-1]: #2<=2
                            value[1].append(value[1][-1]+curr_service) 
                        value[2].append(value[3][0][0])
                        value[4].append(value[3][0][1])
                        value[3].pop(0)


        all_curr_end_time.clear()
        all_curr_priority.clear()
        
        if i>C_count:   
            C_count=C_count+1    #C_count=3
            #Case when the minimum priority of the customer being last in server queue is greater than the priority of customer just arrived 
            if min_priority>priority[i]:    #2>2
                for key,value in Servers.items():
                    if min_priority==value[2][-1]: 
                        end_now.append(value[1][-1]) #end_now=[]             
                        min_prior_end_time=min(end_now) #min_prior_end_time=
                end_now.clear()
                        
                for key,value in Servers.items():
                    if min_prior_end_time==value[1][-1] and min_priority==value[2][-1]: 
                        if min_prior_end_time>arrival[i]: #16>14
                            value[3].append([priority[i],s_no[i],service[i]])   #S2:value[3]=[[]]
                            value[3].sort(key= lambda x: x[0],reverse=True)     #S2:value[3]=[[]]
                        if min_prior_end_time<=arrival[i] or i==(len(arrival)-1): #6<=3
                            curr_end=min_prior_end_time
                            for j in range(len(value[3])):
                                value[2].append(value[3][j][0])
                                cust_serv_no.append(value[3][j][1])
                                value[4].append(value[3][j][1])
                                value[0].append(curr_end)
                                value[1].append(curr_end+value[3][j][2])
                                curr_end=curr_end+value[3][j][2]
                            value[3].clear()
                        break
                    
            #Case when the minimum priority of the customer being last in server queue is equal to the priority of customer just arrived        
            if min_priority==priority[i]: #2==2
                for key,value in Servers.items():
                    if min_priority==value[2][-1]: #2==2
                        end_now.append(value[1][-1])  #end_now=[4]
                        min_prior_end_time=min(end_now) #min_prior_end_time=4
                end_now.clear()
                        
                for key,value in Servers.items(): 
                    if min_prior_end_time==value[1][-1] and min_priority==value[2][-1]: #4==4 and 2==2        
                        if min_prior_end_time>arrival[i]: #4>3
                            value[3].append([priority[i],s_no[i],service[i]]) #S1:value[3]=[[1,6,2],[]]
                            value[3].sort(key= lambda x: x[0],reverse=True) #S1:value[3]=[[1,6,2]]
                        if min_prior_end_time<=arrival[i] or i==(len(arrival)-1):
                            curr_end=min_prior_end_time
                            for j in range(len(value[3])):
                                value[2].append(value[3][j][0])
                                value[4].append(value[3][j][1])
                                cust_serv_no.append(value[3][j][1])
                                value[0].append(curr_end)
                                value[1].append(curr_end+value[3][j][2])
                                curr_end=curr_end+value[3][j][2]
                            value[3].clear()

                        break

            #Case when the minimum priority of the customer being last in server queue is less than the priority of customer just arrived
            if min_priority<priority[i]: #1<2
                for key,value in Servers.items():
                    if min_priority==value[2][-1]: #1<2
                        end_now.append(value[1][-1]) #end_now=[2,1]
                        min_prior_end_time=min(end_now)#min_prior_end_time=3
                end_now.clear()

                for key,value in Servers.items():
                    if min_prior_end_time==value[1][-1] and min_priority==value[2][-1]: #3==3 and 1<3
                        if min_prior_end_time>arrival[i]: #3>2
                            service_left = value[1][-1] - arrival[i]  #service_left=1
                            value[3].append([value[2][-1],value[4][-1],service_left]) #value[3]=[[1,2,1]]
                            value[3].sort(key= lambda x: x[0],reverse=True) #value[3]=[[1,2,1]]
                        if min_prior_end_time<=arrival[i] or i==(len(arrival)-1): 
                            curr_end=min_prior_end_time
                            for j in range(len(value[3])):
                                value[2].append(value[3][j][0])
                                cust_serv_no.append(value[3][j][1])
                                value[4].append(value[3][j][1])
                                value[0].append(curr_end)
                                value[1].append(curr_end+value[3][j][2])
                                curr_end=curr_end+value[3][j][2]
                            value[3].clear()

                        cust_serv_no.append(key)                  #cust_serv_no=[1]
                        if arrival[i]<=value[0][-1]:
                            value[0].pop(-1)
                            value[1].pop(-1)
                            value[2].pop(-1)
                            value[4].pop(-1)
                        else:
                            value[1].pop(-1)
                            value[1].append(arrival[i])
                        value[0].append(arrival[i])               # value[0]=[13]
                        value[1].append(arrival[i]+service[i])    # value[1]=[16]
                        value[2].append(priority[i])              # value[2]=[2]
                        value[4].append(s_no[i])                  # value[4]=[7]
                        break

            

    print("Service=",service)
    print("Arrival=",arrival)
    print("Priority=",priority)
    print("Start=",S)
    print("End=",E)
    for key, value in Servers.items():
        value[0].pop(0)
        value[1].pop(0)
        value[2].pop(0)
    for key, value in Servers.items():
        print(f"Server: {key}")
        for nested in value:
            print(" ",nested)
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
    result=[cp,cpl,int_arrival,arrival,service,S,E,cust_serv_no,priority,TA,WT,RT]
    df=pd.DataFrame(result,index=["CP","CPL","Inter-arrival","Arrival","Service","Start","End","Server No","Priority","TurnAround","WaitTime","ResponseTime"])
    df=df.transpose()
    pd.set_option('display.max_columns', None)

    for key, value in Servers.items():
        print(f"Server: {key}")
        for nested in value:
            print(" ",nested)
    
    return print(df),print("Average Inter-Arrival Time=",avg_interarrival,"\nAverage Service Time=",avg_service,"\nAverage Turn-Around Time=",avg_TA,"\nAverage Wait Time=",avg_WT,"\nAverage Response Time=",avg_RT),ServerUtilization(Server_util),entVsService(s_no,service),entVsArrival(s_no,arrival),entVsTA(s_no,TA),entVsWT(s_no,WT)        

#testing
MMC(1.58,2.58,2)
                
