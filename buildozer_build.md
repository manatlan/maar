# Recipe to build the apk

The "github action recipe" ([ArtemSBulgakov/buildozer-action@v1](https://github.com/ArtemSBulgakov/buildozer-action)) does'nt work anymore ;-(. Because of [this bug](https://github.com/ArtemSBulgakov/buildozer-action/issues/34). So this recipe will use the `buildozer's docker method`.

So now (2023/11/13) : this recipe is the official one to create an APK from an [Htag](https://github.com/manatlan/htag)'s app ;-)

2023/11/14 : take a look at [make.py](make.md), it's a command-line which should help you to create an apk (not related to this repo/maar) ! (it basically do all that is decribed bellow)

## Build a docker image -> mybuildozer
In any folder, you will create a docker image, using buidolzer's sources from git (up to date)
```bash
git clone https://github.com/kivy/buildozer.git
cd buildozer
docker build --tag=mybuildozer .
```
It will create a docker image named `mybuildozer`

## Build apk
In the "app" folder (where buildozer.spec is)...
```bash
mkdir .buildozer
docker run -v $(pwd)/.buildozer:/home/user/.buildozer -v $(pwd):/home/user/hostcwd mybuildozer android debug
```
**note** : the first time is a lot longer, following will be less than 2 minutes.

## Install the APK
The apk is generated in `./bin`

Plug your device, and ensure that it's in `developper mode`, and plugged in your host.
```bash
adb devices
```

If you want to remove previous version, before installing the new one
```bash
adb uninstall org.manatlan.maar
```

And install it
```bash
adb install -d ./bin/maar-0.1-arm64-v8a-debug.apk
```


# Enter into the DOCKER
It can be useful to enter in the docker image (but you will need to commit your changes, if you make changes)
```bash
docker run --interactive --tty --rm \
   --volume "$PWD/.buildozer":/home/user/.buildozer \
   --volume "$PWD":/home/user/hostcwd \
   --entrypoint /bin/bash \
   mybuidozer
```


