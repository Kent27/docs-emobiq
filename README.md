# Documentation - Format

-

### Templates

Contains the format of the different md files for the documentation.

[See - Template Function](template/template-function.md)

### Guidelines (Important)
- Embedding Images - The path should be based on the root folder.

### Folder Structure

Legend

- ()   : Description
- {}   : Parameter
- N    : Number
- ...  : Future Plans

```
├── template (Document structure)
    └── template-{type}.md
└── document (Documentation)
    ├── function
    │   └── {function-group}
    │       └── {function-name} 
    │           ├── {function-name}.md
    │           ├── {function-name}-{type}-{N}.png
    │           └── {function-name}.vsdx
    ├── ...
    └── ...
```

### Tools

Online Markdown Editor: [https://dillinger.io/](https://dillinger.io/)

Online Diagram Editor: [https://www.draw.io/](https://www.draw.io/)

### Notes

- Main file video storage would be stored in this link [One Drive][One Drive Link] under the **'Videos'** folder, it's also following the naming convention similar to our folder structure.
- All video links would be redirected in this [YouTube][YouTube Link] channel.
- For all outputs that can be displayed in the console will use the `console` function in the example provided for those functions. For these functions, the example will be documented in a table including the expected result and explanation.
- For functions that require components to show output, the example will include the specific steps and results.

[One Drive Link]: <https://mscconsulting-my.sharepoint.com/:f:/g/personal/kevin_orangekloud_com/EqsSA77l559GshRRN1EyadkBlBX4OAXWBEfplMFyIRcsHQ>

[YouTube Link]: <https://www.youtube.com/channel/UCQGKn9kDzXdbVed8uPOzasQ>