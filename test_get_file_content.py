from functions.get_file_content import get_file_content

files_to_read = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

for file in files_to_read:

    content = get_file_content("calculator", file)
    print(f"* File readed = {file}")
    if content.startswith("Error"):
        print(content)
    else:
        print(f"* Length of the file = {len(content)}")
        if len(content) > 10000:
            print(f"* {file} truncated: True")
        else:
            print(f"* {file} truncated: False")

        if len(content) > 100:
            print(f"* Begin of file = {content[:400]}")
            print(f"* End of file = {content[-400:]}")
        else:
            print(content)
    print("---------------------------------")


