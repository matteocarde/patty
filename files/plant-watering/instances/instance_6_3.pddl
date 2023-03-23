;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_6_3)
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
	(= (x agent1) 3)
	(= (y agent1) 1)
	(= (x plant2) 6)
	(= (y plant2) 6)
	(= (x plant3) 4)
	(= (y plant3) 4)
	(= (x tap1) 5)
	(= (y tap1) 5)
	(= (x plant4) 5)
	(= (y plant4) 5)
	(= (x plant1) 3)
	(= (y plant1) 3)
  )

  (:goal (and 
    (= (poured plant1) 8)
	(= (poured plant2) 2)
	(= (poured plant3) 1)
	(= (poured plant4) 4)
	(= (total_poured) (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) )
  ))

  
  

  
)
