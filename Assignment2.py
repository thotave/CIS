curr_date= "202208"
curr_quar= "Q3"
def date_fun(curr_date,curr_quar):
    dic=dict()
    current_year=curr_date[:4]
    current_month=curr_date[4:]
    current_quar_int=int(curr_quar[1:])
    future_year=int(current_year)+1

    previous_month=int(current_month)-1
    if previous_month==0:
        previous_month=12
    previous_year=int(current_year)-1
    if previous_month<10:
        previous_month="0"+str(previous_month)



    dic["pre_month"]=str(current_year)+str(previous_month)

    previous_quarter=str(current_quar_int-1)
    if previous_quarter==0:
        previous_quarter=4
    p_quarter=curr_quar[:1]+previous_quarter
    
    dic["pre_quarter"]=p_quarter+"_"+current_year

    future_month=(int(current_month)+11)%12
    if future_month<10:
        future_month="0"+str(future_month)

    dic["fut_month"]=str(future_year)+str(future_month)

    dic["quart"]=curr_quar+"_"+current_year

    return dic

print(date_fun(curr_date,curr_quar))




