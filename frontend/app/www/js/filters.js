angular.module('starter.filters', [])

.filter('dateFromTimestamp', function() {
    return function(timestamp) {
        return new Date(timestamp);
    };
})

;