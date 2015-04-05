
---


# **Current Status - Date: 23 Feb 2009** #

Okay. Finally, it has to start from somewhere. I am starting with current status of our project.

As with the last meeting with Mr. Haridas Acharaya, our project guide, he asked to proceed ahead developing the backend. Specific details are as follows:

## **Design oriented Tasks** ##
  * Determine all the valid positions for a particular element (like various positions of eyes, mount, etc.).
  * Various combinations of element values will be available. But only some of them will have a recoginized meaning or interpretation. Try to make a set of such combination values that correspond to valid interpretations.
  * Prepare the database for the combinations.

## **Programming Related Tasks** ##
  * Make a program that generates the image or model corresponding to the various combinations.
  * Make a program that generates the combinations for a given image or model. This one requires some tool that allows us to move the model on runtime. Also, if any valid model position correspond to some valid interpretation, then store the same into the database.

## **Proposed Learning Mechanism** ##

---

We can analyze what words are being responded by the end user for the actions enacted. We can assign the total count as the weight-age for each of these words to relate to action sequences.

For instance, for an action sequence, we get following words with their individual count.
```
say     1204
tell     690
speak    180
utter     54
```

Then the probability of people responding the word "say" for the same action sequence is more than for the word "utter".

## **Demo Video** ##
http://www.youtube.com/watch?v=X2Alkoy1PYg