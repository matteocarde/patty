(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats pork lamb)
		(eats flounder rice)
		(craves hangover rice)
		(= (locale pear) 2.0)
		(= (harmony rest) 3.0)
		(= (locale flounder) 4.0)
		(eats flounder lamb)
		(eats okra pork)
		(eats rice rice)
		(craves depression flounder)
		(craves abrasion pork)
		(craves rest pork)
		(eats rice flounder)
		(eats pear okra)
		(eats rice pear)
		(= (locale okra) 6.0)
		(eats pear rice)
		(= (locale rice) 1.0)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)