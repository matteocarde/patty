(define (problem pb01)
  (:domain alchemy)
  (:objects
    water earth fire air pressure energy dust gunpowder explosion - element
  )
  (:init
    (have water)
    (have earth)
    (have fire)
    (have air)
    (combination air air pressure)
    (combination air fire energy)
    (combination air earth dust)
    (combination dust fire gunpowder)
    (combination gunpowder fire explosion)
  )
  (:goal
    (and (have explosion))
  )
)