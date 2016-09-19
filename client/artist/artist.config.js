angular.module('talent')
  .config(($routeProvider) => (
    $routeProvider
    .when('/artist/:artistID', {
      templateUrl: 'artist/artist.html',
      controller: 'ArtistController',
    })
    ))
