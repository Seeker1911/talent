angular.module('talent')
.controller('ProfileController', function($scope, $http, RootFactory) {
  // Get the user page.
  $http.get("http://localhost:8000/Musicians")
       .then((res) => {
         console.log('res.data', res.data);

         user = RootFactory.getUserName()
         console.log("user: ", user);
         $scope.musician = res.data.filter(musician => {
           return musician.user.username === user
         })
         console.log('musician', $scope.musician);
       });



})
