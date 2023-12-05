(define (problem mprime-x-2)
	(:domain mystery-prime-typed)
	(:objects
		beef onion tuna flounder cherry muffin ham - food
		satiety stimulation curiosity entertainment - pleasure
		anger depression prostatitis grief abrasion loneliness dread angina boils laceration sciatica hangover anxiety jealousy jealousy-2 depression-1 grief-7 dread-8 prostatitis-3 boils-4 - pain
	)
	(:init
		(= (locale tuna) 2.0)
		(eats tuna muffin)
		(eats onion muffin)
		(craves boils tuna)
		(= (locale ham) 4.0)
		(craves laceration tuna)
		(eats tuna ham)
		(eats beef cherry)
		(eats onion beef)
		(craves satiety onion)
		(eats muffin onion)
		(craves prostatitis-3 ham)
		(craves abrasion beef)
	)
	(:goal
			(and
				(craves grief-7 beef)
				(craves depression-1 beef)
			)
	)
)