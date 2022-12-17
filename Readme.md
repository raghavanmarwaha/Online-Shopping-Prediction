# Shopping Prediction

AI to predict whether online shopping customers will complete a purchase
## 1. Methodolgy
We build a **nearest-neighbor classifier** to solve this problem. Given information about a user — how many pages they've visited, whether they're shopping on a weekend, what web browser they're using, etc. — this classifier will predict whether or not the user will make a purchase.<br>
<br>
We'll measure two values: **sensitivity** (also known as the "true positive rate") and **specificity** (also known as the "true negative rate") to check the accuracy of the classifier. Sensitivity refers to the proportion of positive examples that were correctly identified: in other words, the proportion of users who did go through with a purchase who were correctly identified. Specificity refers to the proportion of negative examples that were correctly identified: in this case, the proportion of users who did not go through with a purchase who were correctly identified. Our goal is to build a classifier that performs reasonably on both metrics.

## 2. Description
When users are shopping online, not all will end up purchasing something. Most visitors to an online shopping website, in fact, likely don't end up going through with a purchase during that web browsing session. It might be useful, though, for a shopping website to be able to predict whether a user intends to make a purchase or not: perhaps displaying different content to the user, like showing the user a discount offer if the website believes the user isn't planning to complete the purchase.<br>
<br>


## 3. Input/Output
Input : Data from Google Meta data analysis
Output:
```
Correct: 4073
Incorrect: 859
True Positive Rate: 6.37%
True Negative Rate: 76.22%
```
## 4. Live Link

## 5. Screenshot of Interface
![image](https://user-images.githubusercontent.com/64203412/208244623-b06e040b-2aca-426a-a7f3-9fba296ca276.png)

