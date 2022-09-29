from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Tarea(Base):

    __tablename__ = "tarea"
    __table_args__ = {'sqlite_autoincrement': True}
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(255), nullable=False)
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha

    def __repr__(self):
        return f"Tarea: {self.id_tarea} -> {self.contenido}, {self.hecha}"
    
    def __str__(self):
        return f"Tarea: {self.id_tarea} -> {self.contenido}, {self.hecha}"