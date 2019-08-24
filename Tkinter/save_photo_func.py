from pyscreenshot import grab
import random
import string
import os
import wx

# def shot(show = 0):
#     app = wx.App(False) # the wx.App object must be created first.
#     w, h = wx.GetDisplaySize()  # returns a tuple
#
#     full = (0, 0, w, h)
#
#     path = '/Users/fsociety/Desktop/'
#
#     name = ''
#
#     for _ in range(8):
#         name += random.choice(string.ascii_letters)
#
#     im = grab(bbox=full)
#     im.save(path + name + '.png')
#     if show == 1:
#         im.show()

def save_photo(photo):
    path = '/Users/fsociety/Desktop/images/'

    name = ''

    for _ in range(8):
        name += random.choice(string.ascii_letters)

    photo.save(path + name + '.png')
