(define (problem instance_11_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (poured plant2) 0.0)
		(= (y plant2) 2.0)
		(= (maxx) 11.0)
		(= (minx) 1.0)
		(= (x plant2) 10.0)
		(= (x plant5) 8.0)
		(= (maxy) 11.0)
		(= (miny) 1.0)
	)
	(:goal
			(and
				(= (poured plant1) 10.0)
				(= (poured plant2) 1.0)
				(= (poured plant3) 8.0)
				(= (poured plant4) 8.0)
				(= (poured plant5) 1.0)
				(= (total_poured) (total_loaded))
			)
	)
)