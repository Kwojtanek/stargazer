/**
 * Created by root on 12.01.16.
 */
SearchApp.controller('MainExploreCtrl', ['$scope',function($scope) {
    $scope.Types = SearchTypes;
    $scope.Catalogues = SearchCatalogues;
    $scope.ddtypes = ddtypes;
    $scope.Constellations = ConstList;
    $scope.maxid = maxid;
    $scope.familycount = familycount
}])
