from pydantic import BaseModel

class PropagationConstant(BaseModel):

    omega: float
    mi: float
    epsilon: float
    sigma: float