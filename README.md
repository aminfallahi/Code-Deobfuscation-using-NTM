To run the project, you should have python3 with numpy, scipy, and tensorflow installed. Then you can use the following command to run the project:
`python3 run_tasks.py --experiment_name amin`

The experiment name is a required parameter and according to the $name, file head_logs/$name.p should be created with write permissions before running the program. In this package, amin.p is already created in head_logs, so with experiment_name "amin", it should work without any errors.

Other parameters of the network are modifyable using inline parameters, or they can be hardcoded in run_tasks.py. For a list of available commands, run: `python3 run_tasks.py --help`
