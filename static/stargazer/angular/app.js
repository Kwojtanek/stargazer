var SearchApp = angular.module('SearchApp', ['ngResource','ngRoute'])
SearchApp.run(function($rootScope,BugTrackerFactory,ContactAppletFactory,$routeParams) {
    $rootScope.hashtag = hashtag;
});
SearchApp.config(function($routeProvider,$locationProvider){
    $locationProvider.html5Mode({
        enabled:true,
        requireBase:false
    });

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
        controller: 'ListCtrl',
        templateUrl: '/static/stargazer/angular/directives/stellar-list.html'
    }
}).directive('stellarFooter', function(){
    return {
        restrict: 'E',
        controller: 'FooterCtrl',
        templateUrl: '/static/stargazer/angular/directives/stellar-footer.html'
    }
}).directive('stellarCharts', function(){
    return {
        restrict: 'E',
        templateUrl: '/static/stargazer/angular/directives/stellar-charts.html'
    }
})