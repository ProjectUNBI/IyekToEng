

# import re
# result=re.sub('([^꯭])ꯔ$', '\1R', 'ꯗꯤꯔꯦꯛꯇꯔ')
# print(result)
#
# result=re.sub('([^꯭])ꯔ$', '\1R', 'ꯗꯤꯔꯦꯛꯇꯔ')
# print(result)
#
# result=re.sub('([^꯭])ꯔ$', '$1R', 'ꯗꯤꯔꯦꯛꯇꯔ')
# print(result)

import re
PYTHONIOENCODING="UTF-8"
pattern = re.compile("^.*?r$")
if pattern.match("ra"):
    pass