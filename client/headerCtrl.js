angular.module('talent')
.controller('headerCtrl', ['RootFactory', '$scope', '$location', function(RootFactory, $scope, $location){
  $scope.loggedIn = function(){
    return RootFactory.credentials()
  }
  $scope.logout = function(){
    RootFactory.logout()
  }

  // $scope.event = function(){
  //   $location.path('/createEvent')
  // }

  $scope.selected = null;

}])
