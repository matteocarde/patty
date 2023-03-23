;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_7_5_2_1)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 - block
  )

  (:init
    (= (x b3) 1)
	(= (y b3) 4)
	(= (x b4) 3)
	(= (y b4) 6)
	(= (x b2) 1)
	(= (y b2) 5)
	(= (x b1) 4)
	(= (y b1) 3)
	(= (x b5) 5)
	(= (y b5) 5)
	(= (max_x) 7 )
	(= (min_x) 1 )
	(= (max_y) 7 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (or (not (= (x b1) (x b2))) (not (= (y b1) (y b2))))
	(= (x b1) (x b3))
(= (y b1) (y b3))
	(or (not (= (x b1) (x b4))) (not (= (y b1) (y b4))))
	(= (x b1) (x b5))
(= (y b1) (y b5))
	(or (not (= (x b2) (x b3))) (not (= (y b2) (y b3))))
	(= (x b2) (x b4))
(= (y b2) (y b4))
	(or (not (= (x b2) (x b5))) (not (= (y b2) (y b5))))
	(or (not (= (x b3) (x b4))) (not (= (y b3) (y b4))))
	(= (x b3) (x b5))
(= (y b3) (y b5))
	(or (not (= (x b4) (x b5))) (not (= (y b4) (y b5))))
  ))

  
  

  
)
