(define (domain motion_planning_v1)

;(:requirements :typing :fluents)

(:types box - object)

(:functions (x)
            (y)
            (maxy)
            (maxx)
            (miny)
            (minx)
            (a1 ?b -box)
            (b1 ?b -box)
            (c1 ?b -box)
            (a2 ?b -box)
            (b2 ?b -box)
            (c2 ?b -box)
            (a3 ?b -box)
            (b3 ?b -box)
            (c3 ?b -box)
            (a4 ?b -box)
            (b4 ?b -box)
            (c4 ?b -box)
)

;; @action@ ["moveup",[0,1]]
(:action moveup
 :parameters ()
 :precondition (and (< (+ (y) 1) (maxy)))
 :effect (and
		(increase (y) 1)))

;; @action@ ["movedown",[0,-1]]
(:action movedown
 :parameters ()
 :precondition (and (> (- (y) 1) (miny)))
 :effect (and
		(decrease (y) 1)))

;; @action@ ["moveright",[1,0]]
(:action moveright
 :parameters ()
 :precondition (and (< (+ (x) 1) (maxx)))
 :effect (and
		(increase (x) 1)))

;; @action@ ["moveleft",[-1,0]]
(:action moveleft
 :parameters ()
 :precondition (and (> (- (x) 1) (minx)))
 :effect (and
		(decrease (x) 1)))

(:constraint box
    :parameters (?b -box)
    :condition (or  (>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
                    (>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
                    (>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
                    (>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
                   )
)




)
