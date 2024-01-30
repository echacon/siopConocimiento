#Modulo para la descripción del producto y su modelo
from .declarative_base import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    codigo_interno = Column(String(20))
    es_fabricado = Column(Boolean)
    es_adquirido = Column(Boolean)
    es_final = Column(Boolean)
    es_insumo = Column(Boolean)
    es_intermedio = Column(Boolean)
class Modelo_Producto(Base):
    __tablename__ = "modelos_producto"
    id = Column(Integer, primary_key=True)
    producto = Column(Integer, ForeignKey('productos.id'))
    fecha_modelo = Column(Date)
    nombre_modelo = Column(String(50))
    formula = relationship("Formula", uselist=False, backref="modelo_producto")
    dinamica =  relationship("ModeloProductoDinamica", uselist=False, backref="modelo_producto")
class Formula(Base):
    __tablename__='formulas'
    id = Column(Integer, primary_key=True)
    modelo_producto = Column(Integer, ForeignKey('modelos_producto.id')) 
class ModeloProductoDinamica(Base):
    __tablename__='mod_prod_dinamica'
    id = Column(Integer, primary_key=True)
    modelo_producto = Column(Integer, ForeignKey('modelos_producto.id')) 