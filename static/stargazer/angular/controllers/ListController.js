/**
 * Created by root on 04.07.16.
 */
SearchApp.controller('ListCtrl',['$scope','CommonData', 'ChartsFactory', function($scope,CommonData,ChartsFactory){
    $scope.displayDetails = function($index){
        var el = document.querySelector('.display-details-fullframe');
        $scope.stellob = CommonData.get().results[$index];
        $(el).fadeIn();
        var CharF = ChartsFactory.get(
            {
                'asc': $scope.stellob.rightAsc,
                'dec': $scope.stellob.declination,
                'mag': $scope.stellob.magnitudo,
                'index': $index
            })
    }
    $scope.hideDetails = function(){
        el =document.querySelector('.display-details-fullframe');
        $(el).fadeOut()

    }
}])