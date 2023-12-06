(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 city3 - city
	)
	(:init
		(located person2 city0)
		(= (fuel plane1) 174.0)
		(= (total-fuel-used) 0.0)
		(= (distance city0 city1) 569.0)
		(= (zoom-limit plane1) 3.0)
		(= (distance city2 city0) 607.0)
		(= (distance city3 city3) 0.0)
		(located person4 city1)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city3)
				(located person3 city3)
				(located person4 city3)
			)
	)
)