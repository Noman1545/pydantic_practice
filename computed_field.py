from pydantic import BaseModel,computed_field

class patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi

patient_info={ 'name':'noman','age':22,'weight':60,'height':1.8}
def show(p:patient):
    print(p.name)
    print(p.age)
    print(p.height)
    print(p.weight)
    print(p.bmi)

patient1=patient(**patient_info)
show(patient1)
