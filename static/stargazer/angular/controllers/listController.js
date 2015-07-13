app.controller('ListController', ['$scope', '$http', 'StellarFactory', function($scope, $http,StellarFactory){
    getData = function(page) {
        $scope.StellarList = StellarFactory.get({page: page});;
    };
    getData();
    page = 1;
    $scope.clickNext = function(){
        if ($scope.StellarList.next != null) {
            page++;
            getData(page);
        }
    };
    $scope.clickPrevious = function(){
        if (page != 1) {
            page--;
            getData(page);
        }
    };
}]);