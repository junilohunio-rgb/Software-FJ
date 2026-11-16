"""Clase abstracta Servicio y tres servicios especializados."""
from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


class Servicio(ABC):
    """Define la estructura común de cualquier servicio."""

    def __init__(self, codigo, nombre, tarifa):
        if not codigo or not str(codigo).strip():
            raise ErrorValidacion("El código del servicio es obligatorio.")
        if not nombre or not str(nombre).strip():
            raise ErrorValidacion("El nombre del servicio es obligatorio.")
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise ErrorValidacion("La tarifa debe ser un número positivo.")

        self.codigo = str(codigo).strip()
        self.nombre = str(nombre).strip()
        self.tarifa = float(tarifa)
        self.disponible = True

    def _calcular_total(self, duracion, descuento=0, impuesto=0.19):
        """Lógica común de cálculo; acepta parámetros opcionales."""
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorValidacion("La duración debe ser un número positivo.")
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ErrorValidacion("El descuento debe estar entre 0 y 100.")
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
            raise ErrorValidacion("El impuesto debe estar entre 0 y 1.")

        subtotal = self.tarifa * duracion
        subtotal_descuento = subtotal * (1 - descuento / 100)
        return round(subtotal_descuento * (1 + impuesto), 2)

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """Calcula el costo. Los parámetros opcionales permiten varias formas de uso."""
        raise NotImplementedError

    @abstractmethod
    def describir(self):
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, duracion):
        raise NotImplementedError


class ReservaSala(Servicio):
    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorValidacion("Las horas de reserva de sala deben ser positivas.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        self.validar_parametros(duracion)
        return self._calcular_total(duracion, descuento, impuesto)

    def describir(self):
        return f"{self.nombre}: reserva de salas por hora."


class AlquilerEquipos(Servicio):
    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorValidacion("La duración del alquiler debe ser positiva.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        self.validar_parametros(duracion)
        return self._calcular_total(duracion, descuento, impuesto)

    def describir(self):
        return f"{self.nombre}: alquiler de equipos tecnológicos."


class AsesoriaEspecializada(Servicio):
    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorValidacion("La duración de la asesoría debe ser positiva.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        self.validar_parametros(duracion)
        return self._calcular_total(duracion, descuento, impuesto)

    def describir(self):
        return f"{self.nombre}: asesoría profesional especializada."
