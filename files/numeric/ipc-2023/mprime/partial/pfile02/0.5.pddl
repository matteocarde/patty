(define (problem mprime-x-2)
	(:domain mystery-prime-typed)
	(:objects
		beef onion tuna flounder cherry muffin ham - food
		satiety stimulation curiosity entertainment - pleasure
		anger depression prostatitis grief abrasion loneliness dread angina boils laceration sciatica hangover anxiety jealousy jealousy-2 depression-1 grief-7 dread-8 prostatitis-3 boils-4 - pain
	)
	(:init
		(craves dread onion)
		(eats tuna muffin)
		(craves boils-4 ham)
		(craves depression beef)
		(craves curiosity cherry)
		(= (locale ham) 4.0)
		(craves hangover tuna)
		(= (harmony stimulation) 2.0)
		(= (harmony curiosity) 2.0)
		(eats muffin ham)
		(eats muffin onion)
		(craves jealousy-2 cherry)
		(eats beef tuna)
		(craves loneliness onion)
		(eats cherry flounder)
		(craves stimulation flounder)
		(craves depression-1 muffin)
		(= (harmony satiety) 1.0)
		(eats beef onion)
		(eats beef cherry)
		(eats cherry beef)
		(eats tuna ham)
		(craves boils tuna)
		(craves entertainment ham)
		(= (locale muffin) 2.0)
		(eats onion muffin)
		(craves laceration tuna)
	)
	(:goal
			(and
				(craves grief-7 beef)
				(craves depression-1 beef)
			)
	)
)