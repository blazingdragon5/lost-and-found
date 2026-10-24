# Lost & Found App

A web app that helps students get their lost stuff back. When you report
something you lost, it searches everything that's been turned in and shows you
the closest matches — and explains why it thinks they match. It then proceeds 
to show the contact information from the reporter along with a pickup code so 
you can get your item back quickly and safely.

Built for the 2026 Congressional App Challenge.
---

## The problem

Current Lost & Found systems that schools use are very disorganized. Usually, it's just a box that has piles of clothes, water bottles, backpacks, and other belongings. Students have to search through everything to find their missing items, which can be frustrating and time-consuming. I know this problem personally because I once lost my own water bottle at school and never found it again. It made me realize how easy it is for belongings to get lost in a pile of unorganized items, even when someone might have turned them in. This experience inspired me to create the Lost & Found App. I wanted to make it easier for students to find their missing belongings without having to dig through a box full of random items. By allowing students to report lost and found items online and automatically showing possible matches, my app aims to make the process faster, easier, and more organized.

## What it does

- Report a lost item
- Report a found item, with a photo
- Search and filter everything
- **Suggests matches with a 0–100 confidence score and plain-English reasons**
- Mark items as claimed
- Stats page showing return rate

## How the matching works

The app compares lost and found items using their category, date, description, color, and location. Items with different categories or dates that do not make sense are rejected. Otherwise, the app awards points for matching details, including shared description words, matching colors, and locations. The final score is capped at 100, and the app displays reasons explaining the match.
For example:
- Common words in the description each add 10 point (Capped at 50)
- Same location the item is lost and found in adds 20 points
- Common colors add 15 each (Capped at 30)
- Same category of item adds 15 points while score set to 0 if it doesn't match
- If dates don't make sense, score set to 0
- Total score is capped at 100 and the program shows the top 4 results

## Built with

Python · FastAPI · SQLite · Jinja2 · Pillow

See `CREDITS.md` for the full list of libraries and `AI_USAGE.md` for how AI
was used.

## Running it yourself

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000

## Testing

```bash
pytest
```

## What I learned




## Roadmap / Future Improvements

I would make several improvements to my app in a Version 2.0. These improvements would focus on making the app more useful, efficient, and user-friendly. I chose these improvements based on what I believe would make the app better, as well as feedback from users who tested it.

1. I want to make my app multitenant which means that it can be used by multiple institutions. For example, an app used by one school would only show items that were reported by members of that school. This would make my app better because currently I can really only use my app in one institution because a waterbottle lost in one school has a very low chance of being found in another school which will make finding your items more confusing. Also, when you report an item you could include location which is sometimes specific to a institution like Classroom A105.

2. Another improvement thatt would be beneficial to my app would be deploying it on the app store so people can use it on their phones instead of only using it on the web. This would be beneficial because if you're in the middle of something, using your mobile phone is way more convenient than having to take out your laptop and sit somewhere to use it.

3. Another improvement I would make is adding an automatic notification system. Currently, users have to return to the app and check whether a potential match has appeared for their lost item. In Version 2.0, users could receive an email or phone notification when someone reports an item that closely matches theirs. This would make the app more convenient because students wouldn't have to repeatedly check the website, and they could find their belongings sooner. I would make this notification so it only appears when the math is 90 percent or higher so you don't get a bombardment of notifications.

I would prioritize changes that address users' difficulties and make finding lost belongings easier. My goal would be to continue improving the app based on real user needs.

Built by Aditya Sawant · 2026 Congressional App Challenge
