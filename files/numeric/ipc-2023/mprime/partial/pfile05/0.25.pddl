(define (problem mprime-x-5)
	(:domain mystery-prime-typed)
	(:objects
		broccoli chocolate turkey tuna sweetroll shrimp cherry scallop - food
		satisfaction excitement intoxication lubricity - pleasure
		sciatica anxiety grief boils depression abrasion prostatitis angina jealousy laceration anger grief-2 dread loneliness hangover - pain
	)
	(:init
		(craves depression turkey)
		(= (locale chocolate) 2.0)
		(craves laceration shrimp)
		(craves abrasion turkey)
		(eats chocolate turkey)
		(craves excitement turkey)
		(eats shrimp cherry)
		(= (locale sweetroll) 0.0)
		(craves lubricity sweetroll)
		(craves dread scallop)
		(craves hangover scallop)
		(eats tuna turkey)
	)
	(:goal
			(and
				(craves loneliness shrimp)
				(craves grief shrimp)
			)
	)
)