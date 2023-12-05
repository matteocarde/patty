(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(craves jealousy guava)
		(eats flounder wurst)
		(craves dread flounder)
		(eats wurst flounder)
		(eats guava haroset)
		(eats apple guava)
		(eats haroset hamburger)
		(craves curiosity hotdog)
		(craves grief guava)
		(craves anxiety wurst)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)