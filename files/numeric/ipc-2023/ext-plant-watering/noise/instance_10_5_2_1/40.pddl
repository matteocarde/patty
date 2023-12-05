(define (problem instance_10_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (maxx) 44.0)
		(= (minx) -7.0)
		(= (maxy) -2.0)
		(= (miny) -37.0)
		(= (total_poured) 20.0)
		(= (total_loaded) 25.0)
		(= (water_reserve) 6.0)
		(= (carrying agent1) 30.0)
		(= (max_carry agent1) 8.0)
		(= (carrying agent2) 39.0)
		(= (max_carry agent2) 34.0)
		(= (poured plant1) 23.0)
		(= (poured plant2) -21.0)
		(= (poured plant3) 17.0)
		(= (poured plant4) 30.0)
		(= (poured plant5) 0.0)
		(= (x plant1) 0.0)
		(= (y plant1) -8.0)
		(= (x plant2) -19.0)
		(= (y plant2) 35.0)
		(= (x plant3) 20.0)
		(= (y plant3) -9.0)
		(= (x plant4) 31.0)
		(= (y plant4) 11.0)
		(= (x plant5) 33.0)
		(= (y plant5) -26.0)
		(= (x tap1) 13.0)
		(= (y tap1) 9.0)
		(= (x agent1) -8.0)
		(= (y agent1) -33.0)
		(= (x agent2) 41.0)
		(= (y agent2) 7.0)
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