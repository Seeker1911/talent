'use strict'

angular.module('talent')
  .config($routeProvider => {
    $routeProvider
      .when('/login', {
        controller: 'LoginController',
        templateUrl: 'auth/login.html'
      });
  })
