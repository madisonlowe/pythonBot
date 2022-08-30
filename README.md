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
- See notes in `main.py` on importing and running that code.

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

Programming in Python:

-
