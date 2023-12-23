import logging
from fastapi import APIRouter, Request, Response, Depends, HTTPException, status
from fastapi.security import APIKeyQuery,OAuth2PasswordBearer
from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope
import requests
import ephem

api_key_query = APIKeyQuery(name="api_key", auto_error=True)


router = APIRouter()
initialize(
    tenant_id_="8953f2c0-cb9d-4969-926b-c4726bd5de68",
    client_id_="94a86940-adf4-4001-9388-cefaf3c8001d"
)
expected_scope = "data.read"

def validate_api_key(api_key: str = Depends(api_key_query)):
    if api_key != "6bfced44-72df-487e-9003-8f40cf266628":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key

@requires_auth(expected_scope)
@router.get("/{satellite_id}")
async def get_satellite_location(satellite_id: str, api_key: str = Depends(validate_api_key)):
    if satellite_id.upper() == "ISS":
        try:
            try:
                url = 'https://tle.ivanstanojevic.me/api/tle/25544?api_key=8rsVZgPU1iY5192hd4DPbC1rXv8VEU4eQX432HNl'
                response = requests.get(url)
                data = response.json()
                line1 = data['line1']
                line2 = data['line2']
                satellite = ephem.readtle('ISS', line1, line2)
                time = ephem.now()
                time = ephem.localtime(time)
                satellite.compute(time)
            except Exception as e:
                return Response(status_code=500, content=str(e))    
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI":
        try:
            try:
                url = 'https://tle.ivanstanojevic.me/api/tle/42788?api_key=8rsVZgPU1iY5192hd4DPbC1rXv8VEU4eQX432HNl'
                response = requests.get(url)
                data = response.json()
                line1 = data['line1']
                line2 = data['line2']
                satellite = ephem.readtle('SUCHAI', line1, line2)
                time = ephem.now()
                time = ephem.localtime(time)
                satellite.compute(time)
            except Exception as e:
                return Response(status_code=500, content=str(e))    
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI-2":
        try:
            try:
                url = 'https://tle.ivanstanojevic.me/api/tle/52192?api_key=8rsVZgPU1iY5192hd4DPbC1rXv8VEU4eQX432HNl'
                response = requests.get(url)
                data = response.json()
                line1 = data['line1']
                line2 = data['line2']
                satellite = ephem.readtle('SUCHAI-2', line1, line2)
                time = ephem.now()
                time = ephem.localtime(time)
                satellite.compute(time)
            except Exception as e:
                return Response(status_code=500, content=str(e))    
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI-3":
        try:
            try:
                url = 'https://tle.ivanstanojevic.me/api/tle/52191?api_key=8rsVZgPU1iY5192hd4DPbC1rXv8VEU4eQX432HNl'
                response = requests.get(url)
                data = response.json()
                line1 = data['line1']
                line2 = data['line2']
                satellite = ephem.readtle('SUCHAI-3', line1, line2)
                time = ephem.now()
                time = ephem.localtime(time)
                satellite.compute(time)
            except Exception as e:
                return Response(status_code=500, content=str(e))    
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)    
    elif satellite_id == "PlantSAT":
        try:
            try:
                url = 'https://tle.ivanstanojevic.me/api/tle/52188?api_key=8rsVZgPU1iY5192hd4DPbC1rXv8VEU4eQX432HNl'
                response = requests.get(url)
                data = response.json()
                line1 = data['line1']
                line2 = data['line2']
                satellite = ephem.readtle('PlantSAT', line1, line2)
                time = ephem.now()
                time = ephem.localtime(time)
                satellite.compute(time)
            except Exception as e:
                return Response(status_code=500, content=str(e))    
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    
    return Response(status_code=404, content="Satellite not found")