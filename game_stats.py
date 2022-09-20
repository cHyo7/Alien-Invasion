class GameStats():
    """Track statistic for Allien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0

        # Start the game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statitisc that cand change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

