import logging
from fastapi import APIRouter, Request, Response, Depends, HTTPException, status
import fastapi
from fastapi.security import APIKeyQuery,OAuth2PasswordBearer
from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope
import requests
import ephem
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient


credential = ManagedIdentityCredential()
key_vault_url = "https://astroapi-vault.vault.azure.net/"
client = SecretClient(vault_url=key_vault_url, credential=credential)
secret_name = "apikey"
secret_name2 = "apikey2"
secret_name3 = "client-app"
retrieved_secret = client.get_secret(secret_name)
retrieved_secret2 = client.get_secret(secret_name2)
retrieved_secret3 = client.get_secret(secret_name3)
api_key_query = APIKeyQuery(name="api_key", auto_error=True)


router = APIRouter()
#Commented lines are for authentication of Azure AD B2C OAUTH2.0
#initialize(
 #   tenant_id_="",
  #  client_id_=""
#)
#expected_scope = ""

def validate_api_key(request: Request,api_key: str = Depends(api_key_query)):
    
    if request.client.host == 'https://www.derquisanhueza.cl':
        return api_key
    
    elif api_key != retrieved_secret2.value:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key

#@requires_auth
@router.get("/{satellite_id}")
async def get_satellite_location(request: Request,satellite_id: str, api_key: str = Depends(validate_api_key)):
    #try:
    #   validate_scope(expected_scope, request)
    #except AuthError as ae:
    #   return fastapi.Response(content=ae.error_msg, status_code=ae.status_code)
    if satellite_id.upper() == "ISS":
        try:
            
            try:
                url = f"https://tle.ivanstanojevic.me/api/tle/25544?api_key={retrieved_secret.value}"
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
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "elevation": str(satellite.elevation), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI":
        try:
            try:
                url = f"https://tle.ivanstanojevic.me/api/tle/42788?api_key={retrieved_secret.value}"
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
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "elevation": str(satellite.elevation), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI-2":
        try:
            try:
                url = url = f"https://tle.ivanstanojevic.me/api/tle/52192?api_key={retrieved_secret.value}"
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
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "elevation": str(satellite.elevation), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    elif satellite_id.upper() == "SUCHAI-3":
        try:
            try:
                url = f"https://tle.ivanstanojevic.me/api/tle/52191?api_key={retrieved_secret.value}"
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
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "elevation": str(satellite.elevation), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)    
    elif satellite_id.upper() == "PLANTSAT":
        try:
            try:
                url = f"https://tle.ivanstanojevic.me/api/tle/52188?api_key={retrieved_secret.value}"
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
            return {"satellite": satellite_id, "location": {"latitude": str(satellite.sublat), "longitude": str(satellite.sublong), "elevation": str(satellite.elevation), "timestamp": str(time)}}
        except AuthError as e:
            return Response(status_code=e.status_code, content=e.message)
    
    return Response(status_code=404, content="Satellite not found")