from pydantic import BaseModel , EmailStr,AnyUrl,Field,field_validator
from typing import Annotated

class patient_data(BaseModel):
    url:AnyUrl
    email:EmailStr
    @field_validator('email')
    def email_validator(cls,value):
        valid_fields=['pak.com','sahiwal.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_fields:
            raise ValueError('invalid')
        return value
        
def insert_patient_data(a:patient_data):

    print(a.email)
    print(a.url)
    
patient_info={'name':'noman','age':22,'weight':40,'married':True,'allergies':['pollen','dust'],'contact_info':{'phone_number':'0300','address':'sahiwal'},'email':'asim@pa.com','url':'https://noman.com'}

patient1=patient_data(**patient_info)
insert_patient_data(patient1)
