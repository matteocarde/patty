;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_7_3)
  (:domain mt-plant-watering-constrained)
  (:objects
    tap1 - tap
	agent1 - agent
	plant3 plant1 plant4 plant2 - plant
  )

  (:init
    (= (max_int) 80)
	(= (maxx) 7)
	(= (minx) 1)
	(= (maxy) 7)
	(= (miny) 1)
	(= (carrying) 0)
	(= (total_poured) 0)
	(= (total_loaded) 0)
	(= (poured plant1) 0)
	(= (poured plant2) 0)
	(= (poured plant3) 0)
	(= (poured plant4) 0)
	(= (x agent1) 6)
	(= (y agent1) 4)
	(= (x plant2) 1)
	(= (y plant2) 1)
	(= (x plant3) 4)
	(= (y plant3) 4)
	(= (x tap1) 4)
	(= (y tap1) 4)
	(= (x plant4) 7)
	(= (y plant4) 7)
	(= (x plant1) 6)
	(= (y plant1) 6)
  )

  (:goal (and 
    (= (poured plant1) 5)
	(= (poured plant2) 4)
	(= (poured plant3) 2)
	(= (poured plant4) 8)
	(= (total_poured) (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) )
  ))

  
  

  
)
