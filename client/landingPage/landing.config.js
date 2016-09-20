angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/', {
        templateUrl: 'landingPage/landingPage.html',
        controller: 'LandingController',
      })))
