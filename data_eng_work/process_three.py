import pandas as pd
import sys
inputt=sys.stdin.read()
############################### read_csv first_output.csv ####################################
first_data=pd.read_csv(f'{inputt}/third_output.csv')
############################### your code goes here ##########################################
first_data # your dataframe
# please write your data manipulation here
print("log 3")














############################### your code ends here ##########################################
first_data.to_csv(f'{inputt}/final.csv',index=False) # can replace first_data to any name (dont change second_output.csv)
first_data.to_json(f'{inputt}/api.json',index=False)
############################### write_csv second_output.csv ##################################
