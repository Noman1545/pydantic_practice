from os import name

from pydantic import BaseModel

class Adress(BaseModel):
    house:int
    street:int
    block:str
    
class patient(BaseModel):
    name:str
    age:int
    adress:Adress
    
adress_info={'house':389,'street':14,'block':'DHA'}
adress1=Adress(**adress_info)
patient_info={ 'name':'noman','age':22,'adress':adress1}
patient1=patient(**patient_info)

def show(p:patient):
    print(p.name)
    print(p.age)
    print(p.adress)
    print(p.adress.house)
    print(p.adress.block)
show(patient1)
temp=patient1.model_dump_json(include=['name','age'])

print(type(temp))