[app]
title = CV Creator
package.name = cvcreator
package.domain = org.gabrielspark
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,pyjnius,reportlab
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/logo.png

android.api = 33
android.minapi = 21
android.private_storage = True
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = armeabi-v7a,arm64-v8a
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
