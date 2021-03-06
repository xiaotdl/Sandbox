class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Init the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship settings.
        self.ship_speed_factor = 20
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed_factor = 100
        self.bullet_width = 400
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings.
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
