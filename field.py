class fields():
    def __init__(self, right=None, left=None, top=None, bottom=None):
        self.value = None
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom

    def reset_value(self):
        self.value = None

    def merge_value(self, field):
        """Merges the current value with another field."""
        if field.value is not None and self.value == field.value:
            field.value *= 2
            self.reset_value()

    def move(self, side):
        """Moves value to the empty neighbor in the given direction."""
        target = None
        if side == "right" and self.right and self.right.value is None:
            target = self.right
        elif side == "left" and self.left and self.left.value is None:
            target = self.left
        elif side == "top" and self.top and self.top.value is None:
            target = self.top
        elif side == "bottom" and self.bottom and self.bottom.value is None:
            target = self.bottom
        
        if target:
            target.value = self.value
            self.reset_value()

    def merge(self, side):
        """Merges value with the neighboring tile if they are equal."""
        target = None
        if side == "right":
            target = self.right
        elif side == "left":
            target = self.left
        elif side == "top":
            target = self.top
        elif side == "bottom":
            target = self.bottom
        
        if target and self.value is not None and self.value == target.value:
            self.merge_value(target)
