/**
 * Created by root on 04.07.16.
 */
SearchApp.controller('ListCtrl',['$scope','CommonData', 'ChartsFactory', function($scope,CommonData,ChartsFactory){
    var el = document.querySelector('.display-details-fullframe');
    $scope.displayDetails = function($index){

        $scope.MainObject = CommonData.get().results[$index];
        el.style.opacity = 1;
        el.style.visibility = 'visible';
        ChartsFactory.get(
            {
                'asc': $scope.MainObject.rightAsc,
                'dec': $scope.MainObject.declination,
                'mag': $scope.MainObject.magnitudo,
                'index': $index
            }).$promise.then(function(ob){
                $scope.charts = ob;
            })
    }
    $scope.hideDetails = function(){
        el.style.opacity = 0;
        el.style.visibility = 'hidden';
    }
}])