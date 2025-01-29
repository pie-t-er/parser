# Parser:
import json
from parse import parse

def parser(file_path):
  """
    This function is borrowed from Pieter Alley, another student in this class.
    Parses a file containing preferences for applicants and companies.
    File format must match that of the given example in the assignment 1 document.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        tuple: (n, appPref, companyPref)
            - n: Number of entries.
            - applicant_preferences (appPref): List of preference lists for applicants.
            - company_preferences (comPref) List of preference lists for companies.
    """
  try:
    # opening and reading file
    with open(file_path, "r") as file:
      lines = file.readlines()

    # initializing return variables
    n = int(parse("n = {}\n", lines[0])[0])
    appPref = []
    comPref = []

    # parsing for applicant preferences
    for line in lines[2:n+2]:
      appPref.append(json.loads(parse("{}: {}\n", line)[1]))

    # parsing for company preferences
    for line in lines[n+4:-2]:
      comPref.append(json.loads(parse("{}: {}\n", line)[1]))
    comPref.append(json.loads(parse("{}: {}", lines[-1])[1]))

    return n, appPref, comPref

  except FileNotFoundError:
    raise ValueError(f"File not found: {file_path}")
  except (ValueError, IndexError, KeyError) as e:
    raise ValueError(f"Error parsing file {file_path}: {e}")