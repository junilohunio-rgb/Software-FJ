"""Clase Cliente con encapsulación y validaciones."""
from entidades import Entidad
from excepciones import ErrorValidacion


class Cliente(Entidad):
    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre no puede estar vacío.")
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ErrorValidacion("El correo electrónico no es válido.")

        telefono = str(telefono)
        if not telefono.isdigit() or len(telefono) < 7:
            raise ErrorValidacion("El teléfono debe contener al menos 7 dígitos.")

        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.nombre} | Documento: {self.identificacion} | "
            f"Correo: {self.correo} | Teléfono: {self.telefono}"
        )
