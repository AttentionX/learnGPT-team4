### `test_6.py` (1)?

> `gpt_v1` & `gpt_2` do not preserve orders  - why?

### `test_6.py` (2)?

> pos_encodings is designed such that each pos is different - how?
  
With position integer *pos*, create a vector d which is a sequence of sin(pos/C) and cos(pos/C) where C is a $$$$ n^{2i/d} $$$$ where n is a scalar (10000) and i is the column indices from 0 to d/2

### `test_6.py` (3)?

> pos_encodings is designed such that  |PE(pos + k) - PE(pos)| stays constant - why & how?

PE encodes an integer to a d dimensional vector but due to the usage of sin and cosine and the relationship between them, the l2 norm of PE will always be the same. While k determines the distance between two positional vectors which is proportional to the angle between them.   

For example,  
Assuming 
$$$$PE(pos)[0] = sin(pos) $$$$, and  
$$$$ PE(pos)[1] = cons(pos) $$$$  
Then the l2 norm would be the same as 1,  
$$$$ \lVert PE(0) \rVert == \lVert PE(\frac{\pi}{2}) \rVert == \lVert PE(\pi) \rVert == 1 $$$$  
While the differences are  
$$$$ \lVert PE(0) - PE(\frac{\pi}{2}) \rVert = \sqrt{2}  $$$$  
$$$$ \lVert PE(0) - PE(\pi) \rVert = 2 $$$$


### `test_6.py` (4)?

>  `gpt_v3` does preserve order  - how?

-  what changes did you make to `token_emb`?