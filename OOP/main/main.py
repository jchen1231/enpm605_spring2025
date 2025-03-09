import sys
import os.path

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path)

# from warehouse.robot_practice import Robot
from warehouse.robot import Robot
from warehouse.operator import Operator
from warehouse.battery import Battery


if __name__ == "__main__":
    # titan = Robot(robot_id="TN-8800", model="Titan", battery_charge_level=20.0)
    # print(Robot.get_total_robots()) # 1
    # nomad = Robot(robot_id="NMD-427", model="Nomad", battery_charge_level=50.0)
    # print(Robot.get_total_robots()) # 2
    
    # -----------------
    # try:
    #     robot1 = Robot.build_from_id("TN-8800", 75)
    #     print(robot1.robot_id, "->", robot1.model)  # TN-8800 -> Titan

    #     robot2 = Robot.build_from_id("NMD-500", 60)
    #     print(robot2.robot_id, "->", robot2.model)  # NMD-500 -> Nomad

    #     robot3 = Robot.build_from_id("UNKNOWN-9999", 50)  # Should raise an error
    # except ValueError as e:
    #     print(f"Error: {e}")
    
    # -----------------
    titan = Robot(robot_id="TN-8800", model="Titan", battery=Battery(200, 80))
    operator = Operator("John Doe")
    titan.assign_operator(operator)
    print(titan)
