var format = {format: 'json'}
SearchApp.factory('BugTrackerFactory', function($resource) {
    return $resource('/endpoint/bugtrackerAPI', format);
})
SearchApp.factory('ContactAppletFactory', function($resource) {
    return $resource('/endpoint/contactappletAPI', format);
})