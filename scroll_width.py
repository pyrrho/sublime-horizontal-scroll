import sublime, sublime_plugin

class ScrollWidthCommand(sublime_plugin.TextCommand):
    def run(self, edit, amount, by_character=True):
        old_position = self.view.viewport_position()
        delta = amount * (self.view.em_width() if by_character else 1)
        new_x = old_position[0] + delta

        # Are we moving right?
        if (amount > 0):
            viewport_width = self.view.viewport_extent()[0]
            layout_width = self.view.layout_extent()[0]
            # If moving the desired amount would set us past the rendered
            # characters (e.g. there's no extending text, or Word Wrap is on),
            # pull back the `new_x` variable some. 
            if new_x + viewport_width > layout_width:
                new_x = layout_width - viewport_width
        else:
            # If we're about to scroll past column 0, just.. don't.
            # This may be a superflous test, actually, I'm not sure.
            if new_x < 0:
                new_x = 0

        # Finally, perform the scroll.
        self.view.set_viewport_position((new_x, old_position[1]), True)
