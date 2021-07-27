import numpy as np
import scipy.stats as stats
import pymc3 as pm
import pandas as pd
from scipy.special import expit

def simulate_school(seed=1997,years=None,admission_sessions=None,return_df=True,average_admission=20):
    np.random.seed(42)
    days_in_school=np.zeros(0)
    
    other_disputes=np.zeros(0)


    far=np.zeros(0)
    left=np.zeros(0)
    date=np.zeros(0)
    
    far_route=np.zeros(0)
    far_dis=np.zeros(0)
    bus=np.zeros(0)
    bus_dis=np.zeros(0)

    for year in years:
        for day in range(1,366):
            disputes_day_far=np.random.uniform(0,0.2,size=len(far_dis[far==1]))
            far_dis[far==1]=disputes_day_far          
            #far_dis[far==1]=far_dis[far==1]+disputes_day_far
            
            disputes_from_bus=np.random.uniform(0,0.005,size=len(bus_dis[bus==1]))
            bus_dis[bus==1]=bus_dis[bus==1]+disputes_from_bus
            
            days_in_school[left==0]=days_in_school[left==0]+np.ones(len(days_in_school[[left==0]]))
            other_disputes=np.random.uniform(-18,-4,size=(len(other_disputes)))

            

            total_unsatisfaction=other_disputes + far_dis+ bus_dis
            # if day<10:
            #   print(other_disputes)
            #   print('_____________________________')
            left_today=stats.binom(1,p=expit(total_unsatisfaction)).rvs()
            left[left==0]=left[left==0]+left_today[left==0]   # 0 puls 0 is o and 0 plus 1 is 1

            if day in admission_sessions:
                
                new_admissions=pm.Poisson.dist(average_admission).random()
                new_admitted=np.zeros(new_admissions)
                
                adm_date=np.repeat(f'{year}-{day}',new_admissions)
                date=np.append(date,adm_date)


                far_new=stats.binom(1,0.3).rvs(new_admissions)
                days_in_school=np.hstack([days_in_school,new_admitted])
                far=np.hstack([far,far_new])
                
                bus_new=np.zeros(new_admissions)
                bus_new[far_new==1]=stats.binom(1,0.8).rvs(len(bus_new[far_new==1]))
                bus=np.append(bus,bus_new)

                other_disputes_day_1=np.ones(new_admissions)-9
                other_disputes=np.append(other_disputes,other_disputes_day_1)

                far_dis_new=np.zeros(new_admissions)
                far_dis=np.append(far_dis,far_dis_new)
                
                
                bus_dis_new=np.zeros(new_admissions)
                bus_dis=np.append(bus_dis,bus_dis_new)

                left_status_new=np.zeros(new_admissions)
                left=np.append(left,left_status_new)
                
    if return_df==True:
        df=pd.DataFrame()
        df['adm_date']=pd.to_datetime(date,format='%Y-%j')
        df['dropped']=left
        df['days_at_school']=days_in_school
        df['far']=far
        df['bus']=bus
    return df

years=np.array(['2019','2020','2021','2022','2023'])
adm_sessions=np.arange(1,16)
df=simulate_school(years=years,admission_sessions=adm_sessions,average_admission=30)
df.to_csv('data.csv',index=False)