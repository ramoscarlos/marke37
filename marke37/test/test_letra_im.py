#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Carlos Ramos.

import unittest
from pprint import pprint
import sys
sys.path.insert(0, '../')
from letra_im import LetraIM
from test_letra_base import TestLetraBase

class TestLetraIM(TestLetraBase):
    def test_letra_im_se_puede_instanciar(self):
        letra = LetraIM()

        self.assertIsInstance(letra, LetraIM)

    def test_letra_im_imprime_titulo(self):
        """
        Revisamos que se imprima verso en formato IM
        """

        letra = self._letra_lee_archivo("titulo_y_verso")

        self.assertEqual(len(letra.secciones), 1)

        s = letra.secciones[0]
        self.assertEqual(s.tipo, "verso")
        self.assertEqual(len(s.bloque), 5)
        self.assertEqual(s.bloque[1].imprimir(), "Primer renglón")
        self.assertEqual(s.bloque[2].imprimir(), "Segundo renglón")
        self.assertEqual(s.bloque[3].imprimir(), "Tercer renglón")
        self.assertEqual(s.bloque[4].imprimir(), "Cuarto renglón")

    def test_letra_im_imprime_verso_y_coro(self):
        """
        Revisamos la impresión correcta de verso y coro
        """

        letra = self._letra_lee_archivo("titulo_verso_y_coro")

        self.assertEqual(len(letra.secciones), 2)

        s = letra.secciones[0]
        self.assertEqual(s.tipo, "verso")
        self.assertEqual(len(s.bloque), 5)
        self.assertEqual(s.bloque[1].imprimir(), "Primer renglón")
        self.assertEqual(s.bloque[2].imprimir(), "Segundo renglón")
        self.assertEqual(s.bloque[3].imprimir(), "Tercer renglón")
        self.assertEqual(s.bloque[4].imprimir(), "Cuarto renglón")

        s = letra.secciones[1]
        self.assertEqual(s.tipo, "coro")
        self.assertEqual(len(s.bloque), 5)
        self.assertEqual(s.bloque[1].imprimir(), "*Coro 1*")
        self.assertEqual(s.bloque[2].imprimir(), "*Coro 2*")
        self.assertEqual(s.bloque[3].imprimir(), "*Coro 3*")
        self.assertEqual(s.bloque[4].imprimir(), "*Coro 4*")

    def test_letra_im_imprime_verso_coro_y_puente(self):
        """
        Letra imprime verso, coro, y puente.
        """

        letra = self._letra_lee_archivo("titulo_verso_coro_y_puente")

        s = letra.secciones[0]
        self.assertEqual(s.tipo, "verso")
        self.assertEqual(s.bloque[1].imprimir(), "Primer renglón")

        s = letra.secciones[1]
        self.assertEqual(s.tipo, "coro")
        self.assertEqual(s.bloque[1].imprimir(), "*Coro 1*")

        s = letra.secciones[2]
        self.assertEqual(s.tipo, "puente")
        self.assertEqual(s.bloque[1].imprimir(), "_Puente 1_")

    ###########################################################################
    ### Funciones privadas para cargar los archivos de texto de las letras. ###
    ###########################################################################

    def _letra_lee_archivo(self, nombre_archivo):
        """
        Carga el archivo .me37 en un objeto Letra, mismo que es regresado tras
        leer dicho archivo.
        """

        letra = LetraIM()
        contenido = self._leer_archivo(nombre_archivo)

        return letra.leer(contenido)