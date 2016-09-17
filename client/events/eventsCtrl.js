angular.module('talent')
.controller('EventsController', function($scope, $http) {
  // Get the events data.
  $http.get("http://localhost:8000/Events")
       .then((res) => $scope.events = res.data)



})
