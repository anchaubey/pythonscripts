#/bin/bash

#$ git init
#Add the files in your new local repository. This stages them for the first commit.

#$ git add .
# Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
#Commit the files that you've staged in your local repository.

#$ git commit -m "First commit"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit# and add the file again.
#At the top of your GitHub repository's Quick Setup page, click  to copy the remote repository URL.

#Copy remote repository URL field
#In the Command prompt, add the URL for the remote repository where your local repository will be pushed.

#$ git remote add origin remote repository URL
# Sets the new remote
#$ git remote -v
# Verifies the new remote URL
#Push the changes in your local repository to GitHub.

#$ git push origin master
# Pushes the changes in your local repository up to the remote repository you specified

git add . 
git commit -m "Add existing file"
git push origin master <<EOF
anchaubey
Mummayou@345
EOF 
