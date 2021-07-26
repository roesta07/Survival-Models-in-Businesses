## Introduction
___
Businesses are often interested to know about the rate at which their customers enroll and quit. It is through these rates any business decides upon its customer retention strategies and evaluates lifetime values from each customer

In this project we are considering some schools' data; we are interested in the dropout rate of our students during their junior years where it is presumed that the admissions & dropouts are particularly high.

Understanding such rates are crucial for schools for mainly two reasons; first, they can further investigate the causes to student's dropout and improve the system by making right inference and second such rates helps school evaluate the lifetime value of each student which helps schools to spend wisely.

## Hypothesis
Although many factors lead students to quit school we can quickly start analyzing few known properties of our students which are already in our system. In this example, we are interested in improving customer retention and further want to investigate upon factors particularly we want to check our Bus Administration’s performance. Thus we can formulate our Hypothesis as

>Are our Students unhappy by our ***Bus Service*** or Is it just that being ***located far*** generally tends to more dropouts?


*Check the Generative Model at the end of this to further understand the phenomenon.*

## Problems and Challenges
One problem with these types of analyses is that the dataset represents a certain time window. There will be a mix of students currently continuing and students who have dropped out in the dataset.This can create confusion as the students currently continuing their academics will still be in that dataset but we are interested in only drop-out rates and therefore an instinct will be to ***delete data*** of students who haven't dropped out.

But *this is a mistake* and can cause ***biased estimates*** because the students who have not dropped out until we download the data give us information about the dropout rate by representing that they haven't dropped out. 

This is confusing, but one loose example to understand this can be simple as; the probability of head gives us information about probability tail as they are *complementary* of each other.


## Survival Models
Such data are called censored Data and now you could guess why it’s called censored. Survival models are goto models for such data. Survival analysis has been used for data involving time to a certain event such as death, the onset of a disease,  or other biology, but we can borrow its applications in business. Here we will be using a simple version of Survival models and using Exponential Distribution for our likelihood.
### Exponential Distribution And its Assumptions
The Exponential Distribution is the probability distribution of the time between events in which such events occurs continuously and independently at the constant average rate.

It has only one parameter lambda ($\lambda$). The lambda($\lambda$) parameter is the rate of an event happening; which is exactly what we wanted to figure out.
Also, The memorylessness feature of exponential distribution state that every day each student have the some constant rate of dropping out every day. This is a little unfair with students with higher classes but this assumption is close to the truth for students at junior years.


## Model 
Let D be the days to Dropout
$$D_{i}|dropout==1 \sim Exponential(\lambda_{i})$$
$$D_{i}|dropout==0 \sim Exponential-CCDF(\lambda_{i})$$
where,
$$\lambda_{i}= exp(\alpha_{[far]}+  \beta_{[bus]}) $$

For students who have dropped out its just Exponential liklihood function but for students who have not yet dropped out we can incorporate their information using Exponential CCDF which is just the cummulative complementry of Exponential. For example we asking two different questions for the same answer for plian Exponential the question is  what is the probability of student dropping out at day 25 and for Exponential CCDF we are asking what is the probability of student dropping out given a student is still enrolling. 
We can further explore these topics mathematically.
The above notation can be further written as
$$\begin{Bmatrix}
 & e^{-\lambda *t} & &if dropout=0 \\ 
 & \lambda * e^{-\lambda *t}& &if dropout==1
\end{Bmatrix}$$
<div><img src="fig//expon.png" width="820"  class="inline"> </div>


We also want to control for weather students live far or not so that we want to know that is there stil some strong association between bus service and dropout.

## Priors
Priors are your beliefs about our parameters before seeing the data. It’s just a way of telling our model that what is infinity and whats not. You can also incorporate your expert beliefs, findings you’re your previous studies or even some sensible reasoning about your parameter into your prior.

In this example, we are estimating the Dropout Rate of each student per day i.e parameter  $(\lambda)$. Before even seeing the data we can have some reasoning about this parameter; even though we can’t exactly estimate what value $(\lambda)$ can take right now but we know what values it cannot take. For instance, imagine $(\lambda)$ is 0.50 or more i.e dropout rate of each student per day is 50 % more; we know for certain that no school can even think of running a successful business with that dropout rate until and unless it’s into some serious money-laundering. Of course, we can do far  better than that but even a simple restriction can improve our model’s estimation because our model does not have to go look for impossible infinite space. We want $(\lambda)$ to fall under 0.5 and increase our beliefs as we move below.

But our beliefs should to converted into mathematical notation for our model to make sense. And, Eliciting priors especially on these kinds of Generalized Linear Models(glms) is tricky because we have morphed the parameters using some link function to our glms. Therefore it’s always suggested plotting the priors. 

<div><img src="fig//priors.png" width="820"  class="inline"> </div>

*Fig: Prior Predective simulations for 3 different beliefs*


The plot in the middle exactly goes with our beliefs as you can see from the fig (*bottom-mid*) our beliefs about the dropout-rate $(\lambda)$  fall under 0.5 and the mass increases as we move below
The middle plot exactly goes with our belief

$$\alpha \sim Normal(1,1.5) $$
$$\beta \sim Normal(1,1.5) $$

where,

$$\lambda_{i}= exp(\alpha_{[far]}+  \beta_{[bus]}) $$




## Statistcal Question
What is the average difference in dropout rates for students who uses bus and who doesnot uses bus across all far far students ?

=
## Conclusion


## Generative Model
Each year during admission sessions some average number of students gets admitted to the School.

We Expect 70% of students are within 5 km radius from the school's location and 30% of students 5km far represented with variable *far*.

School arranges bus service to those students which are *far* and most but not all of the far students uses bus.

Each Day each parents may be disatisfied with school mainly aggregrated 3 sources. first Disputes from some Unknown sources. second disputes from being far and third disputes from School's Bus service. this Disatisfaction is not measured and is not in our dataset; however the information of disatisfaction flows towards student's drop out rate.

And just like in any other system of disatisfaction and disputes if handled properly they are resolved else it increases and stacks until some unfortunate events for our case drop out.

