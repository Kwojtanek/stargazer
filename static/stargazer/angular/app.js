var app = angular.module('appList', ['ngResource','ngRoute'])

app.config(function($routeProvider){
    $routeProvider
        .when('/constellation', {
            controller: 'constellationsCtrl',
            templateUrl: '/static/stargazer/angular/routes/browse/Constellations.html'
        })
        .when('/constellation/:abbreviation', {
            controller: 'constallationsDetailCtrl',
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


SearchApp.run(function($rootScope,BugTrackerFactory,ContactAppletFactory) {
    $rootScope.hashtag = hashtag;

});


SearchApp.config(function($routeProvider,$locationProvider){
    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/',
        {
            controller: 'SearchCtrl',
            templateUrl: '/static/stargazer/angular/routes/search/SearchView.html',
        })
        .when('/object/:id',
        {
            controller : 'SingleViewCtrl',
            templateUrl: '/static/stargazer/angular/routes/search/SingleView.html'
        })
        .when('/browse/type', {
            controller: 'TypesCtrl',
            templateUrl: '/static/stargazer/angular/routes/browse/TypesView.html'
        })
        .when('/browse/type/:typesc', {
            controller: 'SingleTypeCtrl',
            templateUrl: '/static/stargazer/angular/routes/browse/SingleTypeView.html'
        })
        .when('/page404',
        {
            templateUrl: '/static/stargazer/angular/routes/404.html'})
        .when('/API',
        {
            templateUrl: '/static/stargazer/angular/routes/API.html'})
        .otherwise({
            redirectTo: '/page404',
        });
});
