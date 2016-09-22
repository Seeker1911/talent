angular.module('talent')
.controller('DiscoverController', function($scope, $http, $location) {
  // Get all the musicians data.
  $http.get("http://localhost:8000/Musicians")
       .then((res) => {$scope.artists = res.data})

})
