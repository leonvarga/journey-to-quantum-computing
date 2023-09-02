# journey-to-quantum-computing
This documents my journey to quantum computing

The code is based on Python 3.11 and the `requirements.txt` file defines the used package versions

## Chapters
In this repository only the programming parts of my journey can be found.

### Chapter 1 Basic of quantum computing
In the first step, I mainly focused on single systems and understood the basic concepts of states and unitary operators.
Based on the first chapter of 
https://learning.quantum-computing.ibm.com/course/basics-of-quantum-information/single-systems
and the theoretical background via
http://theory.caltech.edu/~preskill/ph229/notes/chap1.pdf, http://theory.caltech.edu/~preskill/ph219/chap2_15.pdf

First code snipets can be found:
```
01_introduction/first_kets.py
01_introduction/first_states.py
```

Afterwards, I focused on multiple systems with partial measurements. A important behavior is the entanglement (correlation) of qubits. Also interesting is the combination of operators.

This study was mainly based on https://learning.quantum-computing.ibm.com/course/basics-of-quantum-information/multiple-systems and http://theory.caltech.edu/~preskill/ph219/chap2_15.pdf

A controlled not and partial measurements on the W state, which has a interesting behavior, can be found here:
```
01_introduction/controlled_not.py
```





## Literature
The following literatures help me to dive into this topic:

http://theory.caltech.edu/~preskill/ph219/

https://learning.quantum-computing.ibm.com/

https://www.youtube.com/@QuantenmechanikStudihilfe (German only)
