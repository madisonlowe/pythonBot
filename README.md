# README

## Action Plan

To do, in order:

- ~~Gitignore!~~
- Build D&D bot.
  - Version 1:
    - Literally just follow a tutorial to figure out how it works.
  - Version 2:
    - Functionality:
      - Timezone checks:
        - Save time zone settings from server members.
        - View overlapping free times in each timezone.
      - Causing problems:
        - Fix the dice.
        - Music functionality but it only plays ambient sounds over covers of Careless Whisper.
- Profit.
- Never touch Python again.

Helpful learning side exercises:

- Hello World and some other test code to figure out what Python's trying to achieve.
- Clone down Andy's Python project to play around with.

## Notes

Learning points to remember:

- Run `python3` to open the interpreter. When you have both versions installed, need to specify the one you want to use.
- Imports only run once per session in the interpreter. Docs say import operations are expensive, so they'll only run once.
- Run `quit()` to close the interpreter.
- See notes in `practice.py` on importing and running that code.
- See [this article](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7) on freezing requirements in Python projects.

Learning exercises to pursue:

- Valerio suggested the fCC introduction to Python as a good place to absorb general knowledge.
- Read more about interpreters. Get the point, don't get the implementation, so focus there.
- Positional arguments versus keyword arguments for calling functions? That's fun.

## Log

Setting up on the Discord end:

- Made a Discord dev account.
- Used the Discord Dev Portal to make an application. Any application that interacts with the Discord APIs needs a Discord application, not just bots! Bots are a sub-set of the total interface. However, this will (hopefully) be a bot, so that's what we select all the settings for.
- Created a bot.
- Created a guild (server on Discord) to add it to.
- Added bot to the test server using OAuth2 on the Dev Portal. This is the step at which you can provide your bot with permissions. Be as granular as possible.

### Programming in Python

Setting up pip:

- Install `pip`, which is the standard package manager for Python (like `npm` for JavaScript). To check what version of `pip` you have, you can run `which pip3` in the terminal: `pip` should come bundled with installations of Python3.
- Use `pip` in a Python Virtual Environment.
- "To avoid installing packages directly into your system Python installation, you can use a virtual environment. A virtual environment provides an isolated Python interpreter for your project. Any packages that you use inside this environment will be independent of your system interpreter. This means that you can keep your project’s dependencies separate from other projects and the system at large." [Source](https://realpython.com/what-is-pip/).
- Used the following code to accomplish the above:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 --version
pip 21.2.3 from .../python3.10/site-packages/pip (python 3.10)
(venv) $ pip --version
pip 21.2.3 from .../python3.10/site-packages/pip (python 3.10)
```

- "Here you create a virtual environment named venv by using Python’s built-in venv module. Then you activate it with the source command. The parentheses surrounding your venv name indicate that you successfully activated the virtual environment."
- "Finally, you check the version of the pip3 and pip executables inside your activated virtual environment. Both point to the same pip module, so once your virtual environment is activated, you can use either pip or pip3."

Installing `discord.py`:

- Ran the following code to install the Python Discord API library: `pip install -U discord.py`.

More virtual environment stuff:

- Once you've closed it, to restart the venv for the project, run the following:

```
cd venv
source bin/activate
```

- This changes directory into the venv folder, then reactivates the environment you've set up.
- [This was helpful.](https://ordinarycoders.com/blog/article/python-virtual-environment)

Creating a Discord connection:

- Connected to the client in `bot.py` and went through the code, googled some stuff.
- Set up `.env` and entered details.
- Attempted to run bot, but needed to set [intents](https://discordpy.readthedocs.io/en/stable/intents.html). Did this.
- Ran bot, and client successfully connected to Discord using token!

Interacting with Discord APIs:

- `Client` gives us access to a wide range of Discord APIs.
- Discord calls `on_ready()` once a connection is secured and data is prepared. So, you can access guild data inside of `on_ready()` so long as you connect to a guild by including appropriate tokens inside your `.env` file.
- Set up this connection and attempted to run.
- Had a silly syntax error where had function call after client.guilds in my for in loop. Mind out!
- Got it working.
- You can also pull out everyone who is a member of the guild, from the guild property.
- Did that too.
