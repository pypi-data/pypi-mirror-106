#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, Separator
from pprint import pprint

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen



def formstyle():

    return style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })


def modstyle():

    return style_from_dict({
        Token.Separator: '#00cc00',
        Token.QuestionMark: '#ffcc00 bold',
        Token.Selected: '#00cc00',  # default
        Token.Pointer: '#ffcc00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#ffcc00 bold',
        Token.Question: '',
    })
# may move this to it's own module later
# say to develop full interactive version of Autocleus using 
# asciimattics/bullet/click/PyInquirer...whatever works.
def autocleus_homescreen(screen):

    effects = [
        Cycle(
            screen,
            FigletText("Autocleus", font='isometric3'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen, 
            FigletText("Press spacebar to continue", font='rectangles'),
            int(screen.height / 2 + 3)),
        Stars(screen, 100)
    ] 

    screen.play([Scene(effects, 200)], repeat=False)

def autocleus_banner():
    Screen.wrapper(autocleus_homescreen)