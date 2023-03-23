;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_9_2)
  (:domain mt-plant-watering-constrained)
  (:objects
    tap1 - tap
	agent1 - agent
	plant2 plant3 plant1 plant8 plant6 plant5 plant7 plant4 - plant
  )

  (:init
    (= (max_int) 160)
	(= (maxx) 9)
	(= (minx) 1)
	(= (maxy) 9)
	(= (miny) 1)
	(= (carrying) 0)
	(= (total_poured) 0)
	(= (total_loaded) 0)
	(= (poured plant1) 0)
	(= (poured plant2) 0)
	(= (poured plant3) 0)
	(= (poured plant4) 0)
	(= (poured plant5) 0)
	(= (poured plant6) 0)
	(= (poured plant7) 0)
	(= (poured plant8) 0)
	(= (x agent1) 4)
	(= (y agent1) 4)
	(= (x plant3) 7)
	(= (y plant3) 7)
	(= (x plant1) 8)
	(= (y plant1) 8)
	(= (x plant8) 6)
	(= (y plant8) 6)
	(= (x plant6) 4)
	(= (y plant6) 4)
	(= (x plant4) 3)
	(= (y plant4) 3)
	(= (x plant7) 1)
	(= (y plant7) 1)
	(= (x tap1) 2)
	(= (y tap1) 2)
	(= (x plant5) 8)
	(= (y plant5) 8)
	(= (x plant2) 3)
	(= (y plant2) 3)
  )

  (:goal (and 
    (= (poured plant1) 3)
	(= (poured plant2) 7)
	(= (poured plant3) 10)
	(= (poured plant4) 7)
	(= (poured plant5) 5)
	(= (poured plant6) 3)
	(= (poured plant7) 3)
	(= (poured plant8) 4)
	(= (total_poured) (+ (+ (+ (+ (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) (poured plant5)) (poured plant6)) (poured plant7)) (poured plant8)) )
  ))

  
  

  
)
