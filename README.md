# Ignition

<!--- Badges --->
![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/Ignition)
![GitHub last commit (master)](https://img.shields.io/github/last-commit/thecesrom/Ignition/7.9)
![GitHub license](https://img.shields.io/github/license/thecesrom/Ignition)
![GitHub downloads](https://img.shields.io/github/downloads/thecesrom/Ignition/total)

Ignition is a set of packages and modules that allows developers to get code completion in their IDE of choice.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 2.7
* You are familiar with [Ignition 7.9 Scripting Functions](https://docs.inductiveautomation.com/display/DOC79/Scripting+Functions)

## Using Ignition

To use Ignition, add it as a dependency to your scripting project.

## Packages

Ignition consists of the following packages:

* incendium
* java/javax
* system

### incendium

Is a package that extends and wraps some functions from Ignition's Scripting Functions.

For more information, please refer to the [Wiki](https://github.com/thecesrom/Ignition/wiki/incendium).

### java/javax

These are libraries for some Java packages and functions that are imported on `incendium` and `system` packages meant to be used on systems where no JDK can be installed, and the project interpreter is Python 2.7.

### system

Is a package that includes stubs of all Ignition Scripting Functions.

## Contributing to Ignition

To contribute to Ignition, follow these steps:

1. Fork this repository
2. Create a local copy on your machine
3. Create a branch
4. Make your changes and commit them
5. Push to the original branch
6. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/Ignition/graphs/contributors).

## License

This project is licensed under the GNU GPLv3 license. See the [LICENSE](https://github.com/thecesrom/Ignition/blob/master/LICENSE).


## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
