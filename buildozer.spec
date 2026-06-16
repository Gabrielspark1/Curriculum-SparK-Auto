[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# ✅ CORREGIDO: Dejamos solo lo esencial. 'reportlab' y 'pillow' se instalarán 
# automáticamente a través de la instrucción pip del archivo build.yml
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# =============================================================================
# Android → LO MÍNIMO Y SEGURO (COMPATIBLE CON API 33+)
# =============================================================================

android.api = 33
android.minapi = 21

android.private_storage = True

# ✅ CORREGIDO: Dejamos únicamente internet y acceso a imágenes por si tu CV lleva foto de perfil.
# Se eliminaron los permisos de audio y video que causan bloqueos innecesarios en Android 13.
android.permissions = INTERNET, READ_MEDIA_IMAGES

android.archs = armeabi-v7a,arm64-v8a

# ✅ SOLO ESTAS DOS OBLIGATORIAS (NO TOCAR)
android.enable_androidx = True
android.use_apache_http = True

# ❌ ELIMINADA LA LÍNEA DE ARGUMENTOS OBSOLETA QUE CORRUMPÍA EL MANIFIESTO


# =============================================================================
# Buildozer
# =============================================================================

[buildozer]
log_level = 2
warn_on_root = 1
