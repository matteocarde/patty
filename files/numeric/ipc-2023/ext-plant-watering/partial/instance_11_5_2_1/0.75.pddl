(define (problem instance_11_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (x plant2) 10.0)
		(= (poured plant3) 0.0)
		(= (poured plant1) 0.0)
		(= (total_poured) 0.0)
		(= (minx) 1.0)
		(= (carrying agent2) 0.0)
		(= (x agent2) 4.0)
		(= (y plant3) 8.0)
		(= (water_reserve) 30.0)
		(= (x agent1) 10.0)
		(= (x plant4) 8.0)
		(= (total_loaded) 0.0)
		(= (x plant3) 4.0)
		(= (miny) 1.0)
		(= (carrying agent1) 0.0)
		(= (x tap1) 9.0)
		(= (poured plant4) 0.0)
		(= (poured plant2) 0.0)
		(= (poured plant5) 0.0)
		(= (x plant1) 2.0)
		(= (maxx) 11.0)
		(= (y plant4) 2.0)
		(= (y agent1) 8.0)
		(= (x plant5) 8.0)
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