class RobotID:
    """Stores robot-specific capabilities and translates to universal dictionary."""
    def __init__(self, robot_name, max_speed, mass, signal_type='servo'):
        self.name = robot_name
        self.max_speed = max_speed  # Maximum possible speed (for scaling)
        self.mass = mass            # Mass for energy computations
        self.signal_type = signal_type  # servo, LED, vibration, etc.

    def effort_to_perceptual(self, effort_percent, psychophysics_func):
        """
        Map relative effort (0-1) to perceived intensity using psychophysics.
        """
        actual_velocity = effort_percent * self.max_speed
        return psychophysics_func(actual_velocity)
