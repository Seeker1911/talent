angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/discover', {
        templateUrl: 'discover/discover.html',
        controller: 'DiscoverController',
      })
    .when('/artist/:artistID', {
      templateUrl: 'artist/artist.html',
      controller: 'ArtistController',
    })
    ))
