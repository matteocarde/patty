(define (problem mprime-x-2)
	(:domain mystery-prime-typed)
	(:objects
		beef onion tuna flounder cherry muffin ham - food
		satiety stimulation curiosity entertainment - pleasure
		anger depression prostatitis grief abrasion loneliness dread angina boils laceration sciatica hangover anxiety jealousy jealousy-2 depression-1 grief-7 dread-8 prostatitis-3 boils-4 - pain
	)
	(:init
		(craves angina onion)
		(craves loneliness onion)
		(craves laceration tuna)
		(craves satiety onion)
		(eats onion cherry)
		(craves stimulation flounder)
		(craves prostatitis-3 ham)
		(= (locale muffin) 2.0)
		(craves jealousy-2 cherry)
		(craves dread-8 ham)
		(= (locale tuna) 2.0)
		(= (locale ham) 4.0)
		(eats beef cherry)
	)
	(:goal
			(and
				(craves grief-7 beef)
				(craves depression-1 beef)
			)
	)
)