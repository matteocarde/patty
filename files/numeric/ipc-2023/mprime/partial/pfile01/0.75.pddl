(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(= (locale lamb) 3.0)
		(= (locale okra) 6.0)
		(eats flounder rice)
		(eats okra pear)
		(eats rice pear)
		(eats okra pork)
		(eats pork okra)
		(craves abrasion pork)
		(eats rice flounder)
		(craves hangover rice)
		(eats lamb pork)
		(eats rice rice)
		(eats pork lamb)
		(= (harmony rest) 3.0)
		(craves rest pork)
		(= (locale rice) 1.0)
		(= (locale pear) 2.0)
		(eats pear okra)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)