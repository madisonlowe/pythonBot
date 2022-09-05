# Python Bot Practice

This is a repository to track my attempt at building a Discord bot in Python!

I've never worked with Python before, and I've never built a bot or worked with the Discord API either, so creating functionality is a little slow going! However, my main goal (and main learning point) is to learn more general technical knowledge through the experience of trying out a new language, as I only started programming in the past couple of weeks.

Please see below for my goals with this project, notes of general learnings, and an in-depth chronological log of steps that I have taken and what I have learned through doing them.

Thanks for stopping by!

## Goals

Currently working towards:

- Follow docs on setting up boilerplate, then experiment with customisation to understand what's going on.
- Work on functionality goals.

Functionality goals, in order of (presumed) ease:

- Fixed D&D dice rolls, for fun and evil.
- Timezone checks against player timezones.
- Music mixes with ambient sounds, but only for covers of Careless Whisper.

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

### Pre-Work

<details>

<summary>Setting up on the Discord end.</summary>

- Made a Discord dev account.
- Used the Discord Dev Portal to make an application. Any application that interacts with the Discord APIs needs a Discord application, not just bots! Bots are a sub-set of the total interface. However, this will (hopefully) be a bot, so that's what we select all the settings for.
- Created a bot.
- Created a guild (server on Discord) to add it to.
- Added bot to the test server using OAuth2 on the Dev Portal. This is the step at which you can provide your bot with permissions. Be as granular as possible.
</details>

<br />

### Programming in Python

<details>

<summary>Setting up pip.</summary>

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

</details>

<details>

<summary>Creating a Discord connection.</summary>

- Connected to the client in `bot.py` and went through the code, googled some stuff.
- Set up `.env` and entered details.
- Attempted to run bot, but needed to set [intents](https://discordpy.readthedocs.io/en/stable/intents.html). Did this.
- Ran bot, and client successfully connected to Discord using token!

</details>

<details>

<summary>Interacting with Discord APIs.</summary>

- `Client` gives us access to a wide range of Discord APIs.
- Discord calls `on_ready()` once a connection is secured and data is prepared. So, you can access guild data inside of `on_ready()` so long as you connect to a guild by including appropriate tokens inside your `.env` file.
- Set up this connection and attempted to run.
- Had a silly syntax error where had function call after client.guilds in my for in loop. Mind out!
- Got it working.
- You can also pull out everyone who is a member of the guild, from the guild property.
- Did that too.

</details>

<details>

<summary>Using utility functions.</summary>

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

</details>

<details>

<summary>Responding to events.</summary>

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

</details>

<details>

<summary>DMs to members on joining channels.</summary>

- As of time of writing, had a nightmare with this and couldn't get it to work.
- Not sure whether because of personal Discord settings and linked accounts, potentially making it harder for code to recognise my test account as a new member? Or whether syntax wrong, as some of the syntax in this tutorial is aged, and online implementations of same functionality have been done in different ways from a cursory search.
- Going to look into more resources about it.
- Potential resources: find an active Discord bot and perceive the code. Lots on GitHub to eyeball!
- Current solve: am abandoning this functionality for now in favour of maintaining velocity and continuing tutorial, will circle back when I know more about what's going on. Not finding it useful trying to troubleshoot.

</details>

<details>

<summary>New direction.</summary>

- Confirmed syntax and implementation of tutorial were aged! We love an educational website that publishes no dates on its articles that you have to go digging for, truly.
- Recentering on the official `discord.py` docs and going to follow those from the beginning.
- On reflection, prefer this approach: feels more useful as a general learning tool, as the most fun and productive thing about trying to write in Python hasn't been learning Python, but has been learning more about programming generally. Feels like trying to understand the docs - rather than trying to put together a single working product - can provide benefit in this area.
- Changed previous `bot.py` we've been referring to, and it is now `retiredBot.py` instead. From now on, we're operating on a whole new `bot.py`.

</details>

<br />

### Attempt 2: Docs Time

<details>

<summary>Quickstart Discord docs.</summary>

- See `example_bot.py` for the example bot populated from the discord.py docs.
- Literally worked instantly, absolutely livid.
- Sometimes, I guess you just have to be taught the 'check your docs are decent' lesson a million times in a row. Million and first time lucky!
- Will say, finding the [discord.py docs](https://discordpy.readthedocs.io/en/stable/quickstart.html) a lot easier to read than when I tried to read them at the beginning of the week, I think by virtue of having poured over what all the Python stuff is doing previously. Hopefully this continues to contribute towards moving a little quicker!
- Maybe useful note from the docs: "discord.py revolves around the concept of events. An event is something you listen to and then respond to. For example, when a message happens, you will receive an event about it that you can respond to."

</details>

<details>

<summary>Reading docs and learnings from experimenting.</summary>

- Updating code won't update bot in realtime if the bot is live. Have to shut it down and reboot.
- Debugging and error feedback would be super helpful, but don't totally get how it works in Python yet? It's also something I want to get better at using and implementing in JavaScript, so - taking lessons from this experience - might swap back to a JavaScript project for a bit that focuses on that, for some cross-language learning (tee hee).
- Had a look at [these docs on coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutine).
- "Python's asyncio package (introduced in Python 3.4) and its two keywords, async and await , serve different purposes but come together to help you declare, build, execute, and manage asynchronous code."
- [This article on asynchronicity in Python](https://blog.allegro.tech/2022/01/how-do-coroutines-work-internally-in-python.html) was okay!
- The [bit of the docs on intents](https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents) is especially helpful. Has a lot of the events listed, with sub-pages describing them in more detail. Difficult to find from main page, as these docs are a bit tricky to navigate - look here if you're stuck instead!
- Read a bit more about object-oriented programming and design, and software design more generally. SOLID is the acronym for the first five OOD principles.

</details>

<details>

<summary>TODO: Implement a goal.</summary>

- Going to experiment with some new stuff I've been reading about in the docs on a JavaScript project to learn a bit more in a language and environment I'm more comfortable with!

</details>
