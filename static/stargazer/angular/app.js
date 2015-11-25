var app = angular.module('appList', ['ngResource','ngRoute'])


app.config(function($routeProvider){
    $routeProvider
        .when('/',
        {
            controller: 'ListController',
            templateUrl: '/static/stargazer/angular/routes/browse/StellarList.html',
        })
        .when('/constellation', {
            controller: 'constellationsController',
            templateUrl: '/static/stargazer/angular/routes/browse/Constellations.html'
        })
        .when('/constellation/:abbreviation', {
            controller: 'constallationsDetailController',
            templateUrl: '/static/stargazer/angular/routes/browse/ConstellationsDetail.html'
        })
        .when('/catalogue', {
            controller: 'CatalogueController',
            templateUrl: '/static/stargazer/Catalogue.html'
        })
        .when('/catalogue/:name', {
            controller: 'CatalogueListController',
            templateUrl: '/static/stargazer/CatalogueLists.html'
        })
});


var SearchApp = angular.module('SearchApp', ['ngResource','ngRoute','ngAnimate'])

SearchApp.config(function($routeProvider){
    $routeProvider
        .when('/',
        {
            controller: 'SearchCtrl',
            templateUrl: '/static/stargazer/angular/routes/search/SearchView.html',
        })
        .when('/:id',
        {
            controller : 'SingleViewCtrl',
            templateUrl: '/static/stargazer/angular/routes/search/SingleView.html'
        })
        .otherwise({
        redirectTo: '/'
      });
});

//TODO Dopisz kontroler dla katalogów
//TODO Kontroller do pojedyńczego obiektu