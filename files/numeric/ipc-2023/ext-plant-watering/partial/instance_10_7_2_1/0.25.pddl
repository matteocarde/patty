(define (problem instance_10_7_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 plant6 plant7 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (poured plant2) 0.0)
		(= (poured plant1) 0.0)
		(= (y plant3) 8.0)
		(= (y plant1) 6.0)
		(= (x plant2) 3.0)
		(= (x agent2) 1.0)
		(= (poured plant7) 0.0)
		(= (x tap1) 7.0)
		(= (maxx) 10.0)
	)
	(:goal
			(and
				(= (poured plant1) 10.0)
				(= (poured plant2) 7.0)
				(= (poured plant3) 3.0)
				(= (poured plant4) 9.0)
				(= (poured plant5) 9.0)
				(= (poured plant6) 1.0)
				(= (poured plant7) 10.0)
				(= (total_poured) (total_loaded))
			)
	)
)