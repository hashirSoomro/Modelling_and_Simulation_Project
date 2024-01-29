import streamlit as st
from MMC_v1_15-1-2024 import MMC,GanttChart,entVsWT,entVsTA,entVsArrival,entVsService,ServerUtilization,avg_values
from MGC_v1_16-1-2024 import MGC
from GMC_v1_22-1-2024 import GMC
from GGC_v1_16-1-2024 import GGC
from MMC_Priority_v1_16-1-2024 import MMC_Priority,GanttChart_Priority

def main():
    st.title('Simulation Project')

     # Create a sidebar for navigation
    page = st.sidebar.selectbox('Select Function', ['MMC', 'MGC', 'GMC', 'GGC', 'MMC with Priority'])

    if page == 'MMC':
        # Take user inputs for MMC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MMC function results
        if st.button('Run MMC'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MMC(lembda, meu, server_no)
            st.subheader('Simulation Table:')
            st.write(df)
            st.subheader('Average Information:')
            st.write(avg_values(int_arrival,cp,service,TA,WT,RT))

        # Display plot results
        if st.button('Generate Plots'):
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    elif page == 'MGC':
        # Take user inputs for MGC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        a = st.number_input('Enter Shape Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        d = st.number_input('Enter Scale Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        p = st.number_input('Enter Shape-Scaling Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MGC function results
        if st.button('Run MGC'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MGC(lembda,a,d,p,server_no)
            st.subheader('Simulation Table:')
            st.write(df)
            st.subheader('Average Information:')
            st.write(avg_values(int_arrival,cp,service,TA,WT,RT))

        # Display plot results
        if st.button('Generate Plots'):
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    if page == 'GMC':
        # Take user inputs for GMC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        sigma = st.number_input('Enter Sigma:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display GMC function results
        if st.button('Run GMC'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= GMC(lembda,meu,sigma,server_no)
            st.subheader('Simulation Table:')
            st.write(df)
            st.subheader('Average Information:')
            st.write(avg_values(int_arrival,cp,service,TA,WT,RT))

        # Display plot results
        if st.button('Generate Plots'):
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)
    
    elif page == 'GGC':
        # Take user inputs for GGC function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        a = st.number_input('Enter Shape Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        d = st.number_input('Enter Scale Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        p = st.number_input('Enter Shape-Scaling Parameter of Distribution:', min_value=0.01, step=0.01, format='%f', value=1.0)
        sigma = st.number_input('Enter Sigma:', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display GGC function results
        if st.button('Run GGC'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= GGC(meu,a,d,p,sigma,server_no)
            st.subheader('Simulation Table:')
            st.write(df)
            st.subheader('Average Information:')
            st.write(avg_values(int_arrival,cp,service,TA,WT,RT))

        # Display plot results
        if st.button('Generate Plots'):
            GanttChart(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

    elif page == 'MMC with Priority':
        # Take user inputs for MMC with Priority function
        lembda = st.number_input('Enter Lambda (Arrival Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        meu = st.number_input('Enter Meu (Service Rate):', min_value=0.01, step=0.01, format='%f', value=1.0)
        server_no = st.number_input('Enter Number of Servers:', min_value=1, step=1, value=1)

        # Display MMC with Priority function results
        if st.button('Run MMC with Priority'):
            df,int_arrival,cp,service,TA,WT,RT,Servers,s_no,arrival,server_info= MMC_Priority(lembda, meu, server_no)
            st.subheader('Simulation Table:')
            st.write(df)
            st.subheader('Average Information:')
            st.write(avg_values(int_arrival,cp,service,TA,WT,RT))

        # Display plot results
        if st.button('Generate Plots'):
            GanttChart_Priority(Servers)
            entVsWT(s_no,WT)
            entVsTA(s_no,TA)
            entVsArrival(s_no,arrival)
            entVsService(s_no,service)
            ServerUtilization(server_info)

if __name__ == '__main__':
    main()
