import unittest
import mastermind
from unittest.mock import patch
from io import StringIO
import sys

class  MyTestC(unittest.TestCase):
    
    def test_create_code(self):

        output = StringIO()
        sys.stdout = output

        for i in range(0,100):
            self.assertEqual(len(set(mastermind.create_code())), 4) #checks for duplicates
            self.assertNotIn(int(9), mastermind.create_code())
            self.assertNotIn(int(0), mastermind.create_code())

    #@patch('sys.stdin' ,StringIO("1234\n"))
    def test_check_correctness(self):

        output = StringIO()#hides the output basically
        sys.stdout = output
        self.assertEqual(mastermind.check_correctness(11,4,True), True)#checking if correct_digits_and_position is 4 that it is true

        output = StringIO()
        sys.stdout = output
        mastermind.check_correctness(11,4,True)
        self.assertEqual("Congratulations! You are a codebreaker!\n",output.getvalue())#returning congratulations... if true

        output = StringIO()
        sys.stdout = output
        self.assertEqual(mastermind.check_correctness(11,3, False), False)

        output = StringIO()
        sys.stdout = output#output = mastermind code
        mastermind.check_correctness(1,3,False)#It's one because it took away ONE turn,so 11 is left or should be left
        self.assertEqual("Turns left: 11\n",output.getvalue())

    @patch("sys.stdin",StringIO("123\n"))
    def test_get_answer_input(self):

        output = StringIO()
        sys.stdout = output
   
        mastermind.get_answer_input()
        self.assertEqual("""Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: """, output.getvalue())

    @patch("sys.stdin",StringIO("1243\n"))
    def test_take_turns(self):

        output = StringIO()
        sys.stdout = output

        mastermind.take_turn([1,2,3,4])
        self.assertEqual("""Input 4 digit code: Number of correct digits in correct place:     2
Number of correct digits not in correct place: 2\n""", output.getvalue())

    @patch("sys.stdin",StringIO())
    def test_instructions(self):

        output = StringIO()
        sys.stdout = output

        mastermind.show_instructions()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.\n""", output.getvalue())

    
if __name__ == "__main__":
    unittest.main()
