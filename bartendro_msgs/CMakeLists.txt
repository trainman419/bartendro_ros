cmake_minimum_required(VERSION 2.8.3)
project(bartendro_msgs)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED message_generation std_msgs)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  Drink.msg
  Drinks.msg
  Ingredient.msg
  Ingredients.msg
)

# TODO: generate messages

## Generate added messages and services with any dependencies listed here
generate_messages( DEPENDENCIES std_msgs)

catkin_package( CATKIN_DEPENDS std_msgs)
