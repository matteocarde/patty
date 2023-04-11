;; logistics domain Typed version.
;;

(define (domain logistics)
  (:requirements :strips :typing)
  (:types
    truck airplane drone van - vehicle
    package vehicle - physobj
    airport location hub - place
    city place physobj - object
  )

  (:predicates
    (in-city ?loc - place ?city - city) ;If a place (airport or location) is in a city
    (at ?obj - physobj ?loc - place) ;true if a phisical object (package, truck, airplane) is in a place (airport or location)
    (in ?pkg - package ?veh - vehicle) ;true if a package is in a vehicle (truck or location)
    (link ?a - city ?b - city) ;true if two cities are connected
    (full ?d - drone) ;true if a drone has one package
    (allowsDrones ?c - city) ;true if a city allows drones in the airspace
  )

  ; A truck can be loaded if both the truck and the packages is at the location
  ; the result is that the package is no longer in the location but inside the truck
  (:action load-truck
    :parameters (?pkg - package ?truck - truck ?loc - place)
    :precondition (and
      (at ?truck ?loc)
      (at ?pkg ?loc)
    )
    :effect (and
      (not (at ?pkg ?loc))
      (in ?pkg ?truck)
    )
  )

  (:action load-van
    :parameters (?pkg - package ?van - van ?loc - place)
    :precondition (and
      (at ?van ?loc)
      (at ?pkg ?loc)
    )
    :effect (and
      (not (at ?pkg ?loc))
      (in ?pkg ?van)
    )
  )

  ; A plance can be loaded if both the plance and the packages is at the location
  ; the result is that the package is no longer in the location but inside the plance
  (:action load-airplane
    :parameters (?pkg - package ?airplane - airplane ?loc - place)
    :precondition (and
      (at ?pkg ?loc)
      (at ?airplane ?loc)
    )
    :effect (and
      (not (at ?pkg ?loc))
      (in ?pkg ?airplane)
    )
  )

  ; Loading a drone only if it doesn't contain another package inside
  (:action load-drone
    :parameters (?pkg - package ?drone - drone ?loc - place)
    :precondition (and
      (at ?drone ?loc)
      (at ?pkg ?loc)
      (not (full ?drone))
    )
    :effect (and
      (not (at ?pkg ?loc))
      (in ?pkg ?drone)
      (full ?drone)
    )
  )

  ; Unloading the truck if the package is inside the truck
  ; The result is that the package is at the place of the truck and no longer in the truck
  (:action unload-truck
    :parameters (?pkg - package ?truck - truck ?loc - place)
    :precondition (and
      (at ?truck ?loc)
      (in ?pkg ?truck)
    )
    :effect (and
      (not (in ?pkg ?truck))
      (at ?pkg ?loc)
    )
  )

  (:action unload-van
    :parameters (?pkg - package ?van - van ?loc - place)
    :precondition (and
      (at ?van ?loc)
      (in ?pkg ?van)
    )
    :effect (and
      (not (in ?pkg ?van))
      (at ?pkg ?loc)
    )
  )

  ; Unloading the plane if the package is inside the plane
  ; The result is that the package is at the place of the plane and no longer in the plane
  (:action unload-airplane
    :parameters (?pkg - package ?airplane - airplane ?loc - place)
    :precondition (and
      (in ?pkg ?airplane)
      (at ?airplane ?loc)
    )
    :effect (and
      (not (in ?pkg ?airplane))
      (at ?pkg ?loc)
    )
  )

  ; Unloading a drone if the package is inside the drone
  (:action unload-drone
    :parameters (?pkg - package ?drone - drone ?loc - place)
    :precondition (and
      (at ?drone ?loc)
      (in ?pkg ?drone)
    )
    :effect (and
      (not (in ?pkg ?drone))
      (at ?pkg ?loc)
      (not (full ?drone))
    )
  )

  ; A truck can always drive between locations inside cities
  (:action drive-van
    :parameters (?van - van ?from - place ?to - place ?city - city)
    :precondition (and
      (at ?van ?from)
      (in-city ?from ?city)
      (in-city ?to ?city)
    )
    :effect (and
      (not (at ?van ?from))
      (at ?van ?to)
    )
  )

  ; A truck can move between connected cities
  (:action drive-between-hubs
    :parameters (?truck - truck ?fromHub - hub ?toHub - place ?fromCity - city ?toCity - city)
    :precondition (and
      (at ?truck ?fromHub)
      (in-city ?fromHub ?fromCity)
      (in-city ?toHub ?toCity)
      (link ?fromCity ?toCity)
    )
    :effect (and
      (not (at ?truck ?fromHub))
      (at ?truck ?toHub)
    )
  )

  ; Drones can only move in cities in which they are allowed
  (:action fly-drone
    :parameters (?drone - drone ?from - place ?to - place ?city - city)
    :precondition (and
      (at ?drone ?from)
      (in-city ?from ?city)
      (in-city ?to ?city)
      (allowsDrones ?city)
    )
    :effect (and
      (not (at ?drone ?from))
      (at ?drone ?to)
    )
  )

  ; A plane can only fly between cities which have an airport
  (:action fly-airplane
    :parameters (?airplane - airplane ?from - airport ?to - airport)
    :precondition (at ?airplane ?from)
    :effect (and
      (not (at ?airplane ?from))
      (at ?airplane ?to)
    )
  )
)