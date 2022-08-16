import requests
import pandas as pd
import filecmp

print("Sending test_pic.jpg to uploader API to simulate sending a file which will be analyzed and returned as xlsx")
with open('test_pic.jpg', 'rb') as f:
    r = requests.post('http://localhost:5000/uploader', files={'file': f})
print("Response Code is: ", r, " (200 is OK)")

# saving returned file to a variable
returned_file = r.content

print("Saving the returned test.xlsx file to a different new (not exited yet) file called test2.xlsx")
with open('test2.xlsx', 'wb') as saved_file:
    saved_file.write(returned_file)

# comparing files with filecmp (python native library) to assert they are equal
are_file_same = filecmp.cmp('test.xlsx', 'test2.xlsx')
print("True if files are the same: ", are_file_same)