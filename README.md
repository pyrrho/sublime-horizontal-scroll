Horizontal Scroll
=========================

for [Sublime Text 2][0]

-------------

Ever wanted to scroll horizontally in Sublime Text 2 with your keyboard?  
Well. Now you can.

### Installation

Actually, I'm not set up there yet, so I'm going to focus on getting this package made before providing installation instructions.

-----

## The Short

Is this plug-in installed?  
Is there text running off the edge of your editor?  
Press `alt+up`.

Done.

-----

## The Long

This plug-in adds one command to Sublime Text 2 which exposes an easy-to-use horizontal scrolling, and makes a guess as to how to incorporate it for you.  
By default, the hotkeys to scroll right and left are `alt+up` and `alt+down` respectively -- chosen to reflect Sublime's default `scroll_lines` behavior (`ctrl+up/down`). This, of course, can be mapped to any hotkey combination you might by want by modifying your personal `Preferences -> Key Bindings - User`.

The command that this plug-in adds is (at most) this:

    "command": "scroll_width", "args": {"by_character": True, "amount": 30}

`amount` is simply and indicator of how far every call to `scroll_width` will move the screen. If `by_character` is set left `True` motion is based on the width of the average character, thereby scaling with your font size. If `by_character` is `False`, `scroll_width` will move the screen by `amount` of pixels (I'd strongly recommend pumping `amount` up to at least 150 if you're not scrolling `by_character`). 

-----

**This project is open under the [MIT License][1]**

 [0]: http://www.sublimetext.com/2
 [1]: http://revolunet.mit-license.org
 [2]: http://wbond.net/sublime_packages/package_control