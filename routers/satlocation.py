import logging
from fastapi import APIRouter, Request, Response, Depends, HTTPException, status
from fastapi.security import APIKeyQuery,OAuth2PasswordBearer
from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope


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
    try:
        return {"satellite_id": satellite_id, "location": "1.2, 103.5"}
    except AuthError as e:
        return Response(status_code=e.status_code, content=e.message)