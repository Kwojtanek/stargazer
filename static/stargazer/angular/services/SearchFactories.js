/**
 * Created by root on 02.07.15.
 */
var format = {format: 'json'}
SearchApp.factory('SearchFactory', function($resource){
    return $resource('/endpoint/searchAPI',format);

})
SearchApp.factory('SingleViewFactory', function($resource){
    return $resource('/endpoint/singleAPI/1', format);

})
SearchApp.factory('ChartsFactory'), function($resource,asc,dec,mag){
    return $resource('/endpoint/mapAPI',
        {
            'asc': asc,
            'dec': dec,
            'mag': mag
        })}
SearchApp.factory('CommonData', function() {
    savedData = {}
    function set(data, index, filters, results,page) {
        if(typeof(Storage) !== "undefined") {
            localStorage.setItem('data',JSON.stringify(data));
            localStorage.setItem('results', JSON.stringify(results));
            localStorage.setItem('page',(page));
            if (isNaN(parseInt(index))){localStorage.setItem('index', JSON.stringify(0));}
            else { localStorage.setItem('index',(index));}
            localStorage.setItem('filters',JSON.stringify(filters))
            // Code for localStorage/sessionStorage.
        }       else {
            // Sorry! No Web Storage support..
        }

    };
    function get() {
        if(typeof(Storage) !== "undefined") {
            savedData.data = JSON.parse(localStorage.getItem('data'));
            savedData.index = JSON.parse(localStorage.getItem('index'));
            savedData.filters =JSON.parse(localStorage.getItem('filters'));
            savedData.results = JSON.parse(localStorage.getItem('results'));
            savedData.page = (localStorage.getItem('page'));
            return savedData;
        } else return savedData;
    };

    function isEmpty(savedData) {
        for(var data in savedData) {
            if(savedData.hasOwnProperty(data)){
                return false;
            }
        }
        return true;
    }
    return {
        set: set,
        get: get,
        isEmpty: isEmpty

    };

});