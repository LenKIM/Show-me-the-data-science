**Errata Type: Code | Page: 13**

**It is:** words_in_tweet = first_tweet.split(' ')

**Should be:** words_in_tweet = tweet.split(' ')

**Errata Type: Typo | Chapter: The data science Venn diagram | Page: Example of basic Python** 

**It is:** 5if x + y == 15.3: # If the statement is true: 

**Should be:** if x + y == 15.3: # If the statement is true: 

 

**Errata Type : Typo | Page No. 77**

This:
This means that it would take **2.31** years to double our money.

Should be:
This means that it would take **23.1** years to double our money.



**Errata Type : Typo | Page No. 81**

This:
return **stores / float**(stores_all_together)

Should be:
return **stores_in_common / float**(stores_all_together)

Errata Type: Technical | Chapter 4 | Page 84

This:
The resulting matrix will be a 1 x 1,000 matrix (a vector) of 10,000 predictions for each individual movie.

Should be:
The resulting matrix will be a 1 x 10,000 matrix (a vector) of 10,000 predictions for each individual movie.

This:
movies = np.random.randint(5, size =(3,1000)) + 1

Should be:
movies = np.random.randint(5, size =(3,10000)) + 1

Errata Type: Typo | Chapter 7 | Page 152

This:
The diagonal of the matrix is filled with positive is.

Should be:
The diagonal of the matrix is filled with positive ones.

**Errata Type: code| Chapter 11 | The word "revealing" should be removed from the code.**
spams = df[df.label == 'spam']
for word in ['send', 'cash', 'now']:
print word, spams[spams.msg.str.contains(word)].shape[0] / float(spams.shape[0])**revealing** 
Should be : 
spams = df[df.label == 'spam']
for word in ['send', 'cash', 'now']:
print word, spams[spams.msg.str.contains(word)].shape[0] / float(spams.shape[0])

**Errata Type: Technical, Page number 101 PDF:**

**It is:**

= 1 – (2/36 + 2/36)
= 1 – (4/36)
= 32/36 = 8 / 9
= .89

**Should be:**

= 1 – (1/36 + 2/36)
= 1 – (3/36)
= 33/36 
= .92

**Errata Type: Code |Page Number: 85**

**It is:**

for num_movies in (10000, 100000, 1000000, 10000000, 100000000): movies = np.random.randint(5,size=(3, movies))+1

 **should be:**

 for num_movies in (10000, 100000, 1000000, 10000000, 100000000): movies = np.random.randint(5,size=(3, num_movies))+1

 

**Errata Type: Technical|Page Number:  250**

**It is:**

 we see that the send cash now probability for spam is 38 times higher than for **spam**

**Should be:**

 we see that the send cash now probability for spam is 38 times higher than for **ham**

Errata Type: Code | Page 13

It is: 
tweet = "RT @j_o_n_dnger: $TWTR now top holding for
Andor, unseating $AAPL"

Should be: 
tweet = "RT @robdv: $TWTR now top holding for
Andor, unseating $AAPL"

 

Page 12

In the third bullet:

\>= (greater than or equal to)
3 >= 3 (True)
5 >= 3 (False)


Page 13

The tweet in question is "RT @robdv:

Should read: the tweet in question is "RT @j_o_n_dnger to match the preceding 
code.

**Errata Type: Technical | Page: 171**

**It is:**

Specify the hypotheses.
We will let H0
= the engineering department takes breaks the same as the company
as a whole
If we let this be the company average, we may write:

**H0:**

**Should be:**

Specify the hypotheses.
We will let H0
= the engineering department takes breaks the same as the company
as a whole
If we let this be the company average, we may write:

**H0:(engineers take as long breaks)**

**Errata Type: Technical | Page: 171**

**It is:**

If we wish to answer the question, is the sample mean different from
the company average, then this is called a two-tailed test and our
alternative hypothesis would be as follows:

**Ha:**


**Should be:**

If we wish to answer the question, is the sample mean different from
the company average, then this is called a two-tailed test and our
alternative hypothesis would be as follows:

**Ha:(engineers take different break lengths)**

Errata Type: Technical | Chapter: 2 | Page: 43
This:
It is the square root of the product of all the values.

Should Be:
It is the nth root of the product of n values.