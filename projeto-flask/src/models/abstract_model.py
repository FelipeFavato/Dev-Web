# abstract_model.py
from pymongo.collection import ReturnDocument, Collection


class AbstractModel:
    # Atributo de classe para poder trabalhar com o banco
    _collection: Collection = None

    # Construtor que recebe como dado inicial um dicionario,
    # pois o mongoDB guarda dicionarios (documentos)
    def __init__(self, data: dict):
        self.data = data

    # Método Insert
    def save(self):
        # Insere no banco os dados guardados na instancia
        result = self._collection.insert_one(self.data)
        inserted_document = self._collection.find_one(
            {"_id": result.inserted_id}
        )
        self.data = inserted_document
        return self.data

    def update(self, data: dict):
        # Por padrão o find_one_and_update retorna o estado anterior do
        # registro, por isso, utilizamos o ReturnDocument.AFTER para
        # retornar a versão pós atualização
        result = self._collection.find_one_and_update(
            {"_id": self.data["_id"]},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )

        self.data = result
        return self.data

    def delete(self):
        self._collection.delete_one({"_id": self.data["_id"]})

    # Faz sentido ser um método de classe (classmethod), pois o retorno
    # sera um objeto existente no banco e nao instanciado por essa classe
    @classmethod
    def find(cls, query: dict = {}):
        # O data vai ser um Cursor (que é um tipo de objeto)
        # E eu quero que retorne um lista, entao uso list comprehension
        data = cls._collection.find(query)
        # Gera objetos a partir do construtor da minha classe
        # Retorna uma lista de objetos instanciados da minha classe com
        # o parametro de cada um dos resultados da query
        return [cls(d) for d in data]

    @classmethod
    def find_one(cls, query: dict = {}):
        data = cls._collection.find_one(query)
        # Retorna um objeto instanciado dessa classe usando as informações
        # do documento recuperado no MongoDB
        return cls(data) if data else None


# Exemplo
# class UserModel(AbstractModel):
#     _collection = db['users']
