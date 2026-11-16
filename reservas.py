"""Clase Reserva: relaciona cliente, servicio, duración y estado."""
from datetime import datetime
import logging
from entidades import Entidad
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorValidacion, ErrorReserva, ServicioNoDisponible


class Reserva(Entidad):
    def __init__(self, codigo, cliente, servicio, duracion):
        super().__init__(codigo)

        if not isinstance(cliente, Cliente):
            raise ErrorValidacion("Debe seleccionar un cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ErrorValidacion("Debe seleccionar un servicio válido.")

        servicio.validar_parametros(duracion)
        if not servicio.disponible:
            raise ServicioNoDisponible("El servicio no está disponible.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ErrorReserva("Solo se pueden confirmar reservas pendientes.")
        if not self.servicio.disponible:
            raise ServicioNoDisponible("El servicio no está disponible.")
        self.estado = "Confirmada"
        logging.info("Reserva %s confirmada.", self.identificacion)
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.estado != "Confirmada":
            raise ErrorReserva("Solo se pueden cancelar reservas confirmadas.")
        self.estado = "Cancelada"
        logging.info("Reserva %s cancelada.", self.identificacion)
        return "Reserva cancelada correctamente."

    def procesar(self, *args, **kwargs):
        if self.estado != "Confirmada":
            raise ErrorReserva("La reserva debe estar confirmada para calcular el costo.")
        return self.servicio.calcular_costo(self.duracion, *args, **kwargs)

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.identificacion} | Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | Duración: {self.duracion} | "
            f"Estado: {self.estado}"
        )
