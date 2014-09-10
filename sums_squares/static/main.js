var squaresApp = angular.module( 'squaresApp', [] );

squaresApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

squaresApp.controller( 'SquaresCtrl', ['$scope', '$http', function($scope, $http) {

$scope.updateNumber = function() {
    var difference_url = 'difference?number=' + $scope.number.trim();
    $http({method: 'GET', url: difference_url}).
	success(function(data, status) {
	    $scope.result = data;
	    $scope.status = status;
	}).
        error(function(data, status) {
            $scope.status = status;
	});
};

}]);

