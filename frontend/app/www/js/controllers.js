angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, Evento) {
  Evento.get_eventos().then(
    function(eventos) {
      $scope.eventos = eventos;
    }
  )
})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

;
