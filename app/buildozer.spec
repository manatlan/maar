[app]

title = MAAR
package.name = maar
package.domain = org.manatlan

source.dir = .
source.include_exts = py,png,jpg

# (str) Presplash of the application
presplash.filename = %(source.dir)s/maar.png

# (str) Icon of the application
icon.filename = %(source.dir)s/maar.png

version = 0.2
requirements = python3,kivy,tornado,htag>=0.64.0,mutagen,Pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
# android.archs = armeabi-v7a

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_AUDIO,MEDIA_CONTENT_CONTROL

android.accept_sdk_license = True

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
