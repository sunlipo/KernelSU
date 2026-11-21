from pathlib import Path
root=Path(r"C:\Users\Administrator\Documents\deepseek-harness\default-workspace\wangchsu-latest")
p=root/'kernel/Kbuild'; s=p.read_text(encoding='utf-8')
s=s.replace('KSU_EXPECTED_SIZE ?= 0x033b','KSU_EXPECTED_SIZE ?= 0x033b')
import re
s=re.sub(r'KSU_EXPECTED_HASH \?= [0-9a-f]+','KSU_EXPECTED_HASH ?= 56c3da80ba4b96a376d240c7e6d10a601487cc096404af8e3cf0c8f4403ab56a',s,count=1)
s=re.sub(r'KSU_PACKAGE_NAME \?= .*','KSU_PACKAGE_NAME ?= me.weishu.kernelsu',s,count=2)
p.write_text(s,encoding='utf-8'); print('kbuild patched')
p=root/'manager/gradle.properties'; s=p.read_text(encoding='utf-8')
if 'KSU_NAME' not in s: s+='\nKSU_NAME=WangchSU\n'
p.write_text(s,encoding='utf-8'); print('name patched')
# ensure workflow dispatch
p=root/'.github/workflows/build-manager.yml'; s=p.read_text(encoding='utf-8')
if 'workflow_dispatch:' not in s:
 s=s.replace('  workflow_call:\n','  workflow_dispatch:\n  workflow_call:\n',1)
 p.write_text(s,encoding='utf-8'); print('dispatch added')
else: print('dispatch exists')
