/**
 * Created by root on 02.07.15.
 */
var format = {format: 'json'}
SearchApp.factory('SearchFactory',['$resource', function($resource){
    return $resource('/endpoint/searchAPI',format);

}])
SearchApp.factory('SingleViewFactory',['$resource', function($resource){
    return $resource('/endpoint/singleAPI/:id',format);


}]);
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
SearchApp.factory('HintFactory',['$resource', function($resource, name){
    return $resource('/endpoint/hintAPI',
        {
            'name': name,
            format: 'json'
        })
    }])
SearchApp.factory('CommonData', function() {
    //Variables:
    //  Index: id of object Int
    // filters: filters on main page dict
    // results: resulted data from server List
    // page: adds up if next part of list is downloaded Int
    // show: Remembers if page should be displayed expanded or collapsed Bool
    savedData = {}
    function set(index, filters, results,page,show) {
        if(typeof(Storage) !== "undefined") {
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
