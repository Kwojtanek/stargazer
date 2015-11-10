/**
 * Created by root on 02.07.15.
 */
var format = {format: 'json'}
SearchApp.factory('SearchFactory', function($resource){
    return $resource('/searchAPI',{format: 'json'});

})
SearchApp.factory('SingleViewFactory', function($resource){
    return $resource('/singleAPI/1', format);

})

SearchApp.factory('CommonData', function() {
    var savedData = {};
    function set(data, index, filters) {
        savedData = data;
        savedData.index = index
        savedData.filters = filters
    };
    function get() {
        return savedData;
    };

    return {
        set: set,
        get: get
    };

});