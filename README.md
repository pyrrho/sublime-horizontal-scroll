Horizontal Scroll
=========================

for [Sublime Text 2][0] or [3][3]

-------------

Ever wanted to scroll horizontally in Sublime Text with your keyboard?  
Well. Now you can.

## Installation

**Step 1** -- Go get wbond's beautifully simple [Sublime Package-Control][2].  
**Step 2** -- Hit `ctrl+shift+p` (Windows, Linux) or `cmd+shift+p` (OSX), run the `install package` command.  
**Step 3** -- Search for and install _Horizontal Scroll_.

**Step 4** -- Win and/or Profit.

-----

## Usage

#### The Short

Is there text running off the edge of your editor?  
Is this plug-in installed?  
Press `alt+down`. Or `ctrl+alt+shift+down` if you're on a Mac.

There weren't any good hotkeys left! I'm sorry!


#### The Long

This plug-in adds one command to Sublime Text which exposes easy-to-hotkey horizontal scrolling, and makes a guess as to how to incorporate it for you.

By default, the hotkeys to scroll right and left are, respectively, `alt+down` and `alt+up` for Windows/Linux, or `ctrl+alt+shift+down` and `ctrl+alt+shift+up` if you're on a Mac -- chosen to reflect Sublime's default `scroll_lines` behavior (`ctrl+up/down` and `ctrl+alt+up/down`). This, of course, can be mapped to any hotkey combination you might by want by modifying your personal `Preferences -> Key Bindings - User`. (And seriously, if you're on a Mac, please do.)

The command that this plug-in adds is (at most):

    "command": "scroll_width", "args": {"amount": [+/-]30, "by_character": True}

If `by_character` is left `True` motion is based on the width of an em-dash, which allows this command to scale motion with your current font size. If `by_character` is `False`, `scroll_width` will move the screen by `amount` of raw pixels. I'd recommend pumping `amount` up to at least 150 if you're not scrolling `by_character`.  
`by_character` defaults to `True`, by the way, so if you ever set this command up -- when, say, rebinding the Mac keys -- you can skip that argument.  
`amount` is simply a relative indicator of how far every call to `scroll_width` will move the screen, with negative scrolling the screen left.  

-----

**This project is open under the [MIT License][1]**

 [0]: http://www.sublimetext.com/2
 [1]: http://revolunet.mit-license.org
 [2]: http://wbond.net/sublime_packages/package_control/installation
 [3]: http://www.sublimetext.com/3
