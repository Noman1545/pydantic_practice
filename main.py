from pydantic import BaseModel

class patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    
patient_info={'name':'noman','age':22,"weight":60,"married":True}
patient1=patient(**patient_info)

def show_data(p:patient):
    print(p.name)
    print(p.age)
    print(p.weight)
    print(p.married)
show_data(patient1)