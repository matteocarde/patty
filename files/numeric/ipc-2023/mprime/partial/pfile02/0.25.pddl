(define (problem mprime-x-2)
	(:domain mystery-prime-typed)
	(:objects
		beef onion tuna flounder cherry muffin ham - food
		satiety stimulation curiosity entertainment - pleasure
		anger depression prostatitis grief abrasion loneliness dread angina boils laceration sciatica hangover anxiety jealousy jealousy-2 depression-1 grief-7 dread-8 prostatitis-3 boils-4 - pain
	)
	(:init
		(eats muffin onion)
		(craves dread-8 ham)
		(= (locale onion) 3.0)
		(eats muffin ham)
		(craves dread onion)
		(eats cherry onion)
		(craves curiosity cherry)
		(eats beef onion)
		(craves jealousy-2 cherry)
		(craves prostatitis beef)
		(= (locale tuna) 2.0)
		(craves loneliness onion)
		(craves stimulation flounder)
	)
	(:goal
			(and
				(craves grief-7 beef)
				(craves depression-1 beef)
			)
	)
)