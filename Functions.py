#Terminal Phyton
code ... .py        #make file
python ... .py      #run file
ls                  #list
cp ... .py ... .py  #copy file
mv ... .py ...      #move file into folder
mv ... .py ... .py  #change file name
mv ... .py ..       #move out file from folder
rm ... .py          #remove file (Y or N if savety check)
clear               #clean terminal
mkdir ...           #make folder
rmdir ...           #remove folder
cd .../             #go into folder
cd ..               #go out from folder

black ... .py        #black code (Formating)    Go into folder where file is first

__init__.py         #init file in folder to make it a package

pip list            #list of installed packages
pip uninstall ...   #uninstall package

pytest ... .py      #run test file (from folder.file / from .file / from file import function)
pytest ...          #run all test files in folder   (   file name: test_... .py, def function: def test_...(): )

mypy ... .py        #check type hinting (from folder.file / from .file / from file import function)
mypy ...            #check all test files in folder   (   file name: test_... .py, def function: def test_...(): )

#Python debugger: Debug python file (use a red dot)

-h                  #help in terminal  

pwd                 #Print Working Directory
git config --list   #See git setting
git init            #Placing main branch in working directory (.git)
git help            #For searching commands
git add ... .py     #Or git add .   (moving all file)   for moving file from working tree to staging area
git commit -m "..." #For moving file from staging area to history with massage
#If file just changed, git commit -am "..."   (add and commit in the same time)
git status          #Status = branch name, working tree, staging area, history
git log             #Or git log -3  (3 last log)    or git log -- ...  (log with ... massage while commiting)
git checkout ...    #... = 5 letter from commit hash    or    git checkout ... -- ... .py   remake file that was changed
git checkout ...    #... = name branch, changing branch to ...
git branch          #Mentioning branch   or   git branch ...  for making branch
git log --all --decorate --oneline --graph  #Making branch and commit graph
alias ...="..."     #Making function that include "..."     can use it with   ...
git merge ...       #Merging name branch (...) to branch now
git merge --merged  #Mention the branch name that has merged
git merge -d ...    #Delete branch (...)
git clone ...       #...=https://github...    moving file from remote(github) to git
git remote          #Or git remote -v   for see remote name and source
git push            #Pushing remote to main in graph
git config --global user.email "..."  #Changing email to "..."
git config --global user.name "..."   #Changing username to "..."