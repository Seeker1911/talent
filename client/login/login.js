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
        $http.get(`${res.Production}`).then(Production => {
          user.Production = Production.data;
          console.log('Production.data', Production.data);
        })
        $http.get(`${res.Talent_management}`).then(Talent_management => {
          user.Talent_management = Talent_management.data;
          console.log('Talent_management.data', Talent_management.data);
        })

      })


    }])
