employe_data=[
    {
    
    "emp_id":" " ,
    "name":" ",
    "Birth_date":"",
    },{
    
    "emp_id": " ",
    "name":" ",
    "Birth_date":"",
    },
    {
    
    "emp_id": " ",
    "name":" ",
    "Birth_date":"",
    },
    {
    
    "emp_id":" ",
    "name":" ",
    "Birth_date":"",
    },


    {
    
    "emp_id":" ",
    "name":" ",
    "Birth_date":"",
    },


]
namearr=["Pratiksha","Seeta","Akanksha","Amruta","Roshni"]
birth_date=["1-5-2004","2-5-2003","23-3-2004","25-5-200","10-8-2004"]
empp_id=[1,2,3,4,5]

for i in range(len(namearr)):
    employe_data[i]["emp_id"]=empp_id[i]
    employe_data[i]["name"]=namearr[i]
    employe_data[i]["Birth_date"]=birth_date[i]
     



print(employe_data)
