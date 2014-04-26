
var app = app || angular.module('bongApp',['ngRoute','ngResource','ngGrid']);

app.controller('MainCtrl',function($scope,Vote){
$scope.test="hhhh";
});


app.controller("LeftCtrl",function($scope,$http){
	$http.get('/vote').success(function(response){
		$http.articles = response.rank;
	});
});


app.controller('RightCtrl',function($scope,$http,News,Vote){
	console.log('rightCtrl');

	News.get().then(function(d){
		$scope.newses = 	d.news;
	});
	$scope.like = function(index){
		var link = $scope.newses[index].link;
		console.log(Vote.like(link));
	};
	$scope.dislike = function(index){
		var link = $scope.newses[index].link;
		console.log(Vote.like(link));
	};
	};
});

