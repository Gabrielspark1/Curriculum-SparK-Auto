[app]
title = Creador CV - Gabriel Spark
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Solo librerías necesarias
requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png

# --- ANDROID ---
android.api = 33
android.minapi = 21

# ✅ QUITAMOS COMPLETAMENTE SDK Y NDK → Que Buildozer elija los suyos, así no falla
# (NO VA NADA AQUÍ)

android.private_storage = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = armeabi-v7a,arm64-v8a

# Solo estas dos, que son obligatorias
android.enable_androidx = True
android.use_apache_http = True

# Encriptación (esta sí la dejamos, funciona así)
android.python_encrypt = yes


# --- BUILDOZER ---
[buildozer]
log_level = 2
warn_on_root = 1
