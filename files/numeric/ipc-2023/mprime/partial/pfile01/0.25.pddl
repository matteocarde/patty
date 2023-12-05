(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(= (locale pork) 5.0)
		(= (harmony rest) 3.0)
		(eats pear okra)
		(= (locale flounder) 4.0)
		(eats rice pear)
		(eats okra pear)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)