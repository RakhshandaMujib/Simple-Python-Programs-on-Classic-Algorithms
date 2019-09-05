import math
import random

def distance(pnt_1, pnt_2):
	'''
	Arguments:
	  pnt_1 - Tuple. Has the x and y coordinates of a point.
	  pnt_2 - Tuple. Has the x and y coordinates of a point.
	Returns:
	  Distance beween the two points. 
	'''
	return (math.sqrt((pnt_1[0] - pnt_2[0])**2 + (pnt_1[1] - pnt_2[1])**2 ))

def pre_sort(x_coor, y_coor):
	'''
	Creates tuples of points having their x and y coordinates respectively.
	Arguments:
	  x_coor - List. Contains the x coordinates of points.
	  y_coor - List. Contains the y coordinates of points.
	Returns:
	  points - List. Contains the x and y coordinates of points.
	  x_sorted - List. Contains the points sorted wrt to their x coordinates.
	  y_sorted - List. Contains the points sorted wrt to their y coordinates.
	'''
	points = list(zip(x_coor, y_coor)) 
	x_sorted = sorted(points, key = lambda point: point[0])  
	y_sorted = sorted(points, key = lambda point: point[1])
	return (points, x_sorted, y_sorted)

def brute_force(x_sorted):
	'''
	Uses brute force to get the closest pair po points. Only called when the 
	number of points is less than or equal to 3.
	Argument:
	  x_sorted - List. Contains the points sorted wrt to their x coordinates.
	Returns:
	  closest_points - Tuple. Contains the x and y coordinates of the closest
	  	points found in the list. 
 	  min_dist - Float. Distance between the closest pair i.e. first_pt and 
 	    second_pt.
	'''
	#Points sorted in order of x coordinate is stored in point for better sense.
	point = x_sorted 
	closest_points = (point[0], point[1])
	#Let minimum distance be the distance between the 1st and 2nd points.
	min_dist = distance(closest_points[0], closest_points[1]) 

	if len(point) == 2: #When only 2 points are present. 
		return closest_points, min_dist
	for i in range(len(point) - 1): #Runs from 1st point to 2nd last point.
		for j in range(i+1, len(point)): #Runs from 2nd point to last point.
			if i != 0 and j != 1: 
				dist = distance(point[i], point[j])
				if dist <= min_dist:
					min_dist = dist
					closest_points = point[i], point[j]
	return closest_points, min_dist

def find_the_pair(x_sorted, y_sorted):
	'''
	This method does the major work. It uses recursive calls to constantly 
	follow the algorithm of divide and conquer to get the closest points given 
	in a list and the distance between them. 
	Arguments:
	  x_sorted - List. Contains the points sorted wrt to their x coordinates.
	  y_sorted - List. Contains the points sorted wrt to their y coordinates.
	Returns:
	  closest_points - Tuple. Contains the x and y coordinates of the closest
	  	points found in the list.
	  min_dist - Float. Distance between the closest pair i.e. closest_points[0]
	    and closest_points[1].
	'''
	if len(x_sorted) <= 3:
		return brute_force(x_sorted)
	mid_len = len(x_sorted) // 2 #Mid length.
	
	#Split the list of points sorted in order of x coordinates into two halves.
	l_sorted_x = x_sorted[:mid_len] 
	r_sorted_x = x_sorted[mid_len:]

	l_sorted_y, r_sorted_y = [], []

	#Split the list of points sorted in order of y coordinates into two halves.
	#This is done with the help of the left half of the list sorted in order of 
	#x coordinates- l_sorted_x.
	for point in y_sorted: 
		if point in set(l_sorted_x):  
			l_sorted_y.append(point)
		else:
			r_sorted_y.append(point)

	#Recursive call till we get the closest 2 points in both the halves.
	left_pair, min_dist_left = find_the_pair(l_sorted_x, l_sorted_y)
	right_pair, min_dist_rt = find_the_pair(r_sorted_x, r_sorted_y)

	#Get the closest pair and the distance between them:
	if min_dist_rt <= min_dist_left:
		min_dist = min_dist_rt
		closest_points = right_pair
	else:
		min_dist = min_dist_left
		closest_points = left_pair
	
	#Ccheck for closest pair in the middle strip- between left and right halves:
	mid_pair, mid_dist = in_mid(x_sorted, y_sorted, min_dist, closest_points)
	if mid_dist <= min_dist:
		min_dist = mid_dist
		closest_points = mid_pair

	return closest_points, min_dist

def in_mid(x_sorted, y_sorted, min_dist, closest_points):
	'''
	The method find_the_pair() only took care of closest points in either half 
	of the plane where the points are plotted. This method takes care of the 
	middle strip between the two halves.
	Arguments:
	  x_sorted - List. Contains the points sorted wrt to their x coordinates.
	  y_sorted - List. Contains the points sorted wrt to their y coordinates.
	  min_dist - Float. The minimum distance between the closes pair of points
	    in either of the halves found by the method find_the_pair().
	  closest_points - Tuple. Contains the x and y coordinates of the closest
	  	points found by the method find_the_pair().
	Returns:
	  closest_points - Tuple. Contains the x and y coordinates of the closest
	  	points found after comparing the closest pairs in the halves and in the
	  	middle strip.
	  mid_dist - Float. The minimum distance between the closes pair of points. 
	'''
	mid = len(x_sorted) // 2
	x_mid = x_sorted[mid][0] #Get the x coordinate of the point at the middle.

	#Set the strip's lower and upper bound:
	low, up = int(x_mid - min_dist), int(x_mid + min_dist + 1)

	#Create a sub-list of the points that fall within the strip:
	close_points = [point for point in y_sorted if point[0] in range(low, up)] 
	
	length = len(closest_points)

	for i in range(length - 1): #From the 1st point to the 2nd last point.

		#If a point falls in the strip, it can have at most 7 points that may 
		#have less than min_dist distance in between as per the algorithm. 
		#Hence, we only need to check for the nearest 7 points (since the list
		#is already sorted) or if the list has lesser than 7 close points, we 
		#can check for those number of points. 
		for j in range(i + 1, min(i + 7, length)): #From the 2nd point till the
							   #minimum of 7 nearest or 
							   #total number of points.
			dist = distance(close_points[i], close_points[j])
			if dist <= min_dist:
			 	min_dist = dist
			 	closest_points = close_points[i], close_points[j]
	return closest_points, min_dist

#Driver:
def main():
	total_points = int(input('Enter the total number of points you have:'))

	#Using random numbers to generate the lists of total_points number of x and 
	#y coordinates:
	x_coor = [random.randint(-10*5, 10*5) for x in range(total_points)]
	y_coor = [random.randint(-10*5, 10*5) for y in range(total_points)]

	#Getting the points sorted wrt x and y coordinates:
	points, x_sorted, y_sorted = pre_sort(x_coor, y_coor)

	result = find_the_pair(x_sorted, y_sorted)
	point_1 = result[0][0]
	point_2 = result[0][1]
	distance = result[1]

	#Printing the results:
	print(f"The closest pair of points found in\n{points} is:")
	print(f"\t{point_1} and {point_2}")
	print(f"and the distance between them is:\n\t{distance}")

if __name__ == '__main__':
	main()
