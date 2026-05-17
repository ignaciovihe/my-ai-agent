from functions.write_file import write_file

files_to_write = [
    ("lorem.txt","wait, this isn't lorem ipsum"), 
    ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"), 
    ("/tmp/temp.txt", "this should not be allowed")
]

for file in files_to_write:

    result = write_file("calculator", file[0], file[1])
    print(f"* File writed = {file[0]}")
    print(result)
    print("---------------------------------")