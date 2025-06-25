# IPv6 Converter

## Introduction

I know, there are already built-in libraries for doing this in Python…But sometimes re-inventing the wheel can be fun, and this little task was one I was given on my first-ever coding interview\!  
At the time, I’d only been doing Python coding via [Boot.dev](http://www.boot.dev) for around 5-6wks and couldn’t complete it under the time constraints of the interview.  
Thankfully, I’d got a quick copy-paste of the problem definition and code I’d put together, to revisit it at a later date \- so here we are 🙂

## Installation

To test this out yourself, simply clone the repo to your local machine:

```
git clone https://github.com/FrogOnABike/ipv6-convert-gui.git
```

The GUI part is built using TKinter, which should ship as standard as part of Python \- however, if you encounter issues, you can follow their installation guide [here](https://tkdocs.com/tutorial/install.html)

FWIW, on my Mac I was able to install via Homebrew: 

```
brew install python-tk
```

## Use

Once you have the repo cloned, there are a couple of ways to use it:

### Command Line

```
python3 main.py <address>
```

This will execute and output the converted version directly to the console - this will either be the shortened version if you entered a "full" address or the expanded version if you enter an already compressed one.

With this option you can also add “--debug” at the end to see some extra output from under-the-hood, I’d added these in whilst working through the logic of my compression method

### GUI

Alternatively, you can launch the GUI version using:  

```
Python3 main.py \--gui
```

When that launches you can simply input the IP address in the box and either press “Enter” or click the “Process” button to get the result below.
