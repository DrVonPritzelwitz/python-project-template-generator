import os
import templates

print('Welkom to the project generator')
path = input('please provide a path to where you want me to create a project:\n')
projectName = input('please provide a a name for your project:\n')

projectRootPath = os.path.join(path, projectName)
scriptFolderPath = os.path.join(projectRootPath, 'script')
styleFolderPath = os.path.join(projectRootPath, 'css')

indexFilePath = os.path.join(projectRootPath, 'index.html')
scriptFilePath = os.path.join(scriptFolderPath, 'script.js')
styleFilePath = os.path.join(styleFolderPath, 'main-style.css')

access = 0o755

os.mkdir(projectRootPath)

os.mkdir(scriptFolderPath)
os.mkdir(styleFolderPath)

indexFile = open(indexFilePath, "a")
indexFile.write(templates.getIndexFile(projectName))

jsFile = open(scriptFilePath, "a")
jsFile.write(templates.javascript)

cssFile = open(styleFilePath, "a")
cssFile.write(templates.styles)


print('project is created at: {}'.format(projectRootPath))