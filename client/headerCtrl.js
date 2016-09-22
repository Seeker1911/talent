angular.module('talent')
.controller('headerCtrl', ['RootFactory', '$scope', function(RootFactory, $scope){
  $scope.loggedIn = function(){
    return RootFactory.credentials()
  }
  $scope.logout = function(){
    RootFactory.logout()
  }

  $scope.event = function(){
    
  }

  $scope.selected = null;

}])
