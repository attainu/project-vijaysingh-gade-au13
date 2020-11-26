import os
import sys
import parking
import re


class ParkingCommands(object):

    def __init__(self):
        self.parking = parking.Parking()

    def process_file(self, given_file):
        if not os.path.exists(given_file):
            print("Given file %s does not exist" % given_file)

        with open(given_file, "r+") as file_obj:
            try:
                for line in file_obj:
                    if line.endswith('\n'):
                        line = line[:-1]
                    if line == '':
                        continue
                    self.process_command(line)
            except Exception as ex:
                print("Error occured while processing file %s" % ex)

    def isValidLicence(self, reg_no):
        # Regex to check valid
        # Indian driving license number
        regex = ("^[a-zA-Z]{2}[-]{1}" +
                 "[0-9]{2}[-]{1}" +
                 "[a-zA-Z]{1,2}" +
                 "[-]{1}[0-9]{4}$")
        # Compile
        p = re.compile(regex)
        # If the string is empty
        # return false
        if (reg_no is None):
            return False
        # Return if the string
        # matched the regex
        if(re.search(p, reg_no)):
            return True
        else:
            print("Enter Valid Registration Number")
            print("Registration number should be" +
                  " in format AA-DD-AA-DDDD" +
                  " where A - Alphabet and" +
                  " D - digit")
            return False

    def process_input(self):
        try:
            while True:
                stdin_input = input("Enter command: ")
                command = stdin_input.split(' ')[0]
                if command != 'park':
                    self.process_command(stdin_input)
                elif command == 'park':
                    params = stdin_input.split(' ')[1]
                    if self.isValidLicence(params):
                        self.process_command(stdin_input)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            print("Error occured while processing input %s" % ex)

    def process_command(self, stdin_input):
        inputs = stdin_input.split()
        command = inputs[0]
        params = inputs[1:]
        if hasattr(self.parking, command):
            command_function = getattr(self.parking, command)
            command_function(*params)
        else:
            print("Got wrong command.")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        pk_command = ParkingCommands()
        pk_command.process_input()
    if len(args) == 2:
        pk_command = ParkingCommands()
        pk_command.process_file(args[1])
    else:
        print("Wrong number of arguments.")
