/**
 * Created by root on 02.07.15.
 */
SearchApp.factory('SearchFactory', function($resource){
    return $resource('/searchAPI',{format: 'json'});

})