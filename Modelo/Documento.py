from .declarative_base import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from sqlalchemy.orm import relationship

class DocumentoNegocio(Base):
    __tablename__ = 'documento_negocio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    