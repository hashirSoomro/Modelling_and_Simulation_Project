#importing required libraries
import math
import pandas as pd
import random
import numpy as np
import streamlit as st
from scipy.stats import norm
import matplotlib.pyplot as plt

#Graph plot Section
def GanttChart(Servers):
    for key, value in Servers.items():
        # Create a Gantt chart using Matplotlib
        fig, ax = plt.subplots()
        for i, customer in enumerate(value[2]):
            ax.barh(customer, width=value[1][i] - value[0][i], left=value[0][i], height=0.5, label=f'Customer {customer}')

        # Beautify the plot
        if value[1]==[]:
            plt.xticks(range(0, 10))
        else:
            max_cust_time=max(value[1]) + 1
            plt.xticks(range(0, max_cust_time,math.ceil(max_cust_time/10)))  # Set x-axis ticks to integers
        plt.yticks(value[2])  # Set y-axis ticks to customer IDs
        plt.xlabel('Time')
        plt.ylabel('Customer ID')
        plt.title('Gantt Chart for Server '+f"{key}")
        #plt.show()
        st.pyplot()

def entVsWT(s_no,WT):
    plt.bar(s_no, WT, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Wait Time')
    plt.title('Wait Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    #plt.show()
    st.pyplot()

def entVsTA(s_no,TA):
    plt.bar(s_no, TA, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Turn Around Time')
    plt.title('Turn Around Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    #plt.show()
    st.pyplot()    

def entVsArrival(s_no,arrival):
    plt.bar(s_no, arrival, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Arrival Time')
    plt.title('Arrival Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    #plt.show()
    st.pyplot()
    
def entVsService(s_no,service):
    plt.bar(s_no, service, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Service Time')
    plt.title('Service Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    #plt.show()
    st.pyplot()
    
def ServerUtilization(server_info):
    for i in range(len(server_info)):
        idleTime=server_info[i][0]/server_info[i][1]
        server_util=1-idleTime
        y = np.array([server_util,idleTime])
        mylabels = ["Utilized Server", "Idle time"]

        plt.pie(y, labels = mylabels,autopct='%1.1f%%')
        plt.title("Server Utilization for Server "+f"{server_info[i][2]}")
        #plt.show()
        st.pyplot()
        
def avg_values(int_arrival,cp,service,TA,WT,RT):
    #Avg values of the time given
    avg_interarrival="Average Inter-Arrival Time="+f"{(np.sum(int_arrival))/len(cp)}"
    avg_service="Average Service Time="+f"{(np.sum(service))/len(cp)}"
    avg_TA="Average Turn-Around Time="+f"{(np.sum(TA))/len(cp)}"
    avg_WT="Average Wait Time="+f"{(np.sum(WT))/len(cp)}"
    avg_RT="Average Response Time="+f"{(np.sum(RT))/len(cp)}"
    #avg_info="Average Inter-Arrival Time="+f"{avg_interarrival}"+"Average Service Time="+f"{avg_service}"+"Average Turn-Around Time="+f"{avg_TA}"+"Average Wait Time="+f"{avg_WT}"+"\nAverage Response Time="+f"{avg_RT}"
    return avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT

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
    server_info=[]
    value=0
    C_count=-1
    global min_end

    #Generating values for serial number, cummulative probability and cummulative probability lookup
    x=0
    while cpl[-1]<1:
        s_no.append(x)
        value=value+(((math.exp(-lembda))*lembda**x)/math.factorial(x))
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
        Servers[i]=[[0],[0],[]]
    
    #Assigning customers to server
    for i in range(len(arrival)):
        for key, value in Servers.items():
            if arrival[i]>=value[1][-1]:
                C_count=C_count+1
                cust_serv_no.append(key)
                value[2].append(i+1)
                value[0].append(arrival[i])
                S.append(arrival[i])
                value[1].append(arrival[i]+service[i])
                E.append(arrival[i]+service[i])
                break
            all_curr_end_time.append(value[1][-1])
            min_end=min(all_curr_end_time)
            
        all_curr_end_time.clear()
        if i>C_count:
            C_count=C_count+1
            for key, value in Servers.items():
                if value[1][-1]==min_end:
                    cust_serv_no.append(key)
                    value[2].append(i+1)
                    value[0].append(min_end)
                    S.append(min_end)
                    value[1].append(min_end+service[i])
                    E.append(min_end+service[i])
                    break
    all_last_end=[]
    for key, value in Servers.items():
        value[0].pop(0)
        value[1].pop(0)
        if value[1]==[]:
            pass
        else:
            all_last_end.append(value[1][-1])
    max_end=max(all_last_end)

    #Server Utilization    
    for key,value in Servers.items():
        if value[0] == []:
            idle_time=max_end
            server_info.append([max_end,max_end,key])
        else:
            idle_time=value[0][0]
            for i in range(len(value[0])-1):

                if value[1][i]<value[0][i+1]:
                    idle_now=value[0][i+1]-value[1][i]
                    idle_time=idle_time+idle_now
            server_info.append([idle_time,max_end,key])
    
    #Generating values for TurnAround time,Wait time and Response Time
    for i in range(len(cp)):
        TA.append(E[i]-arrival[i])
        WT.append(TA[i]-service[i])
        RT.append(S[i]-arrival[i])
    
    #printing simulation table and generating list for gantt chart
    result=[cp,cpl,int_arrival,arrival,service,S,E,cust_serv_no,TA,WT,RT]
    df=pd.DataFrame(result,index=["CP","CPL","Inter-arrival","Arrival","Service","Start","End","Server No","TurnAround","WaitTime","ResponseTime"])
    df=df.transpose()
    df.index = df.index + 1
    pd.set_option('display.max_columns', None)

    for key, value in Servers.items():
        print(f"Server: {key}")
        for nested in value:
            print(" ",nested)
    print(df)
    return df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info

##testing
#MMC(1.58,2.5,10)
                
