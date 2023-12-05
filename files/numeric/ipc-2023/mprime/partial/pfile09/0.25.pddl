(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(craves abrasion haroset)
		(= (harmony excitement) 1.0)
		(craves anxiety wurst)
		(eats flounder wurst)
		(eats haroset hamburger)
		(eats guava haroset)
		(= (locale hamburger) 0.0)
		(craves intoxication haroset)
		(eats flounder hamburger)
		(= (locale guava) 4.0)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)