studentData=[
    {
    
    "roll_no":" " ,
    "name":" ",
    "marks":"",
    },{
    
    "roll_no": " ",
    "name":" ",
    "marks":"",
    },
    {
    
    "roll_no": " ",
    "name":" ",
    "marks":"",
    },
    {
    
    "roll_no":" ",
    "name":" ",
    "marks":"",
    },


    {
    
    "roll_no":" ",
    "name":" ",
    "marks":"",
    },


]
namearr=["Pratiksha","Seeta","Akanksha","Amruta","Roshni"]
markarr=[88,90,79,80,65]
roll_no_arr=[1,2,3,4,5]

for i in range(len(namearr)):
    studentData[i]["roll_no"]=roll_no_arr[i]
    studentData[i]["name"]=namearr[i]
    studentData[i]["marks"]=markarr[i]
     



print(studentData)
