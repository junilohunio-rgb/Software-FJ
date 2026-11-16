"""Administración de clientes, servicios y reservas mediante listas."""
import logging
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva
from excepciones import ErrorValidacion


class SistemaSoftwareFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ErrorValidacion("El objeto no corresponde a un cliente.")
        if any(item.identificacion == cliente.identificacion for item in self.clientes):
            raise ErrorValidacion("El cliente ya está registrado.")
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.identificacion)
        return "Cliente registrado correctamente."

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise ErrorValidacion("El objeto no corresponde a un servicio.")
        if any(item.codigo == servicio.codigo for item in self.servicios):
            raise ErrorValidacion("El servicio ya está registrado.")
        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.codigo)
        return "Servicio registrado correctamente."

    def crear_reserva(self, codigo, cliente, servicio, duracion):
        if any(item.identificacion == str(codigo) for item in self.reservas):
            raise ErrorValidacion("El código de reserva ya existe.")
        reserva = Reserva(codigo, cliente, servicio, duracion)
        self.reservas.append(reserva)
        logging.info("Reserva creada: %s", codigo)
        return reserva

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())

    def mostrar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir())

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_informacion())
