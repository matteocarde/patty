(define (problem ZTRAVEL-5-15)
(:domain zenotravel)
(:objects
	plane1 - aircraft
	plane2 - aircraft
	plane3 - aircraft
	plane4 - aircraft
	plane5 - aircraft
	person1 - person
	person2 - person
	person3 - person
	person4 - person
	person5 - person
	person6 - person
	person7 - person
	person8 - person
	person9 - person
	person10 - person
	person11 - person
	person12 - person
	person13 - person
	person14 - person
	person15 - person
	city0 - city
	city1 - city
	city2 - city
	city3 - city
	city4 - city
	city5 - city
	city6 - city
	city7 - city
	city8 - city
	city9 - city
	city10 - city
	city11 - city
	city12 - city
	city13 - city
	)
(:init
	(located plane1 city6)
	(= (capacity plane1) 2468)
	(= (fuel plane1) 562)
	(= (slow-burn plane1) 1)
	(= (fast-burn plane1) 2)
	(= (onboard plane1) 0)
	(= (zoom-limit plane1) 9)
	(located plane2 city0)
	(= (capacity plane2) 14825)
	(= (fuel plane2) 521)
	(= (slow-burn plane2) 5)
	(= (fast-burn plane2) 16)
	(= (onboard plane2) 0)
	(= (zoom-limit plane2) 2)
	(located plane3 city10)
	(= (capacity plane3) 4763)
	(= (fuel plane3) 285)
	(= (slow-burn plane3) 2)
	(= (fast-burn plane3) 4)
	(= (onboard plane3) 0)
	(= (zoom-limit plane3) 6)
	(located plane4 city4)
	(= (capacity plane4) 5095)
	(= (fuel plane4) 1782)
	(= (slow-burn plane4) 2)
	(= (fast-burn plane4) 6)
	(= (onboard plane4) 0)
	(= (zoom-limit plane4) 6)
	(located plane5 city1)
	(= (capacity plane5) 9885)
	(= (fuel plane5) 3681)
	(= (slow-burn plane5) 4)
	(= (fast-burn plane5) 8)
	(= (onboard plane5) 0)
	(= (zoom-limit plane5) 9)
	(located person1 city8)
	(located person2 city12)
	(located person3 city0)
	(located person4 city4)
	(located person5 city13)
	(located person6 city7)
	(located person7 city1)
	(located person8 city2)
	(located person9 city1)
	(located person10 city2)
	(located person11 city10)
	(located person12 city7)
	(located person13 city6)
	(located person14 city1)
	(located person15 city13)
	(= (distance city0 city0) 0)
	(= (distance city0 city1) 887)
	(= (distance city0 city2) 696)
	(= (distance city0 city3) 806)
	(= (distance city0 city4) 844)
	(= (distance city0 city5) 941)
	(= (distance city0 city6) 963)
	(= (distance city0 city7) 639)
	(= (distance city0 city8) 797)
	(= (distance city0 city9) 660)
	(= (distance city0 city10) 689)
	(= (distance city0 city11) 638)
	(= (distance city0 city12) 946)
	(= (distance city0 city13) 879)
	(= (distance city1 city0) 887)
	(= (distance city1 city1) 0)
	(= (distance city1 city2) 569)
	(= (distance city1 city3) 936)
	(= (distance city1 city4) 643)
	(= (distance city1 city5) 583)
	(= (distance city1 city6) 857)
	(= (distance city1 city7) 716)
	(= (distance city1 city8) 643)
	(= (distance city1 city9) 973)
	(= (distance city1 city10) 925)
	(= (distance city1 city11) 833)
	(= (distance city1 city12) 913)
	(= (distance city1 city13) 667)
	(= (distance city2 city0) 696)
	(= (distance city2 city1) 569)
	(= (distance city2 city2) 0)
	(= (distance city2 city3) 568)
	(= (distance city2 city4) 895)
	(= (distance city2 city5) 555)
	(= (distance city2 city6) 761)
	(= (distance city2 city7) 943)
	(= (distance city2 city8) 507)
	(= (distance city2 city9) 648)
	(= (distance city2 city10) 640)
	(= (distance city2 city11) 814)
	(= (distance city2 city12) 992)
	(= (distance city2 city13) 581)
	(= (distance city3 city0) 806)
	(= (distance city3 city1) 936)
	(= (distance city3 city2) 568)
	(= (distance city3 city3) 0)
	(= (distance city3 city4) 778)
	(= (distance city3 city5) 632)
	(= (distance city3 city6) 879)
	(= (distance city3 city7) 938)
	(= (distance city3 city8) 822)
	(= (distance city3 city9) 517)
	(= (distance city3 city10) 885)
	(= (distance city3 city11) 701)
	(= (distance city3 city12) 586)
	(= (distance city3 city13) 822)
	(= (distance city4 city0) 844)
	(= (distance city4 city1) 643)
	(= (distance city4 city2) 895)
	(= (distance city4 city3) 778)
	(= (distance city4 city4) 0)
	(= (distance city4 city5) 844)
	(= (distance city4 city6) 670)
	(= (distance city4 city7) 679)
	(= (distance city4 city8) 561)
	(= (distance city4 city9) 814)
	(= (distance city4 city10) 653)
	(= (distance city4 city11) 986)
	(= (distance city4 city12) 647)
	(= (distance city4 city13) 566)
	(= (distance city5 city0) 941)
	(= (distance city5 city1) 583)
	(= (distance city5 city2) 555)
	(= (distance city5 city3) 632)
	(= (distance city5 city4) 844)
	(= (distance city5 city5) 0)
	(= (distance city5 city6) 654)
	(= (distance city5 city7) 716)
	(= (distance city5 city8) 962)
	(= (distance city5 city9) 709)
	(= (distance city5 city10) 977)
	(= (distance city5 city11) 906)
	(= (distance city5 city12) 717)
	(= (distance city5 city13) 626)
	(= (distance city6 city0) 963)
	(= (distance city6 city1) 857)
	(= (distance city6 city2) 761)
	(= (distance city6 city3) 879)
	(= (distance city6 city4) 670)
	(= (distance city6 city5) 654)
	(= (distance city6 city6) 0)
	(= (distance city6 city7) 547)
	(= (distance city6 city8) 532)
	(= (distance city6 city9) 618)
	(= (distance city6 city10) 629)
	(= (distance city6 city11) 810)
	(= (distance city6 city12) 751)
	(= (distance city6 city13) 508)
	(= (distance city7 city0) 639)
	(= (distance city7 city1) 716)
	(= (distance city7 city2) 943)
	(= (distance city7 city3) 938)
	(= (distance city7 city4) 679)
	(= (distance city7 city5) 716)
	(= (distance city7 city6) 547)
	(= (distance city7 city7) 0)
	(= (distance city7 city8) 749)
	(= (distance city7 city9) 573)
	(= (distance city7 city10) 526)
	(= (distance city7 city11) 634)
	(= (distance city7 city12) 774)
	(= (distance city7 city13) 613)
	(= (distance city8 city0) 797)
	(= (distance city8 city1) 643)
	(= (distance city8 city2) 507)
	(= (distance city8 city3) 822)
	(= (distance city8 city4) 561)
	(= (distance city8 city5) 962)
	(= (distance city8 city6) 532)
	(= (distance city8 city7) 749)
	(= (distance city8 city8) 0)
	(= (distance city8 city9) 957)
	(= (distance city8 city10) 619)
	(= (distance city8 city11) 783)
	(= (distance city8 city12) 637)
	(= (distance city8 city13) 680)
	(= (distance city9 city0) 660)
	(= (distance city9 city1) 973)
	(= (distance city9 city2) 648)
	(= (distance city9 city3) 517)
	(= (distance city9 city4) 814)
	(= (distance city9 city5) 709)
	(= (distance city9 city6) 618)
	(= (distance city9 city7) 573)
	(= (distance city9 city8) 957)
	(= (distance city9 city9) 0)
	(= (distance city9 city10) 597)
	(= (distance city9 city11) 790)
	(= (distance city9 city12) 667)
	(= (distance city9 city13) 745)
	(= (distance city10 city0) 689)
	(= (distance city10 city1) 925)
	(= (distance city10 city2) 640)
	(= (distance city10 city3) 885)
	(= (distance city10 city4) 653)
	(= (distance city10 city5) 977)
	(= (distance city10 city6) 629)
	(= (distance city10 city7) 526)
	(= (distance city10 city8) 619)
	(= (distance city10 city9) 597)
	(= (distance city10 city10) 0)
	(= (distance city10 city11) 857)
	(= (distance city10 city12) 821)
	(= (distance city10 city13) 961)
	(= (distance city11 city0) 638)
	(= (distance city11 city1) 833)
	(= (distance city11 city2) 814)
	(= (distance city11 city3) 701)
	(= (distance city11 city4) 986)
	(= (distance city11 city5) 906)
	(= (distance city11 city6) 810)
	(= (distance city11 city7) 634)
	(= (distance city11 city8) 783)
	(= (distance city11 city9) 790)
	(= (distance city11 city10) 857)
	(= (distance city11 city11) 0)
	(= (distance city11 city12) 820)
	(= (distance city11 city13) 531)
	(= (distance city12 city0) 946)
	(= (distance city12 city1) 913)
	(= (distance city12 city2) 992)
	(= (distance city12 city3) 586)
	(= (distance city12 city4) 647)
	(= (distance city12 city5) 717)
	(= (distance city12 city6) 751)
	(= (distance city12 city7) 774)
	(= (distance city12 city8) 637)
	(= (distance city12 city9) 667)
	(= (distance city12 city10) 821)
	(= (distance city12 city11) 820)
	(= (distance city12 city12) 0)
	(= (distance city12 city13) 939)
	(= (distance city13 city0) 879)
	(= (distance city13 city1) 667)
	(= (distance city13 city2) 581)
	(= (distance city13 city3) 822)
	(= (distance city13 city4) 566)
	(= (distance city13 city5) 626)
	(= (distance city13 city6) 508)
	(= (distance city13 city7) 613)
	(= (distance city13 city8) 680)
	(= (distance city13 city9) 745)
	(= (distance city13 city10) 961)
	(= (distance city13 city11) 531)
	(= (distance city13 city12) 939)
	(= (distance city13 city13) 0)
	(= (total-fuel-used) 0)
)
(:goal (and
	(located plane2 city12)
	(located plane3 city6)
	(located person1 city3)
	(located person2 city4)
	(located person3 city11)
	(located person4 city13)
	(located person5 city11)
	(located person6 city7)
	(located person7 city1)
	(located person8 city11)
	(located person9 city2)
	(located person10 city6)
	(located person11 city0)
	(located person12 city12)
	(located person13 city13)
	(located person14 city4)
	(located person15 city4)
	))

;(:metric minimize (+ (* 5 (total-time))  (* 2 (total-fuel-used))))
)