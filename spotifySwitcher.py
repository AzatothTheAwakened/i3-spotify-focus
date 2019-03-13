import json
import subprocess
import os

def findParent(node, k, v):
    isList = isinstance(node, list)
    isDict = isinstance(node, dict)
    if isList or isDict:
        for x in node:
            val = x
            if isDict:
                val = node[x]
            
            if isinstance(val, str):
                if x==k and val==v:
                    return [{x: val}, node]
            else: 
                val = findParent(val, k, v)
                if val != None:
                    val.append(node)
                    return val                

result = subprocess.run(['i3-msg', '-t', 'get_tree'], stdout=subprocess.PIPE)
jsonOutput = result.stdout
parsed = json.loads(jsonOutput)
parsed = parsed['nodes']
nodePath = findParent(parsed, 'name', 'Spotify')
if nodePath != None:
    workspace = nodePath[3]['num']
    cmd = "i3-msg 'workspace {}'".format(workspace)
    os.system(cmd)
    print("OOF")
