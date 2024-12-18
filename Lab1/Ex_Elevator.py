class Elevator:
  def __init__(self, max_floor):
    self.current_floor = 1
    self.max_floor = max_floor

  def go_to_floor(self, floor):
      if floor <= self.max_floor:
         self.current_floor = floor
      else:
         print("Invalid Floor!")

  def report_current_floor(self):
    print(self.current_floor)

elevator = Elevator(int(input()))
floor = input()
while floor != "Done":
   floor = int(floor)
   elevator.go_to_floor(floor)
   floor = input()
elevator.report_current_floor()