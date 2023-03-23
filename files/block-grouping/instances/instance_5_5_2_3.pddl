;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_5_5_2_3)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 - block
  )

  (:init
    (= (x b3) 4)
	(= (y b3) 3)
	(= (x b4) 1)
	(= (y b4) 4)
	(= (x b2) 4)
	(= (y b2) 5)
	(= (x b1) 2)
	(= (y b1) 3)
	(= (x b5) 1)
	(= (y b5) 4)
	(= (max_x) 5 )
	(= (min_x) 1 )
	(= (max_y) 5 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (= (x b1) (x b2))
(= (y b1) (y b2))
	(= (x b1) (x b3))
(= (y b1) (y b3))
	(= (x b1) (x b4))
(= (y b1) (y b4))
	(= (x b1) (x b5))
(= (y b1) (y b5))
	(= (x b2) (x b3))
(= (y b2) (y b3))
	(= (x b2) (x b4))
(= (y b2) (y b4))
	(= (x b2) (x b5))
(= (y b2) (y b5))
	(= (x b3) (x b4))
(= (y b3) (y b4))
	(= (x b3) (x b5))
(= (y b3) (y b5))
	(= (x b4) (x b5))
(= (y b4) (y b5))
  ))

  
  

  
)
