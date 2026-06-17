[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ LIBRERÍAS CORRECTAS: Tal cual las necesitás + pyjnius para Android
requirements = python3,kivy,pyjnius,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android → CONFIGURACIÓN SEGURA, IGUAL QUE LA RULETA
# =============================================================================

android.api = 33
android.minapi = 21

# ✅ SIN SDK NI NDK FORZADOS (esto fue lo que nos salvó)
# android.sdk = 24
# android.ndk = 25b

android.private_storage = True

# ✅ PERMISOS QUE VOS NECESITÁS PARA GUARDAR EL PDF
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.archs = armeabi-v7a,arm64-v8a

# ✅ OBLIGATORIOS PARA ANDROID 12/13/14
android.enable_androidx = True
android.use_apache_http = True


# =============================================================================
# Buildozer
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
