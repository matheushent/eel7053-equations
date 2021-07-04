from pydantic import BaseModel, confloat


class E(BaseModel):

    Ex: float
    alpha: float
    omega: float
    beta: float


class Gamma(BaseModel):

    alpha: float
    beta: float


class Lambda(BaseModel):

    lambda: confloat(gt=0)


class V(BaseModel):

    v: confloat(gt=0)


class Complex(BaseModel):

    real: float
    imag: float


class Approximation(Gamma):

    value: float


class Poynting(BaseModel):

    x: float
    y: float
    z: float