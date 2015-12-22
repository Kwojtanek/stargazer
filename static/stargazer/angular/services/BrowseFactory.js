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
