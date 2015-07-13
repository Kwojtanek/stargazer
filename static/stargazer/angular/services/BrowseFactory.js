/**
 * Created by root on 12.05.15.
  */
var format = {format: 'json'}
app.factory('Const', function($resource){
    return $resource('/constellationsAPI',format);
});
app.factory('ConstNgcs', function($resource){
    return $resource('/constellationsAPI/:abbreviation',format);
});
app.factory('StellarFactory', function($resource){
    return $resource('/StellarlistAPI',format);
});
