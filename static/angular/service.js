var app = app|| angular.module('bongApp',['ngRoute','ngResource','ngGrid']);

app.service('Vote',function($http){
	 this.get = function(){
	 	return $http.get('/vote').then(function(response){
			return response.data;
		});
	 }
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
