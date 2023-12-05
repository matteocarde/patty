(define (problem instance_10_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (y plant2) 7.0)
		(= (poured plant1) 0.0)
		(= (y agent2) 6.0)
		(= (maxy) 10.0)
		(= (x plant3) 6.0)
		(= (y agent1) 7.0)
		(= (minx) 1.0)
		(= (poured plant5) 0.0)
	)
	(:goal
			(and
				(= (poured plant1) 4.0)
				(= (poured plant2) 2.0)
				(= (poured plant3) 7.0)
				(= (poured plant4) 9.0)
				(= (poured plant5) 5.0)
				(= (total_poured) (total_loaded))
			)
	)
)