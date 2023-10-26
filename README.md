# journey-to-quantum-computing
This documents my journey to quantum computing

The code is based on Python 3.11 and the `requirements.txt` file defines the used package versions

## Chapters
In this repository, only the programming parts of my journey can be found.

### Chapter 1: Basic of quantum computing
For the first step, I focused on single systems and understood the basic concepts of states and unitary operators.
Based on the [first chapter](https://learning.quantum-computing.ibm.com/course/basics-of-quantum-information/single-systems) of the IBM quantum learning course
and the theoretical background via [chapter 1](http://theory.caltech.edu/~preskill/ph229/notes/chap1.pdf) and [chapter 2](http://theory.caltech.edu/~preskill/ph219/chap2_15.pdf) of the quantum computation lecture of the Caltech university by John Preskill.

First code snippets can be found:
```
01_introduction/first_kets.py
01_introduction/first_states.py
```

Afterward, I focused on multiple systems with partial measurements. An important behavior is the entanglement of qubits. Also interesting is the combination of operators.

This study was mainly based on the [second chapter](https://learning.quantum-computing.ibm.com/course/basics-of-quantum-information/multiple-systems) of the IBM course and [chapter 2](http://theory.caltech.edu/~preskill/ph219/chap2_15.pdf) of the Caltech course.

A controlled not and partial measurements on the W state, which has an interesting behavior, can be found here:
```
01_introduction/controlled_not.py
```

Next, I focused on experiments related to entanglement. Starting with teleportation, a protocol to transmit a qubit state with the help of an entangled qubit pair and two classical bits. A code example can be found here:
```
01_introduction/teleportation.py
```

### Chapter 2: Photonic quantum computing: From qubit to qumode
After learning the basics of quantum computing, I switched to quantum computing for bosonic systems (e.g. photons) based on continuous variables, as these seem promising for me.
There are a couple of differences between the continuous variable model and the 'classical' qubit model. For a quick overview, I refer to [here](https://strawberryfields.ai/photonics/concepts/photonics.html).

Even if qumodes and qubits differ widely, the current understanding is that ``qubit-based computations can be embedded into the qumode picture``. So they should have the same power.

Currently, it is not easy to find good introduction literature about this topic.
A possible start is the review paper of [Weedbrook et al.](https://arxiv.org/abs/1110.3234). Further, the videos of [Professor M does Science](https://www.youtube.com/@ProfessorMdoesScience) help to understand the necessary math foundations.

In addition, the Python library [Strawberry Fields](https://strawberryfields.ai/photonics/) is useful to get a better understanding of the topic. Even if the background chapters of the documentation are on a too abstract level for me.

Based on the Strawberry Fields library, I implemented a couple of optical circuits to get a better intuition of the behavior of qumodes. These code snippets can be found here:
```
03_continuous_variables/
```


### Chapter 3: Gaussian Boson Sampling
An important optical experiment is the Gaussian boson sampling, which could show quantum superiority in near future. It is not enough to build a universal quantum computer, but it allows the calculation of the Hafnian, which is a #P-hard problem.

[Here](https://strawberryfields.ai/photonics/demos/run_gaussian_boson_sampling.html) can be found a description of the experiment.
More information about this topic is coming soon.
