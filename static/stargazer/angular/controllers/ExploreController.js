/**
 * Created by root on 29.12.15.
 */
SearchApp.controller('ExploreCtrl',[ '$routeParams', '$scope', '$resource', function( $routeParams, $scope, $resource){
            $("html, body").animate({ scrollTop: 0 }, 600);
    if ($routeParams['type'] == 'type'){$scope.ChooseFieldsTypes = ddtypes}
    if ($routeParams['type'] == 'catalogue'){$scope.ChooseFieldsTypes = SearchCatalogues}
    if ($routeParams['type'] == 'constellation'){$scope.ChooseFieldsTypes = ConstList}

    $scope.pending = true;
    page = 1
    ListFactory = $resource('/'.concat('exploreAPI/',$routeParams['type'],'/',$routeParams['typesc']),{'page':page,'format':'json'})
    getList = function(){
        $('div.box').fadeIn(300);
        ListFactory.get().$promise.then(function(ob){
            $scope.data = ob;
            $scope.results = ob.results
            $('div.box').fadeOut(300);
            $scope.pending = false;
            window.document.title = $scope.data.results[0].type

        })
    }
    getList()

    function LoadOnScroll(){
        if ($scope.data && $scope.data.next !== null ) {
            // Checks if firs part of Data has been downloaded and next data exists
            if (doctop() >  dochaight() - 2200 && $scope.results.length < $scope.data.count){
                if (!$scope.pending) {
                    $scope.pending = true;
                    document.getElementById('annotation-loader').style.display = 'inherit';
                    ListFactory.get(
                        {
                            page: +page + 1,
                        }
                    ).$promise.then(function(ob){
                            page++
                            $scope.pending = false;
                            $scope.data = ob;
                            // appends results to list
                            for (var i = 0; i < ob.results.length; i++){
                                $scope.results.push(ob.results[i]);
                            }
                            document.getElementById('annotation-loader').style.display = '';
                        }
                    )
                }

            }
        }
    };

    document.addEventListener('scroll', LoadOnScroll, false);
}])
