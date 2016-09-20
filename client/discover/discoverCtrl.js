angular.module('talent')
.controller('DiscoverController', function($scope, $http) {
  // Get the events data.
  $http.get("http://localhost:8000/Musicians")
       .then((res) => {$scope.artists = res.data})


})
