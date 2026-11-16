"""Programa principal de Software FJ. Ejecutar: python main.py"""
import logging
from sistema import SistemaSoftwareFJ
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from excepciones import ErrorSistema, ErrorValidacion

logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_error(numero, error):
    """Registra en el log cada error controlado durante las pruebas."""
    logging.exception("Operación %s: %s", numero, error)


def ejecutar_sistema():
    sistema = SistemaSoftwareFJ()

    print("\n==============================================")
    print("       SOFTWARE FJ - SISTEMA DE GESTIÓN")
    print("==============================================")

    # Operación 1: registrar primer cliente válido.
    cliente1 = Cliente("1001", "Carlos Pérez", "carlos@gmail.com", "3001234567")
    print("1.", sistema.registrar_cliente(cliente1))

    # Operación 2: registrar segundo cliente válido.
    cliente2 = Cliente("1002", "María Gómez", "maria@gmail.com", "3101234567")
    print("2.", sistema.registrar_cliente(cliente2))

    # Operación 3: intentar registrar un cliente inválido.
    try:
        Cliente("1003", "", "correo_invalido", "123")
    except ErrorSistema as error:
        registrar_error(3, error)
        print("3. Error de cliente controlado:", error)

    # Operación 4: registrar servicio de salas.
    sala = ReservaSala("S01", "Sala de reuniones", 50000)
    print("4.", sistema.registrar_servicio(sala))

    # Operación 5: registrar servicio de alquiler de equipos.
    equipo = AlquilerEquipos("S02", "Computadores", 30000)
    print("5.", sistema.registrar_servicio(equipo))

    # Operación 6: registrar servicio de asesorías.
    asesoria = AsesoriaEspecializada("S03", "Asesoría informática", 80000)
    print("6.", sistema.registrar_servicio(asesoria))

    # Operación 7: intentar crear un servicio con tarifa inválida.
    try:
        ReservaSala("S04", "Sala inválida", -100)
    except ErrorSistema as error:
        registrar_error(7, error)
        print("7. Error de servicio controlado:", error)

    # Operación 8: crear y confirmar una reserva correcta.
    reserva = sistema.crear_reserva("R001", cliente1, sala, 2)
    print("8.", reserva.confirmar())

    # Operación 9: calcular costo con tarifa normal (parámetros opcionales).
    print("9. Costo normal con impuesto:", reserva.procesar())

    # Operación 10: calcular costo con descuento e impuesto personalizados.
    print("10. Costo con descuento:", reserva.procesar(descuento=10, impuesto=0.19))

    # Operación 11: intentar crear reserva con duración incorrecta.
    try:
        sistema.crear_reserva("R002", cliente2, equipo, -2)
    except ErrorSistema as error:
        registrar_error(11, error)
        print("11. Error de reserva controlado:", error)

    # Operación 12: cancelar la reserva confirmada.
    print("12.", reserva.cancelar())

    # Intento adicional: confirmar nuevamente una reserva ya cancelada.
    try:
        reserva.confirmar()
    except ErrorSistema as error:
        registrar_error("adicional", error)
        print("Error de operación controlado:", error)

    # Demostración de try/except/else/finally.
    print("\n--- PRUEBA try/except/else/finally ---")
    try:
        resultado = 100 / 2
    except ZeroDivisionError as error:
        registrar_error("división", error)
        print("Error matemático:", error)
    else:
        print("Operación matemática correcta:", resultado)
    finally:
        print("Bloque finally ejecutado.")

    # Demostración de encadenamiento de excepciones.
    print("\n--- PRUEBA DE EXCEPCIÓN ENCADENADA ---")
    try:
        try:
            int("dato incorrecto")
        except ValueError as error:
            raise ErrorValidacion("No fue posible convertir el dato.") from error
    except ErrorValidacion as error:
        registrar_error("encadenamiento", error)
        print("Excepción controlada:", error)

    # Resumen final.
    print("\n--- CLIENTES REGISTRADOS ---")
    sistema.mostrar_clientes()
    print("\n--- SERVICIOS REGISTRADOS ---")
    sistema.mostrar_servicios()
    print("\n--- RESERVAS REGISTRADAS ---")
    sistema.mostrar_reservas()
    print("\nEl sistema terminó las pruebas.")
    print("Consulte software_fj.log para revisar eventos y errores.")


if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except Exception:
        logging.exception("Error inesperado en el programa principal.")
        print("Ocurrió un error inesperado. Revise software_fj.log.")
    finally:
        print("Programa Software FJ finalizado.")
