import streamlit as st
from MMC_v1_15_1_2024 import MMC,GanttChart,entVsWT,entVsTA,entVsArrival,entVsService,ServerUtilization,avg_values
from MGC_v1_16_1_2024 import MGC
from GMC_v1_22_1_2024 import GMC
from GGC_v1_16_1_2024 import GGC
from MMC_Priority_v1_16_1_2024 import MMC_Priority,GanttChart_Priority
from QueueingMMC import MMC_Queueing
from QueueingMGC import MGC_Queueing
from QueueingGGC import GGC_Queueing

def main():
    st.title('Simulation Project')

     # Create a sidebar for navigation
    page = st.sidebar.selectbox('Select Function', ['MMC', 'MGC', 'GMC', 'GGC', 'MMC with Priority','MMC Queueing','MGC Queueing','GGC Queueing'])

    if page == 'MMC':
        st.subheader('M/M/C Simulation')
        # Take user inputs for MMC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MMC function results
        if st.button('Run M/M/C'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MMC(lembda, meu, server_no)
            avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=avg_values(int_arrival,cp,service,TA,WT,RT)
            st.subheader('Simulation Table:')
            st.dataframe(df.style.format("{:.6}"))
            st.subheader('Average Information:')
            st.write(avg_interarrival)
            st.write(avg_service)
            st.write(avg_TA)
            st.write(avg_WT)
            st.write(avg_RT)

            # Display plot results
            st.set_option('deprecation.showPyplotGlobalUse', False)
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

        

    elif page == 'MGC':
        st.subheader('M/G/C Simulation')
        # Take user inputs for MGC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        a = st.number_input('Enter Shape Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        d = st.number_input('Enter Scale Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        p = st.number_input('Enter Shape-Scaling Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MGC function results
        if st.button('Run M/G/C'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MGC(lembda,a,d,p,server_no)
            avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=avg_values(int_arrival,cp,service,TA,WT,RT)
            st.subheader('Simulation Table:')
            st.dataframe(df.style.format("{:.6}"))
            st.subheader('Average Information:')
            st.write(avg_interarrival)
            st.write(avg_service)
            st.write(avg_TA)
            st.write(avg_WT)
            st.write(avg_RT)

            # Display plot results
            st.set_option('deprecation.showPyplotGlobalUse', False)
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    if page == 'GMC':
        st.subheader('G/M/C Simulation')
        # Take user inputs for GMC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        sigma = st.number_input('Enter Sigma:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display GMC function results
        if st.button('Run G/M/C'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= GMC(lembda,meu,sigma,server_no)
            avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=avg_values(int_arrival,cp,service,TA,WT,RT)
            st.subheader('Simulation Table:')
            st.dataframe(df.style.format("{:.6}"))
            st.subheader('Average Information:')
            st.write(avg_interarrival)
            st.write(avg_service)
            st.write(avg_TA)
            st.write(avg_WT)
            st.write(avg_RT)

            # Display plot results
            st.set_option('deprecation.showPyplotGlobalUse', False)
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)
    
    elif page == 'GGC':
        st.subheader('G/G/C Simulation')
        # Take user inputs for GGC function
        meu = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        a = st.number_input('Enter Shape Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        d = st.number_input('Enter Scale Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        p = st.number_input('Enter Shape-Scaling Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        sigma = st.number_input('Enter Sigma:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display GGC function results
        if st.button('Run G/G/C'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= GGC(meu,a,d,p,sigma,server_no)
            avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=avg_values(int_arrival,cp,service,TA,WT,RT)
            st.subheader('Simulation Table:')
            st.dataframe(df.style.format("{:.6}"))
            st.subheader('Average Information:')
            st.write(avg_interarrival)
            st.write(avg_service)
            st.write(avg_TA)
            st.write(avg_WT)
            st.write(avg_RT)

            # Display plot results
            st.set_option('deprecation.showPyplotGlobalUse', False)
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    elif page == 'MMC with Priority':
        st.subheader('M/M/C with Priority Simulation')
        # Take user inputs for MMC with Priority function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MMC with Priority function results
        if st.button('Run M/M/C with Priority'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MMC_Priority(lembda, meu, server_no)
            avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=avg_values(int_arrival,cp,service,TA,WT,RT)
            st.subheader('Simulation Table:')
            st.dataframe(df.style.format("{:.6}"))
            st.subheader('Average Information:')
            st.write(avg_interarrival)
            st.write(avg_service)
            st.write(avg_TA)
            st.write(avg_WT)
            st.write(avg_RT)

            # Display plot results
            st.set_option('deprecation.showPyplotGlobalUse', False)
            GanttChart_Priority(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    elif page == 'MMC Queueing':
        st.subheader('M/M/C Queuing')
        # Take user inputs for MMC Queueing
        Arrival_Mean=st.number_input('Mean Arrival Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        Service_Mean=st.number_input('Mean Service Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        No_of_server=st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        if st.button('Run M/M/C Queuing'):
            Lq,Wq,Ws,Ls,Pnot=MMC_Queueing(Arrival_Mean,Service_Mean,No_of_server)
            st.write("Wait in Queue (Wq):",Wq)
            st.write("Wait in System (Ws):",Ws)
            st.write("Probability of Server (P):",Pnot)
            st.write("Length of Queue (Lq):",Lq)
            st.write("Length of System (Ls):",Ls)

    elif page == 'MGC Queueing':
        st.subheader('M/G/C Queuing')
        # Take user inputs for MMC Queueing
        Arrival_Mean=st.number_input('Mean Arrival Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        Service_Mean=st.number_input('Mean Service Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        No_of_server=st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)
        ArrivalVariance=st.number_input('Arrival Variance', min_value=1, step=1, value=1)
        ServiceVariance=st.number_input('Service variance', min_value=1, step=1, value=1)

        if st.button('Run M/G/C Queuing'):
            Lq,Wq,Ws,Ls,Pnot=MGC_Queueing(Arrival_Mean,Service_Mean,No_of_server,ArrivalVariance,ServiceVariance)
            st.write("Wait in Queue (Wq):",Wq)
            st.write("Wait in System (Ws):",Ws)
            st.write("Probability of Server (P):",Pnot)
            st.write("Length of Queue (Lq):",Lq)
            st.write("Length of System (Ls):",Ls)

    elif page == 'GGC Queueing':
        st.subheader('G/G/C Queuing')
        # Take user inputs for MMC Queueing
        Arrival_Mean=st.number_input('Mean Arrival Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        Service_Mean=st.number_input('Mean Service Rate:', min_value=0.01, step=0.01, format='%f', value=1.0)
        No_of_server=st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)
        ArrivalVariance=st.number_input('Arrival Variance', min_value=1, step=1, value=1)
        ServiceVariance=st.number_input('Service variance', min_value=1, step=1, value=1)

        if st.button('Run G/G/C Queuing'):
            Lq,Wq,Ws,Ls,Pnot=GGC_Queueing(Arrival_Mean,Service_Mean,No_of_server,ArrivalVariance,ServiceVariance)
            st.write("Wait in Queue (Wq):",Wq)
            st.write("Wait in System (Ws):",Ws)
            st.write("Probability of Server (P):",Pnot)
            st.write("Length of Queue (Lq):",Lq)
            st.write("Length of System (Ls):",Ls)    

    
if __name__ == '__main__':
    main()
