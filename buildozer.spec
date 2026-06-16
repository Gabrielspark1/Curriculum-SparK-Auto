[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ CORREGIDO: Solo lo justo, pyjnius también ayuda aquí
requirements = python3,kivy,reportlab,pyjnius

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android specific
# =============================================================================

android.api = 33
android.minapi = 21

# ✅ SIN VERSIONES PUESTAS, SEGURO TOTAL
# android.sdk = 24
# android.ndk = 25b

android.private_storage = True

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.archs = armeabi-v7a,arm64-v8a

# ✅ LO MISMO OBLIGATORIO
android.enable_androidx = True
android.use_apache_http = True

# ✅ PROTECCIÓN
android.python_encrypt = yes


# =============================================================================
# Buildozer sections
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
