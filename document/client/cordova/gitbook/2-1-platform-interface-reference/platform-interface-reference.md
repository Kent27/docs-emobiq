# Platform Interface
<!-- Missing: Parent (or Child), Themes, Android, Tutorial -->

## Introduction

Welcome to the eMOBIQ Platform Interface User Guide. This document provides comprehensive information about the eMOBIQ Platform Interface, a user-friendly environment that allows you to manage various aspects of your project such as pages, snippets, layers, screens, and global configurations. This guide is divided into several sections, each dedicated to a specific part of the interface.

## Interface Overview
The eMOBIQ Platform Interface is divided into several sections:

- **Home**: Manage your project pages, snippets, layers, screens, and global configurations.
- **Global Configuration**: Manage your application's global settings.
- **Language**: Define translations from English to your preferred language.
- **Publish**: Publish your project on the eMOBIQ e-store.
- **Lock**: Protect your published application from unauthorized access.
- **Services**: Configure your application to connect with external systems.
- **Database**: Access a visual interface to external databases.

## Detailed Sections

## eMOBIQ Home

### Page
The Page section enables users to manage project pages by adding, duplicating, and deleting them. The selected page is displayed on the interface for easy editing. Users can utilize the Layer section to edit different components of the page.

<!-- Related: 
[Designing Pages](path/to/other/document.md) -->

### Snippets
The Snippets section enables users to manage snippets in a project by adding, duplicating, and deleting them. The selected snippet is displayed on the interface for easy editing. Users can utilize the Layer section to edit different components of the snippet.

<!-- Related: 
[Using Snippets](path/to/other/document.md) -->

### Layer
The Layer section allows users to manage components within a snippet or page. Users can add, duplicate, and delete components. Components are presented hierarchically, displaying parent-child relationships. Selected components are focused on the interface and editable through the properties and actions tab.

<!-- Related:
[Rendering Sequence](path/to/other/document.md) -->


### Screen
The Screen section enables users to manage properties and actions of selected components. Users can customize styling properties and behavior under the properties tab, and add event triggers for interactive functionality in the actions tab.

#### Properties
The Properties section enables users to manage and configure the properties of a selected component. Within this section, users have the ability to customize all styling aspects and define default behavioral properties for the component. Additionally, users can tailor the styling properties to display differently on various types of devices.
##### Styling Properties in 3 View Modes:
- **Default Mode:** Base styling properties applied to all supported devices.
- **Mobile Mode:** Styling properties specific to mobile devices.
- **Tablet Mode:** Styling properties specific to tablet devices.

<!-- Related:
[Designing Pages](path/to/other/document.md) -->

#### Action
The Action section allows users to add event-driven functionality to components. Here, users configure the app logic and utilize the visual logic interface to build the component logic. By selecting the desired event trigger type and dragging actions from the action list, users can easily define the component's event logic. The section also includes an action inspector, enabling users to customize each action within the visual logic interface. This includes defining parameters to be passed for precise configuration.

##### Inspector
The Inspector allows users to configure selected actions in the visual logic interface. These configurations serve as inputs for each action, which then produces the corresponding outputs. Actions resemble traditional programming functions and their behavior is specified in the action reference.

<!-- Related:
[Action Reference](path/to/other/document.md) -->

##### Parent (or Item) - Visual Logic Interface
Description for the parent section...

##### Event - Visual Logic Interface
This selector enables users to select and configure events for the component. Multiple events with distinct behaviors can be assigned to a component. For detailed instructions on physically triggering each event, refer to the event reference documentation.

<!-- Related:
[Event Reference](path/to/other/document.md) -->

### Themes
Description for the themes section...

### Global
This section enables users to create and manage custom global functions within the project. Functions can be created and modified using the visual logic interface, and are readily available within the list of actions for easy integration.

#### Global Functions
In this interface, users can choose a global function from a list to modify. The selected function's implementation is displayed on the visual logic interface for easy editing.

<!-- Related:
[Creating Global Functions](path/to/other/document.md) -->

### Editor interface icons
#### Add Page (icon)
Allows user to conveniently create a page in the project.

#### Page Wizard (icon)
The Page Wizard initiates the page wizard interface for generating new pages. It offers a convenient and efficient method to create pages with template UIs tailored to specified requirements.

<!-- Related:
[Using Wizards](path/to/other/document.md) -->

#### Function Wizard (icon)
The Function Wizard initiates the function wizard interface for adding event-driven logic to a selected component. It offers a convenient and efficient method to construct commonly used logic flow based on specified requirements. The generated logic for the component can be viewed in the visual logic interface.

<!-- Related:
[Using Wizards](path/to/other/document.md) -->

#### Media Library (icon)
The Media Library feature enables users to upload and manage media resources for use within the project. These media files are stored alongside the compiled app file as static resources.

#### Copy (icon)
Provides a quick way to copy selected components.

#### Paste (icon)
Provides a quick way to paste copied components. Ensure that the target location is selected in the page layer before pasting.

#### Delete (icon)
Provides a quick way to delete the selected components or pages.

#### Page layout size and orientation (icon)
Users can change the size and orientation of the editor interface to visualize the project's appearance on different screen dimensions. This is useful for visualising how the project will look like when running on devices with different screen sizes. 

---

## Global Configuration

The Global Configuration component is a powerful tool within our app development platform that allows you to manage the global settings of your application. It serves as a centralized location where you can define and modify various configuration options that impact the behavior and appearance of your app.

With the Global Configuration component, you have the ability to customize the following settings.

<!-- ![General Configuration](url-of-the-general-image) -->

### General

- **Package Name**: The name of the application which needs to be unique. This name can be used to set up iOS developer configuration.
- **Application Default Page**: Defines the first landing page when the application is opened or running.
- **Enable Auto Update**: 
    - **On**: Asks for automatic update when opening the application after upgrading the app version.
    - **Off**: Does not prompt for update and requires manual update.

<!-- ![Android Configuration](url-of-the-android-image) -->

### Android

<!-- ![iOS Configuration](url-of-the-ios-image) -->

### iOS

To set up building iOS apps:
- **iOS Code Sign**: Common name of your Apple Developer Certificate.
- **iOS Team ID**: User ID of your Apple Developer Certificate.
- **iOS Provision File**: Upload the file directory of your Apple profile for the application.
- **iOS Private Key File**: Upload the file directory of your Apple Developer Certificate File.

<!-- ![Third Party Configuration](url-of-the-third-party-image) -->

### Third Party

This is used to set up the following:
- Google API Key (if using Google Service in the application)
- Facebook App ID (if using Facebook Service in the application)

<!-- ![Properties Configuration](url-of-the-properties-image) -->

### Properties

To set up the default CSS properties of the application. All screens within the application will apply this global CSS.
- **Dialog Theme**: Default background color of the dialog box.
- **Background Image**: Default background image of the application page.
- **Background Color**: Default background color of the application page.
- **Background Position**: Default position of the background image.
- **Background Size**: Default size of the background image.

<!-- ![Plugins Configuration](url-of-the-plugins-image) -->

### Plugins

This feature enables users to manage external plugins for integration with the project. Users can create plugins externally and import them through this interface for seamless integration.

---
## Language
This functionality allows users to define a list of translations from English to their preferred language. These translations can be utilized with language actions in the visual logic interface to modify the displayed language within specific components.

<!-- Related:
[Changing Language](path/to/other/document.md) -->

---
## Publish
This feature enables users to publish their project on the eMOBIQ e-store. Publishing can only be performed after the project has been built.

<!-- Related:
[Build and publish](path/to/other/document.md) -->

---
## Lock
This feature allows users to protect their published application from unauthorized access. Users can set a password for their application, ensuring authentication is required before others can download the application from the e-store.

---
## Services
The Services section provides configuration options to connect your application with various external systems (data sources) seamlessly. These systems include ERP, Payment Gateway, Push Notification, and SQL Lite for local storage. For a full list of services, you may refer to the [Services Reference]
<!-- (path/to/other/document.md). -->

### Available Connectors for ERPs:

- NAV Connector
- SAP B1 Connector
- Accumatica Connector
- REST Connector
- SOAP Connector

### Available Connector for Push Notification:

- Firebase Connector

### Available Connectors for Payment Gateway:

- MC Payment Connector
- ENets Payment Connector
- 2C2P Payment Connector
- PayPal Connector

---

## Database
This feature provides a visual interface to external databases. Currently, eMOBIQ supports staging databases hosted on eMOBIQ servers and AWS DynamoDB for visual interfacing. Please note that these databases are considered external data sources and need to be configured through the Services layer before they can be utilized.

Additional Disclaimer: The eMOBIQ staging database is designed for lightweight testing purposes during app development and should not be relied upon for production-level features. We do not assume responsibility for any issues arising from the use of the eMOBIQ staging database.

## Build
The Build feature enables you to generate mobile app versions of your project based on the selected options in the build interface. This includes specifying the build mode (Debug/Development/Release), versioning, and cross-platform build options such as iOS and Android.

Before using the iOS and Android build options, make sure to configure the Android and iOS settings within the Global Configuration section.

## Download
The download button allows you to download the application after it has been built.

## Tutorial
Description for the tutorial section...

## Help
The Help section offers a comprehensive reference guide for available actions that can be utilized within the visual logic interface. It serves as a valuable resource for understanding and implementing various actions in your project.

## Save
Allows you to save the current state of your project. It is important that you remember to save your project to ensure no progress is lost.

## Preview
Preview enables users to visually preview their projects before proceeding with the build process. This valuable feature allows users to assess their app's layout and behavior during the development phase.

Previewing can be done in three ways:

Scan the QR code and preview on your own device.
Directly preview on the editor.
Open a www3 page to preview.
This functionality facilitates a seamless and efficient development process by providing users with immediate visual feedback on their app's appearance and functionality.
