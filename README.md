# Python Battlesnake

Watch my snake in action [here](https://play.battlesnake.com/s/snk_9gM8RBkRrDjrCKvF9Mrd9qfc/).

## Info

My [Battlesnake AI](http://battlesnake.io) is written in Python. It currently uses A\* and other logic to determine the best path to gather food and follow its tail.

Visit [https://github.com/battlesnakeio/community/blob/master/starter-snakes.md](https://github.com/battlesnakeio/community/blob/master/starter-snakes.md) for API documentation and instructions for running the AI.

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

## Basic Logic

1. Create a Variables object with all the relevant information
1. Populate a board with given information (size, your location, opposing snake locations, food)
1. Populate the board with special symbols for bigger snake's possible moves
1. Populate the board with special symbols for dead ends
1. Determine move
   1. Decide if we need to eat
      1. Check if it is safe to eat
      1. Use A* to navigate to closest food
      1. Otherwise, chase our tail or move toward free space
   1. If we don't need to eat we chase our tail or move toward free space

## Todo

- Better predict path of larger snakes
- Avoid edges of the board / try to chase tail in free space
- Check if I am closer to food
- Factor if tail will be there in flood flow
- Zone off snakes
- Change snake tactic depending on amount of snakes left and how long the game has been going
- Keep track of wins/losses

## Running the Snake Locally

#### You will need...

- a working Python 3.7 development environment
- [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies

1. [Fork this repo](https://github.com/OliverMKing/Battlesnake/fork).

2. Clone repo to your development environment:

```
git clone git@github.com:<your github username>/Battlesnake.git
```

3. Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):

```
pip install -r requirements.txt
```

4. Run local server:

```
python app/main.py
```

5. Test your snake by sending a curl to the running snake

```
curl -XPOST -H 'Content-Type: application/json' -d '{ "hello": "world"}' http://localhost:8080/start
```

## Deploying to Heroku

1. Create a new Heroku app:

```
heroku create [APP_NAME]
```

2. Deploy code to Heroku servers:

```
git push heroku master
```

3. Open Heroku app in browser:

```
heroku open
```

or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4. View server logs with the `heroku logs` command:

```
heroku logs --tail
```
