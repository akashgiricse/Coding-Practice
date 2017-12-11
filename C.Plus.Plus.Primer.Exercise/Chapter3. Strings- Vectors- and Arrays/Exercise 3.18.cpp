There will be "segmentation fault" because we are assigning value 42 to a non existing memory. 
The vector is initially empty. There is no such place in the memory of ivec[0]
We can fix this by using push_back.ivec;
