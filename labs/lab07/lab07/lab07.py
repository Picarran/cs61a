def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are all true values
    
    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    "*** YOUR CODE HERE ***"
    if x:
        yield x
        yield from amplify(f,f(x))


class Person:
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat()       # initialized person has the below starting repeat phrase!
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    repeat_content = None

    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"
        self.repeat_content = 'I squirreled it away before it could catch on fire.'

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.repeat_content = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.say(self.repeat_content)


class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Oh no, we need more Mayo!'
    >>> fridgey.add_item('Eggs', 12)
    'I now have 12 Eggs'
    >>> fridgey.use_item('Eggs', 15)
    'Oh no, we need more Eggs!'
    >>> fridgey.add_item('Eggs', 1)
    'I now have 1 Eggs'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += quantity
        print("'I now have {0} {1}'".format(self.items[item], item))

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if self.items[item]<=quantity:
            self.items[item]=0
            print("'Oh no, we need more {0}!'".format(item))
        else:
            self.items[item]-=quantity
            print("'I have {0} {1} left'".format(self.items[item],item))


class CucumberGame:
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> g = CucumberGame()
    >>> g.play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    >>> g.winners
    [1]
    >>> g.play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It is not your turn, player 3
    It is not your turn, player 0
    The round is over, player 1
    >>> g.winners
    [1, 3]
    >>> g.play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It is not your turn, player 2
    >>> g.winners
    [1, 3]
    """

    def __init__(self):
        self.winners = []

    def play_round(self, starter, cards):
        r = Round(starter)
        for who, card in cards:
            try:
                r.play(who, card)
            except AssertionError as e:
                print(e)
        if r.winner != None:
            self.winners.append(r.winner)


class Round:
    players = 4
    cnt = 1

    def __init__(self, starter):
        self.starter = starter
        self.next_player = starter
        self.highest = -1
        self.winner = None
        self.tmp_winner = None

    def play(self, who, card):
        assert not self.is_complete(), f'The round is over, player {who}'
        assert who == self.next_player, f'It is not your turn, player {who}'
        self.next_player = (who+1)%4
        if card >= self.highest:
            self.highest = card
            self.tmp_winner = who
        self.cnt += 1

        if self.is_complete():
            self.winner = self.tmp_winner

    def is_complete(self):
        """ Checks if a game could end. """
        return self.cnt > self.players


g = CucumberGame()
g.play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
g.play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])