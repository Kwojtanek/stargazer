var format = {format: 'json'}
SearchApp.factory('BugTrackerFactory',['$resource', function($resource) {
    return $resource('/endpoint/bugtrackerAPI', format);
}])
SearchApp.factory('ContactAppletFactory',['$resource', function($resource) {
    return $resource('/endpoint/contactappletAPI', format);
}])