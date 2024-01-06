import pandas as pd
import sys
inputt=sys.stdin.read()
############################### read_csv first_output.csv ####################################
first_data=pd.read_csv(f'{inputt}/first_output.csv')
############################### your code goes here ##########################################
first_data # your dataframe
# please write your data manipulation here

print("log 1")

















############################### your code ends here ###########################################
first_data.to_csv(f'{inputt}/second_output.csv',index=False) # can replace (dont change second_output.csv)
############################### write_csv second_output.csv ###################################
