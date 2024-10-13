from pydantic import BaseModel

class dto_user_input(BaseModel):
    active_learning:int
    analytical:int
    communication:int
    complex_problem_solving:int
    creativity:int
    digital_quotience_literacy:int
    entrepreneurship:int
    integrity:int
    interpersonal_skills:int
    leadership:int
    resilience:int

    