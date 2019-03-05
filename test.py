import re

title = '''
"
                
                    
                    Lessons learned: How smaller cities can get smart
                     | Smart Cities Dive
                
            "
'''
title = title.strip()
title = title.replace('\n', '')
title = re.sub(' +', ' ', title)
print(title)