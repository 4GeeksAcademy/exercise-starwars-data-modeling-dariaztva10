import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable = False, unique=True)
    password = Column(String(250), nullable = False)
    suscription = Column(String(250), nullable = False)
    name = Column(String(250), nullable = False)
    surname = Column(String(250), nullable = False)

    favoritod = relationship('favoritos', back_populates='usuario')


class Favoritos(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True)
     # Claves foráneas para relacionar con personajes, planetas y vehículos
    personajes_id = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'), nullable=True)

    # Relacion con usuario
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    usuario = relationship('Usuario', back_populates='favoritos')

    # Relaciones con las demás tablas
    personaje = relationship('Personajes')
    planeta = relationship('Planetas')
    vehiculo = relationship('Vehiculos')
    

class Personajes(Base):
    __tablename__ = "personajes"
    id =  id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)


class Planetas(Base):
    __tablename__ = "planetas"
    id =  id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)


class Vehiculos(Base):
    __tablename__ = "vehiculos"
    id =  id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)



    def to_dict(self):
        return {}


#CREANDO LA BASE DE DATOS SQLite
engine = create_engine('sqlite:///test.db')


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png :)")
except Exception as e:
    print("Hubo un problema al generar el diagrama :(")
    raise e
