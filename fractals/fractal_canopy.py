from turtle import *

shape("turtle")
speed(0)

def snowflake(length, levels):
  if levels == 0:
    forward(length)
    return

  length /= 3.0
  snowflake(length, levels - 1)
  left(60)
  snowflake(length, levels - 1)
  right(120)
  snowflake(length, levels - 1)
  left(60)
  snowflake(length, levels - 1)

def creat_snowflake(sides, length):
  for _ in range(sides):
    snowflake(length, sides)
    right(360 / sides)

creat_snowflake(3, 50)

mainloop()
