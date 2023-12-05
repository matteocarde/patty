(define (problem ZTRAVEL-2-5)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 person5 - person
		city0 city1 city2 - city
	)
	(:init
	)
	(:goal
			(and
				(located plane1 city0)
				(located person2 city2)
				(located person3 city0)
				(located person4 city1)
				(located person5 city2)
			)
	)
)