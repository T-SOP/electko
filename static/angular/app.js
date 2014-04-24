var app = angular.module('bongApp',['ngRoute','ngResource']);

app.controller('MainCtrl',function($scope){
$scope.test="hhhh";
});
app.controller("LeftCtrl",function($scope,$http){
	$http.get('/vote').success(function(response){
		$http.articles = response.rank;
	});
});
app.controller('RightCtrl',function($scope,$http){
	console.log('rightCtrl');
	$http.get('/news/info').success(function(response){
		$scope.newses = response.news;
	});
  $scope.phones = [
	    {'name': 'Nexus S',
				     'snippet': 'Fast just got faster with Nexus S.'},
	    {'name': 'Motorola XOOM™ with Wi-Fi',
				     'snippet': 'The Next, Next Generation tablet.'},
	    {'name': 'MOTOROLA XOOM™',
				     'snippet': 'The Next, Next Generation tablet.'}
  ];
});

