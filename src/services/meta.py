import os
from typing import List


class MetaDataService:

    def __init__(self, dir_path: str) -> None:
        self.dir_path = dir_path

    def __get_type(self, file_name: str) -> str:
        path_to_file = os.path.join(self.dir_path, file_name)
        if os.path.isdir(path_to_file):
            return 'folder'
        return 'file'

    def __get_created_time(self, file_name: str) -> float:
        path_to_file = os.path.join(self.dir_path, file_name)
        created_time = os.stat(path_to_file).st_ctime
        return round(created_time * 1000)

    def get_meta_data(self) -> List[dict]:
        files = os.listdir(self.dir_path)
        data = []
        for f in files:
            self.__get_type(f)
            data.append({
                'name': f,
                'type': self.__get_type(f),
                'time': self.__get_created_time(f)
            })
        return data
