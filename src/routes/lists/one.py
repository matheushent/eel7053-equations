from starlette.responses import RedirectResponse
from pydantic import Field, confloat, conlist
from fastapi import APIRouter

from src.models import input, output
from src.utils import responses
from src.utils import vector

import cmath
import math

router = APIRouter(prefix='/list/one')


@router.get('/opu/general/propagation-constant',
            responses={200: {'model': output.Gamma,
                             'description': 'Propagation constant given by alpha and beta: γ = α + jß'}})
async def propagation_constant(omega: confloat(gt=0), sigma: confloat(ge=0), epsilon: confloat(gt=0), mi: confloat(gt=0)):

    gamma = cmath.sqrt(complex(1, -(sigma / (omega * epsilon)))) * \
        complex(0, omega * math.sqrt(mi * epsilon))

    return responses.success({
        'alpha': gamma.real,
        'beta': gamma.imag
    })


@router.get('/opu/general/wave-length', responses={
    200: {'model': output.Lambda, 'description': 'Wave length in meters'}
})
async def wave_length(beta: confloat(gt=0)):

    return responses.success({
        'lambda': 2 * math.pi / beta
    })


@router.get('/opu/general/phase-speed', responses={
    200: {'model': output.V, 'description': 'Phase speed'}
})
async def phase_speed(omega: confloat(gt=0), beta: confloat()):

    if beta == 0:
        return responses.bad_request({'message': 'ß = 0 not supported'})

    return responses.success({
        'v': omega / beta
    })


@router.get('/opu/general/intrinsic-impedance', responses={
    200: {'model': output.Complex, 'description': 'Intrinsic impedance'}
})
async def phase_speed(omega: confloat(gt=0), sigma: confloat(ge=0), epsilon: confloat(gt=0), mi: confloat(gt=0)):

    impedance = (1 / cmath.sqrt(complex(1, -(sigma/(omega * epsilon))))) * math.sqrt(mi / epsilon)

    return responses.success({
        'real': impedance.real,
        'imag': impedance.imag
    })


@router.get('/opu/general/approximation', responses={
    200: {'model': output.Approximation, 'description': 'sigma / (omega * epsilon)'}
})
async def approximation(omega: confloat(gt=0), sigma: confloat(ge=0), epsilon: confloat(gt=0), mi: confloat(gt=0)):

    return responses.success({
        'value': omega / (sigma * epsilon),
        'alpha': (sigma / 2) * math.sqrt(mi / epsilon),
        'beta': omega * math.sqrt(mi * epsilon)
    })


@router.post('/opu/general/poynting', responses={
    200: {'model': output.Poynting, 'description': 'Poynting vector'}
})
async def poynting(E: conlist(item_type=confloat(), min_items=3, max_items=3), H: conlist(item_type=confloat(), min_items=3, max_items=3)):

    return responses.success(output.Poynting(**vector.cross(E, H)))