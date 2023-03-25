;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; counters-inv domain, functional strips version
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain fn-counters-inv)
    ;(:requirements :strips :typing :equality :adl)
    (:types counter)

    (:functions
        (value ?c - counter) ;; The value shown in counter ?c
        (max_int) ;; The maximum integer we consider - a static value
    )

    ;; Increment the value in the given counter by one
    (:action increment
         :parameters (?c - counter)
         :precondition (and (< (value ?c) (max_int)))
         :effect (and (increase (value ?c)  1))
    )

    ;; Decrement the value in the given counter by one
    (:action decrement
         :parameters (?c - counter)
         :precondition (and (> (value ?c) 0))
         :effect (and (decrease (value ?c)1))
    )
)
