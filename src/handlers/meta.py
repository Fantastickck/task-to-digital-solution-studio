from fastapi import APIRouter

from models.meta import MetaData
from services.file import FileService


router = APIRouter()


@router.get('/', response_model=MetaData)
def get_meta_data() -> MetaData:
    file_service = FileService()
    data = file_service.get_files_data()
    return {'data': data}
