var app = angular.module('bongApp',['ngRoute','ngResource','ngGrid','ngCookies']);

app.config(['$httpProvider','$cookiesProvider',function($httpProvider,$cookies){
	$httpProvider.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken
}]);
/*
app.service('Vote',function(){
	 this.like = function(link){
	 		return "this like link link is " + link;
	 }
	 this.dislike = function(link){
	 		return "this dislike link link is " + link;
	 }
});

app.service('News',function($http){
	 this.get = function(){
	 	//	return "this like link link is " + link;
	 		return $http.get('/news/info').then(function(response){
					return response.data;
			});
	 }
});

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
*/
