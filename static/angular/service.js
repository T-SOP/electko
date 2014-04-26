var app = app|| angular.module('bongApp',['ngRoute','ngResource','ngGrid','ngCookies']);

app.service('Vote',function($http,$cookies){
	 this.get = function(){
	 	return $http.get('/vote').then(function(response){
			return response.data;
		});
	 }
	 this.like = function(news){
		 return $http.post('/vote/like',news,{
		 	headers:{
				'X-CSRFToken' : $cookies.csrftoken
			}
		 }).then(function(response){
			return response.data;
		});
 	//	return "this like link link is " + link;
	 }
	 this.unlike = function(news){

		return $http.post('/vote/unlike',news,{
			headers: {
				'X-CSRFToken' : $cookies.csrftoken
			}
		}).then(function(response){
			return response.data;
		}); 
	// 		 return "this dislike link link is " + link;
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
