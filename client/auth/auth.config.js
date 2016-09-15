'use strict'

angular.module('talent')
  .config($routeProvider => {
    $routeProvider
      .when('/login', {
        controller: 'LoginController',
        templateUrl: 'auth/login.html'
      })
      .when('/register', {
        controller: 'LoginController',
        templateUrl: 'auth/register.html'
      });
  })
