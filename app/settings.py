from os import environ

class ENV:
    __slots__ = "DB_USERNAME", "DB_PASSWORD", "DB_NAMESPACE", "DB_DATABASE", "DB_HOST", "DB_PORT"

    def __init__(self):
        self.DB_USERNAME = environ.get("DB_USERNAME")
        self.DB_PASSWORD = environ.get("DB_PASSWORD")
        self.DB_NAMESPACE = environ.get("DB_NAMESPACE")
        self.DB_DATABASE = environ.get("DB_DATABASE")
        self.DB_HOST = environ.get("DB_HOST")
        self.DB_PORT = environ.get("DB_PORT")

    def __repr__(self):
        return " ".join((self.DB_USERNAME, self.DB_PASSWORD,
                        self.DB_NAMESPACE, self.DB_DATABASE,
                        self.DB_HOST, self.DB_PORT))

    def db_get(self) -> tuple:
        return (self.DB_USERNAME, self.DB_PASSWORD, self.DB_NAMESPACE,
                self.DB_DATABASE, self.DB_HOST, self.DB_PORT
                )
