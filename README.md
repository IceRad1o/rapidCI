### What is a Continuous Integration System?

CI systems are dedicated systems used to test new code.



##### Basic structure of CI

* Observer: watch the repo, when it notices that a commit has been made, it notifies the job dispatcher

* Test job dispatcher : finds a test runner and gives it the commit number to test

* A test runner: run test jobs.

##### Architecture

To build a CI system that is fault-tolerant and load-bearing, in this project, each of these components has its own process which means each part is indepedent of the others.



##### Detailed Components

Repo_observer.py: 