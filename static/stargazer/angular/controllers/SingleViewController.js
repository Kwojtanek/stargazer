/**
 * Created by root on 05.11.15.
 */
SearchApp.controller('SingleViewCtrl',['$scope', '$routeParams','CommonData','$resource', '$location','$anchorScroll', function($scope, $routeParams,CommonData, $resource,$location,$anchorScroll){
    $scope.CommonData = CommonData.get();
    document.body.scrollTop = 75;


    // If you were redirected from search page you will get infos about the objects passed throu CommonData service
    // Otherwise data will be downloaded from server according to id param in url.
    if ($scope.CommonData.hasOwnProperty('index') === true){
        $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index]
        var aladin = A.aladin('#aladin-lite-div', {
            survey: "P/DSS2/color",
            fov: $scope.MainObject.Fov,
            target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
            showReticle : false});
    }
    else
    {
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
    $scope.nextIndex = function(index){
        if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index < $scope.CommonData.results.length) {
            console.log($scope.CommonData.index)
            $scope.CommonData.index++
            $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index]

            $location.path('#/'.concat($scope.MainObject.id))
            var aladin = A.aladin('#aladin-lite-div', {
                survey: "P/DSS2/color",
                fov: $scope.MainObject.Fov,
                target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
                showReticle : false});

        }

    }
    $scope.leastIndex = function(index){
        if (typeof $scope.CommonData !== 'undefinded' && $scope.CommonData.index >= 0) {
            console.log($scope.CommonData.index)
            $scope.CommonData.index--
            $scope.MainObject = $scope.CommonData.results[$scope.CommonData.index];
            var aladin = A.aladin('#aladin-lite-div', {
                survey: "P/DSS2/color",
                fov: $scope.MainObject.Fov,
                target: ($scope.MainObject.rightAsc).concat(' ',$scope.MainObject.declination),
                showReticle : false});
        }



    }
}])