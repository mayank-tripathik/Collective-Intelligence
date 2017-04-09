import math

# Sample data of Critics with the list of movies they rated
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


#returns common movies between two persons
def common_movies(person1,person2):
	common=[]
	n_movies=critics[person1]
	for movie in n_movies:
		if(movie in critics[person2]):
			common.append(movie)
	return common

#returns euclidean distance between two persons calculated over common movies
def euclidean_distance(person1,person2,common_movie):
	d=0.0
	for movie in common_movie:
		x=critics[person1][movie]
		y=critics[person2][movie]
		d=d+math.pow(x-y,2)
	return 1/(1+d)

#pearson coefficient formula
def pearson_coefficient_formula(sigma_x,sigma_y,sigma_xsquare,sigma_ysquare,sigma_xy,n):
	numerator=sigma_xy-((sigma_x*sigma_y)/n)
	denominator=(math.sqrt(sigma_xsquare-((math.pow(sigma_x,2))/n)))*(math.sqrt(sigma_ysquare-((math.pow(sigma_y,2))/n)))
	coefficient=numerator/denominator
	return coefficient

#returns pearson coefficient of two persons calculated over common movies, ranges between -1 to +1
def pearson_coefficient(person1,person2,common_movie):
	sigma_xsquare=0
	sigma_ysquare=0
	sigma_x=0
	sigma_y=0
	sigma_xy=0
	n=0
	for movie in common_movie:
		x=critics[person1][movie]
		y=critics[person2][movie]
		sigma_x=sigma_x+x
		sigma_y=sigma_y+y
		sigma_xsquare=sigma_xsquare+math.pow(x,2)
		sigma_ysquare=sigma_ysquare+math.pow(y,2)
		sigma_xy=sigma_xy+(x*y)
		n=n+1
	coefficient=pearson_coefficient_formula(sigma_x,sigma_y,sigma_xsquare,sigma_ysquare,sigma_xy,n)
	return coefficient

# Calculate similarity between each pair of critics using two type of metrics
# First is euclidean distance
# Second is Pearson Coefficient which gives linear correlation between two variables
def calculate_similarity():
	critics_name=[]
	for i in critics:
		critics_name.append(i)
	for i in range(0,7):
		for j in range(i+1,7):
			person1=critics_name[i]
			person2=critics_name[j]
			common_movie=common_movies(person1,person2)
			rel=euclidean_distance(person1,person2,common_movie)
			#print person1,"and",person2,"has euclidean relation:",rel
			rel=pearson_coefficient(person1,person2,common_movie)
			#print person1,"and",person2,"has pearson correlation:",rel


#returns list of movies person has not seen
def movies_not_seen(person):
	list_of_movies_not_seen=set()
	for critic,movies in critics.items():
		for movie in movies:
			if movie not in critics[person]:
				list_of_movies_not_seen.add(movie)
	return list_of_movies_not_seen


#returns list of movies recommended for a person on the basis of certain score
def getRecommendations(person):
	list_of_movies_not_seen=movies_not_seen(person)
	reccommended_list_of_movies=[]
	similarity=dict()
	for critic in critics:
			if critic != person:
				common_movie=common_movies(person,critic)
				similarity[critic]=pearson_coefficient(person,critic,common_movie)
	for movie in list_of_movies_not_seen:
		total=0
		similarity_sum=0
		for critic in critics:
			if movie in critics[critic]:
				#print critic,movie,person
				#print similarity[critic],critics[critic][movie],(similarity[critic])*critics[critic][movie]
				total=total+(similarity[critic])*critics[critic][movie]
				similarity_sum=similarity_sum+similarity[critic]
		reccommendation_score=total/similarity_sum
		#print reccommendation_score
		reccommended_list_of_movies.append([movie,reccommendation_score])
	reccommended_list_of_movies.sort()
	reccommended_list_of_movies.reverse()
	return reccommended_list_of_movies

#calculating recommended movies for each person

def getRecommendationForEachPerson():
	for person in critics:	
		reccommended_list_of_movies=getRecommendations(person)
		if reccommended_list_of_movies:
			print "Following are the recommended list of movies for" , person,":"
			for movie in reccommended_list_of_movies:
				print movie[0]
		else:
			print "No movie recommendation for",person,"because maybe he/she has seen all the movies! :)"
	
getRecommendationForEachPerson()
