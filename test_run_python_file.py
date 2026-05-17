from functions.run_python_file import run_python_file

files_to_run = [("main.py",None), ("main.py", ["3 + 5"]), ("tests.py", None), ("../main.py", None), ("nonexistent.py", None), ("lorem.txt", None)]

for file in files_to_run:

    result = run_python_file("calculator", file[0], file[1])
    print(f"* File run = {file}")
    print(result)
    print("---------------------------------")