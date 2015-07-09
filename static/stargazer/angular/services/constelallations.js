/**
 * Created by root on 12.05.15.
  */
app.factory('Const', function($resource){
    return $resource('/constellationsAPI',{format: 'json'});
});
app.factory('ConstNgcs', function($resource){
    return $resource('/constellationsAPI/:abbreviation', {format: 'json'});
});
