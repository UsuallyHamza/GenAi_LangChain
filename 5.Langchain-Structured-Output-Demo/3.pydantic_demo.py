from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name: str = 'zain' #default value to set 
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4, default=3.8, description= 'A float value representing the cgpa of the student.')

new_Student = {'age':32, 'email': 'abc@gmail.com', 'cgpa': 3.8}

student = Student(**new_Student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
