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
        //  Return musician sub 0 cuz theres only one user here anyway.
         return $scope.musician[0]
       })
       .then(() => {
         for(let i = 0; i < $scope.musician[0].songs.length; i++) {
           $http.get($scope.musician[0].songs[i])
            .then(res => $scope.musician[0].songs[i] = res.data)
         }
       })

  // $http.get('http://localhost:8000/Songs')
  //   .then((res)=>{
  //     console.log('songs res.data:', res.data);
  //     $scope.songs = res.data;
  //   })


})
