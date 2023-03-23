;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_6_1)
  (:domain mt-plant-watering-constrained)
  (:objects
    tap1 - tap
	agent1 - agent
	plant3 plant1 plant4 plant2 - plant
  )

  (:init
    (= (max_int) 80)
	(= (maxx) 6)
	(= (minx) 1)
	(= (maxy) 6)
	(= (miny) 1)
	(= (carrying) 0)
	(= (total_poured) 0)
	(= (total_loaded) 0)
	(= (poured plant1) 0)
	(= (poured plant2) 0)
	(= (poured plant3) 0)
	(= (poured plant4) 0)
	(= (x agent1) 2)
	(= (y agent1) 3)
	(= (x plant2) 1)
	(= (y plant2) 1)
	(= (x plant3) 1)
	(= (y plant3) 1)
	(= (x tap1) 1)
	(= (y tap1) 1)
	(= (x plant4) 4)
	(= (y plant4) 4)
	(= (x plant1) 3)
	(= (y plant1) 3)
  )

  (:goal (and 
    (= (poured plant1) 5)
	(= (poured plant2) 6)
	(= (poured plant3) 7)
	(= (poured plant4) 5)
	(= (total_poured) (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) )
  ))

  
  

  
)
