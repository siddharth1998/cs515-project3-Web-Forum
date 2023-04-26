from flask import Flask,request
import threading
import secrets

from secrets import randbelow

from datetime import timezone

import datetime

app = Flask(__name__)

main_list=[]
sem = threading.Semaphore()

@app.get("/random/<int:sides>")
def roll(sides):
    if sides <= 0:
        return { 'err': 'need a positive number of sides' }, 400
    
    return { 'num': randbelow(sides) + 1 }

def time_bata():
    return datetime.datetime.now(timezone.utc).isoformat()

@app.post("/post")
def post():
    global main_list,sem
    if request.method=="POST":
       
       # can be converted into a function which will be used in other methods
        if len((request.json.keys()))>1 or len((request.json.keys()))==0:
            return {"err":"empty body sent"},400 
        if "msg" in request.json:
            pass
        else:
            return {"err":"msg not found"},400
        if type(request.json["msg"])!=str:
            return {"err":"msg value is not a str type"},400
        print(time_bata())
        sem.acquire()
        flag=True
        for i in main_list:
            
            if "id" in i:
                temp_id=i["id"]
                flag=False
            else:
                flag=True
        if flag==True:
            temp_id=0
            pass
        else:
            temp_id=temp_id+1
            flag=False
        temp_dict={"id":temp_id,"key":secrets.token_hex(32),"timestamp":time_bata(),"msg":request.json["msg"]}
        main_list.append(temp_dict)
        sem.release()
        return {"id":temp_dict["id"],"key":temp_dict["key"],"timestamp":temp_dict["timestamp"]},200
    else:
        return {"err":"Parameters Not Inclucded or this resource not found"},404
    
def exsistence_checker(input_id):
    global main_list, sem
    flag=False
    for index,i in enumerate(main_list):
        if input_id==i["id"]:
            flag=True
            temp_dict=i
            break
    if flag==False:
        return False
    else:
        return temp_dict,index
        # return {"err":"id not found"},404


@app.get("/post/<int:input_id>")
def get(input_id):
    global main_list,sem
    
    if request.method=="GET":
        temp_dict=exsistence_checker(input_id)
        if temp_dict==False:
            return {"err":"id not found"},404
        else:
            temp_dict=temp_dict[0]
            res={"id":input_id,"timestamp":temp_dict["timestamp"],"msg":temp_dict["msg"]}
            return res,200

@app.delete("/post/<int:input_id>/delete/<string:input_key>")
def delete(input_id,input_key):
    global main_list,sem
    if request.method=="DELETE":
        
        temp_dict=exsistence_checker(input_id)
        if temp_dict==False:
            return {"err":"id not found"},404
        else:
            index=temp_dict[1]
            temp_dict=temp_dict[0]
            if temp_dict["key"]==input_key:
               sem.acquire()
               main_list.pop(index)
               sem.release()
               return {"id":input_id,"key":temp_dict["key"],"timestamp":temp_dict["timestamp"]}
            else:
                return {"err":"forbidden"},403 
        
        pass