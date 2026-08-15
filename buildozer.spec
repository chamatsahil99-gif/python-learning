[app]

title = JARVIS
package.name = jarvis
package.domain = org.sahil
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy
android.accept_sdk_license = True

orientation = portrait

android.permissions = RECORD_AUDIO

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1
