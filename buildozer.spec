[app]
title = Creador CV - Gabriel Spark
package.name = creadorcv
package.domain = org.gabrielspark1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png

# ✅ MISMAS VERSIONES Y CONFIGURACIÓN QUE EL DE LA RULETA
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

android.private_storage = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.archs = armeabi-v7a,arm64-v8a

android.enable_androidx = True
android.use_apache_http = True
android.meta_data = android.support.PREFER_ANDROID=true

# ✅ ESTAS SON LAS LÍNEAS QUE LE FALTABAN Y POR ESO FALLABA
android.python_encrypt = yes
android.accept_license = yes
android.ndk_legacy_toolchain = True
android.skip_update = True

[buildozer]
log_level = 2
warn_on_root = 1
