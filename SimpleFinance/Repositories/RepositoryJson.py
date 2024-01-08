import json
import os

class RepositoryJson():
    def __init__(self, fileName):
        self._path = os.path.join(os.getcwd(), 'DataBase', fileName)
        self._serviceResult = {
            "error": None,
            "data": None,
            "isValid": True,
        }

    def Overwrite(self, entity):
        with open(self._path, 'w') as fileToOverwrite:
            try:
                self._serviceResult = {
                    "error": None,
                    "data": entity,
                    "isValid": True,
                }
                json.dump(entity, fileToOverwrite, indent=2)
            except json.decoder.JSONDecodeError as e:
                self._serviceResult = {
                    "error": f"Houve um problema ao sobreescrever o arquivo: {str(e)}",
                    "data": None,
                    "isValid": False,
                }
        return self._serviceResult

    def GetAll(self):
        with open(self._path, 'r') as fileToRead:
            try:
                self._serviceResult = {
                    "error": None,
                    "data": json.load(fileToRead),
                    "isValid": True,
                }
            except json.decoder.JSONDecodeError as e:
                self._serviceResult = {
                    "error": f"Houve um problema ao carregar o arquivo: {str(e)}",
                    "data": None,
                    "isValid": False,
                }
        return self._serviceResult
