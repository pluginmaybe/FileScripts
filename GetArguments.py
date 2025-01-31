import sys

arg = sys.argv

def main():
  if len(arg) <= 1:
    print("No arguments passed. ")
    return 
  
  print(f"argument = {arg[1]}")

          


if __name__ == "__main__":
  main()