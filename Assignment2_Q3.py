"""
Geometric Pattern Generation using Recursive Function (Koch Curve Algorithm)

References:
  [1] H. von Koch, "On a Continious curve without tangents constructible from elementary geometry," Arkiv for Matematik, 
  Astronomi och Fysik, vol.1, pp 681-702, 1984.
  [2] Python Software Foundation, "turtle — Turtle graphics," Python 3.x Documentation. [Online]. 
  Available: https://docs.python.org/3/library/turtle.html
  [3] E. W. Weisstein, "Regular Polygon," MathWorld--A Wolfram Web Resource.[Online]. 
  Available: https://mathworld.wolfram.com/RegularPolygon.html

This program uses Koch Curve[1] Algorith which is a recursive function that uses recursive subdivision to create complex 
geometric patterns using Python's turtle graphics module [2]. 

"""
# start code
# import turtle and math module for graphics drawing and trigonometric calculations respectively
import turtle 
import math 

def koch_edge(t, length, depth): #recursively draws a Koch-like pattern on a single edge
  # Dividing each line segment into four smaller segments with a traingular protrusion in the middle.

  if depth == 0:  # if depth is 0, it draws a straight line [1] (It is a case where no recursion occurs.)
    t.forward(length)  # move turtle forward by specified pixels [2]
  else: 
    # if depth is not 0, recursion starts. The edge is divided into 3 equal parts [1]
    segment_length = length / 3  # calculate lenth of each third

    # Draw first segment (first third of the edge) [1]
    koch_edge(t, segment_length, depth -1)  # recursive call with reduced depth

    # Turn left 60 degrees to start creating a triangular bump [1] (Creates an equilateral triangle protrusion
    t.left(60) # points inward

    # Draw Second segment (At an angle previously stated) [1]
    koch_edge(t, segment_length, depth -1)  # recursive call with reduced depth

    # Turn right 120 degrees to create the peak [1] 
    t.right(120)  # points down and then right

    # Draw third segment (the final side of the triangle) [1]
    koch_edge(t, segment_length, depth-1)  # recursive call with reduced depth

    # Turn left again 60 degrees to return to the original direction to complete the recursion [1]
    t.left(60)

    # Draw fourth and final segment [1]
    koch_edge(t, segment_length, depth -1)  # recursive call with reduced depth

def draw_polygon(sides, side_length, depth): # Drawing a polygon with fractal edges using the Koch Curve algorithm [2][3]
  # Creates a centered (using geometric calculations[3]) user defined number of sided polygon.
  # Each edge is replaced with a Koch Curve pattern. [1]
  # ARGUEMENTS:
  # sides : Number of sides of a polygon (sides must be >=3)
  # side_length : length of each side (pixels)
  # depth : Recursion depth

  # Creating a screen for drawing the pattern. [2]
  screen = turtle.Screen()
  screen.setup(width=1000, height=1000)  # Setting window size
  screen.bgcolor("white")  # Setting background color
  screen.title("Geometric Pattern with Recursive Function")  # Setting window title

  # Creating a turtle object for drawing the pattern [2]
  t = turtle.Turtle()
  t.speed(0)  # Set speed to max
  t.hideturtle()  # Hiding the turtle 

  # Calculating the exterior angle required to turn at every corner [3]
  # For regular polygons, sum of exterior angles=360 [3]
  exterior_angle = 360 / sides

  # Calculate the radius of the circle that contains the polygon for centering [3]
  # radius = side_length / (2 * sin( pi/ numnber_of_sides)) [3]
  radius = side_length / (2 * math.sin(math.pi / sides))

  # Move turtle to starting position at the top of the screen [2]
  t.penup()  # Lift pen to not draw
  t.goto(0, radius)  # Move to the specified cordinate 
  t.setheading(0)  # Point turtle to the right at 0 degrees
  t.pendown()  # Put pen down to draw

  # Make the starting position visually better for every case [2]
  t.penup()  # Left pen to not draw
  start_angle = 90 - (exterior_angle / 2)  # Starting angle [3]
  t.setheading(start_angle)  # Turtle facing direction
  t.forward(side_length /2)  # Move turtle
  t.right(180 - exterior_angle)  # Turn turtle to face the direction of first edge 
  t.pendown()  # Put pen down to draw

  # Going through all the sides of the polygon as a loop [3]
  for _ in range(sides):  # no need loop counter
    koch_edge(t, side_length, depth)  # Draw one fractal edge [1]
    t.right(exterior_angle)   # Turn right for the next side

  # Closing the window
  screen.exitonclick()  # Window closes when clicked

def main():  # Function for user input and pattern generation [2]

  # Print a Header for the Program.
  print("============================\n")
  print(" GEOMETRIC PATTERN GENERATOR\n")
  print("============================\n")

  # Using try-except to handle potential errors [2]
  try:
      # Number of sides
      sides = int(input("Enter the number of sides for a Polygon: "))  # Input must be integer
      # Minumum 3 sides for a polygon [3]
      if sides < 3:
        print("!!!!!!!!!!!!!!!ERROR!!ERROR!!ERROR!!!!!!!!!!!!!!!!!!!")
        print("The number of sides must be at least 3 for a Polygon.")
        return  # Exit
      
      # Length of sides
      side_length = int(input("Enter the length of the sides of the polygon: "))  # Input must be integer
      # Length must be positive [3]
      if side_length <= 0:
        print("!!!!!!!!ERROR!!ERROR!!ERROR!!!!!!!!!!!!")
        print("The length of the side must be positive")
        return  # Exit 

      # Depth of the recursion
      depth = int(input("Enter the depth of the recursion: "))
      # Depth must be positive
      if depth < 0:
        print("!!!!!!!!ERROR!!ERROR!!ERROR!!!!!!!!!")
        print("The recursion depth must be positive")
        return  # Exit

      print("\n\n-----------------\n")
      print("GENERATING PATTERN")
      print("\n\n-----------------\n")
      
      # Call the drawing function
      draw_polygon(sides, side_length, depth)

  # Checking for non-integer inputs [2]
  except ValueError:
    print("Please enter a valid integer")
  # Checking any other unexpected errors [2]
  except Exception as e:
    print(f"An Error occured: {e}")

# Checking if the script runs directly [2]
if __name__ == "__main__":
  main() # Start the program
