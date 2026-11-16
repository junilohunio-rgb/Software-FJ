"""Clase abstracta para las entidades del sistema."""
from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


class Entidad(ABC):
    """Entidad general identificada mediante un código o documento."""

    def __init__(self, identificacion):
        if identificacion is None or not str(identificacion).strip():
            raise ErrorValidacion("La identificación es obligatoria.")
        self._identificacion = str(identificacion).strip()

    @property
    def identificacion(self):
        """Propiedad de solo lectura para la identificación."""
        return self._identificacion

    @abstractmethod
    def mostrar_informacion(self):
        """Cada entidad concreta debe implementar este método."""
        raise NotImplementedError
