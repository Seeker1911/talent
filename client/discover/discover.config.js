'user strict'
angular.module('talent', ['ngRoute', 'ui.bootstrap'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/discover', {
        templateUrl: 'discover/discover.html',
        controller: 'DiscoverController',
      })))
