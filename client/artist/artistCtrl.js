angular.module('talent')
.controller('ArtistController', function($scope, $http, apiUrl, $routeParams) {
  // Get the events data.
  console.log('routeparams', $routeParams.artistID);
  $http.get(`${apiUrl}/Musicians/${$routeParams.artistID}`)
       .then((res) => $scope.artist = res.data)


})
