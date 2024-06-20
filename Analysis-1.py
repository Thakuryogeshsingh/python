## Python file for analysis - 1 of TVS data
## Author: Rajan Kapoor
## Company: MediaTechTemple.com

filePath='/mnt/c/Users/dell/Downloads/'
fileName_report='Lost Customer Calling Report March 2024.xlsx'
fileName_export='TVSExport1_pyscript.xlsx'

filePath='/mnt/c/Users/dell/Downloads/LostCustomerSurvey/'
fileName_report='Lost Customer Calling Report Dec 2023.xlsx'
fileName_export='Dec2023TVSExport1_pyscript.xlsx'

import sys

for arg in sys.argv:
    print(arg)
    
import pandas as pd

with pd.ExcelFile(filePath + fileName_report) as xls:  
    Dump_df = pd.read_excel(xls, "Dump", header=1)

Dump_df_NoDS = Dump_df.dropna(subset = ['call connected disposition status'], inplace=False) 
unique_status = pd.unique(Dump_df_NoDS['call connected disposition status']).tolist()

PGM_status = [k for k in unique_status if 'PGM' in k]
AD_status = [k for k in unique_status if 'AD' in k]
TVS_status = [k for k in unique_status if k in ['Visiting same TVSM Workshop',\
                                                'Already booked an appointment with TVSM WS',\
                                                'Planning to Visit Service Centre'] ]
lackofuse_status = [k for k in unique_status if k in ['Vehicle is not getting used much'] ]
personal_status = [k for k in unique_status if k in ['Money Problem',\
                                                     'Could not come due to lack of time',\
                                                     'Shifted to some other city/town'] ]
sold_status = [k for k in unique_status if k in ['Vehicle sold','Vehicle Sold'] ]
others_status = [k for k in unique_status if k == 'Others' ]

Dump_df_NoDS_df = Dump_df_NoDS[['Zone','Area','Model','Dealer Name','Job Type','call connected disposition status']].value_counts()
Dump_df_NoDS_df = Dump_df_NoDS_df.reset_index().rename(columns={"call connected disposition status": "Status", 0: "count"})

Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(PGM_status),'Category'] = 'PGM'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(AD_status), 'Category'] = 'AD'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(TVS_status), 'Category'] = 'TVS'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(lackofuse_status), 'Category'] = 'lackofuse'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(personal_status), 'Category'] = 'personal'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(sold_status), 'Category'] = 'sold'
Dump_df_NoDS_df.loc[Dump_df_NoDS_df['Status'].isin(others_status), 'Category'] = 'others'


dict_replace={'Visiting same TVSM Workshop': 'Visiting same TVSM WS',
'Already booked an appointment with TVSM WS' : 'Booked Appointment with TVS',
             'Planning to Visit Service Centre': 'Planning to visit TVS'}

Dump_df_NoDS_df = Dump_df_NoDS_df.replace({"Status": dict_replace})

dict_replace={'Vehicle Serviced in other AMD/ AD Due to location convinience': 'Closer Location',\
              'Serviced at other TVSM AMD /AD due to bad past service experience' : 'Bad Service Experience'}
Dump_df_NoDS_df = Dump_df_NoDS_df.replace({"Status": dict_replace})

dict_replace={"Serviced at PGM due to bad past service experience at TVSM WS": "Bad Service at TVSM WS",\
              'Serviced at PGM due to convinience of location' : 'Location',\
              'Serviced at PGM due to high service charges at TVSM WS' : 'Lower Charges',\
              'Serviced at PGM as known to customer' : 'Personal Acquaintance',\
              'Serviced at PGM due to convinience of time-Less Waiting Time ( High Service time in TVSM WS)' : 'Less Waiting Time',\
              'Serviced at PGM as behaviour of PGMs are good' : 'Good behaviour',\
              'Serviced at PGM due to time flexibility (Can go anytime/Anyday to PGM)' : 'Flexibility',\
              'Serviced at PGM as they are more reliable' : 'Reliability',\
              'Serviced at PGM as they are much competent': 'Competence'
                                                }
Dump_df_NoDS_df = Dump_df_NoDS_df.replace({"Status": dict_replace})

dict_replace={"Money Problem": "Financial Issues",\
              'Could not come due to lack of time' : 'Lack of Time',\
              'Shifted to some other city/town' : 'Moved to another city',\
              'Vehicle Sold':'Vehicle sold',\
              'Vehicle is not getting used much' : 'Vehicle not used much'}
Dump_df_NoDS_df = Dump_df_NoDS_df.replace({"Status": dict_replace})


with pd.ExcelWriter(filePath+fileName_export) as writer:
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    Dump_df_NoDS_df.to_excel(writer, sheet_name='TVSExport1', index=False)
