import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from kivy.uix.popup import Popup

# --- COLORES ---
COLOR_PRIMARIO = "#2c3e50"
COLOR_BOTON = "#27ae60"
COLOR_TEXTO = "#333333"

class CvCreatorApp(App):
    def build(self):
        Window.softinput_mode = 'pan'
        self.datos = {}

        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        titulo = Label(
            text="[b]CREADOR DE CURRÍCULUM VITAE[/b]",
            markup=True,
            font_size='20sp',
            color=get_color_from_hex(COLOR_PRIMARIO),
            size_hint_y=None,
            height=50
        )
        root.add_widget(titulo)

        scroll = ScrollView()
        self.form_layout = GridLayout(
            cols=1,
            spacing=12,
            size_hint_y=None,
            padding=10
        )
        self.form_layout.bind(minimum_height=self.form_layout.setter('height'))

        # 🔹 DATOS PERSONALES
        self.agregar_seccion("📋 DATOS PERSONALES")
        self.agregar_campo("Nombre completo", "nombre")
        self.agregar_campo("Profesión / Cargo", "profesion")
        self.agregar_campo("Dirección completa", "direccion")
        self.agregar_campo("Teléfono / Celular", "telefono")
        self.agregar_campo("Correo electrónico", "correo")
        self.agregar_campo("Enlace a LinkedIn", "linkedin")

        # 🔹 PERFIL
        self.agregar_seccion("📝 PERFIL PROFESIONAL")
        self.agregar_campo("Descripción breve sobre vos", "perfil", multiline=True)

        # 🔹 EXPERIENCIA
        self.agregar_seccion("💼 EXPERIENCIA LABORAL")
        self.agregar_campo("Periodo (ej: 2018-2020)", "exp1_fecha")
        self.agregar_campo("Cargo / Puesto", "exp1_cargo")
        self.agregar_campo("Empresa / Organización", "exp1_empresa")
        self.agregar_campoFunciones("Tareas y logros", "exp1_tareas")

        self.agregar_campo("Periodo", "exp2_fecha")
        self.agregar_campo("Cargo / Puesto", "exp2_cargo")
        self.agregar_campo("Empresa / Organización", "exp2_empresa")
        self.agregar_campoFunciones("Tareas y logros", "exp2_tareas")

        # 🔹 EDUCACIÓN
        self.agregar_seccion("🎓 EDUCACIÓN")
        self.agregar_campo("Periodo", "edu1_fecha")
        self.agregar_campo("Título / Estudios", "edu1_titulo")
        self.agregar_campo("Institución educativa", "edu1_inst")

        self.agregar_campo("Periodo", "edu2_fecha")
        self.agregar_campo("Título / Estudios", "edu2_titulo")
        self.agregar_campo("Institución educativa", "edu2_inst")

        # 🔹 INFORMACIÓN ADICIONAL
        self.agregar_seccion("ℹ️ INFORMACIÓN ADICIONAL")
        self.agregar_campo("Datos extra (disponibilidad, licencias, etc)", "adicional", multiline=True)

        # 🔹 IDIOMAS
        self.agregar_seccion("🗣️ IDIOMAS")
        self.agregar_campo("Idioma 1 y nivel (ej: Inglés: C2)", "idioma1")
        self.agregar_campo("Idioma 2 y nivel", "idioma2")
        self.agregar_campo("Idioma 3 y nivel", "idioma3")

        scroll.add_widget(self.form_layout)
        root.add_widget(scroll)

        btn_generar = Button(
            text="📄 GENERAR PDF",
            background_color=get_color_from_hex(COLOR_BOTON),
            size_hint_y=None,
            height=60,
            bold=True,
            font_size='18sp'
        )
        btn_generar.bind(on_release=self.generar_pdf)
        root.add_widget(btn_generar)

        return root

    def agregar_seccion(self, texto):
        lbl = Label(
            text=f"[b]{texto}[/b]",
            markup=True,
            font_size='16sp',
            size_hint_y=None,
            height=40,
            halign='left',
            color=get_color_from_hex(COLOR_PRIMARIO)
        )
        self.form_layout.add_widget(lbl)

    def agregar_campo(self, texto, clave, multiline=False):
        lbl = Label(
            text=texto,
            font_size='14sp',
            size_hint_y=None,
            height=30,
            halign='left',
            color=get_color_from_hex(COLOR_TEXTO)
        )
        self.form_layout.add_widget(lbl)
        entrada = TextInput(
            hint_text=f"Ingresar {texto.lower()}",
            multiline=multiline,
            size_hint_y=None,
            height=80 if multiline else 50,
            padding=[10,10]
        )
        entrada.id = clave
        entrada.bind(text=self.guardar_texto)
        self.form_layout.add_widget(entrada)

    def agregar_campoFunciones(self, texto, clave):
        lbl = Label(
            text=texto,
            font_size='14sp',
            size_hint_y=None,
            height=30,
            halign='left',
            color=get_color_from_hex(COLOR_TEXTO)
        )
        self.form_layout.add_widget(lbl)
        entrada = TextInput(
            hint_text="• Escribir cada punto en una línea",
            multiline=True,
            size_hint_y=None,
            height=100,
            padding=[10,10]
        )
        entrada.id = clave
        entrada.bind(text=self.guardar_texto)
        self.form_layout.add_widget(entrada)

    def guardar_texto(self, instancia, valor):
        self.datos[instancia.id] = valor

    # --- ✅ GENERACIÓN PDF - ESTILO IGUAL A TU EJEMPLO + TU MARCA ---
    def generar_pdf(self, instancia):
        if not self.datos.get("nombre"):
            self.mostrar_aviso("⚠️ Escribí al menos el nombre para continuar")
            return

        ruta_pdf = os.path.join(os.path.expanduser("~"), "Curriculum_Vitae.pdf")
        c = canvas.Canvas(ruta_pdf, pagesize=A4)
        ancho, alto = A4

        # 📌 RECUADRO FINO ELEGANTE
        c.setLineWidth(0.3)
        c.setStrokeColorRGB(0.4, 0.4, 0.4)
        c.rect(1.8*cm, 1.8*cm, ancho - 3.6*cm, alto - 3.6*cm)

        # 📌 TU MARCA - TEXTO VERTICAL, SUTIL, INGLÉS
        c.saveState()
        c.translate(0.7*cm, alto/2)
        c.rotate(90)
        c.setFont("Helvetica-Light", 6)
        c.setFillColorRGB(0.65, 0.65, 0.65)
        c.drawCentredString(0, 0, "© Created by Gabriel Spark | Independent Designer | Contact: +54 2616 68 5065")
        c.restoreState()

        # 📌 CONTENIDO PRINCIPAL (IGUAL A TU EJEMPLO DE IMAGEN)
        y = alto - 3*cm
        margen_izq = 2.5*cm

        # NOMBRE Y PROFESIÓN
        c.setFont("Helvetica-Bold", 18)
        c.setFillColorRGB(0.1,0.1,0.1)
        c.drawString(margen_izq, y, self.datos.get("nombre", "Nombre Completo").upper())
        y -= 0.8*cm

        c.setFont("Helvetica", 12)
        c.setFillColorRGB(0.3,0.3,0.3)
        c.drawString(margen_izq, y, self.datos.get("profesion", "Profesión"))
        y -= 1*cm

        # DATOS DE CONTACTO
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(0.25,0.25,0.25)
        if self.datos.get("direccion"): c.drawString(margen_izq, y, f"📍 {self.datos['direccion']}"); y -= 0.5*cm
        if self.datos.get("telefono"): c.drawString(margen_izq, y, f"📞 {self.datos['telefono']}"); y -= 0.5*cm
        if self.datos.get("correo"): c.drawString(margen_izq, y, f"✉ {self.datos['correo']}"); y -= 0.5*cm
        if self.datos.get("linkedin"): c.drawString(margen_izq, y, f"🔗 {self.datos['linkedin']}"); y -= 1*cm

        # LÍNEA SEPARADORA
        c.setLineWidth(0.2)
        c.line(margen_izq, y, ancho - 2.5*cm, y)
        y -= 0.8*cm

        # --- SECCIONES ---
        def seccion(titulo, contenido):
            nonlocal y
            if contenido and contenido.strip():
                c.setFont("Helvetica-Bold", 11)
                c.setFillColorRGB(0.1,0.1,0.1)
                c.drawString(margen_izq, y, titulo.upper())
                y -= 0.6*cm
                c.setFont("Helvetica", 9)
                c.setFillColorRGB(0.2,0.2,0.2)
                for linea in contenido.split("\n"):
                    if linea.strip():
                        c.drawString(margen_izq + 0.2*cm, y, f"• {linea}")
                        y -= 0.45*cm
                y -= 0.3*cm

        # EXPERIENCIA
        exp_completo = ""
        if self.datos.get("exp1_fecha"): exp_completo += f"{self.datos['exp1_fecha']}    {self.datos['exp1_cargo']}\n    {self.datos['exp1_empresa']}\n{self.datos.get('exp1_tareas','')}\n\n"
        if self.datos.get("exp2_fecha"): exp_completo += f"{self.datos['exp2_fecha']}    {self.datos['exp2_cargo']}\n    {self.datos['exp2_empresa']}\n{self.datos.get('exp2_tareas','')}"
        seccion("Experiencia", exp_completo)

        # EDUCACIÓN
        edu_completo = ""
        if self.datos.get("edu1_fecha"): edu_completo += f"{self.datos['edu1_fecha']}    {self.datos['edu1_titulo']}\n    {self.datos['edu1_inst']}\n\n"
        if self.datos.get("edu2_fecha"): edu_completo += f"{self.datos['edu2_fecha']}    {self.datos['edu2_titulo']}\n    {self.datos['edu2_inst']}"
        seccion("Educación", edu_completo)

        # INFORMACIÓN ADICIONAL
        seccion("Información adicional", self.datos.get("adicional",""))

        # IDIOMAS
        idiomas_completos = ""
        if self.datos.get("idioma1"): idiomas_completos += f"{self.datos['idioma1']}\n"
        if self.datos.get("idioma2"): idiomas_completos += f"{self.datos['idioma2']}\n"
        if self.datos.get("idioma3"): idiomas_completos += f"{self.datos['idioma3']}"
        seccion("Idiomas", idiomas_completos)

        c.save()
        self.mostrar_aviso(f"✅ PDF GENERADO\nGuardado en:\n{ruta_pdf}", True)

    def mostrar_aviso(self, texto, exito=False):
        popup = Popup(
            title="✅ LISTO" if exito else "ℹ️ AVISO",
            content=Label(text=texto, markup=True, font_size='14sp', halign='center'),
            size_hint=(0.85, 0.4)
        )
        popup.open()

if __name__ == "__main__":
    CvCreatorApp().run()
