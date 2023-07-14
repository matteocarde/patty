(define (domain blocks)
  (:requirements :typing :fluents)
(:types block -object piston -object)
(:constants 
b0 -block  b1 -block  b2 -block  b3 -block  b4 -block  c0 -piston  c1 -piston  c2 -piston  )

(:predicates (on ?x - block ?y - block)
(onbottom ?x - block)
(clear ?x - block)
(handempty)
(holding ?x - block)
(in ?x - block ?y -piston)
(empty ?z -piston)
(true))
(:functions (w ?x -block) ;;indicates the current weight of a block (constant)
                 (p ?z -piston) ;;indicates the weith of the fluid inside a cylinder
                 (active ?x -block ?z -piston) ;;indicates the numerical implication of having a block inside a cylinder 
                 (a ?z -piston) ;;this is the cylunder's crhossectional area (constant)
                 (d ?z -piston) ;;the height of the fluid in each cylinder 
                (l ?z -piston) ;;the maximum height of the fluid in each cylinder (constant)
                 (f ?z -piston) ;;the downward force at the bottom of each cylinder 
                 (rho) ;;the fluid density. this is independent from the specific cylinder (constant)
                 (v) ;;the total amount of fluid over the cylinders never change (constant)
   )            
  (:free_functions
     (d ?z -piston) ;;the height of the fluid in each cylinder 
     (f ?z -piston) ;;the downward force at the bottom of each cylinder 
   ) 
   (:action pick-up 
	     :parameters (?x - block ?z -piston)
 	     :precondition (and (clear ?x) (onbottom ?x) (in ?x ?z) (handempty))
 	     :effect 	     (and (not (onbottom ?x))
            (empty ?z)
 		   (not (clear ?x))
            (not (in ?x ?z))
 		   (not (handempty))
            (decrease (p ?z) (w ?x))
 		   (holding ?x)))
   (:action put-down 
	     :parameters (?x - block ?z -piston)
 	     :precondition (and (holding ?x) (empty ?z))
 	     :effect 	     (and (not  (holding ?x))
 		   (clear ?x)
            (not (empty ?z))
 		   (handempty)
            (increase (p ?z) (w ?x))
		   (onbottom ?x)
            (in ?x ?z)))
   (:action stack 
	     :parameters (?x - block ?y - block ?z -piston)
 	     :precondition (and (holding ?x) (clear ?y) (in ?y ?z))
 	     :effect 
	     (and (not (holding ?x))
 		   (not (clear ?y))
 		   (clear ?x)
 		   (handempty)
            (increase (p ?z) (w ?x))
		   (on ?x ?y)
            (in ?x ?z)))
   (:action unstack 
	     :parameters (?x - block ?y - block ?z -piston)
 	     :precondition (and (on ?x ?y) (clear ?x) (handempty) (in ?x ?z) (in ?y ?z))
 	     :effect 
	     (and (holding ?x)
 		   (clear ?y) 
           (not (in ?x ?z))
 		   (not (clear ?x))
            (not (handempty))
            (decrease (p ?z) (w ?x))
 		   (not (on ?x ?y))))
 ;piston constraints
 
   (:constraint maxheightpiston
          :parameters (?p - piston)
          :condition (and (>= (d ?p) 0) (<= (d ?p) (l ?p)))
   )
 
 
   (:constraint downwardforce
          :parameters (?p - piston)
          :condition (= (f ?p) (+ (p ?p) (* (rho) (* (a ?p )(d ?p)))))
   )
 
;constraints over all the pistons 

  (:constraint totalamountoffluid
         :parameters ()
         :condition (= (v) (+ (*(a c2) (d c2)) (+ (*(a c1) (d c1)) (*(a c0) (d c0)))))
  )  
  (:constraint pressureequilibrium
         :parameters ()
         :condition (and (=(/ (f c2) (a c2)) (/ (f c1) (a c1))) (=(/ (f c1) (a c1)) (/ (f c0) (a c0))))
  ))
