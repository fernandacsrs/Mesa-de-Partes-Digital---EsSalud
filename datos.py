# Variables compartidas del sistema: arreglos paralelos y contador.

# Establece la cantidad máxima de expedientes que permite el sistema.
LIMITE = 100

# Nombres de los archivos utilizados para almacenar los expedientes.
ARCHIVO_BINARIO = "expedientes.dat"
ARCHIVO_PLANO = "expedientes.txt"

# Listas paralelas que almacenan la identificación del expediente.
codigos = []
tiposDoc = []
numerosDoc = []

# Listas que almacenan los datos personales y de contacto del solicitante.
nombresExp = []
correos = []
telefonos = []

# Listas que almacenan la información correspondiente al trámite.
tiposTramite = []
asuntos = []
areasDestino = []

# Listas que almacenan la fecha y hora de ingreso del expediente.
fechas = []
horas = []

# Listas que almacenan el estado y la cantidad de folios del expediente.
estados = []
foliosExp = []

# Contador que registra la cantidad de expedientes ingresados.
contador = 0
