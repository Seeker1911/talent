angular.module('talent', ['ngRoute'])
  .config(($routeProvider) => (
    $routeProvider
    .when('/login', {
      templateUrl: 'login/login.html',
      controller: 'LoginCtrl',
    })
    .when('/signup', {
      templateUrl: 'signup/signup.html',
      controller: 'SignupCtrl',
      })

    )
  )

  .factory('RootFactory', ($http, $timeout) => {
  let apiRoot = null;
  let httpGet = $http.get("http://localhost:8000");

  return {
    getApiRoot () {
      return httpGet.then(res => res.data)
    }
  }
})
