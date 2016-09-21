angular.module('talent')
  .controller('LoginController', [
    '$scope',
    '$http',
    '$location',
    'RootFactory',
    'apiUrl',

    function($scope, $http, $location, RootFactory, apiUrl) {

      // Default values for scope variables
      $scope.user = {
        username: "",
        password: ""
      };
      $scope.root = null;


      $scope.register = function() {
        let input = document.querySelector('[type="file"]');
        let image_file = input.files[0];

        let randomInteger = Math.random() * 1e17;
        let getFileExtension = image_file.type.split('/').slice(-1)[0];
        let randomPath = `${randomInteger}.${getFileExtension}`;

        firebase.storage().ref().child(randomPath).put(image_file)
            .then((res) => {
        $http({
          url: `${apiUrl}/register/`,
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            "username": $scope.user.username,
            "password": $scope.user.password,
            "email": $scope.user.email,
            "first_name": $scope.user.first_name,
            "last_name": $scope.user.last_name,
            "phone": $scope.user.phone,
            "social": $scope.user.social,
            "genre": $scope.user.genre,
            "company": $scope.user.company,
            "engineering": $scope.user.engineering,
            "artistDevelopment": $scope.user.artistDevelopment,
            "bio": $scope.user.bio,
            "location": $scope.user.location,
            "image": res.downloadURL
          }
        }).success(res => {
          if (res.success) {
            console.log("Registered");
            $location.path('/discover');
          }
        }).error(console.error);
      });

      /*
        Post the user-provided credentials to API
       */
      $scope.login = function() {
        $http({
          url: `${apiUrl}/login/`,
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            "username": $scope.user.username,
            "password": $scope.user.password
          }
        }).success(res => {
          if (res.success) {
            console.log('Success')
            /*
            Login was successful, store credentials for use in requests
            to API that require permissions
             */
            RootFactory.credentials({
              username: $scope.user.username,
              password: $scope.user.password
            });

            // Redirect on successful login
            $location.path('/discover');
          }
        }).error(console.error);
      };

    }
}]);
