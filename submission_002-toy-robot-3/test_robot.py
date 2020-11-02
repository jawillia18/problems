import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import robot

class TestToyRobot(unittest.TestCase):
    def test_get_robot_name(self):
        with captured_io(StringIO('Jay\n')):
            self.assertEqual(robot.get_robot_name(), 'Jay')

    def test_get_command(self):
        with captured_io(StringIO('Forward 10')):
            self.assertEqual(robot.get_command('Jay'),'forward 10' )

    def test_split_command_input(self):
        with captured_io(StringIO('back 5')):
            self.assertEqual(robot.get_command('back 5'),'back 5' )

    def test_is_int_true(self):
        with captured_io(StringIO('Forward 10')):
            self.assertEqual(robot.is_int('10'),True )
            
    def test_is_int_false(self):
        with captured_io(StringIO('Forward hj')):
            self.assertEqual(robot.is_int('hj'),False )

    def test_valid_command_invalid(self):
        with captured_io(StringIO('Forward Forward 5')):
            self.assertEqual(robot.is_int('Forward 5'),False )

    def test_valid_command_is_valid(self):
        with captured_io(StringIO('forward 5')):
            self.assertEqual(robot.valid_command('forward 5'),True )


    def test_valid_command_reversed_command(self):
        with captured_io(StringIO('5 forward')):
            self.assertEqual(robot.valid_command('5 forward'),False )


    def test_valid_command_replay_silent(self):
        with captured_io(StringIO('replay silent')):
            self.assertEqual(robot.valid_command('replay silent'),True )
    

    def test_valid_command_replay_reversed(self):
        with captured_io(StringIO('replay reversed')):
            self.assertEqual(robot.valid_command('replay reversed'),True )


    def test_valid_command_replay_reversed_silent(self):
        with captured_io(StringIO('replay silent')):
            self.assertEqual(robot.valid_command('replay reversed silent'),True )

    
    def test_do_help(self):
        self.assertEqual(robot.do_help(),(True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - Command that must filter out all non-movement commands and redo only the movement commands
REPLAY SILENT - Replays the commands but only prints out the new co-ordinates
REPLAY REVERSE - replays commands in reverse
REPLAY REVERSE SILENT - combines the function of the replay silent and replay reverse
"""))

    def test_is_position_allowed_true(self):
        self.assertEqual(robot.is_position_allowed(500,500), False)
    

    def test_is_position_allowed_false(self):
        self.assertEqual(robot.is_position_allowed(50,50), True)

    def test_update_position_true(self):
        self.assertEqual(robot.update_position(5),True ) 

    def test_update_position_false(self):
        self.assertEqual(robot.update_position(5000), False)


if __name__ == "__main__":
    unittest.main()