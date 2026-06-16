[app]

title = Creador CV
package.name = creadorcv
package.domain = org.gabrielspark1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,reportlab

orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png


# ANDROID
android.api = 33
android.minapi = 21

android.private_storage = True

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.archs = armeabi-v7a,arm64-v8a

android.enable_androidx = True
android.use_apache_http = True

android.python_encrypt = yes


[buildozer]
log_level = 2
warn_on_root = 1
