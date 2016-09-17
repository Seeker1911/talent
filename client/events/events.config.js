'user strict'
angular.module('talent', ['ngRoute', 'ui.bootstrap'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/events', {
        templateUrl: 'events/events.html',
        controller: 'EventsController',
      })))
