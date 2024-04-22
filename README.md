# Documentation - Format

### Templates

- Contains the format of the different md files for the documentation.
    - [See - Template Function](template/template-function.md)

### Guidelines

#### General

- Folder Structure
    - If you want to organize the folder structure use this format:
        ```
        # Format
        {000}-{folder_name}

        # Example
        001-first-folder
        ```

#### Functions

- Structure
    - If there is no value please remove the header except for the following: Description, Input/Parameter and Output. 
    - For the three exceptions, if it is totally empty include N/A.
- Examples
    - Try to create examples that can be seen in the application directly, don't rely on console/write.
    - For functions that require components to show output, the example will include the specific steps and results.
- Images
    - Embedding images, the path should be based on the root folder.
    - Please follow the format {function-name}-{type}-{number}.png whenever you add a new image.

### Notes

- Deploying to gitbook requires running the scripts, make sure to do this first.

    ```sh
    cd script
    {python3.10} run.py
    ```

- Main file video storage would be stored in this link [One Drive][One Drive Link] under the **'Videos'** folder, it's also following the naming convention similar to our folder structure.
- All video links would be redirected in this [YouTube][YouTube Link] channel.

[One Drive Link]: <https://mscconsulting-my.sharepoint.com/:f:/g/personal/kevin_orangekloud_com/EqsSA77l559GshRRN1EyadkBlBX4OAXWBEfplMFyIRcsHQ>

[YouTube Link]: <https://www.youtube.com/channel/UCQGKn9kDzXdbVed8uPOzasQ>