(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats lamb pork)
		(craves abrasion pork)
		(= (harmony rest) 3.0)
		(eats lamb flounder)
		(eats pear okra)
		(craves hangover rice)
		(eats pear rice)
		(= (locale lamb) 3.0)
		(eats pork lamb)
		(eats rice flounder)
		(craves rest pork)
		(eats flounder rice)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)