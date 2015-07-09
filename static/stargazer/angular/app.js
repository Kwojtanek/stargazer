var app = angular.module('appList', ['ngResource','ngRoute'])

var SearchApp = angular.module('SearchApp', ['ngResource'])


app.config(function($routeProvider){
    $routeProvider
        .when('/',
        {
            controller: 'ListController',
            templateUrl: '/static/stargazer/ngc_list.html'
        })
        .when('/constellation', {
            controller: 'constellationsController',
            templateUrl: '/static/stargazer/constellations.html'
        })
        .when('/constellation/:abbreviation', {
            controller: 'constallationsDetailController',
            templateUrl: '/static/stargazer/constellationsDetail.html'
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
//TODO Dopisz kontroler dla katalogów
//TODO Kontroller do pojedyńczego obiektu