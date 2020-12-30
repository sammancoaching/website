---
layout: default
title: Navigating without syntax details
parent: Warm-up Questions
grand_parent: Exercises
nav_order: 6
---

Match the words the navigator speaks to the code the typist should type. Write your answers in the “Code snippet number” column


1. Check if the numbers array is empty
2. Return an error if n is zero, otherwise return n
3. Declare an empty integer array called numbers
4. Foreach loop over the numbers array
5. Assert that the result is 42
6. Declare a new function called foobar. It takes an integer argument called baz
7. Convert n to a float

### Code snippets in Python:

#### 1
	def foobar(baz):
    	pass

#### 2

	assert result == 42

#### 3
	for n in numbers:
    	pass

#### 4

	if len(numbers) == 0:
    	pass

#### 5
	if n == 0:
    	raise ValueError("n is zero")
	else:
    	return n

#### 6
	numbers = []

#### 7
	float(n)


### Code snippets in Go:

#### 1
	func foobar(baz int) {
	}

#### 2
	assert.Equal(t, 42, result)

#### 3
	for n := range numbers {
	}

#### 4
	if len(numbers) == 0 {
	}


#### 5
	if n == 0 {
	    return 0, errors.New("n is zero")
	}
	return n, nil

#### 6 
	var numbers = []int{}

#### 7 
	float64(n)
