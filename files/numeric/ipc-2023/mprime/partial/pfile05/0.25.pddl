(define (problem mprime-x-5)
	(:domain mystery-prime-typed)
	(:objects
		broccoli chocolate turkey tuna sweetroll shrimp cherry scallop - food
		satisfaction excitement intoxication lubricity - pleasure
		sciatica anxiety grief boils depression abrasion prostatitis angina jealousy laceration anger grief-2 dread loneliness hangover - pain
	)
	(:init
		(= (locale chocolate) 2.0)
		(craves grief broccoli)
		(craves boils broccoli)
		(= (locale sweetroll) 0.0)
		(craves anxiety broccoli)
		(eats chocolate broccoli)
		(craves abrasion turkey)
		(craves grief-2 scallop)
		(eats cherry scallop)
		(eats scallop cherry)
		(eats sweetroll shrimp)
		(craves loneliness scallop)
	)
	(:goal
			(and
				(craves loneliness shrimp)
				(craves grief shrimp)
			)
	)
)