[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ LIBRERÍAS CORRECTAS: reportlab para PDF + pyjnius para Android
requirements = python3,kivy,reportlab,pyjnius

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android → LO MÍNIMO Y SEGURO
# =============================================================================

android.api = 33
android.minapi = 21

android.private_storage = True

# ✅ CORREGIDO: Adaptado para Android 13+ (Se eliminó WRITE_EXTERNAL_STORAGE que causa 'crash')
# ✅ Se agregaron permisos específicos para leer multimedia si tu app requiere cargar fotos para el CV
android.permissions = INTERNET, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO

# ✅ CLAVE PARA PDF EN API 33: Permite guardar archivos en el almacenamiento compartido (Descargas/Documentos) usando Scoped Storage
android.manifest.application_arguments = --requestLegacyExternalStorage=true

android.archs = armeabi-v7a,arm64-v8a

# ✅ SOLO ESTAS DOS OBLIGATORIAS (NO TOCAR)
android.enable_androidx = True
android.use_apache_http = True


# =============================================================================
# Buildozer
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
