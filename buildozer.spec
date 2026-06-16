[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Quedan solo estos tres requerimientos base. Reportlab y Pillow entran mediante el yml.
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png

# =============================================================================
# Android Específico
# =============================================================================

android.api = 33
android.minapi = 21

android.private_storage = True
android.permissions = INTERNET, READ_MEDIA_IMAGES

android.archs = armeabi-v7a,arm64-v8a

android.enable_androidx = True
android.use_apache_http = True

# =============================================================================
# Buildozer
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
