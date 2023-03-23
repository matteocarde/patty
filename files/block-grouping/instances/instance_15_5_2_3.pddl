;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_15_5_2_3)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 - block
  )

  (:init
    (= (x b3) 1)
	(= (y b3) 10)
	(= (x b4) 8)
	(= (y b4) 1)
	(= (x b2) 4)
	(= (y b2) 11)
	(= (x b1) 14)
	(= (y b1) 1)
	(= (x b5) 12)
	(= (y b5) 15)
	(= (max_x) 15 )
	(= (min_x) 1 )
	(= (max_y) 15 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (= (x b1) (x b2))
(= (y b1) (y b2))
	(= (x b1) (x b3))
(= (y b1) (y b3))
	(or (not (= (x b1) (x b4))) (not (= (y b1) (y b4))))
	(= (x b1) (x b5))
(= (y b1) (y b5))
	(= (x b2) (x b3))
(= (y b2) (y b3))
	(or (not (= (x b2) (x b4))) (not (= (y b2) (y b4))))
	(= (x b2) (x b5))
(= (y b2) (y b5))
	(or (not (= (x b3) (x b4))) (not (= (y b3) (y b4))))
	(= (x b3) (x b5))
(= (y b3) (y b5))
	(or (not (= (x b4) (x b5))) (not (= (y b4) (y b5))))
  ))

  
  

  
)
