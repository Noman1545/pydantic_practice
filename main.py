from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Annotated
class patient(BaseModel):
    name:Annotated[str ,Field(max_length=20,min_length=3,title='main',description='add your name')]
    age:Annotated[int,Field(strict=True)]
    weight:float | None =Field(default=None,gt=30)
    married:Annotated[bool,Field(default=True)]
    diseases:list[str]
    contact:dict[str,str]
    email:EmailStr
    url:AnyUrl
    
patient_info={'name':'noman','age':22,"married":True,"diseases":['flue','fever','cold'],'contact':{"mob":"0324","house":'389'},"email":'asim@gmail.com',"url":'https://linkedin.com'}
patient1=patient(**patient_info)

def show_data(p:patient):
    print(p.name)
    print(p.age)
    print(p.weight)
    print(p.married)
    print(p.diseases)
    print(p.contact)
    print(p.email)
    print(p.url)
show_data(patient1)