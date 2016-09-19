angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/portfolio', {
        templateUrl: 'profile/profile.html',
        controller: 'ProfileController',
      })))
