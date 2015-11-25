/**
 * Created by root on 05.11.15.
 */
SearchApp.controller('SingleViewCtrl',['$scope', '$routeParams','CommonData','$resource', '$location','$anchorScroll', function($scope, $routeParams,CommonData, $resource,$location,$anchorScroll){
    /* $scope.Common data -> Data passed throu CommonData factory from search page
     $scope.MainObject -< Data from CommonData matching index or if CommonData not passed from server
     */
    $scope.CommonData = CommonData.get();
    document.body.scrollTop = 75;

    // Returns Name of firts found catalogue amd number of object
    $scope.getNextLast = function(index) {
        if (index < $scope.CommonData.results.length && index >= 0)

        {
            console.log(index);

            return $scope.CommonData.results[index].catalogues[0].object_catalogue.concat(' ', $scope.CommonData.results[index].catalogues[0].object_number)}
        else{return false}
    }


    // If you were redirected from search page you will get infos about the objects passed throu CommonData service
    // Otherwise data will be downloaded from server according to id param in url.
    if ($scope.CommonData.hasOwnProperty('index') === true){
        $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index]
        //Name of next object
        $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
        //Name of last object
        $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)

        ;



        var aladin = A.aladin('#aladin-lite-div', {
            survey: "P/DSS2/color",
            fov: $scope.MainObject.Fov,
            target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
            showReticle : false});
    }
    else
    {
        $scope.nextObject = false
        $scope.lastObject = false

        $('div.box').fadeIn(300);
        var SingleViewFactory = $resource('/singleAPI/:id',{id:$routeParams.id,format:'json'});
        SingleViewFactory.get().$promise.then(function(ob){
            $scope.MainObject = ob;
            $('div.box').fadeOut(300);
            var aladin = A.aladin('#aladin-lite-div', {
                survey: "P/DSS2/color",
                fov:$scope.MainObject.Fov,
                target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
                showReticle : false
            });
        })
    }

    $scope.scrollTo = function(id) {
        var old = $location.hash();
        $location.hash(id);
        $anchorScroll();
        //reset to old to keep any additional routing logic from kicking in
        $location.hash(old);
    };

    // Sets Next or last Main object
    $scope.nextIndex = function(index){
        if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index < $scope.CommonData.results.length) {

            $scope.CommonData.index++

            $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
            $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)

            $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts
            $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index]
            var aladin = A.aladin('#aladin-lite-div', {
                survey: "P/DSS2/color",
                fov: $scope.MainObject.Fov,
                target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
                showReticle : false});

        }
    }

    $scope.leastIndex = function(index){
        if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index >= 0) {

            $scope.CommonData.index--

            $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
            $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)

            $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts
            $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index];
            var aladin = A.aladin('#aladin-lite-div', {
                survey: "P/DSS2/color",
                fov: $scope.MainObject.Fov,
                target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
                showReticle : false});
        }
    }
    $scope.getConstelationName = function() {
        for (var index = 0; index < ConstList.length; index++) {
            if (ConstList[index].value == $scope.MainObject.constelation) {
                return ConstList[index].label
            }
        }
    }
    // Pobiera z za API dane na temat mapy
    $scope.getCharts = function() {
        ChartMapFactory = $resource('/mapAPI', {
            'asc': $scope.MainObject.rightAsc,
            'dec': $scope.MainObject.declination,
            'mag': $scope.MainObject.magnitudo
        })

        if ($scope.CommonData.hasOwnProperty('index') === true) {
            if ($scope.CommonData.results[$scope.CommonData.index].hasOwnProperty('charts') === false) {
                $('div.box').fadeIn(300);
                console.log('click');
                ChartMapFactory.get().$promise.then(function (ob) {
                    $scope.charts = ob;
                    $scope.CommonData.results[$scope.CommonData.index].charts = $scope.charts;
                    $('div.box').fadeOut(300);
                })
            }
            else {
                $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts;
            }
        }
        else {
            if (!$scope.charts){
            $('div.box').fadeIn(300);
            ChartMapFactory.get().$promise.then(function (ob) {
                $scope.charts = ob;
                $('div.box').fadeOut(300);
            })
        }
            }
    }
}])