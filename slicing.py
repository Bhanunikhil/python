#slicing = create a substring by extracting elements from another string.

#indexing[] or slice() ..[start:stop:step]

txt= "My name is Nikhil"

slicing = txt[0]
print(slicing)

#substring from starting index to a particular index
slicing = txt[0:2]
print(slicing)

#substring from starting index 0 to a particular index and I am checking here whether it consider a space as an index or not.
slicing = txt[0:3]
print(slicing)

slicing = txt[2:7]
print(slicing)

#substring from start to end index and the last part .step. is like which index should it consider in every iteration 
slicing =txt[0:17:2]
print(slicing)

#reversing a string using slicing

reverse_txt = txt[::-1]
print(reverse_txt)
