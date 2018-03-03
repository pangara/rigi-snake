import bottle
import os
from Game import Game

games = {}


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    data["id"] = data["game_id"]
    games[data["game_id"]] = Game(data)
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
    return {
        'color': '#BADA55',
        'taunt': 'from the sneakerson family of snakes',
        'head_url': head_url,
        'name': 'Sneakey Sneakerson'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    return {
        print "game id-------------", games[data["id"]]
        'move': games[data["id"]].move(data),
        'taunt': 'Good ol sneakeys baaack'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8081'))
