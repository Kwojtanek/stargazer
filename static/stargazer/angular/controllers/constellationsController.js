/**
 * Created by root on 10.05.15.
  */

app.controller('constellationsController', function($scope, Const){
    var constellation = Const.query()
    $scope.constellation = constellation
})
app.controller('constallationsDetailController', function( $routeParams, $scope, ConstNgcs){
    getData = function(page) {
        var ngcs = ConstNgcs.get({abbreviation: $routeParams.abbreviation, page: page});
        $scope.ngcs = ngcs;
    };
    page = 1;
    getData();

    $scope.clickNext = function(){
        if ($scope.ngcs.next != null) {
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

})

