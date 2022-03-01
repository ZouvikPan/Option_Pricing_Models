# Option_Pricing_Models
## Description
- In this project I have compared the time performance of the two option pricing models, the **Binomial Tree** and **Black-Scholes** models' implementation in Python and Cython.
- **Python** offers a vast set of open-source packages that provide tools for computing in financial engineering and has a developer friendly syntax. It is used in exploratory analysis in an interactive manner on the interactive shell/environment of IPython for research, prototyping and data analysis purposes. But, since it is interpreted and dynamically typed it is not as fast as statically typed languages like C/C++.
- However, Python can be used as a glue language to integrate it with other languages and improve its performance. **Cython** is one of such implementations.
- **Cython** offers a compiler and set of language extensions to Python. Using Cython we can generate an optimized C code that can be compiled faster using native CPU instructions.
- I have taken the following Option Pricing Models:
    1. **Jarrow-Rudd Binomial Option Pricing Model**
    2. **Black-Scholes-Merton Option Pricing Model**
## Results 
### Jarrow-Rudd Binomial Option Pricing Model
#### Python
- Average time taken on ***European*** call or put options - **4.51 ms**
- Average time taken on ***American*** call or put options - **8.08 ms**
#### Cython
- Average time taken on ***European*** call or put options - **26.6 µs**
- Average time taken on ***American*** call or put options - **50.7 µs**
#### Time Improvement in Cython as compared to Python
- For ***European*** Options - **170 times faster**
- For ***American*** Options - **160 times faster**

### Black-Scholes-Merton Option Pricing Model
#### Python
- Time taken on ***European put*** option - **130 µs**
- Time taken on ***European call*** option - **133 µs**
#### Cython
- Time taken on ***European put*** option - **133 ns**
- Time taken on ***European call*** option - **128 ns**
#### Time Improvement in Cython as compared to Python
- For ***European put*** Options - **977 times faster**
- For ***European call*** Options - **1040 times faster**
