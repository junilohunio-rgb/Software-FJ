"""Excepciones personalizadas del sistema Software FJ."""


class ErrorSistema(Exception):
    """Excepción general de la aplicación."""


class ErrorValidacion(ErrorSistema):
    """Se produce cuando un dato no cumple las reglas del sistema."""


class ErrorReserva(ErrorSistema):
    """Se produce cuando una operación de reserva no está permitida."""


class ServicioNoDisponible(ErrorSistema):
    """Se produce cuando se intenta usar un servicio no disponible."""
