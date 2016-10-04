'use strict'
var config = {
   apiKey: "AIzaSyAav7EOX67IV25U6-PKHldUy8tGYW6hcuE",
   authDomain: "talent-31556.firebaseapp.com",
   databaseURL: "https://talent-31556.firebaseio.com",
   storageBucket: "talent-31556.appspot.com",
   messagingSenderId: "503379600864"
 };
 firebase.initializeApp(config);

const app = angular.module('talent', ['ngRoute', 'ui.bootstrap', 'ngCookies'])
app.constant('apiUrl', "http://musiccitytalent.com:8000")

// app.config($httpProvider => {
//     $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//     $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
// })

// angular.module('talent')
app.factory('RootFactory', [
    "$http",
    "$timeout",
    "apiUrl",
    "$cookies",
    "$location",

    ($http, $timeout, apiUrl, $cookies, $location) => {
        let apiRoot = null;
        let httpGet = $http.get(apiUrl);
        let userCredentials = null;

        return {
            getApiRoot() {
                return httpGet.then(res => res.data)
            },
            credentials (creds) {
              if (creds) {
                // Encodes to base 64 string
                userCredentials = window.btoa(`${creds.username}:${creds.password}`);
                $cookies.put('talent', userCredentials);
              } else {
                return userCredentials;
              }
            },
            logout () {
              userCredentials = null;
              $cookies.remove('talent');
              $location.path("/");
            },
            read () {
              return userCredentials = $cookies.get('talent');
            },
            update (creds) {
              userCredentials = creds;
            },
            getUserName() {
              // un-encodes base 64 string to JS
              try {
                let userName = window.atob(userCredentials).split(':')[0];
                return userName;
              }
              catch(e) {
                $location.path("/");
                return null;
              }

            }
        }
    }
])
angular.module('talent').run((RootFactory) => {
  RootFactory.read();
});
