SOFTWARE FJ - FASE 4 - PROGRAMACIÓN UNAD

ARCHIVOS DEL PROYECTO
- main.py: punto de entrada y pruebas del sistema.
- excepciones.py: excepciones personalizadas.
- entidades.py: clase abstracta Entidad.
- clientes.py: clase Cliente con datos encapsulados.
- servicios.py: clase abstracta Servicio y tres clases derivadas.
- reservas.py: clase Reserva.
- sistema.py: administración mediante listas.
- software_fj.log: se crea automáticamente al ejecutar el programa.

REQUISITOS
- Python 3 instalado.
- Visual Studio Code recomendado.
- No necesita instalar paquetes externos.
- No utiliza bases de datos.

EJECUCIÓN
1. Extraiga el archivo ZIP.
2. Abra la carpeta Software_FJ_Fase4_Completo en Visual Studio Code.
3. Seleccione Terminal > Nueva terminal.
4. Ejecute: python main.py
   En Windows también puede usar: py main.py

IMPORTANTE
Ejecute main.py. Los demás archivos son módulos importados por el programa principal.

SOBRE LOS MÉTODOS CON VARIAS FORMAS DE USO
Python no implementa sobrecarga tradicional de métodos por firma como otros
lenguajes. En este proyecto se demuestra el uso de parámetros opcionales:
calcular_costo(duracion)
calcular_costo(duracion, descuento=10)
calcular_costo(duracion, descuento=10, impuesto=0.19)
