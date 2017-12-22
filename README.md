# XL Deploy WebSphere Set-Dynamic-Cluster-Mode plugin v1.0.0


[![License: MIT][xld-was-set-dynamic-cluster-mode-plugin-license-image]][xld-was-set-dynamic-cluster-mode-plugin-license-url]


[xld-was-set-dynamic-cluster-mode-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-was-set-dynamic-cluster-mode-plugin-license-url]: https://opensource.org/licenses/MIT

## Preface

This document describes the functionality provided by the XL Deploy WebSphere Set-Dynamic-Cluster-Mode plugin.

See the [XL Deploy reference manual](https://docs.xebialabs.com/xl-deploy) for background information on XL Deploy and deployment automation concepts.  

## Overview

This plugin inserts steps to set the Operational Mode of a WAS Dynamic Cluster before and after a deployment.

## Requirements

XL Deploy 4.5+

## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xld-was-set-dynamic-cluster-mode-plugin/releases) into the `XL_DEPLOY_SERVER/plugins` directory.
* Restart the XL Deploy server.

## Usage

The step(s) to set the operational mode will be inserted into the deployment plan automatically if the OpsModeBeforeDeployment and/or OpsModeAfterDeployment properties are set.

### Configuration

![configuration](images/configuration.png)

### Deployment mapping

![deployment-preview](images/deployment-preview.png)

## References

https://www.ibm.com/support/knowledgecenter/en/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/rwve_adtaskdc.html#rwve_adtaskdc__DynamicClusterCommands.cmd20

   