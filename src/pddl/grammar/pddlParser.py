# Generated from pddl.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,761,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,1,0,
        1,0,3,0,173,8,0,1,1,1,1,1,1,1,1,3,1,179,8,1,1,1,3,1,182,8,1,1,1,
        3,1,185,8,1,1,1,3,1,188,8,1,1,1,3,1,191,8,1,1,1,1,1,1,1,1,1,5,1,
        197,8,1,10,1,12,1,200,9,1,1,1,3,1,203,8,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,5,4,218,8,4,10,4,12,4,221,9,4,1,4,
        1,4,1,5,1,5,1,5,1,6,1,6,1,7,4,7,231,8,7,11,7,12,7,232,1,7,5,7,236,
        8,7,10,7,12,7,239,9,7,1,8,1,8,1,8,4,8,244,8,8,11,8,12,8,245,1,8,
        1,8,1,9,4,9,251,8,9,11,9,12,9,252,1,9,1,9,1,9,1,10,1,10,1,10,5,10,
        261,8,10,10,10,12,10,264,9,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,
        1,13,1,14,4,14,275,8,14,11,14,12,14,276,1,14,1,14,1,14,1,15,1,15,
        3,15,284,8,15,1,16,1,16,5,16,288,8,16,10,16,12,16,291,9,16,1,17,
        1,17,5,17,295,8,17,10,17,12,17,298,9,17,1,18,1,18,1,18,1,18,1,18,
        3,18,305,8,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,3,21,318,8,21,1,22,1,22,1,22,4,22,323,8,22,11,22,12,22,324,
        1,22,1,22,1,23,1,23,1,23,4,23,332,8,23,11,23,12,23,333,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,3,29,
        350,8,29,1,30,1,30,1,31,1,31,1,31,3,31,357,8,31,1,32,1,32,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,
        37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,3,38,400,
        8,38,1,39,1,39,3,39,404,8,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,
        425,8,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,436,8,
        43,1,43,1,43,1,44,1,44,1,44,1,44,3,44,444,8,44,1,45,1,45,3,45,448,
        8,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,
        1,47,1,47,1,47,1,47,1,47,4,47,467,8,47,11,47,12,47,468,1,47,1,47,
        1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,4,48,481,8,48,11,48,12,48,
        482,1,48,1,48,1,49,1,49,1,49,4,49,490,8,49,11,49,12,49,491,1,49,
        1,49,1,50,1,50,1,50,4,50,499,8,50,11,50,12,50,500,1,50,1,50,1,51,
        1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,3,52,514,8,52,1,53,1,53,
        3,53,518,8,53,1,54,1,54,1,54,1,54,1,54,4,54,525,8,54,11,54,12,54,
        526,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,3,55,537,8,55,1,55,1,
        55,1,56,1,56,1,56,1,56,1,56,1,56,3,56,547,8,56,1,56,1,56,1,57,1,
        57,1,57,1,57,1,57,1,57,3,57,557,8,57,1,57,1,57,1,58,1,58,1,58,1,
        58,1,58,3,58,566,8,58,1,59,1,59,1,59,1,59,1,59,3,59,573,8,59,1,59,
        1,59,1,60,1,60,1,60,1,60,1,60,3,60,582,8,60,1,60,1,60,1,61,1,61,
        1,61,1,61,1,61,3,61,591,8,61,1,61,1,61,1,62,1,62,1,62,3,62,598,8,
        62,1,63,1,63,1,63,4,63,603,8,63,11,63,12,63,604,1,63,1,63,1,64,1,
        64,3,64,611,8,64,1,65,1,65,5,65,615,8,65,10,65,12,65,618,9,65,1,
        65,1,65,1,66,1,66,1,67,1,67,1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,
        70,1,70,1,70,1,71,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,73,3,
        73,646,8,73,1,73,3,73,649,8,73,1,73,1,73,1,73,1,74,1,74,1,74,1,74,
        3,74,658,8,74,1,74,3,74,661,8,74,1,74,3,74,664,8,74,1,74,1,74,1,
        74,1,75,1,75,1,75,1,75,3,75,673,8,75,1,75,3,75,676,8,75,1,75,1,75,
        1,75,1,76,1,76,1,76,1,76,3,76,685,8,76,1,76,3,76,688,8,76,1,76,1,
        76,1,76,1,77,1,77,1,77,1,77,1,77,1,77,4,77,699,8,77,11,77,12,77,
        700,1,77,1,77,1,77,1,78,1,78,1,78,1,78,1,78,3,78,711,8,78,1,78,1,
        78,1,78,3,78,716,8,78,1,78,1,78,1,79,1,79,1,79,1,79,1,79,1,80,1,
        80,1,80,1,80,1,80,1,81,1,81,1,81,5,81,733,8,81,10,81,12,81,736,9,
        81,1,81,1,81,1,82,1,82,1,82,1,82,4,82,744,8,82,11,82,12,82,745,1,
        82,1,82,1,83,1,83,1,83,1,83,1,83,1,84,1,84,1,84,1,84,1,84,1,84,1,
        84,0,0,85,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,
        120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,
        152,154,156,158,160,162,164,166,168,0,5,1,0,53,54,1,0,11,13,2,0,
        5,5,14,16,1,0,17,21,1,0,49,50,782,0,172,1,0,0,0,2,174,1,0,0,0,4,
        206,1,0,0,0,6,211,1,0,0,0,8,214,1,0,0,0,10,224,1,0,0,0,12,227,1,
        0,0,0,14,230,1,0,0,0,16,240,1,0,0,0,18,250,1,0,0,0,20,257,1,0,0,
        0,22,267,1,0,0,0,24,269,1,0,0,0,26,271,1,0,0,0,28,274,1,0,0,0,30,
        283,1,0,0,0,32,285,1,0,0,0,34,292,1,0,0,0,36,304,1,0,0,0,38,306,
        1,0,0,0,40,310,1,0,0,0,42,317,1,0,0,0,44,319,1,0,0,0,46,328,1,0,
        0,0,48,337,1,0,0,0,50,339,1,0,0,0,52,341,1,0,0,0,54,343,1,0,0,0,
        56,345,1,0,0,0,58,349,1,0,0,0,60,351,1,0,0,0,62,356,1,0,0,0,64,358,
        1,0,0,0,66,364,1,0,0,0,68,370,1,0,0,0,70,376,1,0,0,0,72,382,1,0,
        0,0,74,387,1,0,0,0,76,399,1,0,0,0,78,403,1,0,0,0,80,405,1,0,0,0,
        82,411,1,0,0,0,84,417,1,0,0,0,86,428,1,0,0,0,88,443,1,0,0,0,90,447,
        1,0,0,0,92,449,1,0,0,0,94,458,1,0,0,0,96,472,1,0,0,0,98,486,1,0,
        0,0,100,495,1,0,0,0,102,504,1,0,0,0,104,513,1,0,0,0,106,517,1,0,
        0,0,108,519,1,0,0,0,110,530,1,0,0,0,112,540,1,0,0,0,114,550,1,0,
        0,0,116,565,1,0,0,0,118,567,1,0,0,0,120,576,1,0,0,0,122,585,1,0,
        0,0,124,597,1,0,0,0,126,599,1,0,0,0,128,610,1,0,0,0,130,612,1,0,
        0,0,132,621,1,0,0,0,134,623,1,0,0,0,136,626,1,0,0,0,138,629,1,0,
        0,0,140,632,1,0,0,0,142,635,1,0,0,0,144,638,1,0,0,0,146,641,1,0,
        0,0,148,653,1,0,0,0,150,668,1,0,0,0,152,680,1,0,0,0,154,692,1,0,
        0,0,156,705,1,0,0,0,158,719,1,0,0,0,160,724,1,0,0,0,162,729,1,0,
        0,0,164,739,1,0,0,0,166,749,1,0,0,0,168,754,1,0,0,0,170,173,3,2,
        1,0,171,173,3,156,78,0,172,170,1,0,0,0,172,171,1,0,0,0,173,1,1,0,
        0,0,174,175,5,51,0,0,175,176,5,1,0,0,176,178,3,4,2,0,177,179,3,8,
        4,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,182,3,16,
        8,0,181,180,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,185,3,20,
        10,0,184,183,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,188,3,44,
        22,0,187,186,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,191,3,46,
        23,0,190,189,1,0,0,0,190,191,1,0,0,0,191,198,1,0,0,0,192,197,3,146,
        73,0,193,197,3,148,74,0,194,197,3,150,75,0,195,197,3,152,76,0,196,
        192,1,0,0,0,196,193,1,0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,
        200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,201,203,3,154,77,0,202,201,1,0,0,0,202,203,1,0,0,0,203,
        204,1,0,0,0,204,205,5,52,0,0,205,3,1,0,0,0,206,207,5,51,0,0,207,
        208,5,2,0,0,208,209,5,54,0,0,209,210,5,52,0,0,210,5,1,0,0,0,211,
        212,5,3,0,0,212,213,5,54,0,0,213,7,1,0,0,0,214,215,5,51,0,0,215,
        219,5,4,0,0,216,218,3,6,3,0,217,216,1,0,0,0,218,221,1,0,0,0,219,
        217,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,219,1,0,0,0,222,
        223,5,52,0,0,223,9,1,0,0,0,224,225,5,5,0,0,225,226,3,12,6,0,226,
        11,1,0,0,0,227,228,5,54,0,0,228,13,1,0,0,0,229,231,3,12,6,0,230,
        229,1,0,0,0,231,232,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,
        237,1,0,0,0,234,236,3,10,5,0,235,234,1,0,0,0,236,239,1,0,0,0,237,
        235,1,0,0,0,237,238,1,0,0,0,238,15,1,0,0,0,239,237,1,0,0,0,240,241,
        5,51,0,0,241,243,5,6,0,0,242,244,3,14,7,0,243,242,1,0,0,0,244,245,
        1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,
        5,52,0,0,248,17,1,0,0,0,249,251,3,24,12,0,250,249,1,0,0,0,251,252,
        1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,254,1,0,0,0,254,255,
        5,5,0,0,255,256,3,12,6,0,256,19,1,0,0,0,257,258,5,51,0,0,258,262,
        5,7,0,0,259,261,3,18,9,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,
        1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,262,1,0,0,0,265,266,
        5,52,0,0,266,21,1,0,0,0,267,268,5,54,0,0,268,23,1,0,0,0,269,270,
        5,54,0,0,270,25,1,0,0,0,271,272,7,0,0,0,272,27,1,0,0,0,273,275,3,
        26,13,0,274,273,1,0,0,0,275,276,1,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,278,1,0,0,0,278,279,5,5,0,0,279,280,3,12,6,0,280,29,
        1,0,0,0,281,284,3,26,13,0,282,284,3,24,12,0,283,281,1,0,0,0,283,
        282,1,0,0,0,284,31,1,0,0,0,285,289,3,22,11,0,286,288,3,30,15,0,287,
        286,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,
        33,1,0,0,0,291,289,1,0,0,0,292,296,3,22,11,0,293,295,3,28,14,0,294,
        293,1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,
        35,1,0,0,0,298,296,1,0,0,0,299,300,5,51,0,0,300,301,3,32,16,0,301,
        302,5,52,0,0,302,305,1,0,0,0,303,305,3,26,13,0,304,299,1,0,0,0,304,
        303,1,0,0,0,305,37,1,0,0,0,306,307,5,51,0,0,307,308,3,34,17,0,308,
        309,5,52,0,0,309,39,1,0,0,0,310,311,5,51,0,0,311,312,5,8,0,0,312,
        313,3,36,18,0,313,314,5,52,0,0,314,41,1,0,0,0,315,318,3,36,18,0,
        316,318,3,40,20,0,317,315,1,0,0,0,317,316,1,0,0,0,318,43,1,0,0,0,
        319,320,5,51,0,0,320,322,5,9,0,0,321,323,3,38,19,0,322,321,1,0,0,
        0,323,324,1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,326,1,0,0,
        0,326,327,5,52,0,0,327,45,1,0,0,0,328,329,5,51,0,0,329,331,5,10,
        0,0,330,332,3,38,19,0,331,330,1,0,0,0,332,333,1,0,0,0,333,331,1,
        0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,336,5,52,0,0,336,47,1,
        0,0,0,337,338,7,1,0,0,338,49,1,0,0,0,339,340,7,2,0,0,340,51,1,0,
        0,0,341,342,7,3,0,0,342,53,1,0,0,0,343,344,5,56,0,0,344,55,1,0,0,
        0,345,346,5,22,0,0,346,57,1,0,0,0,347,350,3,54,27,0,348,350,3,56,
        28,0,349,347,1,0,0,0,349,348,1,0,0,0,350,59,1,0,0,0,351,352,3,54,
        27,0,352,61,1,0,0,0,353,357,3,64,32,0,354,357,3,36,18,0,355,357,
        3,58,29,0,356,353,1,0,0,0,356,354,1,0,0,0,356,355,1,0,0,0,357,63,
        1,0,0,0,358,359,5,51,0,0,359,360,3,50,25,0,360,361,3,62,31,0,361,
        362,3,62,31,0,362,363,5,52,0,0,363,65,1,0,0,0,364,365,5,51,0,0,365,
        366,5,21,0,0,366,367,3,36,18,0,367,368,3,60,30,0,368,369,5,52,0,
        0,369,67,1,0,0,0,370,371,5,51,0,0,371,372,5,21,0,0,372,373,5,23,
        0,0,373,374,3,62,31,0,374,375,5,52,0,0,375,69,1,0,0,0,376,377,5,
        51,0,0,377,378,3,52,26,0,378,379,3,62,31,0,379,380,3,62,31,0,380,
        381,5,52,0,0,381,71,1,0,0,0,382,383,5,51,0,0,383,384,5,8,0,0,384,
        385,3,70,35,0,385,386,5,52,0,0,386,73,1,0,0,0,387,388,5,51,0,0,388,
        389,3,48,24,0,389,390,3,36,18,0,390,391,3,62,31,0,391,392,5,52,0,
        0,392,75,1,0,0,0,393,400,3,94,47,0,394,400,3,96,48,0,395,400,3,42,
        21,0,396,400,3,72,36,0,397,400,3,70,35,0,398,400,3,102,51,0,399,
        393,1,0,0,0,399,394,1,0,0,0,399,395,1,0,0,0,399,396,1,0,0,0,399,
        397,1,0,0,0,399,398,1,0,0,0,400,77,1,0,0,0,401,404,3,90,45,0,402,
        404,3,100,50,0,403,401,1,0,0,0,403,402,1,0,0,0,404,79,1,0,0,0,405,
        406,5,51,0,0,406,407,5,24,0,0,407,408,3,76,38,0,408,409,3,78,39,
        0,409,410,5,52,0,0,410,81,1,0,0,0,411,412,5,51,0,0,412,413,5,25,
        0,0,413,414,3,130,65,0,414,415,3,80,40,0,415,416,5,52,0,0,416,83,
        1,0,0,0,417,418,5,51,0,0,418,419,5,25,0,0,419,424,3,130,65,0,420,
        425,3,84,42,0,421,425,3,86,43,0,422,425,3,94,47,0,423,425,3,96,48,
        0,424,420,1,0,0,0,424,421,1,0,0,0,424,422,1,0,0,0,424,423,1,0,0,
        0,425,426,1,0,0,0,426,427,5,52,0,0,427,85,1,0,0,0,428,429,5,51,0,
        0,429,430,5,26,0,0,430,435,3,130,65,0,431,436,3,84,42,0,432,436,
        3,86,43,0,433,436,3,94,47,0,434,436,3,96,48,0,435,431,1,0,0,0,435,
        432,1,0,0,0,435,433,1,0,0,0,435,434,1,0,0,0,436,437,1,0,0,0,437,
        438,5,52,0,0,438,87,1,0,0,0,439,444,3,42,21,0,440,444,3,74,37,0,
        441,444,3,80,40,0,442,444,3,82,41,0,443,439,1,0,0,0,443,440,1,0,
        0,0,443,441,1,0,0,0,443,442,1,0,0,0,444,89,1,0,0,0,445,448,3,42,
        21,0,446,448,3,74,37,0,447,445,1,0,0,0,447,446,1,0,0,0,448,91,1,
        0,0,0,449,450,5,51,0,0,450,451,5,8,0,0,451,452,5,51,0,0,452,453,
        5,21,0,0,453,454,3,26,13,0,454,455,3,26,13,0,455,456,5,52,0,0,456,
        457,5,52,0,0,457,93,1,0,0,0,458,459,5,51,0,0,459,466,5,27,0,0,460,
        467,3,94,47,0,461,467,3,96,48,0,462,467,3,92,46,0,463,467,3,42,21,
        0,464,467,3,72,36,0,465,467,3,70,35,0,466,460,1,0,0,0,466,461,1,
        0,0,0,466,462,1,0,0,0,466,463,1,0,0,0,466,464,1,0,0,0,466,465,1,
        0,0,0,467,468,1,0,0,0,468,466,1,0,0,0,468,469,1,0,0,0,469,470,1,
        0,0,0,470,471,5,52,0,0,471,95,1,0,0,0,472,473,5,51,0,0,473,480,5,
        28,0,0,474,481,3,94,47,0,475,481,3,96,48,0,476,481,3,92,46,0,477,
        481,3,42,21,0,478,481,3,72,36,0,479,481,3,70,35,0,480,474,1,0,0,
        0,480,475,1,0,0,0,480,476,1,0,0,0,480,477,1,0,0,0,480,478,1,0,0,
        0,480,479,1,0,0,0,481,482,1,0,0,0,482,480,1,0,0,0,482,483,1,0,0,
        0,483,484,1,0,0,0,484,485,5,52,0,0,485,97,1,0,0,0,486,487,5,51,0,
        0,487,489,5,27,0,0,488,490,3,88,44,0,489,488,1,0,0,0,490,491,1,0,
        0,0,491,489,1,0,0,0,491,492,1,0,0,0,492,493,1,0,0,0,493,494,5,52,
        0,0,494,99,1,0,0,0,495,496,5,51,0,0,496,498,5,27,0,0,497,499,3,90,
        45,0,498,497,1,0,0,0,499,500,1,0,0,0,500,498,1,0,0,0,500,501,1,0,
        0,0,501,502,1,0,0,0,502,503,5,52,0,0,503,101,1,0,0,0,504,505,5,51,
        0,0,505,506,5,52,0,0,506,103,1,0,0,0,507,514,3,94,47,0,508,514,3,
        96,48,0,509,514,3,42,21,0,510,514,3,72,36,0,511,514,3,70,35,0,512,
        514,3,102,51,0,513,507,1,0,0,0,513,508,1,0,0,0,513,509,1,0,0,0,513,
        510,1,0,0,0,513,511,1,0,0,0,513,512,1,0,0,0,514,105,1,0,0,0,515,
        518,3,88,44,0,516,518,3,98,49,0,517,515,1,0,0,0,517,516,1,0,0,0,
        518,107,1,0,0,0,519,520,5,51,0,0,520,524,5,27,0,0,521,525,3,110,
        55,0,522,525,3,112,56,0,523,525,3,114,57,0,524,521,1,0,0,0,524,522,
        1,0,0,0,524,523,1,0,0,0,525,526,1,0,0,0,526,524,1,0,0,0,526,527,
        1,0,0,0,527,528,1,0,0,0,528,529,5,52,0,0,529,109,1,0,0,0,530,531,
        5,51,0,0,531,536,5,29,0,0,532,537,3,42,21,0,533,537,3,72,36,0,534,
        537,3,70,35,0,535,537,3,94,47,0,536,532,1,0,0,0,536,533,1,0,0,0,
        536,534,1,0,0,0,536,535,1,0,0,0,537,538,1,0,0,0,538,539,5,52,0,0,
        539,111,1,0,0,0,540,541,5,51,0,0,541,546,5,30,0,0,542,547,3,42,21,
        0,543,547,3,72,36,0,544,547,3,70,35,0,545,547,3,94,47,0,546,542,
        1,0,0,0,546,543,1,0,0,0,546,544,1,0,0,0,546,545,1,0,0,0,547,548,
        1,0,0,0,548,549,5,52,0,0,549,113,1,0,0,0,550,551,5,51,0,0,551,556,
        5,31,0,0,552,557,3,42,21,0,553,557,3,72,36,0,554,557,3,70,35,0,555,
        557,3,94,47,0,556,552,1,0,0,0,556,553,1,0,0,0,556,554,1,0,0,0,556,
        555,1,0,0,0,557,558,1,0,0,0,558,559,5,52,0,0,559,115,1,0,0,0,560,
        566,3,108,54,0,561,566,3,110,55,0,562,566,3,112,56,0,563,566,3,114,
        57,0,564,566,3,102,51,0,565,560,1,0,0,0,565,561,1,0,0,0,565,562,
        1,0,0,0,565,563,1,0,0,0,565,564,1,0,0,0,566,117,1,0,0,0,567,568,
        5,51,0,0,568,572,5,29,0,0,569,573,3,42,21,0,570,573,3,74,37,0,571,
        573,3,98,49,0,572,569,1,0,0,0,572,570,1,0,0,0,572,571,1,0,0,0,573,
        574,1,0,0,0,574,575,5,52,0,0,575,119,1,0,0,0,576,577,5,51,0,0,577,
        581,5,32,0,0,578,582,3,42,21,0,579,582,3,74,37,0,580,582,3,98,49,
        0,581,578,1,0,0,0,581,579,1,0,0,0,581,580,1,0,0,0,582,583,1,0,0,
        0,583,584,5,52,0,0,584,121,1,0,0,0,585,586,5,51,0,0,586,590,5,31,
        0,0,587,591,3,42,21,0,588,591,3,74,37,0,589,591,3,98,49,0,590,587,
        1,0,0,0,590,588,1,0,0,0,590,589,1,0,0,0,591,592,1,0,0,0,592,593,
        5,52,0,0,593,123,1,0,0,0,594,598,3,118,59,0,595,598,3,120,60,0,596,
        598,3,122,61,0,597,594,1,0,0,0,597,595,1,0,0,0,597,596,1,0,0,0,598,
        125,1,0,0,0,599,600,5,51,0,0,600,602,5,27,0,0,601,603,3,124,62,0,
        602,601,1,0,0,0,603,604,1,0,0,0,604,602,1,0,0,0,604,605,1,0,0,0,
        605,606,1,0,0,0,606,607,5,52,0,0,607,127,1,0,0,0,608,611,3,124,62,
        0,609,611,3,126,63,0,610,608,1,0,0,0,610,609,1,0,0,0,611,129,1,0,
        0,0,612,616,5,51,0,0,613,615,3,28,14,0,614,613,1,0,0,0,615,618,1,
        0,0,0,616,614,1,0,0,0,616,617,1,0,0,0,617,619,1,0,0,0,618,616,1,
        0,0,0,619,620,5,52,0,0,620,131,1,0,0,0,621,622,5,54,0,0,622,133,
        1,0,0,0,623,624,5,33,0,0,624,625,3,130,65,0,625,135,1,0,0,0,626,
        627,5,34,0,0,627,628,3,104,52,0,628,137,1,0,0,0,629,630,5,35,0,0,
        630,631,3,116,58,0,631,139,1,0,0,0,632,633,5,36,0,0,633,634,3,106,
        53,0,634,141,1,0,0,0,635,636,5,36,0,0,636,637,3,128,64,0,637,143,
        1,0,0,0,638,639,5,37,0,0,639,640,3,68,34,0,640,145,1,0,0,0,641,642,
        5,51,0,0,642,643,5,38,0,0,643,645,3,132,66,0,644,646,3,134,67,0,
        645,644,1,0,0,0,645,646,1,0,0,0,646,648,1,0,0,0,647,649,3,136,68,
        0,648,647,1,0,0,0,648,649,1,0,0,0,649,650,1,0,0,0,650,651,3,140,
        70,0,651,652,5,52,0,0,652,147,1,0,0,0,653,654,5,51,0,0,654,655,5,
        39,0,0,655,657,3,132,66,0,656,658,3,134,67,0,657,656,1,0,0,0,657,
        658,1,0,0,0,658,660,1,0,0,0,659,661,3,144,72,0,660,659,1,0,0,0,660,
        661,1,0,0,0,661,663,1,0,0,0,662,664,3,138,69,0,663,662,1,0,0,0,663,
        664,1,0,0,0,664,665,1,0,0,0,665,666,3,142,71,0,666,667,5,52,0,0,
        667,149,1,0,0,0,668,669,5,51,0,0,669,670,5,40,0,0,670,672,3,132,
        66,0,671,673,3,134,67,0,672,671,1,0,0,0,672,673,1,0,0,0,673,675,
        1,0,0,0,674,676,3,136,68,0,675,674,1,0,0,0,675,676,1,0,0,0,676,677,
        1,0,0,0,677,678,3,140,70,0,678,679,5,52,0,0,679,151,1,0,0,0,680,
        681,5,51,0,0,681,682,5,41,0,0,682,684,3,132,66,0,683,685,3,134,67,
        0,684,683,1,0,0,0,684,685,1,0,0,0,685,687,1,0,0,0,686,688,3,136,
        68,0,687,686,1,0,0,0,687,688,1,0,0,0,688,689,1,0,0,0,689,690,3,140,
        70,0,690,691,5,52,0,0,691,153,1,0,0,0,692,693,5,51,0,0,693,694,5,
        42,0,0,694,695,5,51,0,0,695,698,5,27,0,0,696,699,3,84,42,0,697,699,
        3,86,43,0,698,696,1,0,0,0,698,697,1,0,0,0,699,700,1,0,0,0,700,698,
        1,0,0,0,700,701,1,0,0,0,701,702,1,0,0,0,702,703,5,52,0,0,703,704,
        5,52,0,0,704,155,1,0,0,0,705,706,5,51,0,0,706,707,5,1,0,0,707,708,
        3,158,79,0,708,710,3,160,80,0,709,711,3,162,81,0,710,709,1,0,0,0,
        710,711,1,0,0,0,711,712,1,0,0,0,712,713,3,164,82,0,713,715,3,166,
        83,0,714,716,3,168,84,0,715,714,1,0,0,0,715,716,1,0,0,0,716,717,
        1,0,0,0,717,718,5,52,0,0,718,157,1,0,0,0,719,720,5,51,0,0,720,721,
        5,43,0,0,721,722,5,54,0,0,722,723,5,52,0,0,723,159,1,0,0,0,724,725,
        5,51,0,0,725,726,5,44,0,0,726,727,5,54,0,0,727,728,5,52,0,0,728,
        161,1,0,0,0,729,730,5,51,0,0,730,734,5,45,0,0,731,733,3,18,9,0,732,
        731,1,0,0,0,733,736,1,0,0,0,734,732,1,0,0,0,734,735,1,0,0,0,735,
        737,1,0,0,0,736,734,1,0,0,0,737,738,5,52,0,0,738,163,1,0,0,0,739,
        740,5,51,0,0,740,743,5,46,0,0,741,744,3,36,18,0,742,744,3,66,33,
        0,743,741,1,0,0,0,743,742,1,0,0,0,744,745,1,0,0,0,745,743,1,0,0,
        0,745,746,1,0,0,0,746,747,1,0,0,0,747,748,5,52,0,0,748,165,1,0,0,
        0,749,750,5,51,0,0,750,751,5,47,0,0,751,752,3,104,52,0,752,753,5,
        52,0,0,753,167,1,0,0,0,754,755,5,51,0,0,755,756,5,48,0,0,756,757,
        7,4,0,0,757,758,3,62,31,0,758,759,5,52,0,0,759,169,1,0,0,0,68,172,
        178,181,184,187,190,196,198,202,219,232,237,245,252,262,276,283,
        289,296,304,317,324,333,349,356,399,403,424,435,443,447,466,468,
        480,482,491,500,513,517,524,526,536,546,556,565,572,581,590,597,
        604,610,616,645,648,657,660,663,672,675,684,687,698,700,710,715,
        734,743,745
    ]

class pddlParser ( Parser ):

    grammarFileName = "pddl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'define'", "'domain'", "':'", "':requirements'", 
                     "'-'", "':types'", "':constants'", "'not'", "':predicates'", 
                     "':functions'", "'assign'", "'increase'", "'decrease'", 
                     "'+'", "'*'", "'/'", "'>'", "'>='", "'<='", "'<'", 
                     "'='", "'#t'", "'?duration'", "'when'", "'forall'", 
                     "'exists'", "'and'", "'or'", "'at start'", "'over all'", 
                     "'at end'", "'overall'", "':parameters'", "':precondition'", 
                     "':condition'", "':effect'", "':duration'", "':action'", 
                     "':durative-action'", "':event'", "':process'", "':constraints'", 
                     "'problem'", "':domain'", "':objects'", "':init'", 
                     "':goal'", "':metric'", "'maximize'", "'minimize'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LP", "RP", 
                      "VAR", "NAME", "VARIABLE", "NUMBER", "WS" ]

    RULE_pddlDoc = 0
    RULE_domain = 1
    RULE_domainName = 2
    RULE_requireKey = 3
    RULE_requirements = 4
    RULE_parentType = 5
    RULE_typeName = 6
    RULE_type = 7
    RULE_types = 8
    RULE_typedObjects = 9
    RULE_constants = 10
    RULE_atomName = 11
    RULE_groundAtomParameter = 12
    RULE_liftedAtomParameter = 13
    RULE_typedAtomParameter = 14
    RULE_atomParameter = 15
    RULE_atom = 16
    RULE_typedAtom = 17
    RULE_positiveLiteral = 18
    RULE_typedPositiveLiteral = 19
    RULE_negativeLiteral = 20
    RULE_booleanLiteral = 21
    RULE_predicates = 22
    RULE_functions = 23
    RULE_modificator = 24
    RULE_operator = 25
    RULE_comparator = 26
    RULE_number = 27
    RULE_delta = 28
    RULE_constant = 29
    RULE_assignmentSide = 30
    RULE_operationSide = 31
    RULE_operation = 32
    RULE_assignment = 33
    RULE_durationAssignment = 34
    RULE_comparation = 35
    RULE_negatedComparation = 36
    RULE_modification = 37
    RULE_ceCond = 38
    RULE_ceEff = 39
    RULE_ce = 40
    RULE_forallEffect = 41
    RULE_forall = 42
    RULE_exists = 43
    RULE_effect = 44
    RULE_effectNoCes = 45
    RULE_inequality = 46
    RULE_andClause = 47
    RULE_orClause = 48
    RULE_andEffect = 49
    RULE_andEffectNoCes = 50
    RULE_emptyPrecondition = 51
    RULE_preconditions = 52
    RULE_effects = 53
    RULE_andDurClause = 54
    RULE_atStartPre = 55
    RULE_overAllPre = 56
    RULE_atEndPre = 57
    RULE_durativeConditions = 58
    RULE_atStartEffect = 59
    RULE_overAllEffect = 60
    RULE_atEndEffect = 61
    RULE_durativeEffect = 62
    RULE_andDurativeEffect = 63
    RULE_durativeEffects = 64
    RULE_parameters = 65
    RULE_opName = 66
    RULE_opParameters = 67
    RULE_opPrecondition = 68
    RULE_opDurativeCondition = 69
    RULE_opEffect = 70
    RULE_opDurativeEffect = 71
    RULE_opDuration = 72
    RULE_action = 73
    RULE_durativeAction = 74
    RULE_event = 75
    RULE_process = 76
    RULE_constraints = 77
    RULE_problem = 78
    RULE_problemName = 79
    RULE_problemDomain = 80
    RULE_objects = 81
    RULE_init = 82
    RULE_goal = 83
    RULE_metric = 84

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireKey", "requirements", 
                   "parentType", "typeName", "type", "types", "typedObjects", 
                   "constants", "atomName", "groundAtomParameter", "liftedAtomParameter", 
                   "typedAtomParameter", "atomParameter", "atom", "typedAtom", 
                   "positiveLiteral", "typedPositiveLiteral", "negativeLiteral", 
                   "booleanLiteral", "predicates", "functions", "modificator", 
                   "operator", "comparator", "number", "delta", "constant", 
                   "assignmentSide", "operationSide", "operation", "assignment", 
                   "durationAssignment", "comparation", "negatedComparation", 
                   "modification", "ceCond", "ceEff", "ce", "forallEffect", 
                   "forall", "exists", "effect", "effectNoCes", "inequality", 
                   "andClause", "orClause", "andEffect", "andEffectNoCes", 
                   "emptyPrecondition", "preconditions", "effects", "andDurClause", 
                   "atStartPre", "overAllPre", "atEndPre", "durativeConditions", 
                   "atStartEffect", "overAllEffect", "atEndEffect", "durativeEffect", 
                   "andDurativeEffect", "durativeEffects", "parameters", 
                   "opName", "opParameters", "opPrecondition", "opDurativeCondition", 
                   "opEffect", "opDurativeEffect", "opDuration", "action", 
                   "durativeAction", "event", "process", "constraints", 
                   "problem", "problemName", "problemDomain", "objects", 
                   "init", "goal", "metric" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    LP=51
    RP=52
    VAR=53
    NAME=54
    VARIABLE=55
    NUMBER=56
    WS=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PddlDocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(pddlParser.DomainContext,0)


        def problem(self):
            return self.getTypedRuleContext(pddlParser.ProblemContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_pddlDoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPddlDoc" ):
                listener.enterPddlDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPddlDoc" ):
                listener.exitPddlDoc(self)




    def pddlDoc(self):

        localctx = pddlParser.PddlDocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pddlDoc)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.problem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def domainName(self):
            return self.getTypedRuleContext(pddlParser.DomainNameContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def requirements(self):
            return self.getTypedRuleContext(pddlParser.RequirementsContext,0)


        def types(self):
            return self.getTypedRuleContext(pddlParser.TypesContext,0)


        def constants(self):
            return self.getTypedRuleContext(pddlParser.ConstantsContext,0)


        def predicates(self):
            return self.getTypedRuleContext(pddlParser.PredicatesContext,0)


        def functions(self):
            return self.getTypedRuleContext(pddlParser.FunctionsContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ActionContext)
            else:
                return self.getTypedRuleContext(pddlParser.ActionContext,i)


        def durativeAction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.DurativeActionContext)
            else:
                return self.getTypedRuleContext(pddlParser.DurativeActionContext,i)


        def event(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.EventContext)
            else:
                return self.getTypedRuleContext(pddlParser.EventContext,i)


        def process(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ProcessContext)
            else:
                return self.getTypedRuleContext(pddlParser.ProcessContext,i)


        def constraints(self):
            return self.getTypedRuleContext(pddlParser.ConstraintsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)




    def domain(self):

        localctx = pddlParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(pddlParser.LP)
            self.state = 175
            self.match(pddlParser.T__0)
            self.state = 176
            self.domainName()
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 177
                self.requirements()


            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 180
                self.types()


            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 183
                self.constants()


            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 186
                self.predicates()


            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 189
                self.functions()


            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 196
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 192
                        self.action()
                        pass

                    elif la_ == 2:
                        self.state = 193
                        self.durativeAction()
                        pass

                    elif la_ == 3:
                        self.state = 194
                        self.event()
                        pass

                    elif la_ == 4:
                        self.state = 195
                        self.process()
                        pass

             
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 201
                self.constraints()


            self.state = 204
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_domainName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainName" ):
                listener.enterDomainName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainName" ):
                listener.exitDomainName(self)




    def domainName(self):

        localctx = pddlParser.DomainNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domainName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(pddlParser.LP)
            self.state = 207
            self.match(pddlParser.T__1)
            self.state = 208
            self.match(pddlParser.NAME)
            self.state = 209
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_requireKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireKey" ):
                listener.enterRequireKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireKey" ):
                listener.exitRequireKey(self)




    def requireKey(self):

        localctx = pddlParser.RequireKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requireKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(pddlParser.T__2)
            self.state = 212
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def requireKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.RequireKeyContext)
            else:
                return self.getTypedRuleContext(pddlParser.RequireKeyContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_requirements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirements" ):
                listener.enterRequirements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirements" ):
                listener.exitRequirements(self)




    def requirements(self):

        localctx = pddlParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(pddlParser.LP)
            self.state = 215
            self.match(pddlParser.T__3)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 216
                self.requireKey()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_parentType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentType" ):
                listener.enterParentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentType" ):
                listener.exitParentType(self)




    def parentType(self):

        localctx = pddlParser.ParentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(pddlParser.T__4)
            self.state = 225
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = pddlParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.parent = None # ParentTypeContext

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypeNameContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypeNameContext,i)


        def parentType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ParentTypeContext)
            else:
                return self.getTypedRuleContext(pddlParser.ParentTypeContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = pddlParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 229
                    self.typeName()

                else:
                    raise NoViableAltException(self)
                self.state = 232 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 234
                localctx.parent = self.parentType()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypeContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypeContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)




    def types(self):

        localctx = pddlParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(pddlParser.LP)
            self.state = 241
            self.match(pddlParser.T__5)
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.type_()
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==54):
                    break

            self.state = 247
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedObjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def groundAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.GroundAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.GroundAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedObjects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedObjects" ):
                listener.enterTypedObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedObjects" ):
                listener.exitTypedObjects(self)




    def typedObjects(self):

        localctx = pddlParser.TypedObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typedObjects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 249
                self.groundAtomParameter()
                self.state = 252 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==54):
                    break

            self.state = 254
            self.match(pddlParser.T__4)
            self.state = 255
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedObjects(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedObjectsContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedObjectsContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_constants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstants" ):
                listener.enterConstants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstants" ):
                listener.exitConstants(self)




    def constants(self):

        localctx = pddlParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(pddlParser.LP)
            self.state = 258
            self.match(pddlParser.T__6)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 259
                self.typedObjects()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 265
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_atomName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomName" ):
                listener.enterAtomName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomName" ):
                listener.exitAtomName(self)




    def atomName(self):

        localctx = pddlParser.AtomNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atomName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroundAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_groundAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundAtomParameter" ):
                listener.enterGroundAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundAtomParameter" ):
                listener.exitGroundAtomParameter(self)




    def groundAtomParameter(self):

        localctx = pddlParser.GroundAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_groundAtomParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiftedAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(pddlParser.VAR, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_liftedAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiftedAtomParameter" ):
                listener.enterLiftedAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiftedAtomParameter" ):
                listener.exitLiftedAtomParameter(self)




    def liftedAtomParameter(self):

        localctx = pddlParser.LiftedAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_liftedAtomParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.atomsType = None # TypeNameContext

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def liftedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.LiftedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedAtomParameter" ):
                listener.enterTypedAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedAtomParameter" ):
                listener.exitTypedAtomParameter(self)




    def typedAtomParameter(self):

        localctx = pddlParser.TypedAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typedAtomParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 273
                self.liftedAtomParameter()
                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53 or _la==54):
                    break

            self.state = 278
            self.match(pddlParser.T__4)
            self.state = 279
            localctx.atomsType = self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liftedAtomParameter(self):
            return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,0)


        def groundAtomParameter(self):
            return self.getTypedRuleContext(pddlParser.GroundAtomParameterContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomParameter" ):
                listener.enterAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomParameter" ):
                listener.exitAtomParameter(self)




    def atomParameter(self):

        localctx = pddlParser.AtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atomParameter)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.liftedAtomParameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.groundAtomParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomName(self):
            return self.getTypedRuleContext(pddlParser.AtomNameContext,0)


        def atomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.AtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = pddlParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.atomName()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53 or _la==54:
                self.state = 286
                self.atomParameter()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomName(self):
            return self.getTypedRuleContext(pddlParser.AtomNameContext,0)


        def typedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedAtom" ):
                listener.enterTypedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedAtom" ):
                listener.exitTypedAtom(self)




    def typedAtom(self):

        localctx = pddlParser.TypedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typedAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.atomName()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53 or _la==54:
                self.state = 293
                self.typedAtomParameter()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositiveLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None # LiftedAtomParameterContext

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def atom(self):
            return self.getTypedRuleContext(pddlParser.AtomContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def liftedAtomParameter(self):
            return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_positiveLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositiveLiteral" ):
                listener.enterPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositiveLiteral" ):
                listener.exitPositiveLiteral(self)




    def positiveLiteral(self):

        localctx = pddlParser.PositiveLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_positiveLiteral)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(pddlParser.LP)
                self.state = 300
                self.atom()
                self.state = 301
                self.match(pddlParser.RP)
                pass
            elif token in [53, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                localctx.param = self.liftedAtomParameter()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedPositiveLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def typedAtom(self):
            return self.getTypedRuleContext(pddlParser.TypedAtomContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_typedPositiveLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedPositiveLiteral" ):
                listener.enterTypedPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedPositiveLiteral" ):
                listener.exitTypedPositiveLiteral(self)




    def typedPositiveLiteral(self):

        localctx = pddlParser.TypedPositiveLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typedPositiveLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(pddlParser.LP)
            self.state = 307
            self.typedAtom()
            self.state = 308
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegativeLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_negativeLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativeLiteral" ):
                listener.enterNegativeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativeLiteral" ):
                listener.exitNegativeLiteral(self)




    def negativeLiteral(self):

        localctx = pddlParser.NegativeLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_negativeLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(pddlParser.LP)
            self.state = 311
            self.match(pddlParser.T__7)
            self.state = 312
            self.positiveLiteral()
            self.state = 313
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def negativeLiteral(self):
            return self.getTypedRuleContext(pddlParser.NegativeLiteralContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = pddlParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_booleanLiteral)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.positiveLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.negativeLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedPositiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedPositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedPositiveLiteralContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_predicates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicates" ):
                listener.enterPredicates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicates" ):
                listener.exitPredicates(self)




    def predicates(self):

        localctx = pddlParser.PredicatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_predicates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(pddlParser.LP)
            self.state = 320
            self.match(pddlParser.T__8)
            self.state = 322 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 321
                self.typedPositiveLiteral()
                self.state = 324 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 326
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedPositiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedPositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedPositiveLiteralContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = pddlParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(pddlParser.LP)
            self.state = 329
            self.match(pddlParser.T__9)
            self.state = 331 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 330
                self.typedPositiveLiteral()
                self.state = 333 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 335
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModificatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_modificator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModificator" ):
                listener.enterModificator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModificator" ):
                listener.exitModificator(self)




    def modificator(self):

        localctx = pddlParser.ModificatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_modificator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = pddlParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = pddlParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4063232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(pddlParser.NUMBER, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = pddlParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(pddlParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeltaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_delta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelta" ):
                listener.enterDelta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelta" ):
                listener.exitDelta(self)




    def delta(self):

        localctx = pddlParser.DeltaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_delta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(pddlParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(pddlParser.NumberContext,0)


        def delta(self):
            return self.getTypedRuleContext(pddlParser.DeltaContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = pddlParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_constant)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.number()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.delta()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(pddlParser.NumberContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_assignmentSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentSide" ):
                listener.enterAssignmentSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentSide" ):
                listener.exitAssignmentSide(self)




    def assignmentSide(self):

        localctx = pddlParser.AssignmentSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignmentSide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(pddlParser.OperationContext,0)


        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def constant(self):
            return self.getTypedRuleContext(pddlParser.ConstantContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_operationSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationSide" ):
                listener.enterOperationSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationSide" ):
                listener.exitOperationSide(self)




    def operationSide(self):

        localctx = pddlParser.OperationSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operationSide)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.positiveLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def operator(self):
            return self.getTypedRuleContext(pddlParser.OperatorContext,0)


        def operationSide(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OperationSideContext)
            else:
                return self.getTypedRuleContext(pddlParser.OperationSideContext,i)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = pddlParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(pddlParser.LP)
            self.state = 359
            self.operator()
            self.state = 360
            self.operationSide()
            self.state = 361
            self.operationSide()
            self.state = 362
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def assignmentSide(self):
            return self.getTypedRuleContext(pddlParser.AssignmentSideContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = pddlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(pddlParser.LP)
            self.state = 365
            self.match(pddlParser.T__20)
            self.state = 366
            self.positiveLiteral()
            self.state = 367
            self.assignmentSide()
            self.state = 368
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperationSideContext

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def operationSide(self):
            return self.getTypedRuleContext(pddlParser.OperationSideContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_durationAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurationAssignment" ):
                listener.enterDurationAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurationAssignment" ):
                listener.exitDurationAssignment(self)




    def durationAssignment(self):

        localctx = pddlParser.DurationAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_durationAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(pddlParser.LP)
            self.state = 371
            self.match(pddlParser.T__20)
            self.state = 372
            self.match(pddlParser.T__22)
            self.state = 373
            localctx.op = self.operationSide()
            self.state = 374
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def comparator(self):
            return self.getTypedRuleContext(pddlParser.ComparatorContext,0)


        def operationSide(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OperationSideContext)
            else:
                return self.getTypedRuleContext(pddlParser.OperationSideContext,i)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_comparation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparation" ):
                listener.enterComparation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparation" ):
                listener.exitComparation(self)




    def comparation(self):

        localctx = pddlParser.ComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_comparation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(pddlParser.LP)
            self.state = 377
            self.comparator()
            self.state = 378
            self.operationSide()
            self.state = 379
            self.operationSide()
            self.state = 380
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegatedComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_negatedComparation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegatedComparation" ):
                listener.enterNegatedComparation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegatedComparation" ):
                listener.exitNegatedComparation(self)




    def negatedComparation(self):

        localctx = pddlParser.NegatedComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_negatedComparation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(pddlParser.LP)
            self.state = 383
            self.match(pddlParser.T__7)
            self.state = 384
            self.comparation()
            self.state = 385
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def modificator(self):
            return self.getTypedRuleContext(pddlParser.ModificatorContext,0)


        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def operationSide(self):
            return self.getTypedRuleContext(pddlParser.OperationSideContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_modification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModification" ):
                listener.enterModification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModification" ):
                listener.exitModification(self)




    def modification(self):

        localctx = pddlParser.ModificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_modification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(pddlParser.LP)
            self.state = 388
            self.modificator()
            self.state = 389
            self.positiveLiteral()
            self.state = 390
            self.operationSide()
            self.state = 391
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CeCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def orClause(self):
            return self.getTypedRuleContext(pddlParser.OrClauseContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def negatedComparation(self):
            return self.getTypedRuleContext(pddlParser.NegatedComparationContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def emptyPrecondition(self):
            return self.getTypedRuleContext(pddlParser.EmptyPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_ceCond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeCond" ):
                listener.enterCeCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeCond" ):
                listener.exitCeCond(self)




    def ceCond(self):

        localctx = pddlParser.CeCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ceCond)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.andClause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.orClause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.booleanLiteral()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.negatedComparation()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.comparation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
                self.emptyPrecondition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CeEffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effectNoCes(self):
            return self.getTypedRuleContext(pddlParser.EffectNoCesContext,0)


        def andEffectNoCes(self):
            return self.getTypedRuleContext(pddlParser.AndEffectNoCesContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_ceEff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeEff" ):
                listener.enterCeEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeEff" ):
                listener.exitCeEff(self)




    def ceEff(self):

        localctx = pddlParser.CeEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ceEff)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.effectNoCes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.andEffectNoCes()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # CeCondContext
            self.eff = None # CeEffContext

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def ceCond(self):
            return self.getTypedRuleContext(pddlParser.CeCondContext,0)


        def ceEff(self):
            return self.getTypedRuleContext(pddlParser.CeEffContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_ce

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCe" ):
                listener.enterCe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCe" ):
                listener.exitCe(self)




    def ce(self):

        localctx = pddlParser.CeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_ce)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(pddlParser.LP)
            self.state = 406
            self.match(pddlParser.T__23)
            self.state = 407
            localctx.cond = self.ceCond()
            self.state = 408
            localctx.eff = self.ceEff()
            self.state = 409
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForallEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def parameters(self):
            return self.getTypedRuleContext(pddlParser.ParametersContext,0)


        def ce(self):
            return self.getTypedRuleContext(pddlParser.CeContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_forallEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForallEffect" ):
                listener.enterForallEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForallEffect" ):
                listener.exitForallEffect(self)




    def forallEffect(self):

        localctx = pddlParser.ForallEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forallEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(pddlParser.LP)
            self.state = 412
            self.match(pddlParser.T__24)
            self.state = 413
            self.parameters()
            self.state = 414
            self.ce()
            self.state = 415
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def parameters(self):
            return self.getTypedRuleContext(pddlParser.ParametersContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def forall(self):
            return self.getTypedRuleContext(pddlParser.ForallContext,0)


        def exists(self):
            return self.getTypedRuleContext(pddlParser.ExistsContext,0)


        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def orClause(self):
            return self.getTypedRuleContext(pddlParser.OrClauseContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_forall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForall" ):
                listener.enterForall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForall" ):
                listener.exitForall(self)




    def forall(self):

        localctx = pddlParser.ForallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_forall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(pddlParser.LP)
            self.state = 418
            self.match(pddlParser.T__24)
            self.state = 419
            self.parameters()
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 420
                self.forall()
                pass

            elif la_ == 2:
                self.state = 421
                self.exists()
                pass

            elif la_ == 3:
                self.state = 422
                self.andClause()
                pass

            elif la_ == 4:
                self.state = 423
                self.orClause()
                pass


            self.state = 426
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExistsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def parameters(self):
            return self.getTypedRuleContext(pddlParser.ParametersContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def forall(self):
            return self.getTypedRuleContext(pddlParser.ForallContext,0)


        def exists(self):
            return self.getTypedRuleContext(pddlParser.ExistsContext,0)


        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def orClause(self):
            return self.getTypedRuleContext(pddlParser.OrClauseContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_exists

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExists" ):
                listener.enterExists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExists" ):
                listener.exitExists(self)




    def exists(self):

        localctx = pddlParser.ExistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exists)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(pddlParser.LP)
            self.state = 429
            self.match(pddlParser.T__25)
            self.state = 430
            self.parameters()
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 431
                self.forall()
                pass

            elif la_ == 2:
                self.state = 432
                self.exists()
                pass

            elif la_ == 3:
                self.state = 433
                self.andClause()
                pass

            elif la_ == 4:
                self.state = 434
                self.orClause()
                pass


            self.state = 437
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def ce(self):
            return self.getTypedRuleContext(pddlParser.CeContext,0)


        def forallEffect(self):
            return self.getTypedRuleContext(pddlParser.ForallEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect" ):
                listener.enterEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect" ):
                listener.exitEffect(self)




    def effect(self):

        localctx = pddlParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_effect)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.modification()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.ce()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.forallEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectNoCesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effectNoCes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffectNoCes" ):
                listener.enterEffectNoCes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffectNoCes" ):
                listener.exitEffectNoCes(self)




    def effectNoCes(self):

        localctx = pddlParser.EffectNoCesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_effectNoCes)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.modification()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InequalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.a1 = None # LiftedAtomParameterContext
            self.a2 = None # LiftedAtomParameterContext

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def liftedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.LiftedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_inequality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality" ):
                listener.enterInequality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality" ):
                listener.exitInequality(self)




    def inequality(self):

        localctx = pddlParser.InequalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_inequality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(pddlParser.LP)
            self.state = 450
            self.match(pddlParser.T__7)
            self.state = 451
            self.match(pddlParser.LP)
            self.state = 452
            self.match(pddlParser.T__20)
            self.state = 453
            localctx.a1 = self.liftedAtomParameter()
            self.state = 454
            localctx.a2 = self.liftedAtomParameter()
            self.state = 455
            self.match(pddlParser.RP)
            self.state = 456
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def andClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AndClauseContext)
            else:
                return self.getTypedRuleContext(pddlParser.AndClauseContext,i)


        def orClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OrClauseContext)
            else:
                return self.getTypedRuleContext(pddlParser.OrClauseContext,i)


        def inequality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.InequalityContext)
            else:
                return self.getTypedRuleContext(pddlParser.InequalityContext,i)


        def booleanLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.BooleanLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,i)


        def negatedComparation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.NegatedComparationContext)
            else:
                return self.getTypedRuleContext(pddlParser.NegatedComparationContext,i)


        def comparation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ComparationContext)
            else:
                return self.getTypedRuleContext(pddlParser.ComparationContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndClause" ):
                listener.enterAndClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndClause" ):
                listener.exitAndClause(self)




    def andClause(self):

        localctx = pddlParser.AndClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_andClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(pddlParser.LP)
            self.state = 459
            self.match(pddlParser.T__26)
            self.state = 466 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 466
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 460
                    self.andClause()
                    pass

                elif la_ == 2:
                    self.state = 461
                    self.orClause()
                    pass

                elif la_ == 3:
                    self.state = 462
                    self.inequality()
                    pass

                elif la_ == 4:
                    self.state = 463
                    self.booleanLiteral()
                    pass

                elif la_ == 5:
                    self.state = 464
                    self.negatedComparation()
                    pass

                elif la_ == 6:
                    self.state = 465
                    self.comparation()
                    pass


                self.state = 468 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 470
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def andClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AndClauseContext)
            else:
                return self.getTypedRuleContext(pddlParser.AndClauseContext,i)


        def orClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OrClauseContext)
            else:
                return self.getTypedRuleContext(pddlParser.OrClauseContext,i)


        def inequality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.InequalityContext)
            else:
                return self.getTypedRuleContext(pddlParser.InequalityContext,i)


        def booleanLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.BooleanLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,i)


        def negatedComparation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.NegatedComparationContext)
            else:
                return self.getTypedRuleContext(pddlParser.NegatedComparationContext,i)


        def comparation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ComparationContext)
            else:
                return self.getTypedRuleContext(pddlParser.ComparationContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_orClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrClause" ):
                listener.enterOrClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrClause" ):
                listener.exitOrClause(self)




    def orClause(self):

        localctx = pddlParser.OrClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_orClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(pddlParser.LP)
            self.state = 473
            self.match(pddlParser.T__27)
            self.state = 480 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 480
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 474
                    self.andClause()
                    pass

                elif la_ == 2:
                    self.state = 475
                    self.orClause()
                    pass

                elif la_ == 3:
                    self.state = 476
                    self.inequality()
                    pass

                elif la_ == 4:
                    self.state = 477
                    self.booleanLiteral()
                    pass

                elif la_ == 5:
                    self.state = 478
                    self.negatedComparation()
                    pass

                elif la_ == 6:
                    self.state = 479
                    self.comparation()
                    pass


                self.state = 482 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 484
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.EffectContext)
            else:
                return self.getTypedRuleContext(pddlParser.EffectContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndEffect" ):
                listener.enterAndEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndEffect" ):
                listener.exitAndEffect(self)




    def andEffect(self):

        localctx = pddlParser.AndEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_andEffect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(pddlParser.LP)
            self.state = 487
            self.match(pddlParser.T__26)
            self.state = 489 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 488
                self.effect()
                self.state = 491 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 493
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndEffectNoCesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def effectNoCes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.EffectNoCesContext)
            else:
                return self.getTypedRuleContext(pddlParser.EffectNoCesContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andEffectNoCes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndEffectNoCes" ):
                listener.enterAndEffectNoCes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndEffectNoCes" ):
                listener.exitAndEffectNoCes(self)




    def andEffectNoCes(self):

        localctx = pddlParser.AndEffectNoCesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_andEffectNoCes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(pddlParser.LP)
            self.state = 496
            self.match(pddlParser.T__26)
            self.state = 498 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 497
                self.effectNoCes()
                self.state = 500 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 502
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_emptyPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyPrecondition" ):
                listener.enterEmptyPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyPrecondition" ):
                listener.exitEmptyPrecondition(self)




    def emptyPrecondition(self):

        localctx = pddlParser.EmptyPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_emptyPrecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(pddlParser.LP)
            self.state = 505
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreconditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def orClause(self):
            return self.getTypedRuleContext(pddlParser.OrClauseContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def negatedComparation(self):
            return self.getTypedRuleContext(pddlParser.NegatedComparationContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def emptyPrecondition(self):
            return self.getTypedRuleContext(pddlParser.EmptyPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_preconditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreconditions" ):
                listener.enterPreconditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreconditions" ):
                listener.exitPreconditions(self)




    def preconditions(self):

        localctx = pddlParser.PreconditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_preconditions)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.andClause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.orClause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.booleanLiteral()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self.negatedComparation()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 511
                self.comparation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 512
                self.emptyPrecondition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effect(self):
            return self.getTypedRuleContext(pddlParser.EffectContext,0)


        def andEffect(self):
            return self.getTypedRuleContext(pddlParser.AndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffects" ):
                listener.enterEffects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffects" ):
                listener.exitEffects(self)




    def effects(self):

        localctx = pddlParser.EffectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_effects)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.effect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.andEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndDurClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def atStartPre(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AtStartPreContext)
            else:
                return self.getTypedRuleContext(pddlParser.AtStartPreContext,i)


        def overAllPre(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OverAllPreContext)
            else:
                return self.getTypedRuleContext(pddlParser.OverAllPreContext,i)


        def atEndPre(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AtEndPreContext)
            else:
                return self.getTypedRuleContext(pddlParser.AtEndPreContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andDurClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndDurClause" ):
                listener.enterAndDurClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndDurClause" ):
                listener.exitAndDurClause(self)




    def andDurClause(self):

        localctx = pddlParser.AndDurClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_andDurClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(pddlParser.LP)
            self.state = 520
            self.match(pddlParser.T__26)
            self.state = 524 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 524
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 521
                    self.atStartPre()
                    pass

                elif la_ == 2:
                    self.state = 522
                    self.overAllPre()
                    pass

                elif la_ == 3:
                    self.state = 523
                    self.atEndPre()
                    pass


                self.state = 526 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 528
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtStartPreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def negatedComparation(self):
            return self.getTypedRuleContext(pddlParser.NegatedComparationContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atStartPre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtStartPre" ):
                listener.enterAtStartPre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtStartPre" ):
                listener.exitAtStartPre(self)




    def atStartPre(self):

        localctx = pddlParser.AtStartPreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_atStartPre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(pddlParser.LP)
            self.state = 531
            self.match(pddlParser.T__28)
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 532
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 533
                self.negatedComparation()
                pass

            elif la_ == 3:
                self.state = 534
                self.comparation()
                pass

            elif la_ == 4:
                self.state = 535
                self.andClause()
                pass


            self.state = 538
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OverAllPreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def negatedComparation(self):
            return self.getTypedRuleContext(pddlParser.NegatedComparationContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_overAllPre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverAllPre" ):
                listener.enterOverAllPre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverAllPre" ):
                listener.exitOverAllPre(self)




    def overAllPre(self):

        localctx = pddlParser.OverAllPreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_overAllPre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(pddlParser.LP)
            self.state = 541
            self.match(pddlParser.T__29)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 542
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 543
                self.negatedComparation()
                pass

            elif la_ == 3:
                self.state = 544
                self.comparation()
                pass

            elif la_ == 4:
                self.state = 545
                self.andClause()
                pass


            self.state = 548
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtEndPreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def negatedComparation(self):
            return self.getTypedRuleContext(pddlParser.NegatedComparationContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def andClause(self):
            return self.getTypedRuleContext(pddlParser.AndClauseContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atEndPre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtEndPre" ):
                listener.enterAtEndPre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtEndPre" ):
                listener.exitAtEndPre(self)




    def atEndPre(self):

        localctx = pddlParser.AtEndPreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_atEndPre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(pddlParser.LP)
            self.state = 551
            self.match(pddlParser.T__30)
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 552
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 553
                self.negatedComparation()
                pass

            elif la_ == 3:
                self.state = 554
                self.comparation()
                pass

            elif la_ == 4:
                self.state = 555
                self.andClause()
                pass


            self.state = 558
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurativeConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andDurClause(self):
            return self.getTypedRuleContext(pddlParser.AndDurClauseContext,0)


        def atStartPre(self):
            return self.getTypedRuleContext(pddlParser.AtStartPreContext,0)


        def overAllPre(self):
            return self.getTypedRuleContext(pddlParser.OverAllPreContext,0)


        def atEndPre(self):
            return self.getTypedRuleContext(pddlParser.AtEndPreContext,0)


        def emptyPrecondition(self):
            return self.getTypedRuleContext(pddlParser.EmptyPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_durativeConditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurativeConditions" ):
                listener.enterDurativeConditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurativeConditions" ):
                listener.exitDurativeConditions(self)




    def durativeConditions(self):

        localctx = pddlParser.DurativeConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_durativeConditions)
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.andDurClause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.atStartPre()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 562
                self.overAllPre()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 563
                self.atEndPre()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 564
                self.emptyPrecondition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtStartEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def andEffect(self):
            return self.getTypedRuleContext(pddlParser.AndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atStartEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtStartEffect" ):
                listener.enterAtStartEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtStartEffect" ):
                listener.exitAtStartEffect(self)




    def atStartEffect(self):

        localctx = pddlParser.AtStartEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_atStartEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(pddlParser.LP)
            self.state = 568
            self.match(pddlParser.T__28)
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 569
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 570
                self.modification()
                pass

            elif la_ == 3:
                self.state = 571
                self.andEffect()
                pass


            self.state = 574
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OverAllEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def andEffect(self):
            return self.getTypedRuleContext(pddlParser.AndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_overAllEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverAllEffect" ):
                listener.enterOverAllEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverAllEffect" ):
                listener.exitOverAllEffect(self)




    def overAllEffect(self):

        localctx = pddlParser.OverAllEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_overAllEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(pddlParser.LP)
            self.state = 577
            self.match(pddlParser.T__31)
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 578
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 579
                self.modification()
                pass

            elif la_ == 3:
                self.state = 580
                self.andEffect()
                pass


            self.state = 583
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtEndEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def andEffect(self):
            return self.getTypedRuleContext(pddlParser.AndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atEndEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtEndEffect" ):
                listener.enterAtEndEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtEndEffect" ):
                listener.exitAtEndEffect(self)




    def atEndEffect(self):

        localctx = pddlParser.AtEndEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_atEndEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(pddlParser.LP)
            self.state = 586
            self.match(pddlParser.T__30)
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 587
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.state = 588
                self.modification()
                pass

            elif la_ == 3:
                self.state = 589
                self.andEffect()
                pass


            self.state = 592
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurativeEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atStartEffect(self):
            return self.getTypedRuleContext(pddlParser.AtStartEffectContext,0)


        def overAllEffect(self):
            return self.getTypedRuleContext(pddlParser.OverAllEffectContext,0)


        def atEndEffect(self):
            return self.getTypedRuleContext(pddlParser.AtEndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_durativeEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurativeEffect" ):
                listener.enterDurativeEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurativeEffect" ):
                listener.exitDurativeEffect(self)




    def durativeEffect(self):

        localctx = pddlParser.DurativeEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_durativeEffect)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.atStartEffect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
                self.overAllEffect()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 596
                self.atEndEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndDurativeEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def durativeEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.DurativeEffectContext)
            else:
                return self.getTypedRuleContext(pddlParser.DurativeEffectContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andDurativeEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndDurativeEffect" ):
                listener.enterAndDurativeEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndDurativeEffect" ):
                listener.exitAndDurativeEffect(self)




    def andDurativeEffect(self):

        localctx = pddlParser.AndDurativeEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_andDurativeEffect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(pddlParser.LP)
            self.state = 600
            self.match(pddlParser.T__26)
            self.state = 602 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 601
                self.durativeEffect()
                self.state = 604 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 606
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurativeEffectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def durativeEffect(self):
            return self.getTypedRuleContext(pddlParser.DurativeEffectContext,0)


        def andDurativeEffect(self):
            return self.getTypedRuleContext(pddlParser.AndDurativeEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_durativeEffects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurativeEffects" ):
                listener.enterDurativeEffects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurativeEffects" ):
                listener.exitDurativeEffects(self)




    def durativeEffects(self):

        localctx = pddlParser.DurativeEffectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_durativeEffects)
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.durativeEffect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
                self.andDurativeEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = pddlParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(pddlParser.LP)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53 or _la==54:
                self.state = 613
                self.typedAtomParameter()
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 619
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_opName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpName" ):
                listener.enterOpName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpName" ):
                listener.exitOpName(self)




    def opName(self):

        localctx = pddlParser.OpNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_opName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(pddlParser.ParametersContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpParameters" ):
                listener.enterOpParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpParameters" ):
                listener.exitOpParameters(self)




    def opParameters(self):

        localctx = pddlParser.OpParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_opParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(pddlParser.T__32)
            self.state = 624
            self.parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preconditions(self):
            return self.getTypedRuleContext(pddlParser.PreconditionsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpPrecondition" ):
                listener.enterOpPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpPrecondition" ):
                listener.exitOpPrecondition(self)




    def opPrecondition(self):

        localctx = pddlParser.OpPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_opPrecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(pddlParser.T__33)
            self.state = 627
            self.preconditions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpDurativeConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.c = None # DurativeConditionsContext

        def durativeConditions(self):
            return self.getTypedRuleContext(pddlParser.DurativeConditionsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opDurativeCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpDurativeCondition" ):
                listener.enterOpDurativeCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpDurativeCondition" ):
                listener.exitOpDurativeCondition(self)




    def opDurativeCondition(self):

        localctx = pddlParser.OpDurativeConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_opDurativeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(pddlParser.T__34)
            self.state = 630
            localctx.c = self.durativeConditions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effects(self):
            return self.getTypedRuleContext(pddlParser.EffectsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpEffect" ):
                listener.enterOpEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpEffect" ):
                listener.exitOpEffect(self)




    def opEffect(self):

        localctx = pddlParser.OpEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_opEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(pddlParser.T__35)
            self.state = 633
            self.effects()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpDurativeEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # DurativeEffectsContext

        def durativeEffects(self):
            return self.getTypedRuleContext(pddlParser.DurativeEffectsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opDurativeEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpDurativeEffect" ):
                listener.enterOpDurativeEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpDurativeEffect" ):
                listener.exitOpDurativeEffect(self)




    def opDurativeEffect(self):

        localctx = pddlParser.OpDurativeEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_opDurativeEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(pddlParser.T__35)
            self.state = 636
            localctx.e = self.durativeEffects()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpDurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def durationAssignment(self):
            return self.getTypedRuleContext(pddlParser.DurationAssignmentContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opDuration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpDuration" ):
                listener.enterOpDuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpDuration" ):
                listener.exitOpDuration(self)




    def opDuration(self):

        localctx = pddlParser.OpDurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_opDuration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(pddlParser.T__36)
            self.state = 639
            self.durationAssignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = pddlParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(pddlParser.LP)
            self.state = 642
            self.match(pddlParser.T__37)
            self.state = 643
            self.opName()
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 644
                self.opParameters()


            self.state = 648
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 647
                self.opPrecondition()


            self.state = 650
            self.opEffect()
            self.state = 651
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurativeActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opDurativeEffect(self):
            return self.getTypedRuleContext(pddlParser.OpDurativeEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opDuration(self):
            return self.getTypedRuleContext(pddlParser.OpDurationContext,0)


        def opDurativeCondition(self):
            return self.getTypedRuleContext(pddlParser.OpDurativeConditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_durativeAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurativeAction" ):
                listener.enterDurativeAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurativeAction" ):
                listener.exitDurativeAction(self)




    def durativeAction(self):

        localctx = pddlParser.DurativeActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_durativeAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(pddlParser.LP)
            self.state = 654
            self.match(pddlParser.T__38)
            self.state = 655
            self.opName()
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 656
                self.opParameters()


            self.state = 660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 659
                self.opDuration()


            self.state = 663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 662
                self.opDurativeCondition()


            self.state = 665
            self.opDurativeEffect()
            self.state = 666
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = pddlParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(pddlParser.LP)
            self.state = 669
            self.match(pddlParser.T__39)
            self.state = 670
            self.opName()
            self.state = 672
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 671
                self.opParameters()


            self.state = 675
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 674
                self.opPrecondition()


            self.state = 677
            self.opEffect()
            self.state = 678
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_process

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcess" ):
                listener.enterProcess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcess" ):
                listener.exitProcess(self)




    def process(self):

        localctx = pddlParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(pddlParser.LP)
            self.state = 681
            self.match(pddlParser.T__40)
            self.state = 682
            self.opName()
            self.state = 684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 683
                self.opParameters()


            self.state = 687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 686
                self.opPrecondition()


            self.state = 689
            self.opEffect()
            self.state = 690
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def forall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ForallContext)
            else:
                return self.getTypedRuleContext(pddlParser.ForallContext,i)


        def exists(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ExistsContext)
            else:
                return self.getTypedRuleContext(pddlParser.ExistsContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraints" ):
                listener.enterConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraints" ):
                listener.exitConstraints(self)




    def constraints(self):

        localctx = pddlParser.ConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_constraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self.match(pddlParser.LP)
            self.state = 693
            self.match(pddlParser.T__41)
            self.state = 694
            self.match(pddlParser.LP)
            self.state = 695
            self.match(pddlParser.T__26)
            self.state = 698 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 698
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 696
                    self.forall()
                    pass

                elif la_ == 2:
                    self.state = 697
                    self.exists()
                    pass


                self.state = 700 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 702
            self.match(pddlParser.RP)
            self.state = 703
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def problemName(self):
            return self.getTypedRuleContext(pddlParser.ProblemNameContext,0)


        def problemDomain(self):
            return self.getTypedRuleContext(pddlParser.ProblemDomainContext,0)


        def init(self):
            return self.getTypedRuleContext(pddlParser.InitContext,0)


        def goal(self):
            return self.getTypedRuleContext(pddlParser.GoalContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def objects(self):
            return self.getTypedRuleContext(pddlParser.ObjectsContext,0)


        def metric(self):
            return self.getTypedRuleContext(pddlParser.MetricContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_problem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblem" ):
                listener.enterProblem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblem" ):
                listener.exitProblem(self)




    def problem(self):

        localctx = pddlParser.ProblemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.match(pddlParser.LP)
            self.state = 706
            self.match(pddlParser.T__0)
            self.state = 707
            self.problemName()
            self.state = 708
            self.problemDomain()
            self.state = 710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 709
                self.objects()


            self.state = 712
            self.init()
            self.state = 713
            self.goal()
            self.state = 715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 714
                self.metric()


            self.state = 717
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_problemName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemName" ):
                listener.enterProblemName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemName" ):
                listener.exitProblemName(self)




    def problemName(self):

        localctx = pddlParser.ProblemNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_problemName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            self.match(pddlParser.LP)
            self.state = 720
            self.match(pddlParser.T__42)
            self.state = 721
            self.match(pddlParser.NAME)
            self.state = 722
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemDomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_problemDomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemDomain" ):
                listener.enterProblemDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemDomain" ):
                listener.exitProblemDomain(self)




    def problemDomain(self):

        localctx = pddlParser.ProblemDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(pddlParser.LP)
            self.state = 725
            self.match(pddlParser.T__43)
            self.state = 726
            self.match(pddlParser.NAME)
            self.state = 727
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedObjects(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedObjectsContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedObjectsContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjects" ):
                listener.enterObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjects" ):
                listener.exitObjects(self)




    def objects(self):

        localctx = pddlParser.ObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_objects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.match(pddlParser.LP)
            self.state = 730
            self.match(pddlParser.T__44)
            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 731
                self.typedObjects()
                self.state = 736
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 737
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def positiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(pddlParser.AssignmentContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)




    def init(self):

        localctx = pddlParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.match(pddlParser.LP)
            self.state = 740
            self.match(pddlParser.T__45)
            self.state = 743 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 743
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 741
                    self.positiveLiteral()
                    pass

                elif la_ == 2:
                    self.state = 742
                    self.assignment()
                    pass


                self.state = 745 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 747
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def preconditions(self):
            return self.getTypedRuleContext(pddlParser.PreconditionsContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)




    def goal(self):

        localctx = pddlParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            self.match(pddlParser.LP)
            self.state = 750
            self.match(pddlParser.T__46)
            self.state = 751
            self.preconditions()
            self.state = 752
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.sign = None # Token
            self.op = None # OperationSideContext

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def operationSide(self):
            return self.getTypedRuleContext(pddlParser.OperationSideContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_metric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric" ):
                listener.enterMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric" ):
                listener.exitMetric(self)




    def metric(self):

        localctx = pddlParser.MetricContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_metric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self.match(pddlParser.LP)
            self.state = 755
            self.match(pddlParser.T__47)
            self.state = 756
            localctx.sign = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==49 or _la==50):
                localctx.sign = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 757
            localctx.op = self.operationSide()
            self.state = 758
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





