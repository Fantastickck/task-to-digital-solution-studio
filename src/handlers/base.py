from fastapi import APIRouter

from handlers import meta


router = APIRouter()

router.include_router(meta.router, prefix='/meta', tags=['meta'])
