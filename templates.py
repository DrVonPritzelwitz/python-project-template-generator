def getIndexFile(projectName):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="./css/main-style.css" rel="stylesheet">
        <title>{}</title>
    </head>
    <body>
        
        <script src="./script/script.js"></script>
    </body>
    </html>
    """.format(projectName)

javascript = """
console.log('Hello world');
"""

styles = """
body {
    margin: 0;
}
"""