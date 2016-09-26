angular.module('talent')
.controller('DiscoverController', function($scope, $http, apiUrl, $location) {
  // Get all the musicians data.
  $http.get(`${apiUrl}/Musicians`)
       .then((res) => {$scope.artists = res.data})

})
