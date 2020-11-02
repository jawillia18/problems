import unittest
from unittest.mock import patch
from io import StringIO
import robot
import sys

class  MyTestC(unittest.TestCase):
    @patch("sys.stdin", StringIO(" \nJay\n"))
    def test_robot_name(self):
        
        output = StringIO()
        sys.stdout = output

        robot.robot_name()
        self.assertEqual(output.getvalue(),"""What do you want to name your robot? """)
    
    def test_robot_response(self):

        output = StringIO()
        sys.stdout = output

        robot.robot_response("Jay")
        self.assertEqual(output.getvalue(),"Jay: Hello kiddo!\n")

    @patch("sys.stdin", StringIO(" \nJay\nForward 10\n"))
    def test_action_prompt(self):

        output = StringIO()
        sys.stdout = output

        robot.action_prompt("Jay","forward")
        self.assertEqual(output.getvalue(),"""Jay: What must I do next? ""","""Jay: Sorry I don't understand 'Jay'\nJay: What must I do next? """)


    @patch("sys.stdin",StringIO("Jay\nrun\nhop\n""\noff\n"))
    def test_dontunderstand(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next? Jay: Sorry, I did not understand 'run'.
Jay: What must I do next? Jay: Sorry, I did not understand 'hop'.
Jay: What must I do next? Jay: Sorry I did not understand
Jay: What must I do next? Jay: Shutting down..\n""")

    def test_split(self):

        self.assertEqual(robot.split("forward 10","FORWARD","Jay"),("forward",10))



    @patch("sys.stdin",StringIO("Jay\nhelp\noff\n"))
    def test_setcommands(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
BACK - Moves the robot backward a certain amount
RIGHT - Turns 90 degrees to the right
LEFT - Turns 90 degrees to the left
SPRINT - Sprint gives it a short burst of speed and some extra distance
FORWARD - Moves robot forward a certain amount
Jay: What must I do next? Jay: Shutting down..\n""")

        @patch("sys.stdin",StringIO("Jay\nforward 10\noff\n"))
        def test_forward(self):

            output = StringIO()
            sys.stdout = output
            robot.robot_start()

            self.assertEqual(output.getvalue(),"""What do you want to name your robot? 
Jay: Hello kiddo!
Jay: What must I do next? 
 > Jay moved forward by 10 steps.
 > Jay now at position (0,10).
Jay: What must I do next? 
Jay: Shutting down..""")

    @patch("sys.stdin",StringIO("Jay\nback 10\noff\n"))
    def test_backward_motion(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved back by 10 steps.
 > Jay now at position (0,-10).
Jay: What must I do next? Jay: Shutting down..\n""")

    
    @patch("sys.stdin",StringIO("Jay\nforward 10\nright\nforward 10\noff\n"))
    def test_right_forward(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (0,10).
Jay: What must I do next?  > Jay turned right.
 > Jay now at position (0,10).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (10,10).
Jay: What must I do next? Jay: Shutting down..\n""")
    
    
    @patch("sys.stdin",StringIO("Jay\nback 10\nright\nforward 10\nright\nforward 10\noff\n"))
    def test_right_right(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved back by 10 steps.
 > Jay now at position (0,-10).
Jay: What must I do next?  > Jay turned right.
 > Jay now at position (0,-10).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (10,-10).
Jay: What must I do next?  > Jay turned right.
 > Jay now at position (10,-10).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (10,-20).
Jay: What must I do next? Jay: Shutting down..\n""")


    @patch("sys.stdin",StringIO("Jay\nforward 10\nleft\nback 10\nleft\nforward 10\noff\n"))
    def test_left_forward_back(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (0,10).
Jay: What must I do next?  > Jay turned left.
 > Jay now at position (0,10).
Jay: What must I do next?  > Jay moved back by 10 steps.
 > Jay now at position (10,10).
Jay: What must I do next?  > Jay turned left.
 > Jay now at position (10,10).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (10,0).
Jay: What must I do next? Jay: Shutting down..\n""")


    @patch("sys.stdin",StringIO("Jay\nforward 10\nsprint 5\noff\n"))
    def test_sprint(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay now at position (0,10).
Jay: What must I do next?  > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
 > Jay now at position (0,25).
Jay: What must I do next? Jay: Shutting down..\n""")


    @patch("sys.stdin",StringIO("Jay\nforward 100\nforward 101\nforward 201\nleft\nforward 100\nforward 1\nforward 101\noff\n"))
    def test_arealimit_forward(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved forward by 100 steps.
 > Jay now at position (0,100).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay turned left.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay moved forward by 100 steps.
 > Jay now at position (-100,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Shutting down..\n""")


    @patch("sys.stdin",StringIO("Jay\nback 100\nback 101\nback 201\nright\nback 60\nback 50\nback 101\noff\n"))
    def test_arealimit_back(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved back by 100 steps.
 > Jay now at position (0,-100).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay turned right.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay moved back by 60 steps.
 > Jay now at position (-60,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next? Jay: Shutting down..\n""")


    @patch("sys.stdin",StringIO("Jay\nsprint 5\nsprint 10\nsprint 20\nright\nsprint 30\nsprint 10\nsprint 5\noff\n"))
    def test_arealimit_sprint(self):

        output = StringIO()
        sys.stdout = output
        robot.robot_start()

        self.assertEqual(output.getvalue(),"""What do you want to name your robot? Jay: Hello kiddo!
Jay: What must I do next?  > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
 > Jay now at position (0,15).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay moved forward by 9 steps.
 > Jay moved forward by 8 steps.
 > Jay moved forward by 7 steps.
 > Jay moved forward by 6 steps.
 > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
 > Jay now at position (0,70).
Jay: What must I do next?  > Jay moved forward by 20 steps.
 > Jay moved forward by 19 steps.
 > Jay moved forward by 18 steps.
 > Jay moved forward by 17 steps.
 > Jay moved forward by 16 steps.
 > Jay moved forward by 15 steps.
 > Jay moved forward by 14 steps.
 > Jay moved forward by 13 steps.
 > Jay moved forward by 12 steps.
 > Jay moved forward by 11 steps.
 > Jay moved forward by 10 steps.
 > Jay moved forward by 9 steps.
 > Jay moved forward by 8 steps.
 > Jay moved forward by 7 steps.
 > Jay moved forward by 6 steps.
 > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay turned right.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay moved forward by 30 steps.
 > Jay moved forward by 29 steps.
 > Jay moved forward by 28 steps.
 > Jay moved forward by 27 steps.
 > Jay moved forward by 26 steps.
 > Jay moved forward by 25 steps.
 > Jay moved forward by 24 steps.
 > Jay moved forward by 23 steps.
 > Jay moved forward by 22 steps.
 > Jay moved forward by 21 steps.
 > Jay moved forward by 20 steps.
 > Jay moved forward by 19 steps.
 > Jay moved forward by 18 steps.
 > Jay moved forward by 17 steps.
 > Jay moved forward by 16 steps.
 > Jay moved forward by 15 steps.
 > Jay moved forward by 14 steps.
 > Jay moved forward by 13 steps.
 > Jay moved forward by 12 steps.
 > Jay moved forward by 11 steps.
 > Jay moved forward by 10 steps.
 > Jay moved forward by 9 steps.
 > Jay moved forward by 8 steps.
 > Jay moved forward by 7 steps.
 > Jay moved forward by 6 steps.
 > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
Jay: Sorry, I cannot go outside my safe zone.
 > Jay now at position (0,0).
Jay: What must I do next?  > Jay moved forward by 10 steps.
 > Jay moved forward by 9 steps.
 > Jay moved forward by 8 steps.
 > Jay moved forward by 7 steps.
 > Jay moved forward by 6 steps.
 > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
 > Jay now at position (55,0).
Jay: What must I do next?  > Jay moved forward by 5 steps.
 > Jay moved forward by 4 steps.
 > Jay moved forward by 3 steps.
 > Jay moved forward by 2 steps.
 > Jay moved forward by 1 steps.
 > Jay now at position (70,0).
Jay: What must I do next? Jay: Shutting down..\n""")




if __name__ == "__main__":  
    unittest.main()