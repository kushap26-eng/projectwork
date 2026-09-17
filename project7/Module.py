# Modular and Package

'''
This module provides basic,safe wrapper functions for common file handling tasks
such as creating,writing,reading and appending text files.
'''
import os

def create_file(filename):
    '''
    Creates a new empty file.
    Parameters: filename(str): The path or name of the file to create.
    '''
    try:
        with open(filename,'w') as f:
            pass
        print("File created Successfully!")
    except Exception as e:
        print(f'Error creating file: {e}')

def write_file(filename,content):
    '''
    Writes text content to afile.
    Parameters:
    filename(str): The path or name of the file to write to
    content(str): the text data to be written.
    '''
    try:
        with open(filename,'w') as f:
            f.write(content)
        print("Data written successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_file(filename):
    '''
    Read and prints the entire contents of a text file 
    Parameters:
    filename(str): The path or name of the file to read.
    '''
    try:
        with open(filename,'r') as f:
            content = f.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def append_file(filename,content):
    '''
    Appends text content to the end of an existing file.
    Parameters:
    filename(str): The path or name of the file to append to
    content(str): The text data to add.
    '''
    try:
        with open(filename,'a')as f:
            f.write(content)
        print("Data appended successfully!")
    except Exception as e:
        print(f"Error appending to file: {e}")