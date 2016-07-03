var SearchApp = angular.module('SearchApp', ['ngResource','ngRoute','ngAnimate'])
SearchApp.run(function($rootScope,BugTrackerFactory,ContactAppletFactory,$routeParams) {
    $rootScope.hashtag = hashtag;
    // IE compability
    var doctop = function(){
        if(document.documentElement && document.documentElement.scrollTop)
        {return document.documentElement.scrollTop}
        if(document.body.scrollTop)
        {return document.body.scrollTop}}
    var dochaight =function(){
        if(document.documentElement && document.documentElement.scrollHeight)
        {return document.documentElement.scrollHeight}
        if(document.body.scrollHeight)
        {return document.body.scrollHeight}
        else return 0;}
    $rootScope.layout = {};
    $rootScope.layout.list = true;
    $rootScope.layout.photo = false;
    function layout_function(lt){
        if (lt == 'list'){
            $rootScope.layout.list = true;
            $rootScope.layout.photo = false;
        }
        if (lt =='photo'){
            $rootScope.layout.photo = true;
            $rootScope.layout.list = false;
        }
    }
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
        .when('/about', {
            templateUrl: '/static/stargazer/angular/routes/about.html'
        })
        .when('/explore/:type/:typesc', {
            controller: 'ExploreCtrl',
            templateUrl: '/static/stargazer/angular/routes/explore/Explore.html'        })
        .when('/explore', {
            controller: 'MainExploreCtrl',
            templateUrl: '/static/stargazer/angular/routes/explore/MainExplore.html'        })
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

SearchApp.directive('stellarList', function(){
    return {
        restricte: 'E',
        templateUrl: '/static/stargazer/angular/directives/stellar-list.html'
    }
})