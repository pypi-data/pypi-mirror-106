import sys
import os

if sys.argv[1] == 'config':
    if sys.argv[2] == 'vscode':
        try:
            os.mkdir('./_tconf')
        except:
            pass

        with open('./_tconf/_value.tshconfig','w') as f:
            value = '''set textvariable $ide => "visualstudiocode"


#set (
    textvariable $env => "python"
)
'''
            f.write(value)

        with open('./__main__.py','w') as f:
            f.write('''from pytsharp_utils.compiler import cmp

cmp('app.tsh')
''')        os.system('echo !Run __main__.py to compile > app.tsh')
            os.system('code app.tsh')
            os.system('code __main__.py')

if sys.argv[1] == 'run':
    os.system('python -b .')

        
