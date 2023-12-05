(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 - city
	)
	(:init
	)
	(:goal
			(and
				(located plane2 city2)
				(located person1 city1)
				(located person2 city0)
				(located person3 city0)
				(located person4 city1)
			)
	)
)