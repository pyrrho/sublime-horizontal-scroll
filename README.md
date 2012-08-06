Horizontal Scroll
=========================

for [Sublime Text 2][0]

-------------

Ever wanted to scroll horizontally in Sublime Text 2 with your keyboard?  
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
Press `alt+down`.

Done.



#### The Long

This plug-in adds one command to Sublime Text 2 which exposes easy-to-hotkey horizontal scrolling, and makes a guess as to how to incorporate it for you.

By default, the hotkeys to scroll right and left are `alt+down` and `alt+up` respectively -- chosen to reflect Sublime's default `scroll_lines` behavior (`ctrl+up/down`). This, of course, can be mapped to any hotkey combination you might by want by modifying your personal `Preferences -> Key Bindings - User`.

The command that this plug-in adds is (at most) this:

    "command": "scroll_width", "args": {"amount": [+/-]30, "by_character": True}

`by_character` defaults to `True`, so if you ever set this command up, you can skip that argument.  
`amount` is simply an indicator of how far every call to `scroll_width` will move the screen (negative to scroll left).  
If `by_character` is left `True` motion is based on the width of an em-dash, thereby scaling motion with your current font size. If `by_character` is `False`, `scroll_width` will move the screen by `amount` of raw pixels. I'd recommend pumping `amount` up to at least 150 if you're not scrolling `by_character`. 

-----

**This project is open under the [MIT License][1]**

 [0]: http://www.sublimetext.com/2
 [1]: http://revolunet.mit-license.org
 [2]: http://wbond.net/sublime_packages/package_control