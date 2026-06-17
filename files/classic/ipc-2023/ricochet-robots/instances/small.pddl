;; From ASP domain-ricochet-robots/asp-2015/005-ricochetrobot-13-0.asp
;; Generated from file 005-ricochetrobot-13-0.asp from the ASP competition 2015
;;
;; +xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+
;; xR1|  x  |  |  |  |  |  |  |  x  |  |  |  |  |R3x
;; +--+--+--+--+xx+--+--+--+--+--+--+--+--+--+xx+--+
;; x  |  |  |  x  |  |  |  |  |  |  |  |  |  x  |  x
;; +--+xx+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; x  |  x  |  |  |  |  |  |  |  |  x  |  |  |  |  x
;; +--+--+--+--+--+--+--+--+--+--+--+xx+--+--+--+--+
;; x  |  |  |  |  |  |  x  |  |  |  |  |  |  |  |  x
;; +--+--+--+--+--+--+xx+--+--+--+--+--+--+--+--+xx+
;; x  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  x
;; +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; x  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  x
;; +xx+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; x  |  |  x  |  |  |  |  |  |  |  |  |  |  x  |  x
;; +--+--+--+xx+--+--+--+xx+xx+--+xx+--+--+xx+--+--+
;; x  |  |G2|  |  |  |  x  |  x  |  x  |  |  |  |  x
;; +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; x  |  |  |  |  |  |  x  |  x  |  |  |  |  |  |  x
;; +--+--+--+--+--+--+--+xx+xx+--+--+--+--+--+--+xx+
;; x  |  |  |  x  |  |  |  |  |  |  |  |  |  |  |  x
;; +--+xx+--+--+xx+--+--+--+xx+--+--+--+--+xx+--+--+
;; x  |  x  |  |  |  |  |  x  |  |  |  |  x  |  |  x
;; +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; x  |  |  |  |  |  |  |  |  |  |  x  |  |  |  |  x
;; +xx+--+--+--+--+--+--+--+--+--+xx+--+--+--+--+--+
;; x  |  |  |  |  |  |  |  |  |  |  |  |  |  x  |  x
;; +--+--+--+--+--+--+xx+--+--+--+--+--+--+--+xx+--+
;; x  |  |  |  |  |  x  |  |  |  |  |  |  |  |  |  x
;; +--+--+--+--+--+--+--+--+--+xx+--+--+--+--+--+--+
;; x  |  |  x  |  |  |  |  |  |  x  |  |  |  |  |  x
;; +--+--+xx+--+--+--+--+--+--+--+--+--+--+--+--+--+
;; xR2|  |  |  x  |  |  |  |  |  |  |  x  |  |  |R4x
;; +xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+xx+

(define (problem ricochet-robots-16x16-13-241179)
    (:domain ricochet-robots)

    (:objects
        cell-1-1 cell-1-2 cell-1-3 cell-1-4 cell-2-1 cell-2-2 cell-2-3 cell-2-4 - cell
        robot-1 - robot
        west east north south - direction
    )

    (:init
        (NEXT cell-1-1 cell-1-2 south)
        (NEXT cell-1-2 cell-1-3 south)
        (NEXT cell-1-3 cell-1-4 south)

        (NEXT cell-2-1 cell-2-2 south)
        (NEXT cell-2-2 cell-2-3 south)
        (NEXT cell-2-3 cell-2-4 south)

        (NEXT cell-1-4 cell-1-3 north)
        (NEXT cell-1-3 cell-1-2 north)
        (NEXT cell-1-2 cell-1-1 north)

        (NEXT cell-2-4 cell-2-3 north)
        (NEXT cell-2-3 cell-2-2 north)
        (NEXT cell-2-2 cell-2-1 north)

        (NEXT cell-1-1 cell-2-1 east)
        (NEXT cell-1-2 cell-2-2 east)
        (NEXT cell-1-3 cell-2-3 east)
        (NEXT cell-1-4 cell-2-4 east)

        (NEXT cell-2-1 cell-1-1 west)
        (NEXT cell-2-2 cell-1-2 west)
        (NEXT cell-2-3 cell-1-3 west)
        (NEXT cell-2-4 cell-1-4 west)

        (BLOCKED cell-1-1 south)
        (BLOCKED cell-2-3 south)
        (BLOCKED cell-1-4 south)
        (BLOCKED cell-2-4 south)
        
        (BLOCKED cell-1-1 north)
        (BLOCKED cell-2-1 north)

        (BLOCKED cell-1-1 west)
        (BLOCKED cell-1-2 west)
        (BLOCKED cell-1-3 west)
        (BLOCKED cell-1-4 west)

        (BLOCKED cell-2-1 east)
        (BLOCKED cell-2-2 east)
        (BLOCKED cell-2-3 east)
        (BLOCKED cell-2-4 east)

        (free cell-1-2)
        (free cell-1-3)
        (free cell-1-4)
        (free cell-2-1)
        (free cell-2-2)
        (free cell-2-3)
        (free cell-2-4)

        (at robot-1 cell-1-1) ;; red

        (nothing-is-moving)
    )
    (:goal
        (and
            (at robot-1 cell-2-4)
            ; (nothing-is-moving)
        )
    )
    (:metric minimize
        (total-cost)
    )
)