(define (problem logistics-10-1)
  (:domain logistics)
  (:objects
    apn1 - airplane
    apt4 apt3 apt2 apt1 - airport
    hub4 hub3 hub2 hub1 - hub
    pos4 pos3 pos2 pos1 - location
    cit4 cit3 cit2 cit1 - city
    tru4 tru3 tru2 tru1 - truck
    van4 van3 van2 van1 - van
    drone1 drone2 drone3 drone4 - drone
    obj43 obj42 obj41 obj33 obj32 obj31 obj23 obj22 obj21 obj13 obj12 obj11 - package
  )

  (:init
    (at apn1 apt2)
    (at tru1 hub1)
    (at obj11 pos1)
    (at obj12 pos1)
    (at obj13 pos1)
    (at tru2 hub2)
    (at obj21 pos2)
    (at obj22 pos2)
    (at obj23 pos2)
    (at tru3 hub3)
    (at obj31 pos3)
    (at obj32 pos3)
    (at obj33 pos3)
    (at tru4 hub4)
    (at obj41 pos4)
    (at obj42 pos4)
    (at obj43 pos4)
    (at van1 hub1)
    (at van2 hub2)
    (at van3 hub3)
    (at van4 hub4)
    (in-city pos1 cit1)
    (in-city apt1 cit1)
    (in-city pos2 cit2)
    (in-city apt2 cit2)
    (in-city pos3 cit3)
    (in-city apt3 cit3)
    (in-city pos4 cit4)
    (in-city apt4 cit4)
    (in-city hub1 cit1)
    (in-city hub2 cit2)
    (in-city hub3 cit3)
    (in-city hub4 cit4)
    (link cit4 cit3)
    (link cit3 cit4)
    (link cit1 cit2)
    (link cit2 cit1)
    (allowsDrones cit1)
    (allowsDrones cit2)
    (allowsDrones cit3)
    (at drone1 pos1)
    (at drone2 pos2)
    (at drone3 pos3)
    (at drone4 pos4)
  )

  (:goal
    (and (at obj43 apt4) (at obj32 pos3) (at obj42 apt3) (at obj12 pos1)
      (at obj41 apt3) (at obj23 pos3) (at obj13 apt4) (at obj22 pos4)
      (at obj31 apt3) (at obj33 apt1))
  )
)