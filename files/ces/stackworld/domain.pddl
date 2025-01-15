(define (domain stackworld)
  (:requirements :strips :equality)
  (:types
    card - object
    first last - card
    movable - card
  )
  (:predicates
    (on-top ?a - card ?b - card)
  )

  (:action rotate
    :parameters ()
    :precondition ()
    :effect(and
      (forall
        (?f - first ?a - movable ?b - movable ?c - movable ?l - last)
        (when
          (and
            (not (= ?a ?b))
            (on-top ?f ?a)
            (on-top ?c ?l)
            (on-top ?a ?b)
          )
          (and
            (not (on-top ?a ?b))
            (on-top ?a ?l)
            (not (on-top ?c ?l))
            (on-top ?c ?a)
            (not (on-top ?f ?a))
            (on-top ?f ?b)
          )
        )
      )
    )
  )

  (:constraints
    (and
      ; (exists
      ;   (?a - movable ?b - card)
      ;   (and
      ;     (not (= ?a ?b))
      ;     (on-top ?a ?b)
      ;   )
      ; )
      ; (exists
      ;   (?a - card ?b - movable)
      ;   (and
      ;     (on-top ?a ?b)
      ;   )
      ; )
      (forall
        (?a - movable ?b - movable)
        (and
          (not (= ?a ?b))
          (or
            (not (on-top ?a ?b))
            (not (on-top ?b ?a))
          )
        )
      )
      (forall
        (?a - movable ?l - last)
        (and
          (not (on-top ?l ?a))
        )
      )
      (forall
        (?f - first ?a - movable)
        (and
          (not (on-top ?a ?f))
        )
      )
      (forall
        (?a - card ?b - movable ?c - movable)
        (and
          (not (= ?a ?b))
          (not (= ?a ?c))
          (not (= ?b ?c))
          (or
            (not (on-top ?a ?b))
            (not (on-top ?a ?c))
          )
        )
      )
      (forall
        (?a - movable ?b - movable ?c - card)
        (and
          (not (= ?a ?b))
          (not (= ?a ?c))
          (not (= ?b ?c))
          (or
            (not (on-top ?a ?c))
            (not (on-top ?b ?c))
          )
        )
      )
      (forall
        (?a - movable)
        (and
          (not (on-top ?a ?a))
        )
      )
      ; (forall
      ;   (?a - card ?f - first)
      ;   (and
      ;     (not (on-top ?a ?f))
      ;   )
      ; )
      ; (forall
      ;   (?l - last ?a - card)
      ;   (and
      ;     (not (on-top ?l ?a))
      ;   )
      ; )
      ; (forall
      ;   (?f - first ?a - movable ?b - movable)
      ;   (and
      ;     (not (= ?a ?b))
      ;     (or
      ;       (not (on-top ?f ?a))
      ;       (not (on-top ?f ?b))
      ;     )
      ;   )
      ; )
      ; (forall
      ;   (?a - movable ?b - movable ?l - last)
      ;   (and
      ;     (not (= ?a ?b))
      ;     (or
      ;       (not (on-top ?a ?l))
      ;       (not (on-top ?b ?l))
      ;     )
      ;   )
      ; )
      ; (exists
      ;   (?a - movable ?c - card)
      ;   (and
      ;     (not (on-top ?a ?c))
      ;   )
      ; )
      ; (forall
      ;   (?a - card)
      ;   (and
      ;     (or
      ;       (not (first ?a))
      ;       (not (last ?a))
      ;     )
      ;   )
      ; )
    )

  )

)