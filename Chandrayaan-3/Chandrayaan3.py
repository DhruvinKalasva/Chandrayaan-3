# Chandrayaan3 Class
class Chandrayaan3:
    def __init__(self):         #initialization
        self.x = 0
        self.y = 0
        self.z = 0
        self.direction = "N"

    # function for movement
    def move(self, command):                        # move Command

        if command == 'f':                          # move Forward
            if self.direction == 'N':
                self.y += 1
            elif self.direction == 'S':
                self.y -= 1
            elif self.direction == 'E':
                self.x += 1
            elif self.direction == 'W':
                self.x -= 1
            elif self.direction == 'UP':
                self.z += 1
            elif self.direction == 'DOWN':
                self.z -= 1

        elif command == 'b':                         # move Backward
            if self.direction == 'N':
                self.y -= 1
            elif self.direction == 'S':
                self.y += 1
            elif self.direction == 'E':
                self.x -= 1
            elif self.direction == 'W':
                self.x += 1
            elif self.direction == 'UP':
                self.z -= 1
            elif self.direction == 'DOWN':
                self.z += 1

    # function for taking turns
    def turn(self, command,directionList):          # turning direction

        if command == 'l':                          # turning left
            if self.direction == 'N':
                self.direction = 'W'
            elif self.direction == 'S':
                self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'N'
            elif self.direction == 'W':
                self.direction = 'S'

            elif self.direction == 'UP' or self.direction == 'DOWN':
                if directionList[-2] == 'N':
                    self.direction = 'W'
                elif directionList[-2] == 'S':
                    self.direction = 'E'
                elif directionList[-2] == 'E':
                    self.direction = 'N'
                elif directionList[-2] == 'W':
                    self.direction = 'S'


        elif command == 'r':                        # turning right
            if self.direction == 'N':
                self.direction = 'E'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'E':
                self.direction = 'S'
            elif self.direction == 'W':
                self.direction = 'N'

            elif self.direction == 'UP' or self.direction == 'DOWN':
                if directionList[-2] == 'N':
                    self.direction = 'E'
                elif directionList[-2] == 'S':
                    self.direction = 'W'
                elif directionList[-2] == 'E':
                    self.direction = 'S'
                elif directionList[-2] == 'W':
                    self.direction = 'N'


        elif command == 'u':                        # turning up
            if self.direction in 'NEWS':
                self.direction = 'UP'
           
        elif command == 'd':                        # turning down
            if self.direction in 'NEWS':
                self.direction = 'DOWN'
           

    

                
    # function for processing commands || main function
    def process_commands(self, command):            
       
       #list for storing directions
       directionList = []

       for i in range(len(command)):
            if command[i] in 'fb':
                self.move(command[i])
                
            elif command[i] in 'lrud':
                directionList.append(self.direction)
                self.turn(command[i],directionList)

    def get_position(self):                         # for getting final co-ordinates of the chandrayan spacecraft
        return (self.x, self.y, self.z)

    def get_direction(self):                        # for getting final direction of the chandrayan spacecraft
        return self.direction     