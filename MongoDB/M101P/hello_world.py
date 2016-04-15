import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach', 'angoor', 'nashpati', 'leechee']

    ##### return "<html><title>Title testing</title><body>Hello World !!!\n by G Singh\n</body></html>" # This is my addition to test the program


    # return bottle.template('hello_world', username='Andrew', things=mythings)
    return bottle.template('hello_world', {'username':"Richard", 'things':mythings})


@bottle.route('/testpage')
def test_page():
    return "This is a test page added by G Singh for testing \n" # This is my addition to test the program


@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"
    return bottle.template('fruit_selection.tpl', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=7777)
