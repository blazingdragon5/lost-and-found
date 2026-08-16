# START HERE 👋

Hey Aditya. This folder is the skeleton of your app.

Here's the deal: **the structure is built, but almost none of it works yet.**
Most files have functions with the insides missing and a note saying
`# TODO: you write this`. That's on purpose. Those TODOs are your project.

Think of it like a model kit. All the pieces are in the box, sorted, with
instructions. You still have to build it.

---

## Week 0 goal (this week, Aug 15–23)

**Get one page to show up in your browser.** That's it. That's the whole goal.

Sounds tiny. It isn't. Setting up Python, a virtual environment, and a web
server for the first time trips up almost everybody. When that page loads,
you've cleared the hardest part of the whole project.

---

## Step 1 — Install stuff

### Python
Go to [python.org/downloads](https://www.python.org/downloads/) and get Python 3.12.

⚠️ **On the very first screen of the installer, there is a checkbox at the
bottom that says "Add Python to PATH." CHECK IT.**

I'm putting this in giant letters because it's the single most common way
people mess this up. If you miss it, your computer won't know what the word
`python` means, and nothing else in this guide will work. If you already
installed it and forgot, just run the installer again and choose "Modify."

### VS Code
Get it at [code.visualstudio.com](https://code.visualstudio.com/). Open it,
click the Extensions icon on the left (looks like four squares), search
"Python," and install the one by Microsoft.

### Git
Get it at [git-scm.com/download/win](https://git-scm.com/download/win). Click
Next through everything — the defaults are fine.

Then make a free account at [github.com](https://github.com).

---

## Step 2 — Open the project

Open VS Code → **File → Open Folder** → pick this `lost-and-found` folder.

Then open a terminal inside VS Code: **Terminal → New Terminal**. A little
command line appears at the bottom. That's where you'll type things.

---

## Step 3 — Make your virtual environment

Type these one at a time, hitting Enter after each:

```
py -m venv venv
```

```
venv\Scripts\activate
```

After the second one, your terminal line should start with `(venv)`.

**What did that just do?** It made a private toolbox for this project. Any
library you install goes in that toolbox instead of getting dumped all over
your computer. That way this project's tools can never break some other
project's tools.

⚠️ You have to run `venv\Scripts\activate` **every time** you open a new
terminal. If you ever get a weird "module not found" error, check for `(venv)`
first — nine times out of ten that's it.

---

## Step 4 — Install the libraries

```
pip install -r requirements.txt
```

This reads the `requirements.txt` file and installs everything your app needs.
It'll spit out a wall of text. That's normal.

---

## Step 5 — Start your website 🚀

```
uvicorn main:app --reload
```

Now open your browser and go to:

```
http://127.0.0.1:8000
```

**You should see your Lost & Found homepage.**

That address means "this computer, door number 8000." The site is only running
on your laptop — nobody else on the internet can see it. That's exactly what
you want for now.

The `--reload` part means the server watches your files and restarts itself
every time you save. So you can edit code, hit save, refresh the browser, and
see the change instantly. You'll use that about 400 times.

To stop the server, click the terminal and press **Ctrl + C**.

---

## Step 6 — Save it to GitHub

```
git init
git add .
git commit -m "Starting my Lost and Found app"
```

Then on github.com, make a new repository called `lost-and-found`, and follow
the two lines it shows you to push your code up.

**Do this every single time you finish working.** It's your undo button for the
whole project. If you ever break something badly, you can go back to a version
that worked.

---

## If something goes wrong

It will. That's not a bad sign, that's just programming. Here's the checklist
before you panic:

| The error says | Try this |
|---|---|
| `'python' is not recognized` | The PATH checkbox. Reinstall Python and check it. |
| `'uvicorn' is not recognized` | You're not in the venv. Run `venv\Scripts\activate` |
| `No module named 'fastapi'` | Same thing — activate the venv, then install again |
| `Address already in use` | The server's already running in another terminal. Ctrl+C it, or use `--port 8001` |
| Page won't load | Is the terminal still running? It has to stay open. |

Still stuck after 15 minutes of trying? Come ask me. Bring the **exact** error
message — copy and paste the whole thing. "It doesn't work" is impossible to
help with; a real error message is usually solvable in about a minute.

---

## What's in this folder

| File | What it's for | Who writes it |
|---|---|---|
| `main.py` | Your web pages and routes | Mostly you |
| `database.py` | Saving and loading items | You |
| `models.py` | What an "item" looks like | You |
| `matching.py` | ⭐ The matching brain | **All you** |
| `templates/` | Your HTML pages | You |
| `static/style.css` | How it looks | Already done — free gift |
| `tests/test_matching.py` | Checks your matching code | Already done — your target |
| `AI_USAGE.md` | Log of AI help | You, every week |

---

## Two things I already did for you

**The CSS is done.** `static/style.css` is already written, and it makes your
app look like the mockup. Design isn't what you're being judged on, and staring
at ugly gray text for 10 weeks is demoralizing. Change any colors you want —
they're all at the top of the file.

**The tests are written.** `tests/test_matching.py` describes exactly what your
matching code has to do. Run it with:

```
pytest
```

Right now everything fails. That's correct! Your job over the next few weeks is
to make them pass one at a time. It's like having the answer key to a puzzle
without the solution — you know when you're right.

---

## Now go

Do Steps 1–6. Get that page on the screen. Then tell me and we'll start Week 1.
