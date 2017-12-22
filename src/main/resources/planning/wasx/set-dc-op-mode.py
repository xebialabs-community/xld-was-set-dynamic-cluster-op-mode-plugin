#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from java.util import HashSet

def dynamicClusters():
    result = HashSet()
    if deployedApplication:
        for container in deployedApplication.environment.members:
            if container.type == "was.DynamicCluster":
                result.add(container)
    if previousDeployedApplication:
        for container in previousDeployedApplication.environment.members:
            if container.type == "was.DynamicCluster":
                result.add(container)
    return result

for dc in dynamicClusters():
    if dc.opModeBeforeDeployment:
        context.addStep(steps.os_script(
            description = "Set %s operational mode to %s" % (dc.name, dc.opModeBeforeDeployment),
            order = 5,
            script = "scripts/wasx/set-dc-op-mode-before",
            target_host = dc.cell.host,
            freemarker_context = {'dc' : dc, 'cell' : dc.cell}
        ))
    if dc.opModeAfterDeployment:
        context.addStep(steps.os_script(
            description = "Set %s operational mode to %s" % (dc.name, dc.opModeAfterDeployment),
            order = 95,
            script = "scripts/wasx/set-dc-op-mode-after",
            target_host = dc.cell.host,
            freemarker_context = {'dc' : dc, 'cell' : dc.cell}
        ))
