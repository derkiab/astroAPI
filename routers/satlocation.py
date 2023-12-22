import logging
from fastapi import APIRouter, Request, Response
from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope


router = APIRouter()
initialize(
    tenant_id_="8953f2c0-cb9d-4969-926b-c4726bd5de68",
    client_id_="94a86940-adf4-4001-9388-cefaf3c8001d"
)
expected_scope = "data.read"

@requires_auth(expected_scope)
@router.get("/{satellite_id}")
async def get_satellite_location(req: Request, satellite_id: str):
    try:
        
        return {"satellite_id": satellite_id, "location": "1.2, 103.5"}
    except AuthError as e:
        
        return Response(status_code=e.status_code, content=e.message)
