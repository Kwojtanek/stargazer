SearchApp.controller('FooterCtrl',['$scope','BugTrackerFactory','ContactAppletFactory', function($scope,BugTrackerFactory,ContactAppletFactory){
    $scope.bugtracker= false;
    $scope.contactapplet = false;
    $scope.sendbug = function(){
        BugTrackerFactory.save({},
            {
                "info" :$scope.bugform.info,
                "author":$scope.bugform.author,
                "userAgent":navigator.userAgent,
                "bugUrl": window.location.href

            })
        $scope.bugtracker= false;
        alert('Thank you');
    }
    $scope.sendcontact = function(){
        ContactAppletFactory.save({},
            {
                "author": $scope.contactapp.author,
                "message": $scope.contactapp.message
            })
        $scope.contactapplet = false;
        alert('Thank you');
    }
}])