### What is a Continuous Integration System?

When developing software, we want to be able to verify that our new features or bug fixes are safe and work as expected. We do this by running tests against our code. Sometimes, developers will run tests locally to verify that their changes are safe, but developers may not have the time to test their code on every system their software runs in. Further, as more and more tests are added the amount of time required to run them, even only locally, becomes less viable. Because of this, continuous integration systems have been created.

Continuous Integration (CI) systems are dedicated systems used to test new code. Upon a commit to the code repository, it is the responsibility of the continuous integration system to verify that this commit will not break any tests. To do this, the system must be able to fetch the new changes, run the tests and report its results. Like any other system, it should also be failure resistant. This means if any part of the system fails, it should be able to recover and continue from that point.

This test system should also handle load well, so that we can get test results in a reasonable amount of time in the event that commits are being made faster than the tests can be run. We can achieve this by distributing and parallelizing the testing effort. This project will demonstrate a small, bare-bones distributed continuous integration system that is designed for extensibility.

------

#### Project Limitaions and Notes

This project uses Git as the repository for the code that needs to be tested. Only standard source code management calls will be used, so if you are unfamiliar with Git but are familiar with other version control systems (VCS) like svn or Mercurial, you can still follow along.

Due to the limitations of code length and unittest, I simplified test discovery. We will *only* run tests that are in a directory named `tests` within the repository.

Continuous integration systems monitor a master repository which is usually hosted on a web server, and not local to the CI's file systems. For the cases of our example, we will use a local repository instead of a remote repository.

Continuous integration systems need not run on a fixed, regular schedule. You can also have them run every few commits, or per-commit. For our example case, the CI system will run periodically. This means if it is set up to check for changes in five-second periods, it will run tests against the most recent commit made after the five-second period. It won't test every commit made within that period of time, only the most recent one.

This CI system is designed to check periodically for changes in a repository. In real-world CI systems, you can also have the repository observer get notified by a hosted repository. Github, for example, provides "post-commit hooks" which send out notifications to a URL. Following this model, the repository observer would be called by the web server hosted at that URL to respond to that notification. Since this is complex to model locally, we're using an observer model, where the repository observer will check for changes instead of being notified.

CI systems also have a reporter aspect, where the test runner reports its results to a component that makes them available for people to see, perhaps on a webpage. For simplicity, this project gathers the test results and stores them as files in the file system local to the dispatcher process.

Note that the architecture this CI system uses is just one possibility among many. This approach has been chosen to simplify our case study into three main components.



##### Basic structure of CI

* Observer: watch the repo, when it notices that a commit has been made, it notifies the job dispatcher

* Test job dispatcher : finds a test runner and gives it the commit number to test

* A test runner: run test jobs.

##### Architecture

To build a CI system that is fault-tolerant and load-bearing, in this project, each of these components has its own process which means each part is indepedent of the others.



##### Detailed Components

