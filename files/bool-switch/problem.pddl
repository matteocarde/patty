(define (problem problem_name)
  (:domain domain_name)
  (:objects
    s1 s2 s3 s4 s5 s6 s7 s8 - switch
  )

  (:init
    (p s1)
    (next s1 s2)
    (next s2 s3)
    (next s3 s4)
    (next s4 s5)
    (next s5 s6)
    (next s6 s7)
    (next s7 s8)
  )

  (:goal
    (and
      (p s8)
    )
  )
)