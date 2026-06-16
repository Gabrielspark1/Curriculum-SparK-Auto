[app]
title = Creador CV - Gabriel Spark
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ SOLO LO NECESARIO, SIN ERRORES
requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android → VERSIONES EXACTAS Y SEGURAS
# =============================================================================

android.api = 33
android.minapi = 21

# ✅ VERSIONES QUE EXISTEN Y FUNCIONAN EN TU ENTORNO
android.sdk = 24
android.ndk = 19c

android.private_storage = True

# ✅ PERMISOS BÁSICOS, SIN EXTRAS
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.archs = armeabi-v7a,arm64-v8a

# ✅ SOLO ESTAS DOS LÍNEAS, SON OBLIGATORIAS
android.enable_androidx = True
android.use_apache_http = True


# =============================================================================
# Buildozer
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
