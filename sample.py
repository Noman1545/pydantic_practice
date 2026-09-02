

from pydantic import BaseModel , EmailStr,AnyUrl,Field
from typing import Annotated

class patient_data(BaseModel):
    url:AnyUrl
    email:EmailStr
    name:Annotated[str ,Field(max_length=50,title='name of student',examples='noman')]
    age:int = Field(gt=0,lt=100,strict=True)
    weight:float
    married:bool = Field(default=False)
    allergies: Annotated[list[str] | None,Field(default=None,max_length=50)]
    contact_info:dict[str,str]
   
def insert_patient_data(a:patient_data):
    print(a.name)
    print(a.age)
    print(a.weight)
    print(a.married)
    print(a.allergies)
    print(a.email)
    print(a.url)
    print(a.contact_info)
    
patient_info={'name':'noman','age':22,'weight':40,'married':True,'allergies':['pollen','dust'],'contact_info':{'phone_number':'0300','address':'sahiwal'},'email':'asim@gmail.com','url':'https://noman.com'}

patient1=patient_data(**patient_info)
insert_patient_data(patient1)
