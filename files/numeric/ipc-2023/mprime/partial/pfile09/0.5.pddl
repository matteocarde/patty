(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(craves intoxication haroset)
		(eats hamburger haroset)
		(= (locale hotdog) 1.0)
		(eats haroset guava)
		(eats wurst flounder)
		(eats apple hotdog)
		(eats hotdog wurst)
		(= (harmony entertainment) 3.0)
		(eats hamburger flounder)
		(= (locale guava) 4.0)
		(= (locale wurst) 1.0)
		(eats flounder hamburger)
		(craves anxiety wurst)
		(= (harmony curiosity) 1.0)
		(craves abrasion haroset)
		(craves loneliness haroset)
		(craves dread flounder)
		(craves prostatitis haroset)
		(eats apple guava)
		(eats hotdog apple)
		(= (locale hamburger) 0.0)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)