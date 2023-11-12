# MAAR (My Android Auto Radio)

<img src="app/maar.png" width="100" height="100">

With python3's [htag](https://github.com/manatlan/htag) module.


~~Android's Apk built thru the [htagapk recipe](https://github.com/manatlan/htagapk)
Build the APK using "Actions > Build Apk > Run workflow", the package.zip(apk) is available after 11-to-13 minutes in the resulted process ;-)~~

Does'nt work anymore ;-( ^^
but I reach to make an apk using buidozer's docker, on my host ;-) (full tuto soon)

in the `app` folder, with a console :
```
$ docker run -v $(pwd)/.buildozer:/home/user/.buildozer -v $(pwd):/home/user/hostcwd buildozerm android debug
$ adb uninstall org.manatlan.maar
$ adb install -r bin/maar-0.1-arm64-v8a-debug.apk
```
note: `buildozerm` is my docker image

**IMPORTANT** : 
You'll need to add manual rights for the app MAAR !!!

## notes

This is a POC, just to see if the whole idea is OK.

history:  I've got an android auto radio, with a 1280x480 (6.86") ... I don't like the current music player. So i try to replace it with something of my own.
It's just to try if an android apk, using htag, can replace the current app.
