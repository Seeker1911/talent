angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/events', {
        templateUrl: 'events/events.html',
        controller: 'EventsController',
      })))
