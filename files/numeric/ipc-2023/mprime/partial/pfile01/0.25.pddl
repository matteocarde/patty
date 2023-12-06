(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats pork lamb)
		(craves hangover rice)
		(eats rice rice)
		(= (locale pear) 2.0)
		(eats flounder rice)
		(= (harmony rest) 3.0)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)