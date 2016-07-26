/**
 * Created by root on 05.11.15.
 */
SearchApp.controller('SingleViewCtrl',
    ['$scope', '$routeParams','CommonData','$resource',
        function($scope, $routeParams,CommonData, $resource){
            /* $scope.Common data -> Data passed throu CommonData factory from search page
             $scope.MainObject -< Data from CommonData matching index or if CommonData not passed from server
             */
            function asideshow(){
                if (doctop() > 200){
                    document.querySelector('aside').setAttribute('style',
                        'width: 100%; ' +
                        'position: fixed;' +
                        'top: 28px;' +
                        'z-index: 101;'
                    )
                }
                else {
                    document.querySelector('aside').setAttribute('style',

                        'width: 100%;' +
                        'position: absolute;' +
                        'top: 125px;' +
                        'left: 10%;' +
                        'z-index: 101;')
                }
            }
            asideshow()
            document.addEventListener('scroll', asideshow, false);
            //Downloads charts info
            getCharts = function () {
                ChartMapFactory = $resource('/endpoint/mapAPI', {
                    'asc': $scope.MainObject.rightAsc,
                    'dec': $scope.MainObject.declination,
                    'mag': $scope.MainObject.magnitudo
                })
                        document.getElementById('annotation-loader').style.display = 'inherit'
                        ChartMapFactory.get().$promise.then(function (ob) {
                            $scope.charts = ob;
                            document.querySelector('#search-charts > a:last-child').style.display = 'none';
                        })
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
            //Function downloads similar objects to main and append
            getSimilar = function(){
                SimilarFactory = $resource('/endpoint/similarAPI',{
                    type: $scope.MainObject.type_shortcut,
                    catalogue: $scope.MainObject.catalogues.slice(-1)[0].object_catalogue,
                    constellation: $scope.MainObject.constelation,
                    pk : $scope.MainObject.id
                });
                document.getElementById('annotation-loader').style.display = 'inherit'
                SimilarFactory.get().$promise.then(function (ob) {
                    $scope.similar = ob;
                    document.getElementById('annotation-loader').style.display = '';
                })

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
                    getSimilar();

                })

                $scope.scrollTo = function (id) {
                    $('html, body').animate({scrollTop:$('#' + id).position().top - 60}, 'slow');
                }

                $scope.getConstelationName = function () {
                    for (var index = 0; index < ConstList.length; index++) {
                        if (ConstList[index].value == $scope.MainObject.constelation) {
                            return ConstList[index].label
                        }
                    }
                }
            }
        }])