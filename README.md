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

Using utility functions:

- There are utility functions available inside of `discord.py`.
- "The term “utility” has no precise definition. A piece of code can be called a utility if it seems too small to be considered as a separate application, and too general-purpose to be considered as part of a particular program. A database program would not be a utility, for example, but a function which performed a single operation on a list could be." [Source](https://www.csee.umbc.edu/courses/331/resources/lisp/onLisp/04utilityFunctions.pdf).
- Python docs have some pages on utilities that are a bit crunchier to read too. Maybe read later!
- So. In the code where we're printing the guild name and identifier, we could clean this code up with some utilities.
- Read the whole tutorial for step-by-step details.
- Basically, `discord.utils` contains a lot of functions which can help us by abstracting away unnecessary code and work.
- For example, we can replace our original for loop checking for guild name matches with `discord.utils.find()` which takes a function (a predicate), which identifies some characteristic of the element in the iterable that you’re looking for. Once `find()` locates that element that satisfies the predicate, it will return it: so, similar to looping and then breaking once the loop is complete.
- Note: below example takes in lambda, which is basically an anonymous function? [Read this](https://stackoverflow.com/questions/16501/what-is-a-lambda-function).
- To simplify `find()` even further, we could even use `get()` instead.
- The `get()` utility takes the iterable and some keyword arguments. The keyword arguments represent attributes of the elements in the iterable that must all be satisfied for `get()` to return the element.
- So, to give examples:

```python
# original code
@client.event # this is a decorator: syntax for calling higher order functions. decorators wrap functions, modifying behaviour
async def on_ready(): # asynchronous function called on_ready()
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds: # for loop through guilds available inside client connection object
        if guild.name == GUILD: # if the guild name matches the .env guild name, break out of the loop
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id:{guild.id}'
        )

    members = '\n - '.join([member.name for member in guild.members]) # assigns members to a formatted string, joined to a loop
    print(f'Guild Members:\n - {members}') # prints out the list of guild members, formatted
# some stackoverflow guy says we could end this function with: on_ready = client.event(on_ready)
# the @ symbol is a shorthand to eliminating having to type that, though
```

```python
# using find()
@client.event
async def on_ready(): # asynchronous function called on_ready()
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds) # find() takes lambda g as predicate, wants g.name to match
    print( # once g.name matches the GUILD variable we've set, it'll return the element and print accordingly
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
```

```python
# using get()
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD) # get checks client.guilds for a name property matching GUILD variable
    print( # when it gets one, runs print code
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
```

- "Technical Detail: Under the hood, get() actually uses the attrs keyword arguments to build a predicate, which it then uses to call find()."

Responding to events:

- So. We know `on_ready()` is an event: its decorator says so.
- An event is something that happens on Discord that you can use to trigger a reaction in your code. Your code will listen for and then respond to events.
- The `on_ready()` event handler handles the event where the `Client` has made a connection to Discord and prepared its response data. When Discord fires an event, `discord.py` will route the event data to the corresponding event handler on your connected `Client`.
- There are two ways in `discord.py` to implement an event handler:
  - Using the client.event decorator.
  - Creating a subclass of Client and overriding its handler methods.
- There should be no difference between these two implementation styles for events. We'll be using the decorator version primarily though, as it looks similar to how bot commands are implemented.
- See below for examples, though, of decorator event implementation versus class event implementation:

```python
# decorator implementation
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
```

```python
# class implementation
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
```

- Just like before, we've created a client variable. The actual Client is different, however. Instead of using the normal base class, client is an instance of CustomClient, which has an overridden on_ready() function.
