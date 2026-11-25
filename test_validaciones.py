# Pruebas automáticas de las funciones de validación.

import unittest
from unittest.mock import patch
from email_validator import EmailNotValidError

import validaciones

class TestValidaciones(unittest.TestCase):

    # Pruebas para validar cadenas numéricas.
    def test_es_numerico(self):
        self.assertTrue(validaciones.es_numerico("12345"))
        self.assertFalse(validaciones.es_numerico("12a45"))
        self.assertFalse(validaciones.es_numerico(""))

    # Pruebas para validar nombres.
    def test_nombre_valido(self):
        self.assertTrue(validaciones.nombre_valido("Ana Pérez"))
        self.assertTrue(validaciones.nombre_valido("José García"))
        self.assertFalse(validaciones.nombre_valido(""))
        self.assertFalse(validaciones.nombre_valido("Al"))
        self.assertFalse(validaciones.nombre_valido("Ana123"))

    # Pruebas para formatear nombres.
    def test_formatear_nombres(self):
        resultado = validaciones.formatear_nombres("ana pérez garcía")
        self.assertEqual(resultado, "Ana Pérez García")

    # Pruebas para validar documentos.
    def test_documento_valido(self):
        self.assertTrue(validaciones.documento_valido("DNI", "12345678"))
        self.assertTrue(validaciones.documento_valido("RUC", "20123456789"))
        self.assertTrue(validaciones.documento_valido("CE", "12345"))
        self.assertTrue(validaciones.documento_valido("PASAPORTE", "ABC123"))

        self.assertFalse(validaciones.documento_valido("DNI", "123"))
        self.assertFalse(validaciones.documento_valido("RUC", "30123456789"))
        self.assertFalse(validaciones.documento_valido("OTRO", "12345678"))

    # Pruebas para validar teléfonos.
    def test_telefono_valido(self):
        self.assertTrue(validaciones.telefono_valido("987654321"))
        self.assertFalse(validaciones.telefono_valido("887654321"))
        self.assertFalse(validaciones.telefono_valido("98765"))
        self.assertFalse(validaciones.telefono_valido("98765432A"))

    # Pruebas para validar correos electrónicos.
    # Se simula la respuesta de la biblioteca para evitar
    # depender de consultas DNS durante las pruebas.
    @patch("validaciones.validate_email")
    def test_correo_valido(self, mock_validate):
        self.assertTrue(validaciones.correo_valido("usuario@gmail.com"))

        mock_validate.assert_called_once_with(
            "usuario@gmail.com",
            check_deliverability=True
        )

    @patch("validaciones.validate_email")
    def test_correo_invalido(self, mock_validate):
        mock_validate.side_effect = EmailNotValidError("Correo inválido")

        self.assertFalse(validaciones.correo_valido("correo-invalido"))

    # Pruebas para validar fechas.
    def test_fecha_valida(self):
        self.assertTrue(validaciones.fecha_valida("24/11/2026"))
        self.assertTrue(validaciones.fecha_valida("29/02/2028"))
        self.assertFalse(validaciones.fecha_valida("29/02/2027"))
        self.assertFalse(validaciones.fecha_valida("32/01/2026"))
        self.assertFalse(validaciones.fecha_valida("01/13/2026"))
        self.assertFalse(validaciones.fecha_valida("01/01/2025"))

    # Pruebas para validar horas.
    def test_hora_valida(self):
        self.assertTrue(validaciones.hora_valida("08:30"))
        self.assertTrue(validaciones.hora_valida("23:59"))
        self.assertTrue(validaciones.hora_valida("00:00"))
        self.assertFalse(validaciones.hora_valida("24:00"))
        self.assertFalse(validaciones.hora_valida("12:60"))
        self.assertFalse(validaciones.hora_valida("8:30"))

# Ejecutar las pruebas automáticamente.
if __name__ == "__main__":
    unittest.main()