var app = angular.module('appList', ['ngResource','ngRoute'])

var SearchApp = angular.module('SearchApp', ['ngResource', 'ngAnimate'])
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
        .when('ngrou/catalogue/:name', {
            controller: 'CatalogueListController',
            templateUrl: '/static/stargazer/CatalogueLists.html'
        })
});
//TODO Dopisz kontroler dla katalogów
//TODO Kontroller do pojedyńczego obiektu