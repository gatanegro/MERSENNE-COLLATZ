We present a deterministic generative grammar for the exponents of Mersenne primes. The grammar expresses every Mersenne exponent \(p_n\) (for \(n \geq 5\)) as the product of two earlier exponents plus or minus the difference of two additional earlier exponents: \(p_n = p_a \times p_b \pm (p_c - p_d)\).

We demonstrate that this formula, using only the largest product of earlier exponents less than the target, successfully generates 48 of the 48 analyzable exponents.

This IS PUBLISHED IN **DOI 10.5281/zenodo.1971398999** by the time that M50 was not found to hold this formula.

##UPDATE : M50 ALSO HOLD THE FORMULA.##

For Mersenne exponents pe with index e > 5 , the generative formula is:

<img width="178" height="27" alt="image" src="https://github.com/user-attachments/assets/e992eb45-84f2-47c2-9af2-454ab35484f3" />


 
 Manual Method — Largest Product + m² Scaling

p_a × p_b = largest product < target. If k too big, scale by m².
Done: 48 found
M#	 |p_e	          |m	    |p_a	 p_b	      |m²×p_a×p_b	    |k
M5	 |13 	          |1	    |2    |5 	      |10	            |3
M6	 |17 	          |1	    |3	   |5 	      |15	            |2
M7	 |19 	          |1	    |3	   |5        |15	            |4
M8	 |31 	          |1	    |2	   |13 	     |26	            |5
M9	 |61 	          |1	    |3	   |19      	|57	            |4
M10	|89 	          |1	    |5	   |17 	     |85	            |4
M11	|107           |1	    |5	   |19    	  |95            	|12
M12	|127          	|1	    |2	   |61      	|122	           |5
M13	|521 	         |1	    |5	   |89      	|445	           |76
M14	|607 	         |1	    |19	  |31 	     |589	           |18
M15	|1,279 	       |1	    |2    |607 	    |1,214	         |65
M16	|2,203        	|1	    |17	  |127     	|2,159	         |44
M17	|2,281 	       |1	    |17  	|127 	    |2,159	         |122
M18	|3,217 	       |1	    |5	   |607 	    |3,035	         |182
M19	|4,253 	       |1	    |7	   |607     	|4,249	         |4
M20	|4,423 	       |1	    |2	   |2,203   	|4,406         	|17
M21	|9,689        	|1	    |3	   |3,217   	|9,651         	|38
M22	|9,941 	       |1	    |19	  |521 	    |9,899	         |42
M23	|11,213       	|1	    |5   	|2,203   	|11,015	        |198
M24	|19,937 	      |1	    |2	   |9,941   	|19,882	        |55
M25	|21,701 	      |1	    |5   	|4,253   	|21,265	        |436
M26	|23,209 	      |1	    |7   	|3,217   	|22,519	        |690
M27	|44,497 	      |1	    |2	   |21,701   |43,402	        |1,095
M28	|86,243 	      |1	    |19	  |4,423   	|84,037	        |2,206
M29	|110,503 	     |1	    |5	   |21,701   |108,505	       |1,998
M30	|132,049      	|1	    |31	  |4,253 	  |131,843	       |206
M31	|216,091 	     |1	    |19	  |11,213   |213,047       	|3,044
M32	|756,839       |1	    |17	  |44,497   |756,449	       |390
M33	|859,433 	     |1	    |89	  |9,689 	  |862,321	       |-2,888
M34	|1,257,787 	   |1	    |127	 |9,941 	  |1,262,507	     |-4,720
M35	|1,398,269 	   |590	  |2	   |2 	      |1,392,400	     |5,869
M36	|2,976,221    	|862	  |2	   |2 	      |2,972,176	     |4,045
M37	|3,021,377    	|868	  |2	   |2 	      |3,013,696	     |7,681
M38	|6,972,593 	   |1320	 |2	   |2     	  |6,969,600	     |2,993
M39	|13,466,917 	  |1835	 |2	   |2       	|13,468,900	    |-1,983
M40	|20,996,011 	  |2291	 |2 	  |2 	      |20,994,724	    |1,287
M41	|24,036,583 	  |2451	 |2 	  |2 	      |24,029,604    	|6,979
M42	|25,964,951 	  |2548 	|2	   |2 	      |25,969,216	    |-4,265
M43	|30,402,457   	|2757	 |2	   |2       	|30,404,196	    |-1,739
M44	|32,582,657 	  |2854	 |2	   |2 	      |32,581,264	    |1,393
M45	|37,156,667 	  |3048	 |2	   |2        |37,161,216	    |-4,549
M46	|42,643,801 	  |3265	 |2	   |2 	      |42,640,900	    |2,901
M47	|43,112,609 	  |3283	 |2	   |2 	      |43,112,356    	|253
M48	|57,885,161 	  |3804	 |2	   |2       	|57,881,664	    |3,497
M49	|74,207,281 	  |4307	 |2 	  |2 	      |74,200,996	    |6,285
M50	|77,232,917 	  |4394	 |2	   |2       	|77,228,944	    |3,973
M51	|82,589,933 	  |4544	 |2	   |2       	|82,591,744	    |-1,811
M52	|136,279,841   |5837 	|2    |2 	      |136,282,276	   |-2,435

48/48 found
