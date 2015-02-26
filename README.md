# Agenda TI

Agenda TI is a mobile app where you can find the next IT events (soon on Play Store).

*This repo is only to be used as a base or example*

## Technologies

### Front

    1. http://ionicframework.com/
    2. https://angularjs.org/
    3. https://github.com/mw-ferretti/angular-resource-tastypie (library to easily connect to the API resources)

### Back

    1. https://github.com/tgonzales/mingus (Simple REST framework that is being built over Tornado, you just need to create a schematic or model and then your API resources and endpoits will be all online, the default database is MongoDB)
    2. Crawler (on this repo, is a simple crawler to be used as an example)

### Other things that is not in this repo but is up and running on production server

    1. Supervidord (to take care of Mingus)
    2. Nginx (you can use with supervisor to do load balance)
    3. Celery & Rabbitmq (so you can periodic run the crawler)

*Etc...*