from pydantic import BaseModel,field_validator,EmailStr

class patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    email:EmailStr
    
    @field_validator('name')
    def validate_name(cls,value):
        return value.upper()
        
    @field_validator('email')
    def  email_validator(cls,value):
        valid=['pak.com','punjab.com']
        new_value=value.split('@')[-1]
        if new_value in valid:
            return value
        raise ValueError('invalid')
       
patient_info={ 'name':'noman','age':22,'weight':60,'height':1.8,'email':'nom@pak.com'}

def show(p:patient):
    print(p.name)
    print(p.age)
    print(p.weight)
    print(p.height)
    print(p.email)
try:   
    patient1=patient(**patient_info)
    show(patient1)
except Exception as e:
    print("invalid details",e)