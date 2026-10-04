from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def dashboard_health() -> dict[str, str]:
    return {"status": "ok"}
