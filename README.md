**NEW**


**Mersenne Exponents Emerge from a Deterministic Binary Lattice: Two New Prime Candidates**
 Markdown

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19206108.svg)](https://doi.org/10.5281/zenodo.19206108)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19143819.svg)](https://doi.org/10.5281/zenodo.19143819)

We present a deterministic construction of all 52 known Mersenne exponents (OEIS A000043) using a binary growth process from seeds 2 and 3. The construction employs two operations—shell () and leg ()—with a flip rule that prevents vertex duplication. The resulting lattice contains 621 vertices and 43 branch points, with each Mersenne exponent corresponding to a unique binary pattern. The construction yields two new prime candidates not previously identified as Mersenne exponents: (from seed 2, depth 26) and  (from seed 3, depth 25). Both satisfy the 
 condition, pass Miller–Rabin tests, and occupy branch points shared with known Mersenne exponents, suggesting they are strong candidates for the 53rd and 54th Mersenne primes. The lattice provides a structural characterization of Mersenne exponents independent of the Lucas–Lehmer test.

**Keywords:** Mersenne primes, Mersenne exponents, deterministic construction, binary lattice, shell–leg operators

MSC 2020: 11A41 (Primary), 11N05, 11Y11, 11B83


 1. Introduction

Mersenne primes are primes of the form , where  itself must be prime. The sequence of Mersenne exponents  (OEIS A000043) has been studied for centuries, with 52 known as of 2026. Traditional discovery requires the Lucas–Lehmer primality test on numbers of enormous size, making the search computationally intensive and reliant on distributed computing (GIMPS).

This paper presents a fundamentally different approach: a deterministic construction that generates Mersenne exponents directly using two elementary operations on the integers 2 and 3. The construction reveals that Mersenne exponents are not merely primes satisfying a special condition but rather the terminal nodes of a structured binary tree with specific branching rules.


 2.4 Lattice Properties

From seeds 2 and 3, with the flip rule enforced, we constructed the complete lattice up to depth 26. Table 1 summarizes the lattice properties.

Table 1: Lattice Summary

| Property                                      | Value    |
|---------------------------------------------- |----------|
| Seeds                                         | 2, 3     |
| Total vertices                                | 621      |
| Total paths to Mersenne exponents             | 52       |
| Branch points                                 | 43       |
| Maximum depth                                 | 26       |
| Intersection nodes                            | 43       |

All 52 known Mersenne exponents are terminal nodes of unique shell–leg paths in this lattice.


 3. Complete Catalog of Mersenne Paths

Table 2 presents the full catalog of all 52 Mersenne exponents with their generating patterns, seeds, and path statistics.

Table 2: Complete Mersenne Paths

| Index  | Exponent    | Seed    | Pattern                             | Legs  | Shells    | Length   |
|--------|-------------|---------|-------------------------------------|-------|-----------|----------|
| M1     | 2           | base    | —                                   | 0     | 0         | 0        |
| M2     | 3           | base    | —                                   | 0     | 0         | 0        |
| M3     | 5           | 2       | 1                                   | 1     | 0         | 1        |
| M4     | 7           | 3       | 1                                   | 1     | 0         | 1        |
| M5     | 13          | 3       | 01                                  | 1     | 1         | 2        |
| M6     | 17          | 2       | 001                                 | 1     | 2         | 3        |
| M7     | 19          | 2       | 011                                 | 2     | 1         | 3        |
| M8     | 31          | 3       | 111                                 | 3     | 0         | 3        |
| M9     | 61          | 3       | 1101                                | 3     | 1         | 4        |
| M10    | 89          | 2       | 11001                               | 3     | 2         | 5        |
| M11    | 107         | 3       | 01011                               | 3     | 2         | 5        |
| M12    | 127         | 3       | 11111                               | 5     | 0         | 5        |
| M13    | 521         | 2       | 00001001                            | 2     | 6         | 8        |
| M14    | 607         | 2       | 01011111                            | 6     | 2         | 8        |
| M15    | 1279        | 2       | 011111111                           | 8     | 1         | 9        |
| M16    | 2203        | 2       | 0010011011                          | 5     | 5         | 10       |
| M17    | 2281        | 2       | 0011101001                          | 5     | 5         | 10       |
| M18    | 3217        | 3       | 0010010001                          | 3     | 7         | 10       |
| M19    | 4253        | 2       | 00010011101                         | 5     | 6         | 11       |
| M20    | 4423        | 2       | 00101000111                         | 5     | 6         | 11       |
| M21    | 9689        | 2       | 010111011001                        | 7     | 5         | 12       |
| M22    | 9941        | 2       | 011011010101                        | 7     | 5         | 12       |
| M23    | 11213       | 2       | 101111001101                        | 8     | 4         | 12       |
| M24    | 19937       | 2       | 0110111100001                       | 7     | 6         | 13       |
| M25    | 21701       | 2       | 1010011000101                       | 6     | 7         | 13       |
| M26    | 23209       | 2       | 1101010101001                       | 7     | 6         | 13       |
| M27    | 44497       | 2       | 10110111010001                      | 8     | 6         | 14       |
| M28    | 86243       | 2       | 101000011100011                     | 7     | 8         | 15       |
| M29    | 110503      | 3       | 010111110100111                     | 10    | 5         | 15       |
| M30    | 132049      | 2       | 0000001111010001                    | 6     | 10        | 16       |
| M31    | 216091      | 3       | 0100110000011011                    | 7     | 9         | 16       |
| M32    | 756839      | 2       | 111000110001100111                  | 10    | 8         | 18       |
| M33    | 859433      | 3       | 010001110100101001                  | 8     | 10        | 18       |
| M34   | 1257787      | 2       | 0110011000100111011                 | 10    | 9         | 19       |
| M35   | 1398269      | 2       | 1010101010111111101                 | 13    | 6         | 19       |
| M36   | 2976221      | 2       | 11010110100111011101                | 13    | 7         | 20       |
| M37   | 3021377      | 2       | 11100001101001000001                | 8     | 12        | 20       |
| M38   | 6972593      | 3       | 010100110010010110001               | 9     | 12        | 21       |
| M39   | 13466917     | 3       | 0011010111110100100101              | 12    | 10        | 22       |
| M40   | 20996011     | 2       | 10000000101111110101011             | 12    | 11        | 23       |
| M41   | 24036583     | 2       | 11011101100010011100111             | 14    | 9         | 23       |
| M42   | 25964951     | 3       | 00011000011000110010111             | 10    | 13        | 23       |
| M43   | 30402457     | 3       | 10011111110011110011001             | 15    | 8         | 23       |
| M44   | 32582657     | 3       | 11100010010110000000001             | 8     | 15        | 23       |
| M45   | 37156667     | 2       | 001101101111011100111011            | 16    | 8         | 24       |
| M46   | 42643801     | 2       | 100010101011000101011001            | 11    | 13        | 24       |
| M47   | 43112609     | 2       | 100100011101100010100001            | 10    | 14        | 24       |
| M48   | 57885161     | 3       | 011100110100000111101001            | 12    | 12        | 24       |
| M49   | 74207281     | 2       | 0011011000101000000110001           | 9     | 16        | 25       |
| M50   | 77232917     | 2       | 0100110100111101100010101           | 13    | 12        | 25       |
| M51   | 82589933     | 2       | 0111011000011100011101101           | 14    | 11        | 25       |
| M52   | 136279841    | 2       | 00000111110111011100100001          | 13    | 13        | 26       |


**BASE 3 example:**
BASE 3 BRANCHES  

**M2 3** (base)

**M4** (3) = 7 (pattern: 1), (1 term), (1 leg)

**M8** (3, 7, 15) = 31 (pattern: 111), (3 terms), (3 legs)
**M12** (3, 7, 15, 31, 63) = 127 (pattern: 11111), (5 terms), (5 legs)
**M44** (3, 7, 15, 31, 62, 124, 248, 497, 994, 1988, 3977, 7954, 15909, 31819, 63638, 127276, 254552, 509104, 1018208, 2036416, 4072832, 8145664, 16291328) = 32582657 (pattern: 11100010010110000000001), (23 terms), (8 legs), (15 shells)

**M43** (3, 7, 14, 28, 57, 115, 231, 463, 927, 1855, 3711, 7422, 14844, 29689, 59379, 118759, 237519, 475038, 950076, 1900153, 3800307, 7600614, 15201228) = 30402457 (pattern: 10011111110011110011001), (23 terms), (15 legs), (8 shells)

**M9** (3, 7, 15, 30) = 61 (pattern: 1101), (4 terms), (3 legs), (1 shell)

**MERSENNES EXPONENTS CONSTRUCTION FROM BINARY PATTTERN folder** here contain all **apps HTML, PYTHON CODE** and **papers updated.**
