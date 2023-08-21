def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura

# Crie a classe Database. Não precisa colocar nada dentro dela,
# somente a palavra reservada pass.


class Database:
    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port: str | int = ''  # Opcional
    ) -> None:
        self.dialect = dialect
        self.user = user
        self.host = host
        self.password = password
        self.database = database
        if not port:
            if dialect == "mysql":
                port = 3306
            elif dialect == "postgres":
                port = 5432
            else:
                raise ValueError(
                    "invalid default `port` for unrecognized `dialect`"
                )
        if type(port) == str and not port.isnumeric():
            raise ValueError("`port` must have a numeric value")

        self.connection_url = (
            f"{dialect}://{user}:{password}@{host}:{port}/{database}"
        )


db_1 = Database()
db_2 = Database()

# Crie um método construtor para a classe Database criada
# no exercício 3. O método deve receber os seguintes parâmetros:

# dialect, user, host, password, database
# port (opcional)
# O parâmetro port pode ser do tipo str ou int, devendo ser
# um valor numérico, levantando ValueError caso contrário.
# Os demais parâmetros devem ser do tipo str.
