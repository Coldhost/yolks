# Yolks

> **! This repository was edited for needs of Coldhost.eu !**

A curated collection of core images that can be used with Coldhost's Egg system. Each image is rebuilt
periodically to ensure dependencies are always up-to-date.

Images are hosted on `ghcr.io` and exist under the `games`, `installers`, and `yolks` spaces. The following logic
is used when determining which space an image will live under:

* `oses` — base images containing core packages to get you started.
* `games` — anything within the `games` folder in the repository. These are images built for running a specific game
or type of game.
* `installers` — anything living within the `installers` directory. These images are used by install scripts for different
Eggs within Coldhost, not for actually running a game server. These images are only designed to reduce installation time
and network usage by pre-installing common installation dependencies such as `curl` and `wget`.
* `yolks` — these are more generic images that allow different types of games or scripts to run. They're generally just
a specific version of software and allow different Eggs within Coldhost to switch out the underlying implementation. An
example of this would be something like Java or Python which are used for running bots, Minecraft servers, etc.

All of these images are available for `linux/amd64` and `linux/arm64` versions, unless otherwise specified, to use
these images on an arm64 system, no modification to them or the tag is needed, they should just work.

Tools is set of scripts that helps with functions that arent really easy with bash and more packages
They are compiled and put onto the docker image, so we dont need to install python on every docker
They contain 2 tarballs, normal and legacy. Legacy is used for images using older libc (musl based, may be working with glibc)

## Contributing

When adding a new version to an existing image, such as `java v42`, you'd add it within a child folder of `java`, so
`java/42/Dockerfile` for example. Please also update the correct `.github/workflows` file to ensure that this new version
is tagged correctly.

## Available Images (Always check for tagged packages, not everything is enabled to be packaged)

[![Installers](https://github.com/Coldhost/yolks/actions/workflows/installers.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/installers.yml)
[![Websites](https://github.com/Coldhost/yolks/actions/workflows/websites.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/websites.yml)
[![Java](https://github.com/Coldhost/yolks/actions/workflows/java.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/java.yml)
[![NodeJS](https://github.com/Coldhost/yolks/actions/workflows/nodejs.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/nodejs.yml)
[![Python](https://github.com/Coldhost/yolks/actions/workflows/python.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/python.yml)
[![Tools-CLI](https://github.com/Coldhost/yolks/actions/workflows/compile_py_tools.yml/badge.svg)](https://github.com/Coldhost/yolks/actions/workflows/compile_py_tools.yml)

* [`base oses`](https://github.com/Coldhost/yolks/tree/master/oses)
  * [`alpine`](https://github.com/Coldhost/yolks/tree/master/oses/alpine)
    * `ghcr.io/coldhost/yolks:alpine`
  * [`debian`](https://github.com/Coldhost/yolks/tree/master/oses/debian)
    * `ghcr.io/coldhost/yolks:debian`
* [`games`](https://github.com/Coldhost/yolks/tree/master/games)
  * [`rust`](https://github.com/Coldhost/yolks/tree/master/games/rust)
    * `ghcr.io/coldhost/games:rust`
  * [`source`](https://github.com/Coldhost/yolks/tree/master/games/source)
    * `ghcr.io/coldhost/games:source`
* [`golang`](https://github.com/Coldhost/yolks/tree/master/go)
  * [`go1.14`](https://github.com/Coldhost/yolks/tree/master/go/1.14)
    * `ghcr.io/coldhost/yolks:go_1.14`
  * [`go1.15`](https://github.com/Coldhost/yolks/tree/master/go/1.15)
    * `ghcr.io/coldhost/yolks:go_1.15`
  * [`go1.16`](https://github.com/Coldhost/yolks/tree/master/go/1.16)
    * `ghcr.io/coldhost/yolks:go_1.16`
  * [`go1.17`](https://github.com/Coldhost/yolks/tree/master/go/1.17)
    * `ghcr.io/coldhost/yolks:go_1.17`
* [`java`](https://github.com/Coldhost/yolks/tree/master/java)
  * [`java8`](https://github.com/Coldhost/yolks/tree/master/java/8)
    * `ghcr.io/coldhost/yolks:java_8`
  * [`java8 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/8j9)
    * `ghcr.io/coldhost/yolks:java_8j9`
  * [`java11`](https://github.com/Coldhost/yolks/tree/master/java/11)
    * `ghcr.io/coldhost/yolks:java_11`
  * [`java11 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/11j9)
    * `ghcr.io/coldhost/yolks:java_11j9`
  * [`java16`](https://github.com/Coldhost/yolks/tree/master/java/16)
    * `ghcr.io/coldhost/yolks:java_16`
  * [`java16 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/16j9)
    * `ghcr.io/coldhost/yolks:java_16j9`
  * [`java17`](https://github.com/Coldhost/yolks/tree/master/java/17)
    * `ghcr.io/coldhost/yolks:java_17`
  * [`java17 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/17j9)
    * `ghcr.io/coldhost/yolks:java_17j9`
  * [`java18`](https://github.com/Coldhost/yolks/tree/master/java/18)
    * `ghcr.io/coldhost/yolks:java_18`
  * [`java18 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/18j9)
    * `ghcr.io/coldhost/yolks:java_18j9`
  * [`java19`](https://github.com/Coldhost/yolks/tree/master/java/19)
    * `ghcr.io/coldhost/yolks:java_19`
  * [`java19 - OpenJ9`](https://github.com/Coldhost/yolks/tree/master/java/19j9)
    * `ghcr.io/coldhost/yolks:java_19j9`
  * [`java21`](https://github.com/Coldhost/yolks/tree/master/java/21)
    * `ghcr.io/coldhost/yolks:java_21`
* [`nodejs`](https://github.com/Coldhost/yolks/tree/master/nodejs)
  * [`node12`](https://github.com/Coldhost/yolks/tree/master/nodejs/12)
    * `ghcr.io/coldhost/yolks:nodejs_12`
  * [`node14`](https://github.com/Coldhost/yolks/tree/master/nodejs/14)
    * `ghcr.io/coldhost/yolks:nodejs_14`
  * [`node15`](https://github.com/Coldhost/yolks/tree/master/nodejs/15)
    * `ghcr.io/coldhost/yolks:nodejs_15`
  * [`node16`](https://github.com/Coldhost/yolks/tree/master/nodejs/16)
    * `ghcr.io/coldhost/yolks:nodejs_16`
  * [`node17`](https://github.com/Coldhost/yolks/tree/master/nodejs/17)
    * `ghcr.io/coldhost/yolks:nodejs_17`
  * [`node18`](https://github.com/Coldhost/yolks/tree/master/nodejs/18)
    * `ghcr.io/coldhost/yolks:nodejs_18`
  * [`node20`](https://github.com/Coldhost/yolks/tree/master/nodejs/20)
    * `ghcr.io/coldhost/yolks:nodejs_20`
  * [`node22`](https://github.com/Coldhost/yolks/tree/master/nodejs/22)
    * `ghcr.io/coldhost/yolks:nodejs_22`
  * [`node23`](https://github.com/Coldhost/yolks/tree/master/nodejs/23)
    * `ghcr.io/coldhost/yolks:nodejs_23`
  * [`discord.js-node12`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-12)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-12`
  * [`discord.js-node14`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-14)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-14`
  * [`discord.js-node15`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-15)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-15`
  * [`discord.js-node16`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-16)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-16`
  * [`discord.js-node17`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-17)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-17`
  * [`discord.js-node18`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-18)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-18`
  * [`discord.js-node20`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-20)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-20`
  * [`discord.js-node22`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-22)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-22`
  * [`discord.js-node23`](https://github.com/Coldhost/yolks/tree/master/nodejs/discord.js-23)
    * `ghcr.io/coldhost/yolks:nodejs_discord.js-23`
* [`python`](https://github.com/Coldhost/yolks/tree/master/python)
  * [`python2.7`](https://github.com/Coldhost/yolks/tree/master/python/2.7)
    * `ghcr.io/coldhost/yolks:python_2.7`
  * [`python3.7`](https://github.com/Coldhost/yolks/tree/master/python/3.7)
    * `ghcr.io/coldhost/yolks:python_3.7`
  * [`python3.8`](https://github.com/Coldhost/yolks/tree/master/python/3.8)
    * `ghcr.io/coldhost/yolks:python_3.8`
  * [`python3.9`](https://github.com/Coldhost/yolks/tree/master/python/3.9)
    * `ghcr.io/coldhost/yolks:python_3.9`
  * [`python3.10`](https://github.com/Coldhost/yolks/tree/master/python/3.10)
    * `ghcr.io/coldhost/yolks:python_3.10`
  * [`python3.11`](https://github.com/Coldhost/yolks/tree/master/python/3.11)
    * `ghcr.io/coldhost/yolks:python_3.11`
  * [`python3.12`](https://github.com/Coldhost/yolks/tree/master/python/3.12)
    * `ghcr.io/coldhost/yolks:python_3.12`
  * [`python3.13`](https://github.com/Coldhost/yolks/tree/master/python/3.13)
    * `ghcr.io/coldhost/yolks:python_3.13`
  * [`discord.py-python2.7`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-2.7)
    * `ghcr.io/coldhost/yolks:python_discord.py-2.7`
  * [`discord.py-python3.7`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.7)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.7`
  * [`discord.py-python3.8`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.8)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.8`
  * [`discord.py-python3.9`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.9)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.9`
  * [`discord.py-python3.10`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.10)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.10`
  * [`discord.py-python3.11`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.11)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.11`
  * [`discord.py-python3.12`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.12)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.12`
  * [`discord.py-python3.13`](https://github.com/Coldhost/yolks/tree/master/python/discord.py-3.13)
    * `ghcr.io/coldhost/yolks:python_discord.py-3.13`
* [`websites`](https://github.com/Coldhost/yolks/tree/master/websites)
  * [`azuriom-php8.2`](https://github.com/Coldhost/yolks/tree/master/websites/azuriom-php8.2)
    * `ghcr.io/coldhost/yolks:azuriom-php8.2`
  * [`azuriom-php8.2`](https://github.com/Coldhost/yolks/tree/master/websites/azuriom-php8.3)
    * `ghcr.io/coldhost/yolks:azuriom-php8.3`
  * [`azuriom-php8.2`](https://github.com/Coldhost/yolks/tree/master/websites/azuriom-php8.4)
    * `ghcr.io/coldhost/yolks:azuriom-php8.4`

### Installation Images

* [`alpine-install`](https://github.com/Coldhost/yolks/tree/master/installers/alpine)
  * `ghcr.io/coldhost/installers:alpine`

* [`debian-install`](https://github.com/Coldhost/yolks/tree/master/installers/debian)
  * `ghcr.io/coldhost/installers:debian`

### Tools CLI

* [`latest full-release tools`](https://github.com/Coldhost/yolks/tree/master/shared/tools)
  * `ghcr.io/coldhost/tools-cli:latest-full-release`
* [`latest full-debug tools`](https://github.com/Coldhost/yolks/tree/master/shared/tools)
  * `ghcr.io/coldhost/toola-cli:latest-full-debug`
* [`latest minimal-release tools`](https://github.com/Coldhost/yolks/tree/master/shared/tools)
  * `ghcr.io/coldhost/tools-cli:latest-minimal-release`
* [`latest minimal-debug tools`](https://github.com/Coldhost/yolks/tree/master/shared/tools)
  * `ghcr.io/coldhost/tools-cli:latest-minimal-debug`
