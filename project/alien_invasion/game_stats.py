class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Init statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """init statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
