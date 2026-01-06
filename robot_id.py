# robot_id.py
robots = {
    "RoboA": {"mass": 2.0, "max_velocity": 1.0},
    "RoboB": {"mass": 5.0, "max_velocity": 0.5}
}

def effort_to_signal(robot_id, effort_percent):
    r = robots[robot_id]
    return effort_percent * r["max_velocity"]
