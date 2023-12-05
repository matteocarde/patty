(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(eats arugula scallop)
		(eats grapefruit wurst)
		(eats bacon arugula)
		(= (locale ham) 2.0)
		(= (locale wurst) 0.0)
		(eats cherry ham)
		(eats muffin cherry)
		(craves loneliness arugula)
		(eats scallop arugula)
		(eats scallion muffin)
		(eats muffin scallion)
		(eats arugula wurst)
		(= (locale arugula) 4.0)
		(craves jealousy bacon)
		(eats wurst arugula)
		(= (locale grapefruit) 0.0)
		(eats muffin ham)
		(craves sciatica grapefruit)
		(eats arugula muffin)
		(eats muffin arugula)
		(eats ham cherry)
		(= (harmony aesthetics) 1.0)
		(craves hangover muffin)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)