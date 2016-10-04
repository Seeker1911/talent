angular.module('talent')
.controller('EventsController', function($scope, $http, apiUrl, $location) {
  // Get the events data.
  $http.get(`${apiUrl}/Events`)
       .then((res) => $scope.events = res.data)

  //  user = RootFactory.getUserName()
  //  console.log("user: ", user);
  //  $scope.musician = res.data.filter(musician => {
  //    return musician.user.username === user
  //  })

  $scope.event = function(){
    // console.log(username);
    $http({
      url: `${apiUrl}/events/`,
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        "name": $scope.name,
        "email": $scope.email,
        "phone": $scope.phone,
        "social": $scope.social,
        "genre": $scope.genre,
        "location": $scope.location,
        "date": $scope.date,
        "musician": $scope.user,
      }
    }).success(res => {
      if (res.success) {
        console.log("Event Created");
        $location.path('/events');
      }
    }).error(console.error);
  }


})
