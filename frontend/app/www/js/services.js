angular.module('starter.services', [])

.service('Evento', function($tastypieResource) {
  var EventosResource = new $tastypieResource('eventos');

  this.get_eventos = function() {
    return EventosResource.objects.$find();
  }
})
;
