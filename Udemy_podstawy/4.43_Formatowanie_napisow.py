if __name__ == '__main__':
   message1 = 'Processing file %s'
   print(message1 % ('file_1.txt)'))

   message2 = 'File %s has size %d KB'
   print(message2 % ('file1.txt',100))

   message3 = 'File %20s has size %10d KB'
   print(message3 % ('file1.txt',100))

   message4 = 'Processing file {0:s}'
   print(message4.format('file2.txt'))

   message5 = 'File {0:s} has size {1:d}'
   print(message5.format('file3.txt',150))

   message6 = 'File {1:s} has size {0:d}'
   print(message6.format(150,'file3.txt'))

   message7 = "File {0:20s} has size {1:10d}"
   print(message7.format('file4.txt',200))
