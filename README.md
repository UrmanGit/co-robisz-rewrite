# A bank heist game, "Co robisz? (rewrite)"

**Or "What do you do? (rewrite)" in English.**

## Game's backstory

Concept of the game came from a word game that I made when I was ~7 years old.
The game was pretty simple. I made a short scenario, for example:
"You are tied to a road. There are two trucks driving at you from both sides. You have a knife, a flamethrower, a chainsaw and a gun. **What do you do?**"
and the person I've been playing the game with (usually my brother/s) must have responded with for example: 
"I use a knife to cut the ropes and run away."
Then I did something like 
"These are steel ropes, so your knife broke. Now **What do you do?**".
You get the concept.

Then, it was like a year ago, me and my brother were bored. So after some time I remembered this game. What if I make it more advanced, like add a... Campaign? So on a table, me and both my brothers started playing multiplayer this time. I made a bank map out of smoked cigarettes and bottle caps, and gave my brothers 1 inventory slot each.
These rules were totally different from the first game, there were cameras, rooms, keys and keycards they needed to get to other rooms... And since I didn't have access to my PC, I thought that it would be an amazing idea to make a computer game out of this.

That's how it all started...


## Rewrites

**Now, the game is in its 4th or 5th rewrite.**

First version of the game was made in pygame zero, in a single file. That's a really easy and beginner-friendly library. Then I made a rewrite, then I learned pygame, then pygame community edition (pygame-ce), then modular files, git... Many rewrites.

And that is - I hope - my last one.

## Contributing

I really want people to help me.  If you want to help, just submit a PR! ...And read the `CONTRIBUTING.md` file. If you have questions, contact me via wojteku229@icloud.com

---

# Run the game

Okay, so how do you run the game?
**If you're familiar with Python**, you can just make a virtual environment and run `pip install -r requirements.txt`, then `python ./main.py`.

If you're not, here are more detailed steps:

1. wwInstall Python. That one you can figure out :)
2. Create a virtual environment (optional)
    - Cd into this repo's root directory (.../co-robisz-rewrite/)
    - Run `python -m venv .venv` and wait
    - If You're on Windows:
        - Run (in PowerShell) `./.venv/Scripts/activate`
    - If You're on Linux:
        - Run `source ./.venv/bin/activate`
3. **Install the requirements**: Run `pip install -r requirements.txt`
    > If you are on Linux, you may have to install some additional SDL packages to build `pygame-ce`. If you get an error during installation, search what package is missing and download it with your package manager (pacman, apt, etc.) and try again.
4. **Run the game**: type `python ./main.py` and it should open a window with my beautiful game. If something doesn't work, google it or ask AI. If you think I'm missing something, email me!

*More to come soon...*
