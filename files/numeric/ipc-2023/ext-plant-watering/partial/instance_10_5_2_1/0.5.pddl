(define (problem instance_10_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (carrying agent2) 0.0)
		(= (y plant3) 2.0)
		(= (y agent1) 7.0)
		(= (y agent2) 6.0)
		(= (max_carry agent1) 5.0)
		(= (minx) 1.0)
		(= (x tap1) 3.0)
		(= (y plant5) 1.0)
		(= (x plant4) 8.0)
		(= (poured plant4) 0.0)
		(= (x plant1) 5.0)
		(= (total_poured) 0.0)
		(= (water_reserve) 29.0)
		(= (poured plant2) 0.0)
		(= (y plant1) 7.0)
		(= (y tap1) 4.0)
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