Title: Add line number in Jupyter Notebook code cell by default
Category: computer
Tags: python
Date: 2016-08-04 23:31

Select a code cell, open browser's JavaScript console, type and execute the following lines:

```javascript
var cell = Jupyter.notebook.get_selected_cell();
var config = cell.config;
var patch = {
    CodeCell:{
        cm_config:{lineNumbers:true}
    }
}
config.update(patch)
```

Then reload the page. These changes will be saved in `.jupyter/nbconfig`. See [Configuring the notebook frontend](http://jupyter-notebook.readthedocs.io/en/latest/frontend_config.html).
