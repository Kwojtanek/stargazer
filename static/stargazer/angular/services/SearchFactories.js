/**
 * Created by root on 02.07.15.
 */
var format = {format: 'json'}
SearchApp.factory('SearchFactory',['$resource', function($resource){
    return $resource('/endpoint/searchAPI',format);

}])
SearchApp.factory('SingleViewFactory',['$resource', function($resource){
    return $resource('/endpoint/singleAPI/1', format);

}])

SearchApp.factory('ChartsFactory',['$resource', function($resource,asc,dec,mag){
    return $resource('/endpoint/mapAPI',
        {
            'asc': asc,
            'dec': dec,
            'mag': mag,
            format: 'json'
        })
    }])
SearchApp.factory('SimilarFactory', ['$resource', function($resource,constellation,type,catalogue){
    return $resource('/endpoint/similarAPI',
        {
            type: type,
            catalogue: catalogue,
            constellation: constellation
        })
}])
SearchApp.factory('CommonData', function() {
    savedData = {}
    function set(data, index, filters, results,page,show) {
        if(typeof(Storage) !== "undefined") {
            if (data !== 'same'){localStorage.setItem('data',JSON.stringify(data))};
            if (results !== 'same'){localStorage.setItem('results', JSON.stringify(results))};
            if (page !== 'same'){localStorage.setItem('page',(page))};
            if (isNaN(parseInt(index))){localStorage.setItem('index', JSON.stringify(0));}
            else { localStorage.setItem('index',(index));}
            if (show !== 'same'){localStorage.setItem('show',(show))};

            if (filters !== 'same'){localStorage.setItem('filters',JSON.stringify(filters))}
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
            savedData.show = JSON.parse(localStorage.getItem('show'));
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
