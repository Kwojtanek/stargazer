app.controller('ListController', ['$scope', '$http', function($scope, $http){
    //TODO Przepisać wczytywanie następnych stron tak jak w konstelacyji kontrolerze
    $scope.current = 'ngclist?format=json&page=1';
    $scope.next = 'ngclist?format=json&page=2';
    $scope.previous = null;

    getData = function(link){
        if ( link === null) {
            return null
        }
        if (link === undefined) link = 'ngclistAPI?format=json&page=1';
        $http.get(link).
            success(function(data, status) {
                $scope.ngcs = data;
                $scope.next = $scope.ngcs.next;
                $scope.previous = $scope.ngcs.previous;
            }).
            error(function(data, status) {
                $scope.ngc = data || "Request failed";
                $scope.status = status;
            });
    };


    getData();

    $scope.clickNext = function(){
        getData($scope.next);
      };
    $scope.clickPrevious = function(){
        getData($scope.previous);
      };
  }]);