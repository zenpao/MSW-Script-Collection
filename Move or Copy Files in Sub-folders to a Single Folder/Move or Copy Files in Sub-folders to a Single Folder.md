#Move or Copy Files in Sub-folders to a Single Folder

##1) Open cmd.exe



##2) Create a folder in your desired location.

md "%USERPROFILE%\Desktop\compiled"



##3) Enter the desired folder to move/copy by changing the path inside "" to your source folder.

cd /d "C:\Users\Zen\Desktop\source"


##4) Changed the path inside "" to your destination folder and run.

for /r %d in (*) do copy "%d" "%USERPROFILE%\Desktop\compiled\"