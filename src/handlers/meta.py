import os

from fastapi import APIRouter, HTTPException, status
from config import BASE_PATH

from models.meta import MetaData
from services.file import FileService


router = APIRouter()


@router.get('/', response_model=MetaData)
def get_meta_data() -> MetaData:
    if os.path.isdir(BASE_PATH):
        file_service = FileService(BASE_PATH)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Path to dir is not correct"
        )
    data = file_service.get_files_data()
    return {'data': data}
