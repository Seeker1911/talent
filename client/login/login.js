  'use strict'
  angular.module('talent')
    .controller('LoginCtrl', ['$scope', 'RootFactory', '$http', '$location', function ($scope, RootFactory, $http, $location) {
      console.log('login');
      const user = this;

      RootFactory.getApiRoot().then(root => {
        return root;
      }).then(res => {
        console.log('res', res);
        $http.get(`${res.Musicians}`).then(Musicians => {
          user.Musicians = Musicians.data;
          console.log('Musicians.data', Musicians.data);
        })

      })

    }])
