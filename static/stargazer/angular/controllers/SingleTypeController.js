SearchApp.controller('SingleTypeCtrl',['TypeFactory', '$scope', '$resource', '$routeParams', function(TypeFactory,SingleTypeFactory,$resource, $scope, $routeParams){
        document.getElementById('annotation-loader').style.display = 'inherit'
    SearchApp.factory('SingleTypeFactory',['$resource', function($resource){
        return $resource('/endpoint/typeAPI/:typesc',format);
    }]);

        $scope.type = SingleTypeFactory.get({typesc:$routeParams.typesc, page:1})

            document.getElementById('annotation-loader').style.display = ''

}])
