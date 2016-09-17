angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/landing', {
        templateUrl: 'landingPage/landingPage.html',
        controller: 'LandingController',
      })))
