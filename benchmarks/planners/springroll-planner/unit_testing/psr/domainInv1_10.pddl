(define (domain psr)
(:requirements :typing :fluents)
(:types switch - object bus - object)
(:constants  l1 -bus  l2 -bus  l3 -bus  l4 -bus  l5 -bus  l6 -bus  l7 -bus  l8 -bus  l9 -bus  l10 -bus  l11 -bus  l12 -bus  l13 -bus  l14 -bus  l15 -bus  l16 -bus  l17 -bus  l18 -bus  l19 -bus  l20 -bus  l21 -bus  l22 -bus  l23 -bus  l24 -bus  l25 -bus  l26 -bus  l27 -bus  l28 -bus  l29 -bus  l30 -bus  l31 -bus  l32 -bus  l33 -bus  l34 -bus  l35 -bus  l36 -bus  l37 -bus  l38 -bus  l39 -bus  l40 -bus  l41 -bus  l42 -bus  l43 -bus  l44 -bus  l45 -bus  )
(:predicates (open ?b1 ?b2 -bus)
            (faulty ?b1 -bus)
            (closed ?b1 ?b2 -bus)
            (generator ?b1 -bus)
            (disabled ?b1 -bus)
            (enabled ?b1 -bus)
            (canbechanged ?b1 -bus ?b2 -bus)
            (true))
(:functions (l ?b -bus)
           (f ?b -bus)
           (g ?b -bus)
           (teta ?b -bus)
           (max_g ?b -bus)
           (p ?b1 -bus ?b2 -bus)
           (b ?b1 -bus ?b2 -bus)
           (max_p ?b1 -bus ?b2 -bus)
           (min_p ?b1 -bus ?b2 -bus))
          (:free_functions 
          (f ?b -bus)
          (g ?b -bus)
          (teta ?b -bus)
          (p ?b1 -bus ?b2 -bus)
          )
(:action close
     :parameters (?b1 -bus ?b2 -bus)
     :precondition (and (open ?b1 ?b2) (canbechanged ?b1 ?b2))
         :effect (and (not (open ?b1 ?b2)) (closed ?b1 ?b2)) 
    )
   (:action open
     :parameters (?b1 -bus ?b2 -bus)
     :precondition (and (closed ?b1 ?b2) (canbechanged ?b1 ?b2))
         :effect (and (not (closed ?b1 ?b2)) (open ?b1 ?b2)) 
   )
 (:constraint connectedbusimplication
 	:parameters (?b1 -bus ?b2 -bus)
 	:condition (or (not (closed ?b1 ?b2)) (= (f ?b1) (f ?b2) ) )
   )
   (:constraint faultybusimplication
 	:parameters (?b1 -bus)
 	:condition (or (not (faulty ?b1)) (= (f ?b1) 0.0) )
 )
  (:constraint generatorbusimplication
 	:parameters (?b1 -bus)
 	:condition (or (not (enabled ?b1)) (= (f ?b1) 1.0) )
 )
  (:constraint propagationForOpen 
 	:parameters (?b1 ?b2 -bus)
 
 	:condition (or (not (open ?b1 ?b2)) (= (p ?b1 ?b2) 0.0) )
  )
   (:constraint propagationForClosed
 	:parameters (?b1 ?b2 -bus)
 	:condition (or (not (closed ?b1 ?b2)) (= (p ?b1 ?b2) (* (* -1 (b ?b1 ?b2)) (- (teta ?b1) (teta ?b2) ) ) ) )
 )
   (:constraint propagationForCircuitBreaker
 	:parameters (?b1 -bus)
 	:condition (or (not (disabled ?b1)) (= (g ?b1 ) 0.0 ) )
 )
   (:action enable
 	:parameters (?b1 -bus)
 	:precondition (and (generator ?b1) (disabled ?b1)) 
 	:effect (and (not (disabled ?b1)) (enabled ?b1))
 )
     (:action disable
 	:parameters (?b1 -bus)
 	:precondition (and (generator ?b1) (enabled ?b1)) 
 	:effect (and (disabled ?b1) (not (enabled ?b1)) )
 )
  (:constraint pboundsl2l3 
 :parameters ()
:condition    (and (<= (p l2 l3) 600.0) (>= (p l2 l3) -600.0))
)
  (:constraint pboundsl5l6 
 :parameters ()
:condition    (and (<= (p l5 l6) 600.0) (>= (p l5 l6) -600.0))
)
  (:constraint pboundsl7l8 
 :parameters ()
:condition    (and (<= (p l7 l8) 600.0) (>= (p l7 l8) -600.0))
)
  (:constraint pboundsl9l10 
 :parameters ()
:condition    (and (<= (p l9 l10) 600.0) (>= (p l9 l10) -600.0))
)
  (:constraint pboundsl12l13 
 :parameters ()
:condition    (and (<= (p l12 l13) 600.0) (>= (p l12 l13) -600.0))
)
  (:constraint pboundsl14l15 
 :parameters ()
:condition    (and (<= (p l14 l15) 600.0) (>= (p l14 l15) -600.0))
)
  (:constraint pboundsl17l18 
 :parameters ()
:condition    (and (<= (p l17 l18) 600.0) (>= (p l17 l18) -600.0))
)
  (:constraint pboundsl19l20 
 :parameters ()
:condition    (and (<= (p l19 l20) 75.0) (>= (p l19 l20) -75.0))
)
  (:constraint pboundsl20l21 
 :parameters ()
:condition    (and (<= (p l20 l21) 600.0) (>= (p l20 l21) -600.0))
)
  (:constraint pboundsl22l23 
 :parameters ()
:condition    (and (<= (p l22 l23) 600.0) (>= (p l22 l23) -600.0))
)
  (:constraint pboundsl23l24 
 :parameters ()
:condition    (and (<= (p l23 l24) 600.0) (>= (p l23 l24) -600.0))
)
  (:constraint pboundsl22l25 
 :parameters ()
:condition    (and (<= (p l22 l25) 600.0) (>= (p l22 l25) -600.0))
)
  (:constraint pboundsl26l29 
 :parameters ()
:condition    (and (<= (p l26 l29) 600.0) (>= (p l26 l29) -600.0))
)
  (:constraint pboundsl30l31 
 :parameters ()
:condition    (and (<= (p l30 l31) 600.0) (>= (p l30 l31) -600.0))
)
  (:constraint pboundsl33l34 
 :parameters ()
:condition    (and (<= (p l33 l34) 600.0) (>= (p l33 l34) -600.0))
)
  (:constraint pboundsl34l35 
 :parameters ()
:condition    (and (<= (p l34 l35) 600.0) (>= (p l34 l35) -600.0))
)
  (:constraint pboundsl35l36 
 :parameters ()
:condition    (and (<= (p l35 l36) 600.0) (>= (p l35 l36) -600.0))
)
  (:constraint pboundsl36l37 
 :parameters ()
:condition    (and (<= (p l36 l37) 600.0) (>= (p l36 l37) -600.0))
)
  (:constraint pboundsl38l39 
 :parameters ()
:condition    (and (<= (p l38 l39) 600.0) (>= (p l38 l39) -600.0))
)
  (:constraint pboundsl39l40 
 :parameters ()
:condition    (and (<= (p l39 l40) 600.0) (>= (p l39 l40) -600.0))
)
  (:constraint pboundsl40l41 
 :parameters ()
:condition    (and (<= (p l40 l41) 600.0) (>= (p l40 l41) -600.0))
)
  (:constraint pboundsl26l27 
 :parameters ()
:condition    (and (<= (p l26 l27) 600.0) (>= (p l26 l27) -600.0))
)
  (:constraint pboundsl42l43 
 :parameters ()
:condition    (and (<= (p l42 l43) 600.0) (>= (p l42 l43) -600.0))
)
  (:constraint pboundsl44l45 
 :parameters ()
:condition    (and (<= (p l44 l45) 600.0) (>= (p l44 l45) -600.0))
)
  (:constraint pboundsl31l32 
 :parameters ()
:condition    (and (<= (p l31 l32) 600.0) (>= (p l31 l32) -600.0))
)
  (:constraint pboundsl2l28 
 :parameters ()
:condition    (and (<= (p l2 l28) 600.0) (>= (p l2 l28) -600.0))
)
  (:constraint pboundsl1l2 
 :parameters ()
:condition    (and (<= (p l1 l2) 600.0) (>= (p l1 l2) -600.0))
)
  (:constraint pboundsl3l4 
 :parameters ()
:condition    (and (<= (p l3 l4) 600.0) (>= (p l3 l4) -600.0))
)
  (:constraint pboundsl4l5 
 :parameters ()
:condition    (and (<= (p l4 l5) 600.0) (>= (p l4 l5) -600.0))
)
  (:constraint pboundsl6l7 
 :parameters ()
:condition    (and (<= (p l6 l7) 600.0) (>= (p l6 l7) -600.0))
)
  (:constraint pboundsl8l9 
 :parameters ()
:condition    (and (<= (p l8 l9) 600.0) (>= (p l8 l9) -600.0))
)
  (:constraint pboundsl10l11 
 :parameters ()
:condition    (and (<= (p l10 l11) 600.0) (>= (p l10 l11) -600.0))
)
  (:constraint pboundsl11l12 
 :parameters ()
:condition    (and (<= (p l11 l12) 600.0) (>= (p l11 l12) -600.0))
)
  (:constraint pboundsl4l14 
 :parameters ()
:condition    (and (<= (p l4 l14) 600.0) (>= (p l4 l14) -600.0))
)
  (:constraint pboundsl15l16 
 :parameters ()
:condition    (and (<= (p l15 l16) 600.0) (>= (p l15 l16) -600.0))
)
  (:constraint pboundsl16l17 
 :parameters ()
:condition    (and (<= (p l16 l17) 600.0) (>= (p l16 l17) -600.0))
)
  (:constraint pboundsl16l19 
 :parameters ()
:condition    (and (<= (p l16 l19) 75.0) (>= (p l16 l19) -75.0))
)
  (:constraint pboundsl21l22 
 :parameters ()
:condition    (and (<= (p l21 l22) 600.0) (>= (p l21 l22) -600.0))
)
  (:constraint pboundsl25l26 
 :parameters ()
:condition    (and (<= (p l25 l26) 600.0) (>= (p l25 l26) -600.0))
)
  (:constraint pboundsl29l30 
 :parameters ()
:condition    (and (<= (p l29 l30) 600.0) (>= (p l29 l30) -600.0))
)
  (:constraint pboundsl30l33 
 :parameters ()
:condition    (and (<= (p l30 l33) 600.0) (>= (p l30 l33) -600.0))
)
  (:constraint pboundsl36l38 
 :parameters ()
:condition    (and (<= (p l36 l38) 600.0) (>= (p l36 l38) -600.0))
)
  (:constraint pboundsl11l41 
 :parameters ()
:condition    (and (<= (p l11 l41) 600.0) (>= (p l11 l41) -600.0))
)
  (:constraint pboundsl25l42 
 :parameters ()
:condition    (and (<= (p l25 l42) 600.0) (>= (p l25 l42) -600.0))
)
  (:constraint pboundsl43l44 
 :parameters ()
:condition    (and (<= (p l43 l44) 600.0) (>= (p l43 l44) -600.0))
)
  (:constraint kirkoffl1 
  :parameters ()
:condition (= (+ (g l1) 0.0 ) (+ (* (l l1) (f l1)) (+ (p l1 l2) 0.0) ))
)
  (:constraint maxgl1 
 :parameters ()
:condition   (and (<= (g l1) 600.0) (>= (g l1) 0.0))
)
  (:constraint feedingdomainl1 
 :parameters ()
:condition    (or (= (f l1) 1.0) (= (f l1) 0.0))
)
  (:constraint kirkoffl2 
  :parameters ()
:condition (= (+ (g l2) (+ (p l1 l2) 0.0) ) (+ (* (l l2) (f l2)) (+ (p l2 l28) (+ (p l2 l3) 0.0)) ))
)
  (:constraint maxgl2 
 :parameters ()
:condition   (and (<= (g l2) 0.0) (>= (g l2) 0.0))
)
  (:constraint feedingdomainl2 
 :parameters ()
:condition    (or (= (f l2) 1.0) (= (f l2) 0.0))
)
  (:constraint kirkoffl3 
  :parameters ()
:condition (= (+ (g l3) (+ (p l2 l3) 0.0) ) (+ (* (l l3) (f l3)) (+ (p l3 l4) 0.0) ))
)
  (:constraint maxgl3 
 :parameters ()
:condition   (and (<= (g l3) 0.0) (>= (g l3) 0.0))
)
  (:constraint feedingdomainl3 
 :parameters ()
:condition    (or (= (f l3) 1.0) (= (f l3) 0.0))
)
  (:constraint kirkoffl4 
  :parameters ()
:condition (= (+ (g l4) (+ (p l3 l4) 0.0) ) (+ (* (l l4) (f l4)) (+ (p l4 l14) (+ (p l4 l5) 0.0)) ))
)
  (:constraint maxgl4 
 :parameters ()
:condition   (and (<= (g l4) 0.0) (>= (g l4) 0.0))
)
  (:constraint feedingdomainl4 
 :parameters ()
:condition    (or (= (f l4) 1.0) (= (f l4) 0.0))
)
  (:constraint kirkoffl5 
  :parameters ()
:condition (= (+ (g l5) (+ (p l4 l5) 0.0) ) (+ (* (l l5) (f l5)) (+ (p l5 l6) 0.0) ))
)
  (:constraint maxgl5 
 :parameters ()
:condition   (and (<= (g l5) 0.0) (>= (g l5) 0.0))
)
  (:constraint feedingdomainl5 
 :parameters ()
:condition    (or (= (f l5) 1.0) (= (f l5) 0.0))
)
  (:constraint kirkoffl6 
  :parameters ()
:condition (= (+ (g l6) (+ (p l5 l6) 0.0) ) (+ (* (l l6) (f l6)) (+ (p l6 l7) 0.0) ))
)
  (:constraint maxgl6 
 :parameters ()
:condition   (and (<= (g l6) 0.0) (>= (g l6) 0.0))
)
  (:constraint feedingdomainl6 
 :parameters ()
:condition    (or (= (f l6) 1.0) (= (f l6) 0.0))
)
  (:constraint kirkoffl7 
  :parameters ()
:condition (= (+ (g l7) (+ (p l6 l7) 0.0) ) (+ (* (l l7) (f l7)) (+ (p l7 l8) 0.0) ))
)
  (:constraint maxgl7 
 :parameters ()
:condition   (and (<= (g l7) 0.0) (>= (g l7) 0.0))
)
  (:constraint feedingdomainl7 
 :parameters ()
:condition    (or (= (f l7) 1.0) (= (f l7) 0.0))
)
  (:constraint kirkoffl8 
  :parameters ()
:condition (= (+ (g l8) (+ (p l7 l8) 0.0) ) (+ (* (l l8) (f l8)) (+ (p l8 l9) 0.0) ))
)
  (:constraint maxgl8 
 :parameters ()
:condition   (and (<= (g l8) 0.0) (>= (g l8) 0.0))
)
  (:constraint feedingdomainl8 
 :parameters ()
:condition    (or (= (f l8) 1.0) (= (f l8) 0.0))
)
  (:constraint kirkoffl9 
  :parameters ()
:condition (= (+ (g l9) (+ (p l8 l9) 0.0) ) (+ (* (l l9) (f l9)) (+ (p l9 l10) 0.0) ))
)
  (:constraint maxgl9 
 :parameters ()
:condition   (and (<= (g l9) 0.0) (>= (g l9) 0.0))
)
  (:constraint feedingdomainl9 
 :parameters ()
:condition    (or (= (f l9) 1.0) (= (f l9) 0.0))
)
  (:constraint kirkoffl10 
  :parameters ()
:condition (= (+ (g l10) (+ (p l9 l10) 0.0) ) (+ (* (l l10) (f l10)) (+ (p l10 l11) 0.0) ))
)
  (:constraint maxgl10 
 :parameters ()
:condition   (and (<= (g l10) 0.0) (>= (g l10) 0.0))
)
  (:constraint feedingdomainl10 
 :parameters ()
:condition    (or (= (f l10) 1.0) (= (f l10) 0.0))
)
  (:constraint kirkoffl11 
  :parameters ()
:condition (= (+ (g l11) (+ (p l10 l11) 0.0) ) (+ (* (l l11) (f l11)) (+ (p l11 l41) (+ (p l11 l12) 0.0)) ))
)
  (:constraint maxgl11 
 :parameters ()
:condition   (and (<= (g l11) 0.0) (>= (g l11) 0.0))
)
  (:constraint feedingdomainl11 
 :parameters ()
:condition    (or (= (f l11) 1.0) (= (f l11) 0.0))
)
  (:constraint kirkoffl12 
  :parameters ()
:condition (= (+ (g l12) (+ (p l11 l12) 0.0) ) (+ (* (l l12) (f l12)) (+ (p l12 l13) 0.0) ))
)
  (:constraint maxgl12 
 :parameters ()
:condition   (and (<= (g l12) 0.0) (>= (g l12) 0.0))
)
  (:constraint feedingdomainl12 
 :parameters ()
:condition    (or (= (f l12) 1.0) (= (f l12) 0.0))
)
  (:constraint kirkoffl13 
  :parameters ()
:condition (= (+ (g l13) (+ (p l12 l13) 0.0) ) (+ (* (l l13) (f l13)) 0.0 ))
)
  (:constraint maxgl13 
 :parameters ()
:condition   (and (<= (g l13) 400.0) (>= (g l13) 0.0))
)
  (:constraint feedingdomainl13 
 :parameters ()
:condition    (or (= (f l13) 1.0) (= (f l13) 0.0))
)
  (:constraint kirkoffl14 
  :parameters ()
:condition (= (+ (g l14) (+ (p l4 l14) 0.0) ) (+ (* (l l14) (f l14)) (+ (p l14 l15) 0.0) ))
)
  (:constraint maxgl14 
 :parameters ()
:condition   (and (<= (g l14) 0.0) (>= (g l14) 0.0))
)
  (:constraint feedingdomainl14 
 :parameters ()
:condition    (or (= (f l14) 1.0) (= (f l14) 0.0))
)
  (:constraint kirkoffl15 
  :parameters ()
:condition (= (+ (g l15) (+ (p l14 l15) 0.0) ) (+ (* (l l15) (f l15)) (+ (p l15 l16) 0.0) ))
)
  (:constraint maxgl15 
 :parameters ()
:condition   (and (<= (g l15) 0.0) (>= (g l15) 0.0))
)
  (:constraint feedingdomainl15 
 :parameters ()
:condition    (or (= (f l15) 1.0) (= (f l15) 0.0))
)
  (:constraint kirkoffl16 
  :parameters ()
:condition (= (+ (g l16) (+ (p l15 l16) 0.0) ) (+ (* (l l16) (f l16)) (+ (p l16 l19) (+ (p l16 l17) 0.0)) ))
)
  (:constraint maxgl16 
 :parameters ()
:condition   (and (<= (g l16) 0.0) (>= (g l16) 0.0))
)
  (:constraint feedingdomainl16 
 :parameters ()
:condition    (or (= (f l16) 1.0) (= (f l16) 0.0))
)
  (:constraint kirkoffl17 
  :parameters ()
:condition (= (+ (g l17) (+ (p l16 l17) 0.0) ) (+ (* (l l17) (f l17)) (+ (p l17 l18) 0.0) ))
)
  (:constraint maxgl17 
 :parameters ()
:condition   (and (<= (g l17) 0.0) (>= (g l17) 0.0))
)
  (:constraint feedingdomainl17 
 :parameters ()
:condition    (or (= (f l17) 1.0) (= (f l17) 0.0))
)
  (:constraint kirkoffl18 
  :parameters ()
:condition (= (+ (g l18) (+ (p l17 l18) 0.0) ) (+ (* (l l18) (f l18)) 0.0 ))
)
  (:constraint maxgl18 
 :parameters ()
:condition   (and (<= (g l18) 400.0) (>= (g l18) 0.0))
)
  (:constraint feedingdomainl18 
 :parameters ()
:condition    (or (= (f l18) 1.0) (= (f l18) 0.0))
)
  (:constraint kirkoffl19 
  :parameters ()
:condition (= (+ (g l19) (+ (p l16 l19) 0.0) ) (+ (* (l l19) (f l19)) (+ (p l19 l20) 0.0) ))
)
  (:constraint maxgl19 
 :parameters ()
:condition   (and (<= (g l19) 0.0) (>= (g l19) 0.0))
)
  (:constraint feedingdomainl19 
 :parameters ()
:condition    (or (= (f l19) 1.0) (= (f l19) 0.0))
)
  (:constraint kirkoffl20 
  :parameters ()
:condition (= (+ (g l20) (+ (p l19 l20) 0.0) ) (+ (* (l l20) (f l20)) (+ (p l20 l21) 0.0) ))
)
  (:constraint maxgl20 
 :parameters ()
:condition   (and (<= (g l20) 0.0) (>= (g l20) 0.0))
)
  (:constraint feedingdomainl20 
 :parameters ()
:condition    (or (= (f l20) 1.0) (= (f l20) 0.0))
)
  (:constraint kirkoffl21 
  :parameters ()
:condition (= (+ (g l21) (+ (p l20 l21) 0.0) ) (+ (* (l l21) (f l21)) (+ (p l21 l22) 0.0) ))
)
  (:constraint maxgl21 
 :parameters ()
:condition   (and (<= (g l21) 0.0) (>= (g l21) 0.0))
)
  (:constraint feedingdomainl21 
 :parameters ()
:condition    (or (= (f l21) 1.0) (= (f l21) 0.0))
)
  (:constraint kirkoffl22 
  :parameters ()
:condition (= (+ (g l22) (+ (p l21 l22) 0.0) ) (+ (* (l l22) (f l22)) (+ (p l22 l25) (+ (p l22 l23) 0.0)) ))
)
  (:constraint maxgl22 
 :parameters ()
:condition   (and (<= (g l22) 0.0) (>= (g l22) 0.0))
)
  (:constraint feedingdomainl22 
 :parameters ()
:condition    (or (= (f l22) 1.0) (= (f l22) 0.0))
)
  (:constraint kirkoffl23 
  :parameters ()
:condition (= (+ (g l23) (+ (p l22 l23) 0.0) ) (+ (* (l l23) (f l23)) (+ (p l23 l24) 0.0) ))
)
  (:constraint maxgl23 
 :parameters ()
:condition   (and (<= (g l23) 0.0) (>= (g l23) 0.0))
)
  (:constraint feedingdomainl23 
 :parameters ()
:condition    (or (= (f l23) 1.0) (= (f l23) 0.0))
)
  (:constraint kirkoffl24 
  :parameters ()
:condition (= (+ (g l24) (+ (p l23 l24) 0.0) ) (+ (* (l l24) (f l24)) 0.0 ))
)
  (:constraint maxgl24 
 :parameters ()
:condition   (and (<= (g l24) 240.0) (>= (g l24) 0.0))
)
  (:constraint feedingdomainl24 
 :parameters ()
:condition    (or (= (f l24) 1.0) (= (f l24) 0.0))
)
  (:constraint kirkoffl25 
  :parameters ()
:condition (= (+ (g l25) (+ (p l22 l25) 0.0) ) (+ (* (l l25) (f l25)) (+ (p l25 l42) (+ (p l25 l26) 0.0)) ))
)
  (:constraint maxgl25 
 :parameters ()
:condition   (and (<= (g l25) 0.0) (>= (g l25) 0.0))
)
  (:constraint feedingdomainl25 
 :parameters ()
:condition    (or (= (f l25) 1.0) (= (f l25) 0.0))
)
  (:constraint kirkoffl26 
  :parameters ()
:condition (= (+ (g l26) (+ (p l25 l26) 0.0) ) (+ (* (l l26) (f l26)) (+ (p l26 l27) (+ (p l26 l29) 0.0)) ))
)
  (:constraint maxgl26 
 :parameters ()
:condition   (and (<= (g l26) 0.0) (>= (g l26) 0.0))
)
  (:constraint feedingdomainl26 
 :parameters ()
:condition    (or (= (f l26) 1.0) (= (f l26) 0.0))
)
  (:constraint kirkoffl27 
  :parameters ()
:condition (= (+ (g l27) (+ (p l26 l27) 0.0) ) (+ (* (l l27) (f l27)) 0.0 ))
)
  (:constraint maxgl27 
 :parameters ()
:condition   (and (<= (g l27) 0.0) (>= (g l27) 0.0))
)
  (:constraint feedingdomainl27 
 :parameters ()
:condition    (or (= (f l27) 1.0) (= (f l27) 0.0))
)
  (:constraint kirkoffl28 
  :parameters ()
:condition (= (+ (g l28) (+ (p l2 l28) 0.0) ) (+ (* (l l28) (f l28)) 0.0 ))
)
  (:constraint maxgl28 
 :parameters ()
:condition   (and (<= (g l28) 0.0) (>= (g l28) 0.0))
)
  (:constraint feedingdomainl28 
 :parameters ()
:condition    (or (= (f l28) 1.0) (= (f l28) 0.0))
)
  (:constraint kirkoffl29 
  :parameters ()
:condition (= (+ (g l29) (+ (p l26 l29) 0.0) ) (+ (* (l l29) (f l29)) (+ (p l29 l30) 0.0) ))
)
  (:constraint maxgl29 
 :parameters ()
:condition   (and (<= (g l29) 0.0) (>= (g l29) 0.0))
)
  (:constraint feedingdomainl29 
 :parameters ()
:condition    (or (= (f l29) 1.0) (= (f l29) 0.0))
)
  (:constraint kirkoffl30 
  :parameters ()
:condition (= (+ (g l30) (+ (p l29 l30) 0.0) ) (+ (* (l l30) (f l30)) (+ (p l30 l33) (+ (p l30 l31) 0.0)) ))
)
  (:constraint maxgl30 
 :parameters ()
:condition   (and (<= (g l30) 0.0) (>= (g l30) 0.0))
)
  (:constraint feedingdomainl30 
 :parameters ()
:condition    (or (= (f l30) 1.0) (= (f l30) 0.0))
)
  (:constraint kirkoffl31 
  :parameters ()
:condition (= (+ (g l31) (+ (p l30 l31) 0.0) ) (+ (* (l l31) (f l31)) (+ (p l31 l32) 0.0) ))
)
  (:constraint maxgl31 
 :parameters ()
:condition   (and (<= (g l31) 360.0) (>= (g l31) 0.0))
)
  (:constraint feedingdomainl31 
 :parameters ()
:condition    (or (= (f l31) 1.0) (= (f l31) 0.0))
)
  (:constraint kirkoffl32 
  :parameters ()
:condition (= (+ (g l32) (+ (p l31 l32) 0.0) ) (+ (* (l l32) (f l32)) 0.0 ))
)
  (:constraint maxgl32 
 :parameters ()
:condition   (and (<= (g l32) 0.0) (>= (g l32) 0.0))
)
  (:constraint feedingdomainl32 
 :parameters ()
:condition    (or (= (f l32) 1.0) (= (f l32) 0.0))
)
  (:constraint kirkoffl33 
  :parameters ()
:condition (= (+ (g l33) (+ (p l30 l33) 0.0) ) (+ (* (l l33) (f l33)) (+ (p l33 l34) 0.0) ))
)
  (:constraint maxgl33 
 :parameters ()
:condition   (and (<= (g l33) 0.0) (>= (g l33) 0.0))
)
  (:constraint feedingdomainl33 
 :parameters ()
:condition    (or (= (f l33) 1.0) (= (f l33) 0.0))
)
  (:constraint kirkoffl34 
  :parameters ()
:condition (= (+ (g l34) (+ (p l33 l34) 0.0) ) (+ (* (l l34) (f l34)) (+ (p l34 l35) 0.0) ))
)
  (:constraint maxgl34 
 :parameters ()
:condition   (and (<= (g l34) 0.0) (>= (g l34) 0.0))
)
  (:constraint feedingdomainl34 
 :parameters ()
:condition    (or (= (f l34) 1.0) (= (f l34) 0.0))
)
  (:constraint kirkoffl35 
  :parameters ()
:condition (= (+ (g l35) (+ (p l34 l35) 0.0) ) (+ (* (l l35) (f l35)) (+ (p l35 l36) 0.0) ))
)
  (:constraint maxgl35 
 :parameters ()
:condition   (and (<= (g l35) 0.0) (>= (g l35) 0.0))
)
  (:constraint feedingdomainl35 
 :parameters ()
:condition    (or (= (f l35) 1.0) (= (f l35) 0.0))
)
  (:constraint kirkoffl36 
  :parameters ()
:condition (= (+ (g l36) (+ (p l35 l36) 0.0) ) (+ (* (l l36) (f l36)) (+ (p l36 l38) (+ (p l36 l37) 0.0)) ))
)
  (:constraint maxgl36 
 :parameters ()
:condition   (and (<= (g l36) 0.0) (>= (g l36) 0.0))
)
  (:constraint feedingdomainl36 
 :parameters ()
:condition    (or (= (f l36) 1.0) (= (f l36) 0.0))
)
  (:constraint kirkoffl37 
  :parameters ()
:condition (= (+ (g l37) (+ (p l36 l37) 0.0) ) (+ (* (l l37) (f l37)) 0.0 ))
)
  (:constraint maxgl37 
 :parameters ()
:condition   (and (<= (g l37) 440.0) (>= (g l37) 0.0))
)
  (:constraint feedingdomainl37 
 :parameters ()
:condition    (or (= (f l37) 1.0) (= (f l37) 0.0))
)
  (:constraint kirkoffl38 
  :parameters ()
:condition (= (+ (g l38) (+ (p l36 l38) 0.0) ) (+ (* (l l38) (f l38)) (+ (p l38 l39) 0.0) ))
)
  (:constraint maxgl38 
 :parameters ()
:condition   (and (<= (g l38) 0.0) (>= (g l38) 0.0))
)
  (:constraint feedingdomainl38 
 :parameters ()
:condition    (or (= (f l38) 1.0) (= (f l38) 0.0))
)
  (:constraint kirkoffl39 
  :parameters ()
:condition (= (+ (g l39) (+ (p l38 l39) 0.0) ) (+ (* (l l39) (f l39)) (+ (p l39 l40) 0.0) ))
)
  (:constraint maxgl39 
 :parameters ()
:condition   (and (<= (g l39) 0.0) (>= (g l39) 0.0))
)
  (:constraint feedingdomainl39 
 :parameters ()
:condition    (or (= (f l39) 1.0) (= (f l39) 0.0))
)
  (:constraint kirkoffl40 
  :parameters ()
:condition (= (+ (g l40) (+ (p l39 l40) 0.0) ) (+ (* (l l40) (f l40)) (+ (p l40 l41) 0.0) ))
)
  (:constraint maxgl40 
 :parameters ()
:condition   (and (<= (g l40) 0.0) (>= (g l40) 0.0))
)
  (:constraint feedingdomainl40 
 :parameters ()
:condition    (or (= (f l40) 1.0) (= (f l40) 0.0))
)
  (:constraint kirkoffl41 
  :parameters ()
:condition (= (+ (g l41) (+ (p l11 l41) (+ (p l40 l41) 0.0)) ) (+ (* (l l41) (f l41)) 0.0 ))
)
  (:constraint maxgl41 
 :parameters ()
:condition   (and (<= (g l41) 0.0) (>= (g l41) 0.0))
)
  (:constraint feedingdomainl41 
 :parameters ()
:condition    (or (= (f l41) 1.0) (= (f l41) 0.0))
)
  (:constraint kirkoffl42 
  :parameters ()
:condition (= (+ (g l42) (+ (p l25 l42) 0.0) ) (+ (* (l l42) (f l42)) (+ (p l42 l43) 0.0) ))
)
  (:constraint maxgl42 
 :parameters ()
:condition   (and (<= (g l42) 0.0) (>= (g l42) 0.0))
)
  (:constraint feedingdomainl42 
 :parameters ()
:condition    (or (= (f l42) 1.0) (= (f l42) 0.0))
)
  (:constraint kirkoffl43 
  :parameters ()
:condition (= (+ (g l43) (+ (p l42 l43) 0.0) ) (+ (* (l l43) (f l43)) (+ (p l43 l44) 0.0) ))
)
  (:constraint maxgl43 
 :parameters ()
:condition   (and (<= (g l43) 0.0) (>= (g l43) 0.0))
)
  (:constraint feedingdomainl43 
 :parameters ()
:condition    (or (= (f l43) 1.0) (= (f l43) 0.0))
)
  (:constraint kirkoffl44 
  :parameters ()
:condition (= (+ (g l44) (+ (p l43 l44) 0.0) ) (+ (* (l l44) (f l44)) (+ (p l44 l45) 0.0) ))
)
  (:constraint maxgl44 
 :parameters ()
:condition   (and (<= (g l44) 0.0) (>= (g l44) 0.0))
)
  (:constraint feedingdomainl44 
 :parameters ()
:condition    (or (= (f l44) 1.0) (= (f l44) 0.0))
)
  (:constraint kirkoffl45 
  :parameters ()
:condition (= (+ (g l45) (+ (p l44 l45) 0.0) ) (+ (* (l l45) (f l45)) 0.0 ))
)
  (:constraint maxgl45 
 :parameters ()
:condition   (and (<= (g l45) 600.0) (>= (g l45) 0.0))
)
  (:constraint feedingdomainl45 
 :parameters ()
:condition    (or (= (f l45) 1.0) (= (f l45) 0.0))
)
)
