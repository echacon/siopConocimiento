# creacion de la base de datos de la aplicacion
import Modelo
from Modelo import declarative_base
from Modelo.declarative_base import Base, Session, engine
from Modelo import Producto
from Modelo import Recurso

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)
