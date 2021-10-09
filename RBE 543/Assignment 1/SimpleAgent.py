import random


class Environment(object):
    def __init__(self):
        self.status = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}


class SRAgent(Environment):
    Performance = 0
    
    def __init__(self, Environment):
        self.status = Environment.status
        self.sequence()
        
    def SimpleReflexAgent(self, status, location):
        if status == 'Dirty':
            self.Performance += 1
            return 'Suck'
        elif location == 'A':
            self.Performance += 1
            return 'Right'
        elif location == 'B':
            self.Performance += 1
            return 'Left'

    def sequence(self):
        vacuumLocation = random.randint(0, 1)

        if vacuumLocation == 0:
            print("Vacuum is at location A.")

            if self.status['A'] == 1:
                print("Location A is dirty.", self.SimpleReflexAgent(
                    'Dirty', 'A'))
                self.status['A'] = 0
                print("Location A has been cleaned.")

                if self.status['B'] == 1:
                    print("Moving to location B: ", self.SimpleReflexAgent(
                        'Clean', 'A'))

                    print("Location B is dirty.", self.SimpleReflexAgent(
                        'Dirty', 'B'))
                    self.status['B'] = 0
                    print("Location B has been cleaned.")

            else:
                if self.status['B'] == 1:
                    print("Moving to location B: ", self.SimpleReflexAgent(
                        'Clean', 'A'))

                    print("Location B is dirty.", self.SimpleReflexAgent(
                        'Dirty', 'B'))
                    self.status['B'] = 0
                    print("Location B has been cleaned.")

        elif vacuumLocation == 1:
            print("Vacuum is at location B.")

            if self.status['B'] == 1:
                print("Location B is dirty.", self.SimpleReflexAgent(
                    'Dirty', 'B'))
                self.status['B'] = 0
                print("Location B has been cleaned.")

                if self.status['A'] == 1:
                    print("Moving to location A: ", self.SimpleReflexAgent(
                        'Clean', 'B'))
                    print("Location A is dirty.", self.SimpleReflexAgent(
                        'Dirty', 'A'))
                    self.status['A'] = 0
                    print("Location A has been cleaned.")

            else:
                if self.status['A'] == 1:
                    print("Moving to location A: ", self.SimpleReflexAgent(
                        'Clean', 'B'))

                    print("Location A is dirty.", self.SimpleReflexAgent(
                        'Dirty', 'A'))
                    self.status['A'] = 0
                    print("Location A has been cleaned.")


environment = Environment()
print('Environment status before running agent: ', environment.status)
vacuum = SRAgent(environment)
vacuum.status = environment.status
print('Environment status after running agent: ', vacuum.status)
print('Performance Score: ', vacuum.Performance)
