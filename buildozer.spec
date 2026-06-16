[app]
title = Creador CV - Gabriel Spark
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ Librerías exactas: reportlab para PDF
requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android → VERSIONES QUE FUNCIONAN CON TU BUILD.YML
# =============================================================================

android.api = 33
android.minapi = 21

# ✅ VERSIONES SEGURAS, EXISTEN EN LOS SERVIDORES, NO FALLAN
android.sdk = 24
android.ndk = 23b

android.private_storage = True

# ✅ PERMISOS PARA GUARDAR EL PDF EN EL CELULAR
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.archs = armeabi-v7a,arm64-v8a

# ✅ OBLIGATORIO PARA ANDROID NUEVO, SIN ESTO SE ROMPE
android.enable_androidx = True
android.use_apache_http = True
android.meta_data = android.support.PREFER_ANDROID=true

# ✅ ENCRIPTACIÓN ACTIVADA
android.python_encrypt = yes


# =============================================================================
# Buildozer sections
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
