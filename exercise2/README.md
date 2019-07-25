# Enablement Team Kata [![Build Status](https://travis-ci.org/ricardolopes86/nvm-exercises.svg?branch=master)](https://travis-ci.org/ricardolopes86/nvm-exercises)

## How to setup the project

In order to have this project running in your PC, you should have the following software installed (this was built in a Debian based Linux distribution a.k.a Ubuntu, it won't work in a Windows-based system):

* `python3`
* `git`
* `pip3`
* `docker`
* `docker-compose`

If you'd like to try our awesome application, run in your terminal:

    $ git clone https://github.com/ricardolopes86/nvm-exercises.git
    $ cd nvm-exercises/exercise2
    $ python3 exercise2.py <list of 6 numbers separated by space goes here>

Then, just interact with all options in the menu.  

If you'd like to do the same, but running in a container, then, follow the steps below:

    $ git clone https://github.com/ricardolopes86/nvm-exercises.git
    $ cd nvm-exercises/exercise2
    $ docker build -t nvm-app -f run-app.Dockerfile .

Wait for the build to finish... you should get the following message at the end of the build process:

    Successfully tagged nvm-app:latest

Now, run this command to have the app running:

    $ docker run -it nvm-app <list of 6 numbers separated by space goes here>

### Run pipeline manually - step by step in the command line

For this boring task (we like everything done automatically on our behalf) you should follow these steps:

1. Install all Python modules before:

    $ pip3 install pylint --user
    $ pip3 install pytest --user

2. Now run our first stage: linting:

    $ pylint exercise2.py

3. Next step: unit tests:

    $ python3 test.py

4. Next step: build:

    $ python3 build.py

5. Next step: packaging:

    $ python3 package.py

6. Last, but not least: cleaning up:

    $ python3 cleanup.py

## How to run pipeline locally

Running the pipeline locally is possible by just running a command which will take advantage of `docker-compose` to orchestrate the build using `docker`. `docker-compose` will take care of building the `docker images` before running it, then it will spin the containers to run the steps - in the proper order.  

Once you're ready, let's get started:  

Clone github repo into your computer by running:

    $ git clone https://github.com/ricardolopes86/nvm-exercises.git

`cd` into the `nvm-exercises`:

    $ cd nvm-exercises/exercise2

Finally, run the `docker-compose` to start the pipe-line:

    $ docker-compose up

That's it! It should go through the `lint`, `test`, `build` and `package` steps and in the end, you should have in your terminal the results of the linthing phase, in `./build/` directory, you'd have the compiled artifact, `./test/` directory the unit test results in `XML` format and finally, in `./package/` directory, a `.tar.gz` file name `nvm.tar.gz` containing our app inside. 

## Extra

You can check the same stages in our Travis CI in this [link](https://travis-ci.com/ricardolopes86/nvm-exercises).  

Everytime we push code to github, it will automatically build our application. The configuration of the pipeline is define in the `.travis.yml` file in the root of our repository.