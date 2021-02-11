# D23: Bokeh - Charting with webviewer

*	Bokeh is a python package that can be visualized on webviewer, instead of using HTML and JavaScript. here we need to install many packages with bokeh, I recommand using python venv (virtual environment) to separate the work space from your own work space.

*	python venv
	*	check whether you have installed virtualenv package:
	`pip install virtualenv` or `python -m pip install virtualenv`<br>
	some of you use: `pip3 install virtualenv` or `python3 -m pip install virtualenv`, up to your python version.
	*	create venv in your folder, you can assign certain path on your venv:
	`python -m venv [venv_name]` replace [venv_name] with your venv name.
	*	you can found there is a folder called "Script" in your venv folder. Goto Script and type `activate`, then you can enter the venv environment. The bash goes:
	```
	([venv_name]) where/you/are ~ %
	```
	*	then you can check what packages you have by: `pip list`

*	in this chapter, we have to install many packages: numpy, Jinja2, six, requests, tornado, pyyaml, python-dateutil, pandas, bokeh, panel, matplotlib, you can copy below:<br>
`python -m pip install numpy matplotlib pandas bokeh Jinja2 siz requests tornado pyyaml python-dateutil panel`<br>

*	bokeh in Jupyter notebook can output html file in default. If you want to change the output file, you can do this: `bokeh.io.reset_output()` then change the function: `output_notebook()`, `output_file()`, or others.

*	More details check here: [Bokeh example](https://towardsdatascience.com/getting-started-with-bokeh-effortlessly-elegant-interactive-data-visualisations-in-python-703249565bb3)









