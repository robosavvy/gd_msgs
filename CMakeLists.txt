cmake_minimum_required(VERSION 2.8.3)
project(gd_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(
 FILES 
 State.msg
 FullState.msg
 FullStateVel.msg
 FullStateVelT.msg
 FullStateSim.msg
 RCValue.msg
 RCArray.msg
 BatteryRegs.msg
 BatteryRegsArray.msg
 MotorSystemVariables.msg
)

add_service_files(
 FILES 
 SetInput.srv
 SetMode.srv
)

generate_messages(
 DEPENDENCIES 
 std_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)
