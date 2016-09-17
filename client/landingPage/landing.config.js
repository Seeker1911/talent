angular.module('talent', ['ngRoute', 'ui.bootstrap'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/landing', {
        templateUrl: 'landingPage/landingPage.html',
        controller: 'LandingController',
      })))
