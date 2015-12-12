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

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

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
