angular.module('talent')
.controller('ArtistController', function($scope, $http, $routeParams) {
  // Get the events data.
  console.log('routeparams', $routeParams.artistID);
  $http.get(`http://localhost:8000/Musicians/${$routeParams.artistID}`)
       .then((res) => $scope.artist = res.data)


})
