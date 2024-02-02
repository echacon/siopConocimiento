# paquete procesos
from .declarative_base import Base
from .Documento import DocumentoNegocio
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from sqlalchemy.orm import relationship

class ProcesoNegocio(Base):
    __tablename__='procesos_negocio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
