'use strict'
var config = {
   apiKey: "AIzaSyAav7EOX67IV25U6-PKHldUy8tGYW6hcuE",
   authDomain: "talent-31556.firebaseapp.com",
   databaseURL: "https://talent-31556.firebaseio.com",
   storageBucket: "",
   messagingSenderId: "503379600864"
 };
 firebase.initializeApp(config);
 
const app = angular.module('talent', ['ngRoute', 'ui.bootstrap'])
app.constant('apiUrl', "http://localhost:8000")

app.config($httpProvider => {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

// angular.module('talent')
app.factory('RootFactory', [
    "$http",
    "$timeout",
    "apiUrl",

    ($http, $timeout, apiUrl) => {
        let apiRoot = null;
        let httpGet = $http.get(apiUrl);
        let userCredentials = {};

        return {
            getApiRoot() {
                return httpGet.then(res => res.data)
            },
            credentials(creds) {
                if (creds) {
                    userCredentials = creds;
                } else {
                    if (userCredentials.hasOwnProperty("password")) {
                        return window.btoa(`${userCredentials.username}:${userCredentials.password}`);
                    } else {
                        return false;
                    }
                }
            },
            getUserName() {
              return userCredentials.username;
            }
        }
    }
])
