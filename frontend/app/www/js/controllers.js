angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, Evento) {
  Evento.get_eventos().then(
    function(eventos) {
      $scope.eventos = eventos;
    }
  )
})

;
