'use strict'
angular.module('talent')
  .controller('SignupCtrl', ['$scope', 'RootFactory', '$http', '$location', function ($scope, RootFactory, $http, $location) {
    console.log('Signup');
    const user = this;

    RootFactory.getApiRoot().then(root => {
      return root;
    }).then(res => {
      console.log('res', res);
      $http.get(`${res.Musicians}`).then(Musicians => {
        user.Musicians = Musicians.data;
        console.log('Musicians.data', Musicians.data);
        return user.Musicians;
      }).then(res => {

      })

    user.newMusician = function () {
      $http.post("http://localhost:8000/talent/Musicians/", {name: user.name, year_began: user.yearBegan, members: user.members})
      .then(res => {
        // getArtistList()
        user.name = '';
        $location.path('/#/');

      }, err => console.log(err))
    }

    })
  }])
