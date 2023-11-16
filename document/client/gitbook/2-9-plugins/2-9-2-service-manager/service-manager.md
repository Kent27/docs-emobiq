# eMOBIQ Service Manager

The eMOBIQ Service Manager is a tool that allows you to create, import, and manage plugins within the platform. This feature enables you to extend the functionality of eMOBIQ by adding your own custom functions, components, and third-party plugins. This documentation will guide you through the process of managing eMOBIQ plugins using the Service Manager.

## 1. Introduction to eMOBIQ Plugin

eMOBIQ Plugin is a feature that allows you to expand the capabilities of the eMOBIQ platform by creating custom functions, components, and integrating third-party plugins. With eMOBIQ Plugin, you can tailor the platform to meet your specific requirements and enhance the user experience.

**Note**: At present, eMOBIQ Plugin is compatible only with Cordova. Support for React Native will be available in the near future.

## 2. Creating a New Plugin

To create your own custom plugin for eMOBIQ, follow these steps:

### 2.1. **Install the eMOBIQ Service Manager CLI (Command Line)**:

**Note**: To develop a package you need to have setup and configure your development environment.

Steps to install eMOBIQ Service Manager CLI:
1. Install [nodejs](https://app.emobiq.com/) in your computer.
2. Open your terminal.
3. Enter "npm install -g emobiq".
4. Enter "emobiq" to test eMOBIQ Service Manager was succesfully installed.
5. The eMOBIQ Service Manager CLI is now installed.

Steps to uninstall eMOBIQ Service Manager CLI:
1. Open your terminal.
2. Enter "npm uninstall -g emobiq".
The eMOBIQ Service Manager CLI is now uninstalled.

### 2.2. **Create an account for eMOBIQ Service Manager**: 
    
**Note**: To access eMOBIQ Service Manager, you need to have an account on eMOBIQ Service Manager.

To manage your packages in eMOBIQ Service Manager, you need an eMOBIQ Service Manager account. This simple guide explains how to request for an eMOBIQ Service Manager account.

Steps to request an account for eMOBIQ Service Manager:

1. You should have a registered account in [eMOBIQ Platform](https://app.emobiq.com/).
2. Send a request to Orangekloud to enable your eMOBIQ Service Manager account.
3. After Orangekloud approved your request and enabled your eMOBIQ Service Manager account, you can now login with the same credentials as your eMOBIQ Platform account [here](https://emsm.emobiq.com/login) and in the eMOBIQ Service Manager cli as well.

### 2.3. **Create an eMOBIQ Service Manager package**:

**Note**: The guide below helps you to create a new package once you have your account.

Steps to create a new package:

1. Open your terminal.
2. Create a new folder for the package to be created.
3. Move to that folder.
4. Login with your eMOBIQ Service Manager account by entering “emobiq login”.
5. Initialize the project by entering “emobiq plugin init”, to generate the necessary files.
6. Using terminal or any IDE, open 'platforms/client/common/editor/index.json' and write your code.
This is where you create the editor related codes, sample codes below:

**Notes**:
- The "type" defines whether it is a "function" or a "component".
- The "attributes.value.default" entry is the component's default attribute.
- The "attributes.custom" entry will be reflected in properties tab.
- The "events" entry will be reflected in the platform event flow selection of event.
```json
[
    // Sample code for function
    {
        // function | component
        "type": "function", 
        "name": "myFunction", 
        "parameters": [ 
            { 
                "name": "value", 
                // string | integer | number | boolean | functionList
                "type": "string" 
            },
            { 
                "name": "callback", 
                // string | integer | number | boolean | functionList
                "type": "functionList" 
            }
        ] 
    },
    // Sample code for component
    {
        "type": "component",
        "name": "MyLabel",
        "attributes": { 
            "value": { 
                "default": {
                "width": "50%"
                }
            }, 
            "custom": [
                { 
                    "name": "name", 
                    "title": "Name",
                    // string
                    "type": "string"
                }
            ] 
        }, 
        // Default: click, scrollBottom, scrollTop, onScroll,
        // press, longPress, sortRelease.
        // Custom: user can define whatever event they want, but they need to enable the logic for it, see tap example.
        "events": [
            "tap"
        ]
    }
]
```
7. Using terminal or any IDE, open 'platforms/client/common/preview/index.js' and platforms/client/cordova/app/index.js' then write your code.

This is where you create the preview/app related codes, sample codes below:

**Notes**:
- Preview refers to the emulator within the platform.
- App refers to the build project from the platform.
- The 'platforms/client/common/preview/index.js' usually same as 'platforms/client/cordova/app/index.js'.

``` js
// Function
// The "function myFunction(...)" is the created function in the editor.
function myFunction(parameters) {
    // Do a hello world to the value passed
    let welcome = "Hello, " + parameters.value + "!";
    
    // cordova-plugin-dialogs
    // The "navigator.notification.alert" is an implementation of a plugin function.
    navigator.notification.alert(
        welcome,          // message
        function(){},     // callback
        'Welcome',        // title
        'Okay'            // buttonName
    );
    
    // Helper function to access component through id or name.
    // @param {string} identifier - the component id or name,
    //                              it will prioritize id before name.
    let component = pluginGetComponent("componentName");
    
    // Helper function to trigger callback function.
    // @param {object} element - main object/caller (make sure this is from the root caller)
    // @param {functionList} functionList - the callback to be triggered
    // @param {object} parameters  - the additonal data that are passed through the callback
    // @param {any} parameters.input - the data to be passed to input field
    // @param {any} parameters.extra - the data to be passed to extra field
    let self = this;
    pluginCallback(self, parameters.callback, {input: welcome});
    
    return welcome;
}
    
// Component
// The "MyLabel" is the created component in the editor.
let MyLabel = {
    // The "createElement" function lets user define how the component is going to be created.
    createElement: function() {
        var element = document.createElement("label");
        element.innerHTML = 'My Label - Plugin';
        
        let self = this;
        element.onclick = function() {
            // Helper function to attach event based action.
            // @param {object} element - main object/caller
            // @param {string} eventName - the component event name, only works if it is defined
            // @param {object} parameters  - the additonal data that are passed through the callback
            // @param {any} parameters.input - the data to be passed to input field
            // @param {any} parameters.extra - the data to be passed to extra field
            pluginEvent(self, "tap", {
                input: "Plugin"
            });
        };

        return element;
    }
};
```

8. Using terminal or any IDE, open 'platforms/client/cordova/plugin/index.json' then write your code.

This is where you include all the plugins to be included, sample codes below:

**Notes**:
- The "name" is the name of the plugin that will be installed.
```json
[
    {
        "name": "cordova-plugin-dialogs"
    }
]
```

9. To build the package that you created, enter in the command line emobiq plugin build”. The built files will be generated in a "dist" folder.
10. Enter in the command line “emobiq plugin test” to test if the codes written are valid.
11. Enter in the command line emobiq plugin version (patch|minor|major)” to increase the version number.
12. Enter in the command line emobiq plugin publish” to publish it on the server and make it accessible to the eMOBIQ platform.
13. Your package is now successfully created/updated and published.

### 2.4. **Plugin Configuration**: 

**Note**: If you’ve successfully created a new package in eMOBIQ Service Manager you can now use it in your eMOBIQ Platform project.

Steps to use a new package in eMOBIQ Platform:
1. Go to [eMOBIQ Platform](https://app.emobiq.com/) and select an application where we will add the created eMOBIQ Service Manager package.
2. Go to the global configuration page, then click the plugins tab.
3. Search the eMOBIQ Service Manager package you created and select that.
4. The eMOBIQ Service Manager package is now added, check the actions/components in your project.

<!-- ## 3. Importing Third-Party Plugins

In addition to creating your own custom plugins, eMOBIQ also supports the importation of third-party plugins. This allows you to leverage pre-built functionality and extend the capabilities of your applications even further.

To import a third-party plugin:

1. **Access eMOBIQ Service Manager**: Log in to your eMOBIQ account and navigate to the eMOBIQ Service Manager.

2. **Import Plugin**: Click on the "Import Third-Party Plugin" option.

3. **Specify Plugin Source**: Provide the source URL or file location of the third-party plugin you wish to import.

4. **Integration**: Configure the integration settings and permissions for the imported plugin to ensure it works seamlessly with eMOBIQ services.

5. **Testing**: Test the third-party plugin within your eMOBIQ project to ensure it meets your requirements.

6. **Deployment**: Once tested successfully, you can deploy the third-party plugin in your eMOBIQ applications.

## 4. Platform Compatibility

As mentioned earlier, eMOBIQ Plugin currently supports the Cordova client project platform. We are actively working on expanding compatibility to include React Native in the near future. Stay tuned for updates on platform support.

By utilizing the eMOBIQ Service Manager to manage your plugins effectively, you can unlock endless possibilities for customization and integration within the eMOBIQ no-code platform. -->
