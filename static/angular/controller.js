
var app = app || angular.module('bongApp',['ngRoute','ngResource','ngGrid','ngCookies']);

app.controller('MainCtrl',function($scope,Vote){
$scope.test="hhhh";
});

app.controller("LeftCtrl",function($scope,Vote){
	Vote.get().then(function(d){
		$scope.votes = d.vote
	});
});

app.controller('RightCtrl',function($scope,$cookies,News,Vote){
	console.log('rightCtrl');
	console.log($cookies.csrftoken);

	News.get().then(function(d){
		$scope.newses = 	d.news;
	});
	$scope.like = function(index){
		var link = $scope.newses[index].link;
		news = $scope.newses[index];
		console.log(news);
		console.log(Vote.like(news));
	};
	$scope.unlike = function(index){
		var link = $scope.newses[index].link,
		news = $scope.newses[index];
		console.log(news);
		console.log(Vote.unlike(news));
	};
});

