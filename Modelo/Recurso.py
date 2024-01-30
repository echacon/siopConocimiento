#Descripcion del Recurso
from .declarative_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

class UnidadFuncional(Base):
    __tablename__ = 'unidades_funcionales'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    recursos = relationship('recursos_equipo', lazy='dynamics')
    unidadesHijas = relationship('unidades_funcionales', lazy='dynamics')
    unidadPadre = Column(Integer, ForeignKey('unidades_funcionales.id'))

class RecursoEquipo(Base):
    __tablename__ = 'recursos_equipo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    modelo = Column(String(50))
    unidad = Column(Integer, ForeignKey('unidades_funcionales.id'))

