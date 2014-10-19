# python-starter-kit

Before you get started here, make sure you have Signed Up at http://monkeymusicchallenge.com. Also make sure that you have registered your team for the warmup and received your API key at http://warmup.monkeymusicchallenge.com. Then head over to your team page to get more detailed instructions on the game itself.

To understand this starter kit you will need to have basic knowledge of

* [Python](https://www.python.org/)

The python library [requests](http://docs.python-requests.org/en/latest/user/install/#install) must be installed on your machine as well.

## Usage

First of all, `fork` this repository to your own github user.

Now open up a terminal and run the following commands:

```bash
git clone git@github.com:<username>/python-starter-kit.git
cd python-starter-kit
TEAM=myteamname API=XXXX python index.py
```

These are all UNIX commands. Windows users are recommended [Cygwin](https://www.cygwin.com/) to make this work.

After running the above sequence, the monkey should be running around randomly on your team page.

The program should exit with a simple "Game over." statement. Now get coding!


## Get started

`index.py` contains the boilerplate needed to communicate with the server. You should not need to change anything in here unless we have done something wrong.

`ai.py` is quite confused and seemingly random at the moment.

In order to complete the challenge, implement your AI so that `ai.move` makes the right choices. Pathfinding and AI ftw!


## Bugs

If you find any bugs in our code. Please submit an issue or a pull request to the original repository.
