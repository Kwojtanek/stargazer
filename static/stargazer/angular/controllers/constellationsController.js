/*
app.controller('constellationsController',['$scope','Const', function($scope, Const){
    var constellation = Const.query()
    $scope.constellation = constellation
}])
app.controller('constallationsDetailController',[ '$routeParams', '$scope', 'ConstNgcs', function( $routeParams, $scope, ConstNgcs){
    getData = function(page) {
        var ngcs = ConstNgcs.get({abbreviation: $routeParams.abbreviation, page: page});
        $scope.ngcs = ngcs;
    };
    getData();
    page = 1;
$scope.clickNext = function(){
    if ($scope.ngcs.next != null) {
        page++;
        getData(page);
    }
};
$scope.clickPrevious = function(){
    if (page != 1) {
        page--;
        getData(page);
    }
};

}])
var format = {format: 'json'}
app.factory('Const',['$resource', function($resource){
    return $resource('/constellationsAPI',format);
}]);
app.factory('ConstNgcs',['$resource', function($resource){
    return $resource('/constellationsAPI/:abbreviation',format);
}]);
app.factory('StellarFactory',['$resource', function($resource){
    return $resource('/StellarlistAPI',format);
}]);
SearchApp.factory('TypeFactory',['$resource', function($resource){
    return $resource('/endpoint',format);
}]);

*/