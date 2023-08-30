# ***Problem Statement***
# As a scientist at ISRO controlling the latest lunar spacecraft Chandrayaan 3, 
# your task is to develop a program that translates commands sent from Earth into 
# instructions understood by the spacecraft. The spacecraft navigates through the 
# galaxy using galactic coordinates, represented by x, y, z coordinates 
# (x for east or west location, y for north or south location, 
# and z for distance above or below the galactic plane).


# ***Here are the controls of the Chandrayaan 3 Lunar Craft: Galactic Space Craft***
# Enter this commands in command array
#     f for move forward
#     b for move backward
#     l for turning left
#     r for turning right
#     u for turning upward
#     d for turning downward



# for testing the code of Chandrayaan3

import unittest 
from Chandrayaan3 import Chandrayaan3

class NamesTestCase(unittest.TestCase):

   def test_chandrayaan3(self):
       command = ["f","r","u","b","l"]                          #command
       
       chandrayaan = Chandrayaan3()
       chandrayaan.process_commands(command)
       final_position = chandrayaan.get_position()
       final_direction = chandrayaan.get_direction()
       
       # testing final co-ordinates
       self.assertEqual(final_position,  (0, 1, -1)) 
                          
       # testing final direction
       self.assertEqual(final_direction,  "N")
       

if __name__ == "__main__":
    unittest.main()