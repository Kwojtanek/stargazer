/**
 * Created by root on 05.11.15.
 */
SearchApp.controller('SingleViewCtrl',
    ['$scope', '$routeParams','CommonData','$resource', '$location','$anchorScroll',
        function($scope, $routeParams,CommonData, $resource,$location,$anchorScroll){
            /* $scope.Common data -> Data passed throu CommonData factory from search page
             $scope.MainObject -< Data from CommonData matching index or if CommonData not passed from server
             */

            //Downloads charts info
            getCharts = function () {
                ChartMapFactory = $resource('/endpoint/mapAPI', {
                    'asc': $scope.MainObject.rightAsc,
                    'dec': $scope.MainObject.declination,
                    'mag': $scope.MainObject.magnitudo
                })
                if ($scope.CommonData.index !== null) {
                    if ($scope.CommonData.results[$scope.CommonData.index].hasOwnProperty('charts') === false) {
                        document.getElementById('annotation-loader').style.display = 'inherit'
                        ChartMapFactory.get().$promise.then(function (ob) {
                            $scope.charts = ob;
                            $scope.CommonData.results[$scope.CommonData.index].charts = $scope.charts;
                            document.getElementById('annotation-loader').style.display = '';
                        })
                    }
                    else {
                        $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts;
                    }
                }
                else {
                    if (!$scope.charts) {
                        document.getElementById('annotation-loader').style.display = 'inherit'
                        ChartMapFactory.get().$promise.then(function (ob) {
                            $scope.charts = ob;
                            document.getElementById('annotation-loader').style.display = ''
                        })
                    }
                }
            }

                            // function that initialize interactive night sky map
                aladin = function () {
                    if ($scope.MainObject.rightAsc && $scope.MainObject.declination) {
                        if (!$scope.MainObject.fov) {
                            $scope.MainObject.fov == 45
                        }
                        var aladin = A.aladin('#aladin-lite-div', {
                            survey: "P/DSS2/color",
                            fov: $scope.MainObject.fov,
                            target: ($scope.MainObject.rightAsc).concat(' ', $scope.MainObject.declination),
                            showReticle:true
                        });
                        return true;
                    }
                    else {
                        var aladin = A.aladin('#aladin-lite-div', {
                            survey: "P/DSS2/color",
                            fov: 180,
                            target: ('0'),
                            showReticle: true
                        });
                        return false;
                    }


                }
            /* Function Checks if id parameter is correct, if it's not will redirect to 404 page */
            if ($routeParams.id > maxid || $routeParams.id <= 0 || isNaN($routeParams.id) )
            {window.location = '/'.concat('page404');}
            else {

                $scope.CommonData = CommonData.get();
                // Returns Name of firts found catalogue amd number of object
                $scope.getNextLast = function (index) {
                    if (index < $scope.CommonData.results.length && index >= 0) {
                        return $scope.CommonData.results[index].catalogues[0].object_catalogue.concat(' ', $scope.CommonData.results[index].catalogues[0].object_number)
                    }
                    else {
                        return false
                    }
                }


                // If you were redirected from search page you will get infos about the objects passed throu CommonData service
                // Otherwise data will be downloaded from server according to id param in url.
                console.log($scope.CommonData.results[$scope.CommonData.index].id, parseInt($routeParams.id))
                if ($scope.CommonData.index !== null && $scope.CommonData.results[$scope.CommonData.index].id == parseInt($routeParams.id)) {
                    $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index]
                    //Name of next object
                    $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
                    //Name of last object
                    $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)
                    title = $scope.MainObject.catalogues[0].object_catalogue.concat(' ',$scope.MainObject.catalogues[0].object_number);
                    window.document.title = title;
                    aladin()
                    getCharts()
                }
                else {
                    $scope.nextObject = false
                    $scope.lastObject = false

                    $('div.box').fadeIn(300);
                    var SingleViewFactory = $resource('/endpoint/singleAPI/:id', {id: $routeParams.id, format: 'json'});
                    SingleViewFactory.get().$promise.then(function (ob) {
                        $scope.MainObject = ob;
                        $('div.box').fadeOut(300);
                        title = $scope.MainObject.catalogues[0].object_catalogue.concat(' ',$scope.MainObject.catalogues[0].object_number);
                        window.document.title = title;
                        aladin();
                        getCharts();


                    })
                }

                $scope.scrollTo = function (id) {
                    var old = $location.hash();
                    $location.hash(id);
                    $anchorScroll();
                    //reset to old to keep any additional routing logic from kicking in
                    $location.hash(old);
                };

                // Sets Next or last Main object
                $scope.nextIndex = function (index) {
                    if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index < $scope.CommonData.results.length) {

                        $scope.CommonData.index++

                        $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
                        $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)

                        $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts;
                        $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index];
                        window.document.title = $scope.MainObject.catalogues[0].object_catalogue.concat(' ',$scope.MainObject.catalogues[0].object_number);
                        CommonData.set('same',$scope.CommonData.index++,'same','same','same');

                        //Aladin does not work when id  href is changed???
                        window.location = '/'.concat('object/',$scope.MainObject.id);
                    }
                }

                $scope.leastIndex = function (index) {
                    if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index >= 0) {

                        $scope.CommonData.index--
                        $scope.nextObject = $scope.getNextLast($scope.CommonData.index + 1)
                        $scope.lastObject = $scope.getNextLast($scope.CommonData.index - 1)

                        $scope.charts = $scope.CommonData.results[$scope.CommonData.index].charts
                        $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index];
                        window.document.title = $scope.MainObject.catalogues[0].object_catalogue.concat(' ',$scope.MainObject.catalogues[0].object_number);
                        window.location = '/'.concat('object/',$scope.MainObject.id);
                        CommonData.set('same',$scope.CommonData.index++,'same','same','same');
                    }
                }
                $scope.getConstelationName = function () {
                    for (var index = 0; index < ConstList.length; index++) {
                        if (ConstList[index].value == $scope.MainObject.constelation) {
                            return ConstList[index].label
                        }
                    }
                }
                // Pobiera z za API dane na temat mapy
            }
        }])