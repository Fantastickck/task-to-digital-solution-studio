from fastapi import APIRouter

from services.file import FileService


router = APIRouter()


@router.get('/')
def get_meta_data():
    file_service = FileService()
    data = file_service.get_files_data()
    return {'data': data}
    