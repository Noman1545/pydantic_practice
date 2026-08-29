from pydantic import BaseModel,model_validator

class patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    
    @model_validator(mode='after')
    
    def mode_check(model):
        if model.weight < 50 and model.height < 1.5:
            raise ValueError ('invalid')
        return model
    
patient_info={ 'name':'noman','age':22,'weight':60,'height':1.8}
def show(p:patient):
    print(p.name)
    print(p.age)
    print(p.height)
    print(p.weight)

patient1=patient(**patient_info)
show(patient1)

    