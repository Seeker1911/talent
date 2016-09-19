angular.module('talent')
.controller('ProfileController', function($scope, $http) {
  // Get the user page.
  $http.get("http://localhost:8000/Musicians")
       .then((res) => $scope.musician = res.data)


})
