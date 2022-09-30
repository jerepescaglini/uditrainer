'''<Este programa ofrece diferentes ejercicios para refinar el oído respecto a cuestiones relacionadas a la mezcla y masterización.>
    Copyright (C) 2022  Jeremias Pescaglini
    Contact: jerepescaglini@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program. If not, see <https://www.gnu.org/licenses/>.
'''
from random import randrange
from pyo import Delay, EQ, Mixer, Server, Fader, SfPlayer
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox
from pydub import AudioSegment
from interfazmain import Ui_Proyecto
import os
import atexit
import sys
from math import log10

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Proyecto()
        self.ui.setupUi(self.main_win)
        self.ui.paneo_bt.clicked.connect(self.show_paneo)
        self.ui.stackedWidget.setCurrentWidget(self.ui.recepcion)
        self.ui.ecualizador_bt.clicked.connect(self.show_ecualizador)
        self.ui.delay_bt.clicked.connect(self.show_delay)
        self.ui.nivel_bt.clicked.connect(self.show_nivel)
        self.ui.verticalSlider.valueChanged.connect(self.volumen_general)
        self.ui.play_bt_general.clicked.connect(self.play_general)
        self.ui.stop_bt_general.clicked.connect(self.stop_general)
        self.ui.about_bt.clicked.connect(self.about)

        self.senal = senal
        self.senal.mul = f
        self.correctos = 0
        self.incorrectos = 0

        self.main_win.setWindowTitle("Uditrainer")

#PISTAS
        self.ui.bt_canciones.clicked.connect(self.show_canciones)
        self.ui.cargar_cancion.clicked.connect(self.getfiles)
        self.ui.pista1_bt.clicked.connect(self.cambiar_pista1)
        self.ui.pista2_bt.clicked.connect(self.cambiar_pista2)
        self.ui.pista3_bt.clicked.connect(self.cambiar_pista3)
        self.ui.pista4_bt.clicked.connect(self.cambiar_pista4)
        self.ui.pista5_bt.clicked.connect(self.cambiar_pista5)

#PANEO
        self.ui.slider_paneo.valueChanged.connect(self.mostrar_valor_paneo)
        self.ui.original_bt_pan.clicked.connect(self.play_original_pan)
        self.ui.paneado_bt_pan.clicked.connect(self.play_paneado)
        self.ui.respuesta_bt_pan.clicked.connect(self.verificar_respuesta_pan)
#ECUALIZADOR
        self.ui.original_bt_eq.clicked.connect(self.play_original_eq)
        self.ui.ecualizado_bt.clicked.connect(self.play_ecualizado)
        self.ui.slider_frecuencia.valueChanged.connect(self.mostrar_valor_freq)
        self.ui.respuesta_bt_eq.clicked.connect(self.verificar_respuesta_eq)
        self.ui.limite_superior.valueChanged.connect(self.redefine_freq_senal)
        self.ui.limite_inferior.valueChanged.connect(self.redefine_freq_senal)
        self.ui.qfactor_box.currentTextChanged.connect(self.redefine_freq_senal)
        self.ui.pot_ganancia.valueChanged.connect(self.redefine_freq_senal)
        self.qfactor = 23
        self.freq = 0
        self.ui.eq_dificultad_1.currentTextChanged.connect(self.cambiar_eq)
        self.ui.eq_dificultad_2.currentTextChanged.connect(self.cambiar_eq)
        self.ui.ecualizado_bt_2.clicked.connect(self.play_ecualizado)
        self.ui.original_bt_eq_2.clicked.connect(self.play_original_eq)
        self.bandas_normalizadas = [31, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        self.ui.bt_31.clicked.connect(self.respuesta_31)
        self.ui.bt_63.clicked.connect(self.respuesta_63)
        self.ui.bt_125.clicked.connect(self.respuesta_125)
        self.ui.bt_250.clicked.connect(self.respuesta_250)
        self.ui.bt_500.clicked.connect(self.respuesta_500)
        self.ui.bt_1000.clicked.connect(self.respuesta_1000)
        self.ui.bt_2000.clicked.connect(self.respuesta_2000)
        self.ui.bt_4000.clicked.connect(self.respuesta_4000)
        self.ui.bt_8000.clicked.connect(self.respuesta_8000)
        self.ui.bt_16000.clicked.connect(self.respuesta_16000)
        self.ui.db12.clicked.connect(self.define_freq_senal_2)
        self.ui.db9.clicked.connect(self.define_freq_senal_2)
        self.ui.db6.clicked.connect(self.define_freq_senal_2)
        self.ui.db3.clicked.connect(self.define_freq_senal_2)
        self.ui.ganancias_negativas.clicked.connect(self.define_freq_senal_2)

        #NIVEL
        self.ui.dificultad_nivel.currentTextChanged.connect(self.cambiar_wg_nivel)
        self.ui.original_bt_nivel.clicked.connect(self.play_original_nivel)
        self.ui.nivel_bt_level.clicked.connect(self.play_nivelado)
        self.ui.respuesta_bt_gain.clicked.connect(self.verificar_respuesta_nivel)
        self.ui.slider_gain.valueChanged.connect(self.mostrar_valor_gain)
        self.ui.opcion1_bt_gain.clicked.connect(self.verificar_respuesta_opcion1)
        self.ui.opcion2_bt_gain.clicked.connect(self.verificar_respuesta_opcion2)
        self.ui.opcion1_bt_gain_2.clicked.connect(self.verificar_respuesta_opcion3)
        self.ui.opcion2_bt_gain_2.clicked.connect(self.verificar_respuesta_opcion4)
        self.ui.opcion3_bt_gain_2.clicked.connect(self.verificar_respuesta_opcion5)
        self.ui.opcion1_bt_gain_3.clicked.connect(self.verificar_respuesta_opcion6)
        self.ui.opcion2_bt_gain_3.clicked.connect(self.verificar_respuesta_opcion7)
        self.ui.opcion3_bt_gain_3.clicked.connect(self.verificar_respuesta_opcion8)
        self.ui.opcion4_bt_gain_3.clicked.connect(self.verificar_respuesta_opcion9)
#DELAY
        self.ui.nivel_delay_facil.currentTextChanged.connect(self.cambiar_delay)
        self.ui.nivel_delay_dificil.currentTextChanged.connect(self.cambiar_delay)
        self.ui.original_bt_delay.clicked.connect(self.play_original_delay)
        self.ui.original_bt_delay_2.clicked.connect(self.play_original_delay)
        self.ui.delayed_bt.clicked.connect(self.play_delayed)
        self.ui.delayed_bt_2.clicked.connect(self.play_delayed)
        self.ui.respuesta_bt_delay.clicked.connect(self.verificar_respuesta_delay)
        self.ui.slider_delay.valueChanged.connect(self.mostrar_valor_delay)
        self.ui.delay_opc_1.clicked.connect(self.verificar_respuesta_delay_1)
        self.ui.delay_opc_2.clicked.connect(self.verificar_respuesta_delay_2)
        self.ui.delay_opc_3.clicked.connect(self.verificar_respuesta_delay_3)

#TOOLTIP
        #BOTON "ORIGINAL"
        self.ui.original_bt_nivel.setToolTip("Reproducir pista sin modificaciones")
        self.ui.original_bt_delay.setToolTip("Reproducir pista sin modificaciones")
        self.ui.original_bt_pan.setToolTip("Reproducir pista sin modificaciones")
        self.ui.original_bt_eq.setToolTip("Reproducir pista sin modificaciones")
        #BOTON "RESPUESTA"
        self.ui.respuesta_label_gain.setToolTip("Comprobar respuesta")
        self.ui.respuesta_label_gain_2.setToolTip("Comprobar respuesta")
        self.ui.respuesta_label_gain_3.setToolTip("Comprobar respuesta")
        self.ui.respuesta_label_gain_4.setToolTip("Comprobar respuesta")
        self.ui.respuesta_bt_eq.setToolTip("Comprobar respuesta")
        self.ui.respuesta_bt_delay.setToolTip("Comprobar respuesta")
        self.ui.respuesta_bt_pan.setToolTip("Comprobar respuesta")
        self.ui.respuesta_bt_gain.setToolTip("Comprobar respuesta")

        #NIVEL
        self.ui.dificultad_nivel.setToolTip("Fácil: selecciona entre 2 opciones\nMedio: selecciona entre 3 opciones\nDifícil: selecciona entre 4 opciones\n"
                                            "Slider: selecciona arrastrando la barra")
        self.ui.nivel_bt_level.setToolTip("Reproducir pista con ganancia modificada")
        #PANEO
        self.ui.paneado_bt_pan.setToolTip("Reproducir pista paneada")
        self.ui.slider_paneo.setToolTip("Desliza para seleccionar la respuesta")
        #ECUALIZADOR
        self.ui.ecualizado_bt.setToolTip("Reproducir pista ecualizada")
        self.ui.margen_error_eq.setToolTip("")
        self.ui.label_margen_error_eq.setToolTip("")
        #DELAY
        self.ui.delayed_bt.setToolTip("Reproducir pista con delay")
        self.ui.slider_delay.setToolTip("Desliza para seleccionar la respuesta")


    def show(self):
        self.main_win.show()

    def getfiles(self):
        self.path_senal = ""
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filename = ""
        if dlg.exec_():
            filename = dlg.selectedFiles()

        if filename != "":
            path = str(filename)[2:-2]
            indice = -1
            for letra in path:
                if path[indice] == "/":
                    b = int(indice+1)
                    break
                indice -= 1
            formato = path[-3:]
            if formato == "mp3":
                self.destino = "Audio Temporal.wav"
                sound = AudioSegment.from_mp3(path)
                sound.export(self.destino, format="wav")
                mm.clear()
                self.senal = SfPlayer(self.destino, loop=True, mul=f)
                mm.addInput(0, self.senal)

            elif formato == "wav":
                mm.delInput(0)
                self.senal = SfPlayer(path)
                mm.addInput(0, self.senal)

    def cambiar_pista1(self):
        f.stop()
        self.senal.stop()
        self.senal = pista1
        mm.clear()
        mm.addInput(0, self.senal)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        f.play()
        self.senal.play()
    def cambiar_pista2(self):
        f.stop()
        self.senal.stop()
        self.senal = pista2
        mm.clear()
        mm.addInput(0, self.senal)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        f.play()
        self.senal.play()
    def cambiar_pista3(self):
        f.stop()
        self.senal.stop()
        self.senal = pista3
        mm.clear()
        mm.addInput(0, self.senal)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        f.play()
        self.senal.play()
    def cambiar_pista4(self):
        f.stop()
        self.senal.stop()
        self.senal = pista4
        mm.clear()
        mm.addInput(0, self.senal)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        f.play()
        self.senal.play()
    def cambiar_pista5(self):
        f.stop()
        self.senal.stop()
        self.senal = pista5
        mm.clear()
        mm.addInput(0, self.senal)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        f.play()
        self.senal.play()

    def volumen_general(self):
        mm.mul = self.ui.verticalSlider.value() / 100
    def play_general(self):
        if not f.isPlaying():
            f.play()
            self.senal.play()
    def stop_general(self):
        f.stop()
        self.senal.stop()

    def show_canciones(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.canciones_wg)
        f.stop()

    def about(self):
        error = QMessageBox.question(self.main_win, 'About', "<Este programa ofrece diferentes ejercicios para refinar "
        "el oído respecto a cuestiones relacionadas a la mezcla y masterización.>\n"
        "Copyright (C) 2022  Jeremias Pescaglini\n"
        "Contact: jerepescaglini@gmail.com\n"
        "\n"
        "This program is free software: you can redistribute it and/or modify"
        "it under the terms of the GNU General Public License as published by"
        "the Free Software Foundation, either version 3 of the License, or"
        "(at your option) any later version.\n"
        "\n"
        "This program is distributed in the hope that it will be useful,"
        "but WITHOUT ANY WARRANTY; without even the implied warranty of"
        "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
        "GNU General Public License for more details.\n"
        "\n"
        "You should have received a copy of the GNU General Public License "
        "along with this program.  If not, see <https://www.gnu.org/licenses/>.",QMessageBox.Ok)


### PANEO:
    def show_paneo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.paneo_wg)
        (self.pan, self.volumen) = self.define_panVol()
        f.stop()
        self.senal.stop()
        mm.clear()
        mm.addInput(0, self.senal)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)

    def define_panVol(self):
        pan = randrange(-100, 101, 1)
        volumen = float((100 - abs(pan)) / 100)
        print(pan)
        return pan, volumen

    def play_original_pan(self):
        #Permite escuchar la señal orignal estableciendo el volumen de esta en 1 y de la otra señal en 0
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        '''self.ui.original_bt_pan.setStyleSheet("QPushButton { background: rgb(139, 38, 53); color: white}")
        self.ui.paneado_bt_pan.setStyleSheet("QPushButton {"
        "border: 2px  solid rgb(46, 53, 50);"
        "border-radius: 5px;"
        "padding: 7px;"
        "margin: 5px;"
        "background: white;"
        "font-size: 14px;"
        "}"
        "QPushButton:hover {"
        "background: rgb(46, 53, 50);"
        "color: white"
        "}"
        "QPushButton:pressed {"
        "background: rgb(139, 38, 53);"
        "border: 2px rgb(139, 38, 53);"
        "}")
'''
    def play_paneado(self):
        #Permite escuchar la señal paneada a la inversa que la funcion play_original
        #Silencio la salida original y habilito la salida paneada
        if self.pan < 0:
            mm.setAmp(0, 0, 1)
            mm.setAmp(0, 1, self.volumen)
        else:
            mm.setAmp(0, 0, self.volumen)
            mm.setAmp(0, 1, 1)
        '''self.ui.paneado_bt_pan.setStyleSheet("QPushButton { background: rgb(139, 38, 53); color: white}")
        self.ui.original_bt_pan.setStyleSheet("QPushButton {"
                                             "border: 2px  solid rgb(46, 53, 50);"
                                             "border-radius: 5px;"
                                             "padding: 7px;"
                                             "margin: 5px;"
                                             "background: white;"
                                             "font-size: 14px;"
                                             "}"
                                             "QPushButton:hover {"
                                             "background: rgb(46, 53, 50);"
                                             "color: white"
                                             "}"
                                             "QPushButton:pressed {"
                                             "background: rgb(139, 38, 53);"
                                             "border: 2px rgb(139, 38, 53);"
                                             "}")
    '''
    def mostrar_valor_paneo(self):
        a = str(abs(self.ui.slider_paneo.value()))
        if self.ui.slider_paneo.value() > 0:
            self.ui.izquierda_derecha.setText('Derecha')
            self.ui.slider_paneo_value.setText(a + "%")
        if self.ui.slider_paneo.value() < 0:
            self.ui.izquierda_derecha.setText('Izquierda')
            self.ui.slider_paneo_value.setText(a + "%")

    def verificar_respuesta_pan(self):
        respuesta = self.ui.slider_paneo.value()
        if respuesta >= self.pan - 10 and respuesta <= self.pan + 10:
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            if self.pan > 0:
                self.ui.izquierda_derecha.setText("Correcto \n(" + str(abs(self.pan)) + "% Derecha)")
            elif self.pan < 0:
                self.ui.izquierda_derecha.setText("Correcto \n(" + str(abs(self.pan)) + "% Izquierda)")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            if self.pan > 0:
                self.ui.izquierda_derecha.setText("Derecha era la\nrespuesta correcta")
                self.ui.slider_paneo_value.setText(str(abs(self.pan)) + "%")
            elif self.pan < 0:
                self.ui.izquierda_derecha.setText("Izquierda era la\nrespuesta correcta")
                self.ui.slider_paneo_value.setText(str(abs(self.pan)) + "%")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
        self.senal.play(delay=1)
        self.ui.slider_paneo.setValue(0)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.pan, self.volumen) = self.define_panVol()


### ECUALIZADOR
    def cambiar_eq(self):
        if self.ui.eq_dificultad_1.currentText()=="Fácil":
            self.ui.stackedWidget.setCurrentWidget(self.ui.ecualizador_facil_wg)
            self.ui.eq_dificultad_1.setCurrentText("Dificil")
            f.stop()
            self.senal.stop()
            self.redefine_freq_senal_2()

        elif self.ui.eq_dificultad_2.currentText()=="Dificil":
            self.ui.stackedWidget.setCurrentWidget(self.ui.ecualizador_wg)
            self.ui.eq_dificultad_2.setCurrentText("Fácil")
            f.stop()
            self.senal.stop()
            (self.freq, self.senal_eq) = self.define_freq_senal()

    def show_ecualizador(self):
        self.ui.eq_dificultad_1.setCurrentText("Fácil")
        self.cambiar_eq()

    def define_freq_senal(self):
        freq = randrange(self.ui.limite_inferior.value(), self.ui.limite_superior.value(), 1)
        senal_eq = EQ(self.senal, freq=freq, q=float(self.qfactor), boost=self.ui.pot_ganancia.value(), mul=f)
        return [freq, senal_eq]

    def redefine_freq_senal(self):###ESTA FUCIÓN SE UTILIZA AL CAMBIAR ALGUN PARÁMETRO
        self.ui.slider_frecuencia_value.setText("")
        self.ui.label_respuesta_eq.setText("")
        f.stop()
        self.senal.stop()
        (self.freq, self.senal_eq) = self.define_freq_senal()
        mm.clear()
        mm.addInput(0, self.senal)
        mm.addInput(1, self.senal_eq)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 0)
        mm.setAmp(0, 1, 0)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)
        a = self.ui.limite_inferior.value()
        b = self.ui.limite_superior.value()
        self.ui.slider_frecuencia.setMinimum(int(log10(a)*1000))
        self.ui.slider_frecuencia.setMaximum(int(log10(b)*1000))
        c = int(log10(a)*1000)
        d = int(log10(b)*1000)
        self.ui.slider_frecuencia.setValue(c + (int((d - c) / 2)))
        if self.ui.qfactor_box.currentText() == "2 octavas":
            self.qfactor = 0.667
        elif self.ui.qfactor_box.currentText() == "1 octava":
            self.qfactor = 1.414
        elif self.ui.qfactor_box.currentText() == "1/2 octava":
            self.qfactor = 2.871
        elif self.ui.qfactor_box.currentText() == "1/3 octava":
            self.qfactor = 4.36
        elif self.ui.qfactor_box.currentText() == "1/4 octava":
            self.qfactor = 5.76
        elif self.ui.qfactor_box.currentText() == "1/8 octava":
            self.qfactor = 11.54
        elif self.ui.qfactor_box.currentText() == "1/16 octava":
            self.qfactor = 23

    def play_original_eq(self):
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        mm.setAmp(1, 0, 0)
        mm.setAmp(1, 1, 0)

    def play_ecualizado(self):
        mm.setAmp(0, 0, 0)
        mm.setAmp(0, 1, 0)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)

    def mostrar_valor_freq(self):
        self.ui.label_respuesta_eq.setText("")
        a = self.ui.slider_frecuencia.value()
        c = int(10 ** (a/1000))
        self.ui.slider_frecuencia_value.setText(str(c) + " Hz")

    def verificar_respuesta_eq(self):
        c = self.ui.slider_frecuencia.value()
        respuesta = int(10 ** (c / 1000))
        resp = str(self.freq)
        if respuesta <= self.freq+self.ui.margen_error_eq.value() and respuesta >= self.freq-self.ui.margen_error_eq.value():
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.label_respuesta_eq.setText("Correcto ("+str(self.freq)+")")

            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.slider_frecuencia_value.setText(resp + " Hz")
            self.ui.label_respuesta_eq.setText("era la respuesta correcta")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.clear()
        (self.freq, self.senal_eq) = self.define_freq_senal()
        mm.addInput(0, self.senal)
        mm.addInput(1, self.senal_eq)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 0)
        mm.setAmp(0, 1, 0)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)
        #Tener en cuenta la escala logaritmica: el slider va de 1301 a 4301.
        #Si aplicamos log10 a esos valores, y multiplicamos por 1000, nos da 20 y 20000.
        self.ui.slider_frecuencia.setMinimum(int(log10(self.ui.limite_inferior.value()) * 1000))
        self.ui.slider_frecuencia.setMaximum(int(log10(self.ui.limite_superior.value()) * 1000))
        a = log10(self.ui.limite_inferior.value()) * 1000
        b = log10(self.ui.limite_superior.value()) * 1000
        d = a + (int((b - a)/2))
        #self.ui.slider_frecuencia.setValue(int(d))

### ECUALIZADOR FÁCIL
    def define_freq_senal_2(self):
        num = randrange(0, 10, 1)
        print(self.bandas_normalizadas[num])
        freq = self.bandas_normalizadas[num]
        ganancias = []
        if not self.ui.db12.isChecked() and not self.ui.db9.isChecked() and not self.ui.db6.isChecked() and not self.ui.db3.isChecked():
            self.ui.db12.setChecked(True)
            error = QMessageBox.question(self.main_win, 'Error', 'Debe seleccionar al menos una opción de ganancia',QMessageBox.Ok)
        if self.ui.db3.isChecked():
            ganancias.append(3)
        if self.ui.db6.isChecked():
            ganancias.append(6)
        if self.ui.db9.isChecked():
            ganancias.append(9)
        if self.ui.db12.isChecked():
            ganancias.append(12)
        gain = ganancias[randrange(0, len(ganancias))]
        if self.ui.ganancias_negativas.isChecked():
            par_impar = randrange(0,2,1)
            if par_impar == 0:
                gain = -gain
        print(gain)
        senal_eq = EQ(self.senal, freq=freq, q=1.414, boost=gain, mul=f)
        return [freq, senal_eq]

    def redefine_freq_senal_2(self):
        mm.clear()
        (self.freq, self.senal_eq) = self.define_freq_senal_2()
        mm.addInput(0, self.senal)
        mm.addInput(1, self.senal_eq)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 0)
        mm.setAmp(0, 1, 0)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)
        f.play()
        self.senal.play(delay=1)

    def eq_facil_correcto(self):
        self.ui.label_respuesta_eq_2.setText("Correcto")
        self.correctos += 1
        self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
        f.stop()
        self.senal.stop()
        correcto.play()
        f.play()
        self.senal.play(delay=1)
    def eq_facil_incorrecto(self):
        self.ui.label_respuesta_eq_2.setText("Incorrecto")
        self.ui.label_respuesta_eq_3.setText("La respuesta correcta era " + str(self.freq) + " Hz")
        self.incorrectos += 1
        self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
        f.stop()
        self.senal.stop()
        incorrecto.play()
        f.play()
        self.senal.play(delay=1)

    def respuesta_31(self):
        if self.freq == 31:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_63(self):
        if self.freq == 63:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_125(self):
        if self.freq == 125:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_250(self):
        if self.freq == 250:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_500(self):
        if self.freq == 500:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_1000(self):
        if self.freq == 1000:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_2000(self):
        if self.freq == 2000:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_4000(self):
        if self.freq == 4000:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_8000(self):
        if self.freq == 8000:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

    def respuesta_16000(self):
        if self.freq == 16000:
            self.eq_facil_correcto()
        else:
            self.eq_facil_incorrecto()
        self.redefine_freq_senal_2()

### NIVEL
    def show_nivel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.nivel_wg)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.opciones_gain_wg)
        f.stop()
        self.senal.stop()
        mm.clear()
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_2()
        mm.addInput(0, self.senal)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)

    def define_nivel_db(self):
        while True:
            nivel_db = randrange(-18, 1, 1)
            nivel_falso_1 = randrange(-18, 1, 1)
            nivel_falso_2 = randrange(-18, 1, 1)
            nivel_falso_3 = randrange(-18, 1, 1)
            if nivel_db != nivel_falso_1 and nivel_db != nivel_falso_2 and nivel_db != nivel_falso_3 and nivel_falso_1 != nivel_falso_2\
                    and nivel_falso_1 != nivel_falso_3 and nivel_falso_2 != nivel_falso_3:
                break
        nivel_mixer = 10 ** (nivel_db/20)
        return [nivel_db, nivel_mixer, nivel_falso_1, nivel_falso_2, nivel_falso_3]

    def play_original_nivel(self):
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)

    def play_nivelado(self):
        mm.setAmp(0, 0, self.nivel_mixer)
        mm.setAmp(0, 1, self.nivel_mixer)

    def cambiar_opciones_2(self):
        a = randrange(0, 2)
        if a == 0:
            self.ui.opcion1_bt_gain.setText(str(self.nivel_db))
            self.ui.opcion2_bt_gain.setText(str(self.nivel_falso_1))
        elif a == 1:
            self.ui.opcion1_bt_gain.setText(str(self.nivel_falso_1))
            self.ui.opcion2_bt_gain.setText(str(self.nivel_db))
    def cambiar_opciones_3(self):
        a = randrange(0, 3)
        if a == 1:
            self.ui.opcion1_bt_gain_2.setText(str(self.nivel_db))
            self.ui.opcion2_bt_gain_2.setText(str(self.nivel_falso_1))
            self.ui.opcion3_bt_gain_2.setText(str(self.nivel_falso_2))
        elif a == 2:
            self.ui.opcion1_bt_gain_2.setText(str(self.nivel_falso_1))
            self.ui.opcion2_bt_gain_2.setText(str(self.nivel_db))
            self.ui.opcion3_bt_gain_2.setText(str(self.nivel_falso_2))
        else:
            self.ui.opcion1_bt_gain_2.setText(str(self.nivel_falso_1))
            self.ui.opcion2_bt_gain_2.setText(str(self.nivel_falso_2))
            self.ui.opcion3_bt_gain_2.setText(str(self.nivel_db))
    def cambiar_opciones_4(self):
        a = randrange(0, 4)
        if a == 1:
            self.ui.opcion1_bt_gain_3.setText(str(self.nivel_db))
            self.ui.opcion2_bt_gain_3.setText(str(self.nivel_falso_1))
            self.ui.opcion3_bt_gain_3.setText(str(self.nivel_falso_2))
            self.ui.opcion4_bt_gain_3.setText(str(self.nivel_falso_3))
        elif a == 2:
            self.ui.opcion1_bt_gain_3.setText(str(self.nivel_falso_1))
            self.ui.opcion2_bt_gain_3.setText(str(self.nivel_db))
            self.ui.opcion3_bt_gain_3.setText(str(self.nivel_falso_2))
            self.ui.opcion4_bt_gain_3.setText(str(self.nivel_falso_3))
        elif a == 3:
            self.ui.opcion1_bt_gain_3.setText(str(self.nivel_falso_2))
            self.ui.opcion2_bt_gain_3.setText(str(self.nivel_falso_1))
            self.ui.opcion3_bt_gain_3.setText(str(self.nivel_db))
            self.ui.opcion4_bt_gain_3.setText(str(self.nivel_falso_3))
        else:
            self.ui.opcion1_bt_gain_3.setText(str(self.nivel_falso_3))
            self.ui.opcion2_bt_gain_3.setText(str(self.nivel_falso_1))
            self.ui.opcion3_bt_gain_3.setText(str(self.nivel_falso_2))
            self.ui.opcion4_bt_gain_3.setText(str(self.nivel_db))

    def cambiar_wg_nivel(self):
        if self.ui.dificultad_nivel.currentText() == "Fácil":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.opciones_gain_wg)
            self.cambiar_opciones_2()
        if self.ui.dificultad_nivel.currentText() == "Medio":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.opciones_3_gain_wg)
            self.cambiar_opciones_3()
        if self.ui.dificultad_nivel.currentText() == "Dificil":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.opciones_4_gain_wg)
            self.cambiar_opciones_4()
        if self.ui.dificultad_nivel.currentText() == "Slider":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.slider_gain_wg)

    def mostrar_valor_gain(self):
        self.ui.respuesta_label_gain_2.setText(str(self.ui.slider_gain.value()) + " dB")
        self.ui.correcta_slider_gain.setText("")

    #VERIFICAR RESPUESTA NIVEL FACIL:
    def verificar_respuesta_opcion1(self):
        if self.ui.opcion1_bt_gain.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain.setText("Correcto")
            self.ui.respuesta_correcta_gain_1.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_1.setText("La respuesta correcta era: "+str(self.nivel_db)+" dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_2()
    def verificar_respuesta_opcion2(self):
        if self.ui.opcion2_bt_gain.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain.setText("Correcto")
            self.ui.respuesta_correcta_gain_1.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_1.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_2()

    #VERIFICAR RESPUESTA NIVEL MEDIO:
    def verificar_respuesta_opcion3(self):
        if self.ui.opcion1_bt_gain_2.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_3.setText("Correcto")
            self.ui.respuesta_correcta_gain_2.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_3.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_2.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            senal.stop()
            incorrecto.play()
            f.play()
            senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_3()
    def verificar_respuesta_opcion4(self):
        if self.ui.opcion2_bt_gain_2.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_3.setText("Correcto")
            self.ui.respuesta_correcta_gain_2.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_3.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_2.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_3()
    def verificar_respuesta_opcion5(self):
        if self.ui.opcion3_bt_gain_2.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_3.setText("Correcto")
            self.ui.respuesta_correcta_gain_2.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_3.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_2.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_3()

    #VERIFICAR RESPUESTA NIVEL DIFICIL:
    def verificar_respuesta_opcion6(self):
        if self.ui.opcion1_bt_gain_3.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_4.setText("Correcto")
            self.ui.respuesta_correcta_gain_3.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_4.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_3.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_4()
    def verificar_respuesta_opcion7(self):
        if self.ui.opcion2_bt_gain_3.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_4.setText("Correcto")
            self.ui.respuesta_correcta_gain_3.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_4.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_3.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_4()
    def verificar_respuesta_opcion8(self):
        if self.ui.opcion3_bt_gain_3.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_4.setText("Correcto")
            self.ui.respuesta_correcta_gain_3.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_4.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_3.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_4()
    def verificar_respuesta_opcion9(self):
        if self.ui.opcion4_bt_gain_3.text() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_4.setText("Correcto")
            self.ui.respuesta_correcta_gain_3.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_4.setText("Incorrecto")
            self.ui.respuesta_correcta_gain_3.setText("La respuesta correcta era: " + str(self.nivel_db) + " dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()
        self.cambiar_opciones_4()

    #VERIFICAR RESPUESTA NIVEL FADER:
    def verificar_respuesta_nivel(self):
        if self.ui.slider_gain.value() == str(self.nivel_db):
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.respuesta_label_gain_2.setText("Correcto")
            self.ui.correcta_slider_gain.setText("")
            f.stop()
            self.senal.stop()
            correcto.play()
            f.play()
            self.senal.play(delay=1)
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.respuesta_label_gain_2.setText("Incorrecto")
            self.ui.correcta_slider_gain.setText("La respuesta correcta era: " + str(self.nivel_db) + "dB")
            f.stop()
            self.senal.stop()
            incorrecto.play()
            f.play()
            self.senal.play(delay=1)

        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        (self.nivel_db, self.nivel_mixer, self.nivel_falso_1, self.nivel_falso_2, self.nivel_falso_3) = self.define_nivel_db()

###DELAY DIFICIL
    def cambiar_delay(self):
        if self.ui.nivel_delay_dificil.currentText()=="Fácil":
            self.ui.stackedWidget.setCurrentWidget(self.ui.delay_facil_wg)
            self.ui.nivel_delay_dificil.setCurrentText("Dificil")
            f.stop()
            self.senal.stop()
            self.definir_delay_facil()

        elif self.ui.nivel_delay_facil.currentText()=="Dificil":
            self.ui.stackedWidget.setCurrentWidget(self.ui.delay_wg)
            self.ui.nivel_delay_facil.setCurrentText("Fácil")
            f.stop()
            self.senal.stop()
            self.definir_delay()

    def show_delay(self):
        self.ui.nivel_delay_dificil.setCurrentText("Fácil")
        self.cambiar_delay()

    def definir_delay(self):
        f.stop()
        self.senal.stop()
        mm.clear()
        self.delay_time = randrange(5, 201, 1) / 1000
        delayed = Delay(self.senal, delay=self.delay_time, mul=0.9)
        mm.addInput(0, self.senal)
        mm.addInput(1, delayed)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)

    def mostrar_valor_delay(self):
        self.ms = self.ui.slider_delay.value()
        self.ui.delay_label.setText(str(self.ms) + " ms")
        self.ui.correcta_delay.setText("")

    def play_original_delay(self):
        mm.setAmp(1, 0, 0)
        mm.setAmp(1, 1, 0)

    def play_delayed(self):
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)

    def verificar_respuesta_delay(self):
        slider = self.ui.slider_delay.value()/1000
        if self.delay_time <= 0.05:
            margen = float(self.delay_time * 0.5)
        elif self.delay_time>0.05 and self.delay_time<0.1:
            margen = self.delay_time * 0.4
        else:
            margen = self.delay_time * 0.3
        self.ui.slider_delay.setValue(0)
        if slider + margen >= self.delay_time and slider - margen <= self.delay_time:
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.delay_label.setText("Correcto")
            self.ui.correcta_delay.setText("(" + str(int(self.delay_time * 1000)) + " ms)")
            f.stop()
            self.senal.stop()
            correcto.play()
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.delay_label.setText("Incorrecto")
            self.ui.correcta_delay.setText("La respuesta correcta era: " + str(int(self.delay_time * 1000)) + " ms")
            f.stop()
            self.senal.stop()
            incorrecto.play()
        self.definir_delay()
        f.play()
        self.senal.play(delay=1)

###DELAY FACIL
    def definir_delay_facil(self):
        f.stop()
        self.senal.stop()
        mm.clear()
        self.delay_1 = randrange(0, 200 , 1)
        print(self.delay_1)
        if self.delay_1 <= 50:
            margen = 50
        elif self.delay_1>50 and self.delay_1<100:
            margen = 40
        else:
            margen = 30
        while True:
            lim_inf = int((self.delay_1) - (margen * (self.delay_1) / 100))
            lim_sup = int((self.delay_1) + (margen * (self.delay_1) / 100))
            self.delay_2 = randrange(lim_inf, lim_sup, 1)
            self.delay_3 = randrange(lim_inf, lim_sup, 1)
            if margen == 50 and abs(self.delay_2 - self.delay_1) > 5 and abs(self.delay_3 - self.delay_1) > 5:
                break
            elif margen == 40 and abs(self.delay_2 - self.delay_1) > 10 and abs(self.delay_3 - self.delay_1) > 10:
                break
            elif margen == 30 and abs(self.delay_2 - self.delay_1) > 20 and abs(self.delay_3 - self.delay_1) > 20:
                break
        a = randrange(0, 3)
        if a == 1:
            self.ui.delay_opc_1.setText(str(self.delay_1) + " ms")
            self.ui.delay_opc_2.setText(str(self.delay_2) + " ms")
            self.ui.delay_opc_3.setText(str(self.delay_3) + " ms")
        elif a == 2:
            self.ui.delay_opc_1.setText(str(self.delay_2) + " ms")
            self.ui.delay_opc_2.setText(str(self.delay_1) + " ms")
            self.ui.delay_opc_3.setText(str(self.delay_3) + " ms")
        else:
            self.ui.delay_opc_1.setText(str(self.delay_3) + " ms")
            self.ui.delay_opc_2.setText(str(self.delay_2) + " ms")
            self.ui.delay_opc_3.setText(str(self.delay_1) + " ms")
        delayed = Delay(self.senal, delay=self.delay_1/1000, mul=0.9)
        mm.addInput(0, self.senal)
        mm.addInput(1, delayed)
        mm.addInput(5, correcto)
        mm.addInput(6, incorrecto)
        mm.setAmp(6, 0, 1)
        mm.setAmp(6, 1, 1)
        mm.setAmp(5, 0, 1)
        mm.setAmp(5, 1, 1)
        mm.setAmp(0, 0, 1)
        mm.setAmp(0, 1, 1)
        mm.setAmp(1, 0, 1)
        mm.setAmp(1, 1, 1)
        f.play()
        self.senal.play(delay=1)

    def verificar_respuesta_delay_1(self):
        if self.ui.delay_opc_1.text() == str(self.delay_1) + " ms":
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.delay_label_facil.setText("Correcto")
            f.stop()
            self.senal.stop()
            correcto.play()
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.delay_label_facil.setText("Incorrecto: " +str(self.delay_1))
            f.stop()
            senal.stop()
            incorrecto.play()
        self.definir_delay_facil()
    def verificar_respuesta_delay_2(self):
        if self.ui.delay_opc_2.text() == str(self.delay_1) + " ms":
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.delay_label_facil.setText("Correcto")
            f.stop()
            self.senal.stop()
            correcto.play()
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.delay_label_facil.setText("Incorrecto: " + str(self.delay_1))
            f.stop()
            senal.stop()
            incorrecto.play()
        self.definir_delay_facil()
    def verificar_respuesta_delay_3(self):
        if self.ui.delay_opc_3.text() == str(self.delay_1) + " ms":
            self.correctos += 1
            self.ui.label_correctos.setText("Correctos: " + str(self.correctos))
            self.ui.delay_label_facil.setText("Correcto")
            f.stop()
            self.senal.stop()
            correcto.play()
        else:
            self.incorrectos += 1
            self.ui.label_incorrectos.setText("Incorrectos: " + str(self.incorrectos))
            self.ui.delay_label_facil.setText("Incorrecto: " + str(self.delay_1))
            f.stop()
            senal.stop()
            incorrecto.play()
        self.definir_delay_facil()

if __name__ == '__main__':
    s = Server().boot()
    s.start()
    mm = Mixer(outs=2)
    mm.out()
    f = Fader(fadeout=0.5, fadein=0.2)
    # LA CLASE FADER ME PERMITE HACER FADE IN Y FADE OUT, LO QUE HACE MENOS ABRUPTAS LAS FUNCIONES PLAY Y PAUSA
    # POR LO QUE ESTABLEZCO QUE EL NIVEL LO INDICA f
    pista1 = SfPlayer("Pista_1.wav", loop=True, mul=f)
    #EL DELAY TIENE QUE CONCIDIR CON EL DEL FADER (f) PARA QUE PARE UNA VEZ QUE EL FADER TERMINÓ:
    pista1.setStopDelay(0.5)
    #AL DARLE PLAY() A f INICIA TAMBIEN LA senal
    pista2 = SfPlayer("Pista_2.wav", loop=True, mul=f)
    pista2.setStopDelay(0.5)
    pista3 = SfPlayer("Pista_3.wav", loop=True, mul=f)
    pista3.setStopDelay(0.5)
    pista4 = SfPlayer("Pista_4.wav", loop=True, mul=f)
    pista4.setStopDelay(0.5)
    pista5 = SfPlayer("Pista_5.wav", loop=True, mul=f)
    pista5.setStopDelay(0.5)
    correcto = SfPlayer("Correcto.wav")
    incorrecto = SfPlayer("Incorrecto.wav")
    senal = pista1

    '''def borrar():
        mm.stop()
        if os.path.exists("Audio Temporal.wav"):
            os.remove("Audio Temporal.wav")
        else:
            print("El archivo no existe")
    atexit.register(borrar)'''

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


