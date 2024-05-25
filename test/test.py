def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()
        
        return content1 == content2

def test_files_content():
    file1_path = 'output_test.txt'  # Path to the first file
    file2_path = '../output.txt'  # Path to the second file

    assert compare_files(file1_path, file2_path) == True, "Files content is not the same"