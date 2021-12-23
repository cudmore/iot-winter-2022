## Intro

Want to install Home Assistant on Pi to act as a local collection server.

Should actually be able to program Huzzah32 over the air (OTA).


Following: https://www.home-assistant.io/installation/raspberrypi/

### Install docker

    https://phoenixnap.com/kb/docker-on-raspberry-pi

### Install libseccomp


### run home assist docker

From: https://www.home-assistant.io/installation/raspberrypi/

```
docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=America/Los_Angeles \
  -v /myhomeassistant:/config \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```

Docker failed miserably

## install home assist image.

Will have to add ssh plugin later

https://pimylifeup.com/home-assistant-raspberry-pi/

at home is

http://192.168.1.12:8123

## activate ssh

https://smarthomepursuits.com/connect-to-home-assistant-ssh/

```
ssh root@192.168.1.12
```

- platform: mqtt
    name: "Nano PH"
    state_topic: "classroom/pushbutton1"
    qos: 0
    unit_of_measurement: "binary"  


## Mosquitto broker on mac os

```
brew install mosquitto
```

config is in 

/opt/homebrew/etc/mosquitto/mosquitto.conf

To restart mosquitto after an upgrade:
  brew services restart mosquitto
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf
