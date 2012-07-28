Horizontal Scroll
=========================

for [Sublime Text 2][0]

-------------

Ever wanted to scroll horizontally in Sublime Text 2?  
Well. Now you can.

### Installation

Actually, I'm not set up there yet, so I'm going to focus on getting this package made before providing installation instructions.

### Usage

The easiest way to get this functionality up and running is to add the following lines to your `Preferences -> Key Bindings - User` file.

        { "keys": ["alt+up"], "command": "scroll_width", "args": {"amount": 30 } },
        { "keys": ["alt+down"], "command": "scroll_width", "args": {"amount": -30 } },

Now, to compliment Sublime's `ctrl+up` and `ctrl+down` mappings to the `scroll_lines` command, `alt+up` will scroll your editor window to the right, and `alt+down` will scroll back to the left.

These commands can be further customized with two arguments:

  * ` "ammount"` --- The larger the number, the farther you'll scroll.
  * ` "by"     ` --- Defines what the amount you scroll is relative to. Accepts one of two values: 
    * `"characters"` --- Scales based on you current font size
    * `"points"    ` --- This might actually be by pixels, not points. I'm not really sure.

----------------

**This project is open under the [MIT License][1]**

 [0]: http://www.sublimetext.com/2
 [1]: http://revolunet.mit-license.org
 [2]: http://wbond.net/sublime_packages/package_control